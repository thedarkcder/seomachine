# Contributing to SEO Machine

Thank you for your interest in improving SEO Machine! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues
If you encounter bugs or have suggestions:
1. Check existing [GitHub Issues](https://github.com/thedarkcder/seomachine/issues) to avoid duplicates
2. Create a new issue with:
   - Clear description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs. actual behavior
   - Your environment (Codex version, OS, etc.)

### Suggesting Improvements

**For Skills**:
- Propose new workflow skills in `.agents/skills/`
- Explain the use case and workflow
- Provide example skill structure

**For Specialists**:
- Suggest new specialist skills in `.agents/skills/specialists/`
- Define the specialist's expertise and output format
- Show how it integrates with existing workflow

**For Context Files**:
- Recommend additions to context templates
- Share successful configurations
- Suggest improvements to guidelines

### Submitting Changes

1. **Fork the Repository**
   ```bash
   git clone https://github.com/thedarkcder/seomachine.git
   cd seomachine
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow existing file structure and conventions
   - Update README.md if adding new features
   - Test your changes thoroughly

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a pull request on GitHub.

## Code Style Guidelines

### Skill Files (`.agents/skills/`)
- Use clear, descriptive skill names
- Include comprehensive "What This Skill Does" section
- Provide detailed "Process" breakdown
- Specify expected "Output" format
- Include "File Management" for automatic saves
- Give usage examples

### Specialist Skill Files (`.agents/skills/specialists/`)
- Define "Core Mission" clearly
- List "Expertise Areas"
- Provide detailed analysis framework
- Specify exact "Output Format" with examples
- Include "Quality Standards"
- State "Guiding Principles"

### Context Files (`context/`)
- Use clear section headers
- Provide examples for guidelines
- Include "Instructions" at top for templates
- Add "Usage Guidelines" where relevant
- Keep language clear and actionable

### Documentation
- Use clear, concise language
- Include examples for complex concepts
- Keep README.md updated with new features
- Add inline comments for complex logic

## Testing Your Contributions

Before submitting:
1. **Test the Skill/Specialist**: Run it with real content
2. **Verify Output**: Ensure output matches expected format
3. **Check Integration**: Confirm it works with existing workflow
4. **Update Documentation**: Add usage examples to README.md
5. **Test Edge Cases**: Try with various content types and scenarios

## Content Quality Standards

Contributions should maintain high quality:
- **Clarity**: Instructions are easy to understand
- **Completeness**: All necessary information included
- **Consistency**: Matches existing style and structure
- **Practicality**: Provides real value to content creators
- **Examples**: Includes relevant examples

## What We're Looking For

**High Priority**:
- Improved skill workflows
- New specialist skills for content optimization
- Better context file templates
- Enhanced SEO capabilities
- Time-saving automation features

**Always Welcome**:
- Bug fixes
- Documentation improvements
- Example content and workflows
- Context file best practices
- Integration with SEO tools

**Please Discuss First**:
- Major architectural changes
- New dependencies
- Breaking changes to existing workflows
- Significant additions to context templates

## Questions?

- Open a GitHub Issue with "Question:" prefix
- Review existing documentation in README.md
- Check Codex documentation

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for helping make SEO Machine better! 🎙️📝
