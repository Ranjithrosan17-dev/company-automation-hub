#!/bin/bash
# ============================================================
# check-commit-message.sh
# Validates commit message follows Conventional Commits:
# <type>(<scope>): <description>
# ============================================================

COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

# Pattern: type(scope): description  OR  type: description
PATTERN="^(feat|fix|hotfix|docs|refactor|test|chore|perf|ci|build|revert)(\([a-zA-Z0-9_-]+\))?: .{10,}"

if [[ "$COMMIT_MSG" =~ $PATTERN ]]; then
  echo "✅ Commit message is valid."
  exit 0
else
  echo "❌ ERROR: Commit message does not follow Conventional Commits format."
  echo ""
  echo "Required: <type>(<scope>): <description (min 10 chars)>"
  echo ""
  echo "Examples:"
  echo "  feat(auth): add JWT refresh token endpoint"
  echo "  fix(payment): handle null response from payment gateway"
  echo "  docs: update API endpoint documentation"
  echo ""
  echo "Allowed types: feat, fix, hotfix, docs, refactor, test, chore, perf, ci, build, revert"
  exit 1
fi
