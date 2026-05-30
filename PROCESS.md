# 📋 Developer Process Guide

This document defines the **mandatory processes** all developers must follow in this project.

---

## 1. 🌿 Branch Naming Convention

All branches MUST follow this pattern:

```
<type>/<ticket-id>-<short-description>
```

### Allowed Types:
| Type | Usage |
|------|-------|
| `feat` | New feature |
| `fix` | Bug fix |
| `hotfix` | Critical production fix |
| `docs` | Documentation only |
| `refactor` | Code refactoring |
| `test` | Adding/updating tests |
| `chore` | Maintenance tasks |

### Examples:
```
feat/PROJ-101-add-user-auth
fix/PROJ-205-null-pointer-exception
docs/PROJ-310-update-api-docs
```

---

## 2. 💬 Commit Message Standard

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>

[optional body]

[optional footer: Closes #issue-number]
```

### Examples:
```
feat(auth): add JWT token refresh endpoint

Added /api/auth/refresh that accepts a valid refresh token
and returns a new access token.

Closes #42
```

---

## 3. 🔀 Pull Request Rules

- ✅ PR title must reference the ticket ID (e.g., `[PROJ-101] Add user auth`)
- ✅ PR must be reviewed by at least **1 team member**
- ✅ All checklist items in PR template must be checked
- ✅ No direct commits to `main` or `develop`
- ✅ CI checks must pass before merge

---

## 4. 🐛 Issue Reporting Rules

- Always use the provided issue templates
- Tag recurring issues with the `recurring` label
- Link related issues using `Related to #<issue-number>`
- Assign severity: `critical`, `high`, `medium`, `low`

---

## 5. 📖 Issue Resolution Blog (MANDATORY)

When closing any issue tagged `bug` or `recurring`:

1. Create a new file: `docs/issue-blog/YYYY-MM-DD-<issue-id>-<title>.md`
2. Use the [blog template](docs/issue-blog/TEMPLATE.md)
3. Fill in: Root Cause, Steps to Reproduce, Fix Applied, Prevention
4. Open a PR with your blog post before closing the issue

---

## 6. 🔄 Workflow Summary

```
Create Issue → Branch → Code → Commit → PR → Review → Merge → Blog Post → Close Issue
```
