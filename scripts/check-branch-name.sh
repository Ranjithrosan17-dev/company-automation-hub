#!/bin/bash
# ============================================================
# check-branch-name.sh
# Validates branch name follows company convention:
# <type>/<ticket-id>-<description>
# ============================================================

BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

# Skip check for main/develop/release branches
if [[ "$BRANCH_NAME" =~ ^(main|master|develop|release/.*)$ ]]; then
  echo "✅ Protected branch '$BRANCH_NAME' — skipping naming check."
  exit 0
fi

# Pattern: type/TICKET-123-description
PATTERN="^(feat|fix|hotfix|docs|refactor|test|chore)/[A-Z]+-[0-9]+-[a-z0-9-]+$"

if [[ "$BRANCH_NAME" =~ $PATTERN ]]; then
  echo "✅ Branch name '$BRANCH_NAME' is valid."
  exit 0
else
  echo "❌ ERROR: Branch name '$BRANCH_NAME' does not follow the convention."
  echo ""
  echo "Required format: <type>/<TICKET-ID>-<short-description>"
  echo "Example: feat/PROJ-101-add-user-auth"
  echo "         fix/PROJ-205-fix-null-pointer"
  echo ""
  echo "Allowed types: feat, fix, hotfix, docs, refactor, test, chore"
  exit 1
fi
