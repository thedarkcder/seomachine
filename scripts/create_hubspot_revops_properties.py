#!/usr/bin/env python3
"""Create the minimal HubSpot properties needed for HubSpot-only RevOps/SDR ops.

Default mode is a dry run. Use --apply to create missing properties.

Expected env var:
  HUBSPOT_PRIVATE_APP_TOKEN=pat-...

Fallback env var:
  HUBSPOT_API_KEY=pat-...
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
from urllib.error import HTTPError
from urllib.request import Request, urlopen


API_BASE = "https://api.hubapi.com"


@dataclass(frozen=True)
class HubSpotProperty:
    object_type: str
    group_name: str
    name: str
    label: str
    description: str
    type: str
    field_type: str
    options: tuple[dict[str, str], ...] = ()

    def payload(self) -> dict[str, Any]:
        data: dict[str, Any] = {
            "groupName": self.group_name,
            "name": self.name,
            "label": self.label,
            "description": self.description,
            "type": self.type,
            "fieldType": self.field_type,
        }
        if self.options:
            data["options"] = [
                {
                    "label": option["label"],
                    "value": option["value"],
                    "description": option.get("description", ""),
                    "displayOrder": index,
                    "hidden": False,
                }
                for index, option in enumerate(self.options)
            ]
        return data


STATUS_OPTIONS = (
    {"label": "Not Started", "value": "not_started"},
    {"label": "In Progress", "value": "in_progress"},
    {"label": "Complete", "value": "complete"},
    {"label": "Needs Review", "value": "needs_review"},
    {"label": "Blocked", "value": "blocked"},
)

DATA_QUALITY_OPTIONS = (
    {"label": "Clean", "value": "clean"},
    {"label": "Missing Required Data", "value": "missing_required_data"},
    {"label": "Duplicate Suspected", "value": "duplicate_suspected"},
    {"label": "Stale", "value": "stale"},
    {"label": "Suppressed", "value": "suppressed"},
    {"label": "Needs Review", "value": "needs_review"},
)

OUTREACH_OPTIONS = (
    {"label": "Not Ready", "value": "not_ready"},
    {"label": "Needs Research", "value": "needs_research"},
    {"label": "Needs Enrichment", "value": "needs_enrichment"},
    {"label": "Needs Verification", "value": "needs_verification"},
    {"label": "Ready for Approval", "value": "ready_for_approval"},
    {"label": "Approved", "value": "approved"},
    {"label": "Blocked", "value": "blocked"},
)

APPROVAL_OPTIONS = (
    {"label": "Not Submitted", "value": "not_submitted"},
    {"label": "Pending Review", "value": "pending_review"},
    {"label": "Approved", "value": "approved"},
    {"label": "Needs Edits", "value": "needs_edits"},
    {"label": "Rejected", "value": "rejected"},
    {"label": "Blocked", "value": "blocked"},
)

BOUNCER_OPTIONS = (
    {"label": "Not Checked", "value": "not_checked"},
    {"label": "Deliverable", "value": "deliverable"},
    {"label": "Risky", "value": "risky"},
    {"label": "Undeliverable", "value": "undeliverable"},
    {"label": "Unknown", "value": "unknown"},
    {"label": "Suppressed", "value": "suppressed"},
)

BUYING_ROLE_OPTIONS = (
    {"label": "Economic Buyer", "value": "economic_buyer"},
    {"label": "Champion", "value": "champion"},
    {"label": "Technical Evaluator", "value": "technical_evaluator"},
    {"label": "User Buyer", "value": "user_buyer"},
    {"label": "Blocker", "value": "blocker"},
    {"label": "Procurement Legal Security", "value": "procurement_legal_security"},
    {"label": "Unknown", "value": "unknown"},
)


PROPERTIES = (
    HubSpotProperty(
        object_type="companies",
        group_name="companyinformation",
        name="icp_fit_score",
        label="ICP Fit Score",
        description="Numeric 0-100 score used to prioritize companies for AI SDR outreach.",
        type="number",
        field_type="number",
    ),
    HubSpotProperty(
        object_type="companies",
        group_name="companyinformation",
        name="data_quality_status",
        label="Data Quality Status",
        description="RevOps data quality state for company cleanse and campaign readiness.",
        type="enumeration",
        field_type="select",
        options=DATA_QUALITY_OPTIONS,
    ),
    HubSpotProperty(
        object_type="companies",
        group_name="companyinformation",
        name="outreach_readiness_status",
        label="Outreach Readiness Status",
        description="Company readiness for enrichment, verification, approval, or outreach.",
        type="enumeration",
        field_type="select",
        options=OUTREACH_OPTIONS,
    ),
    HubSpotProperty(
        object_type="companies",
        group_name="companyinformation",
        name="research_completeness_status",
        label="Research Completeness Status",
        description="Tracks whether company research is complete enough for campaign use.",
        type="enumeration",
        field_type="select",
        options=STATUS_OPTIONS,
    ),
    HubSpotProperty(
        object_type="companies",
        group_name="companyinformation",
        name="campaign_approval_status",
        label="Campaign Approval Status",
        description="Approval state for using this company in an outbound campaign.",
        type="enumeration",
        field_type="select",
        options=APPROVAL_OPTIONS,
    ),
    HubSpotProperty(
        object_type="contacts",
        group_name="contactinformation",
        name="bouncer_verification_status",
        label="Bouncer Verification Status",
        description="Latest Bouncer email verification status for this contact.",
        type="enumeration",
        field_type="select",
        options=BOUNCER_OPTIONS,
    ),
    HubSpotProperty(
        object_type="contacts",
        group_name="contactinformation",
        name="bouncer_verification_reason",
        label="Bouncer Verification Reason",
        description="Reason or detail returned by Bouncer for the latest email verification check.",
        type="string",
        field_type="text",
    ),
    HubSpotProperty(
        object_type="contacts",
        group_name="contactinformation",
        name="bouncer_verified_date",
        label="Bouncer Verified Date",
        description="Date this contact email was last verified with Bouncer.",
        type="date",
        field_type="date",
    ),
    HubSpotProperty(
        object_type="contacts",
        group_name="contactinformation",
        name="buying_committee_role",
        label="Buying Committee Role",
        description="Contact's likely role in the buying committee for sales outreach.",
        type="enumeration",
        field_type="select",
        options=BUYING_ROLE_OPTIONS,
    ),
    HubSpotProperty(
        object_type="contacts",
        group_name="contactinformation",
        name="campaign_approval_status",
        label="Campaign Approval Status",
        description="Approval state for using this contact in an outbound campaign.",
        type="enumeration",
        field_type="select",
        options=APPROVAL_OPTIONS,
    ),
    HubSpotProperty(
        object_type="contacts",
        group_name="contactinformation",
        name="outreach_readiness_status",
        label="Outreach Readiness Status",
        description="Contact readiness for verification, approval, or outreach.",
        type="enumeration",
        field_type="select",
        options=OUTREACH_OPTIONS,
    ),
)


def load_environment() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    for env_path in (
        repo_root / ".env",
        repo_root / "data_sources" / "config" / ".env",
        Path.home() / ".codex" / ".env",
    ):
        if env_path.exists():
            load_env_file(env_path)


def load_env_file(path: Path) -> None:
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


class HubSpotClient:
    def __init__(self, token: str) -> None:
        self.token = token

    def get_property(self, object_type: str, property_name: str) -> Optional[dict[str, Any]]:
        try:
            return self._request("GET", f"/crm/v3/properties/{object_type}/{property_name}")
        except RuntimeError as exc:
            if "HubSpot API error 404" in str(exc):
                return None
            raise

    def create_property(self, prop: HubSpotProperty) -> dict[str, Any]:
        return self._request("POST", f"/crm/v3/properties/{prop.object_type}", prop.payload())

    def _request(self, method: str, path: str, payload: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        body = json.dumps(payload).encode("utf-8") if payload is not None else None
        request = Request(
            f"{API_BASE}{path}",
            data=body,
            method=method,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        try:
            with urlopen(request, timeout=30) as response:
                response_body = response.read().decode("utf-8")
                return json.loads(response_body) if response_body else {}
        except HTTPError as exc:
            detail = exc.read().decode("utf-8")
            raise RuntimeError(f"HubSpot API error {exc.code}: {detail}") from exc


def token_from_env() -> str:
    token = os.getenv("HUBSPOT_PRIVATE_APP_TOKEN") or os.getenv("HUBSPOT_API_KEY")
    if not token:
        raise RuntimeError(
            "Missing HubSpot token. Set HUBSPOT_PRIVATE_APP_TOKEN in .env "
            "(or HUBSPOT_API_KEY as a fallback)."
        )
    return token.strip()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create minimal RevOps/AI SDR custom properties in HubSpot."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Create missing properties. Without this flag, only prints a dry run.",
    )
    parser.add_argument(
        "--object-type",
        choices=["companies", "contacts"],
        help="Limit creation/checks to one object type.",
    )
    args = parser.parse_args()

    load_environment()
    client = HubSpotClient(token_from_env())

    selected = [
        prop for prop in PROPERTIES if not args.object_type or prop.object_type == args.object_type
    ]

    created: list[str] = []
    existing: list[str] = []
    planned: list[str] = []

    for prop in selected:
        label = f"{prop.object_type}.{prop.name}"
        current = client.get_property(prop.object_type, prop.name)
        if current:
            existing.append(label)
            print(f"exists  {label}")
            continue

        if args.apply:
            client.create_property(prop)
            created.append(label)
            print(f"created {label}")
        else:
            planned.append(label)
            print(f"would create {label}")

    print()
    print("Summary")
    print(f"  existing: {len(existing)}")
    print(f"  created:  {len(created)}")
    print(f"  planned:  {len(planned)}")

    if planned:
        print()
        print("Dry run only. Re-run with --apply to create missing properties.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
