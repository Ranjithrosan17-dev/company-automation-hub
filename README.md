# 🏢 Company Automation Hub

A centralized platform to **reduce recurring issues**, **enforce developer workflows**, and maintain a **searchable Issue Resolution Blog**.

---

## 📌 Goals

| Goal | Description |
|------|-------------|
| ✅ Reduce Recurring Issues | Track, tag, and link repeated issues to prevent future occurrences |
| 📋 Enforce Dev Processes | PR checklists, branch naming rules, and commit message standards |
| 📖 Issue Blog | Developers document root cause + resolution for every closed issue |

---

## 📁 Project Structure

```
company-automation-hub/
├── .github/
│   ├── workflows/          # GitHub Actions CI/CD pipelines
│   │   ├── process-check.yml
│   │   └── issue-blog-reminder.yml
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   │   ├── bug_report.md
│   │   ├── recurring_issue.md
│   │   └── issue_blog_post.md
│   └── pull_request_template.md
├── docs/
│   └── issue-blog/         # Issue resolution blog posts (Markdown)
│       └── TEMPLATE.md
├── scripts/
│   ├── check-branch-name.sh
│   ├── check-commit-message.sh
│   └── generate-blog-index.py
├── CONTRIBUTING.md
├── PROCESS.md
└── README.md
```

---

## 🚀 Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/Ranjithrosan17-dev/company-automation-hub.git
   cd company-automation-hub
   ```

2. **Read the process guide** → [`PROCESS.md`](./PROCESS.md)

3. **Submit a bug** → Use the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md)

4. **After fixing an issue** → Add a blog post in `docs/issue-blog/`

---

## 📖 Issue Blog

Every resolved issue must have a blog entry in `docs/issue-blog/`. See the [blog template](docs/issue-blog/TEMPLATE.md).

- Blog posts are auto-indexed by GitHub Actions
- Searchable by tags, date, and component

---

## 👥 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for full guidelines.
