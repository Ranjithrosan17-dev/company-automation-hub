# 📖 Issue Blog: Example - Fix Null Pointer in User Service

> **Issue ID:** #1  
> **Date Resolved:** 2026-05-30  
> **Severity:** High  
> **Component:** User Service  
> **Author:** @Ranjithrosan17-dev  
> **Tags:** `null-pointer` `user-service` `example`

---

## 🐛 Issue Summary

The `UserService.getById()` method crashed with a NullPointerException when the database returned no results for a given user ID. This caused a 500 error on the frontend for deleted users.

---

## 🔍 Root Cause Analysis

The method directly accessed `.name` on the result of `db.findUser(id)` without checking if the result was null. When a user was deleted from the database but the session token was still valid, subsequent API calls triggered this error.

---

## 🔁 Steps to Reproduce (Before Fix)

1. Delete a user from the database directly
2. Use the deleted user's session token to call `GET /api/user/profile`
3. Observe 500 Internal Server Error

---

## 🔧 Fix Applied

Added a null check before accessing properties on the query result.

**Files Changed:**
- `src/services/UserService.js` — added null guard

**Code Snippet (Before):**
```javascript
const user = await db.findUser(id);
return user.name; // ❌ crashes if user is null
```

**Code Snippet (After):**
```javascript
const user = await db.findUser(id);
if (!user) {
  throw new NotFoundError(`User ${id} not found`);
}
return user.name; // ✅ safe
```

---

## 🛡️ Prevention Measures

- [x] Unit test added: `test/UserService.test.js` covers the null case
- [x] Code review checklist updated to flag missing null checks
- [ ] Lint rule to be added for mandatory null checks on DB results

---

## 📎 References

- Issue: #1
- Fix PR: #2
- Related issues: None
