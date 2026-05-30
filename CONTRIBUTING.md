# 🤝 Contributing Guidelines

Welcome! Please read this before contributing to ensure smooth collaboration.

## ✅ Before You Start

- Read [PROCESS.md](./PROCESS.md) completely
- Check existing issues to avoid duplicates
- For bugs, tag with `bug` label; for recurring issues, add `recurring` label

## 🌿 Branch Rules

- Branch off from `develop` (not `main`)
- Follow branch naming: `<type>/<ticket-id>-<description>`
- Example: `fix/PROJ-123-fix-login-crash`

## 📦 Commit Rules

- Use Conventional Commits format
- Reference issue numbers: `Closes #42`
- Keep commits atomic (one logical change per commit)

## 🔀 Pull Request Checklist

Before submitting a PR, ensure:
- [ ] Branch name follows convention
- [ ] All commits follow conventional commits
- [ ] Code is tested locally
- [ ] PR template is fully filled out
- [ ] Related issue is linked
- [ ] No secrets or credentials committed

## 📖 After Merging

For any bug or recurring issue fix:
1. Write a blog post in `docs/issue-blog/`
2. Use the template: `docs/issue-blog/TEMPLATE.md`
3. Run `python scripts/generate-blog-index.py` to update index

## 🚫 What NOT To Do

- ❌ Do NOT push directly to `main` or `develop`
- ❌ Do NOT merge your own PR without review
- ❌ Do NOT close a `bug`/`recurring` issue without a blog post
- ❌ Do NOT use vague commit messages like `fix stuff` or `update`
