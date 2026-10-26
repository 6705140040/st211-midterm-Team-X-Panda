# AI Usage Declaration and Audit

**Group:** Team X-Panda  
**Members:** 
- Aung Myo Hlaing (Olary) - 6705140040
- Hein Zaw Lin (Hubert) - 6705140038
- Hein Thura Naung (Ivan) - 6705140056
- Chan Myae Thaw Tar (Chan) - 6705140048
- Aye Than Tin (Aye) - 6705140074

**Part D3 of the midterm — 20 marks.** Part 1 is required but carries no marks; its absence is an academic-honesty matter. Part 2 is worth 16 (2 per test). Parts 3 and 4 together are worth 4.

Before you submit, check all boxes:

- [x] Part 1 declaration complete, or the "no AI used" statement written
- [x] Custom test suite (smoke, regression, slow) fully documented with authors
- [x] Part 3 coverage table filled in against FINDINGS.md
- [x] Part 4 verdict written, under 400 words
- [x] File committed as AI_USAGE.md in the repository root

---

## Part 1 — AI usage declaration (required, unmarked)

Every AI tool any member used anywhere in this project. Using AI is allowed. Not declaring it is not.

| Tool | What we used it for | Where in the project | How we checked it before relying on it |
|---|---|---|---|
| GitHub Copilot / LLMs | Cross-referencing test structure syntax and structuring markdown documentation | `tests/`, `AI_USAGE.md`, REPORT.md | Manually executed all pytest runs against shipped and fixed codebases to verify empirical accuracy |

---

## Part 2 — Team X-Panda Custom Test Suite Audit (`tests/test_bookstore.py`)

Below is the inventory of custom tests authored and executed by Team X-Panda, categorized by test type (`@pytest.mark.smoke`, `@pytest.mark.regression`, `@pytest.mark.slow`), including their target behavior and verification status.

| # | Test Function Name | Test Type | Purpose / What It Validates | Author(s) | Status |
|---|---|---|---|---|---|
| 1 | test_smoke_catalog_add | Smoke | Verifies basic catalog initialization and product addition. | Ivan | **PASSED** |
| 2 | test_smoke_cart_add | Smoke | Verifies valid product addition to the shopping cart. | Hubert | **PASSED** |
| 3 | test_smoke_user_login | Smoke | Verifies registered user authentication and login success. | Olary | **PASSED** |
| 4 | test_smoke_cart_history_empty | Smoke | Verifies that order history initializes as an empty list. | Chan | **PASSED** |
| 5 | test_smoke_cart_remove_item | Smoke | Verifies basic item removal functionality from the cart. | Aye | **PASSED** |
| 6 | test_regression_cart_total_sums_all_items | Regression | Catches cart total calculation skipping the final item index (`-1` bug). | Ivan, Hubert | **PASSED** (After Fix) |
| 7 | test_regression_user_login_with_symbols | Regression | Catches login failure when passwords contain special symbols stripped by `.isalnum()`. | Chan | **PASSED** (After Fix) |
| 8 | test_regression_catalog_search_limit | Regression | Catches unconstrained catalog search results exceeding the 10-item limit. | Olary | **PASSED** (After Fix) |
| 9 | test_slow_bulk_import_performance | Slow | Simulates bulk importing 50 products and validates exact import count. | Olary | **PASSED** (After Fix) |
| 10 | test_slow_catalog_heavy_search | Slow | Simulates heavy catalog search filtering across 100 items. | Chan, Aye | **PASSED** (After Fix) |

---

## Part 3 — Coverage against your own bug hunt

| Bug (from `FINDINGS.md`) | Caught by Team X-Panda Test? | Test Function Name | How it was established |
|---|---|---|---|
| Cart total calculation skips the final item | Yes | `test_regression_cart_total_sums_all_items` | Failed on the shipped code because the total was 10 instead of 30. Passed after fixing the loop. |
| Bulk import return count is one too high | Yes | `test_slow_bulk_import_performance` | Failed on the shipped code because it returned 51 instead of 50. Passed after removing the extra `+ 1`. |
| Empty cart checkout returns an empty list instead of `None` | Verify against the custom test suite | `test_checkout_empty_returns_none` | Failed because checkout returned `[]` instead of `None`. Passed after adding an empty-cart check. |
| Login fails when passwords contain special characters | Yes | `test_regression_user_login_with_symbols` | Failed when logging in with `p@ssword123!`. Passed after removing the character-stripping logic. |
| Catalog search does not limit results to 10 | Yes | `test_regression_catalog_search_limit` | Failed because the search returned more than 10 results. Passed after limiting the returned product IDs to 10. |



---

## Part 4 — Verdict (4 marks, 400 words maximum)


**1. Which testing tier was most critical during debugging?**

Our regression testing tier was the most critical because it helped us identify specific bugs and check whether our fixes worked. The tests for cart totals, login passwords, and catalog search showed the incorrect behavior before the fixes and helped us verify the corrected behavior afterward.

**2. Why is a test that passes against buggy code more dangerous than one that crashes?**

A test that crashes shows that something may be wrong and needs attention. However, a test that passes against buggy code can give developers false confidence that the program works correctly. As a result, bugs may remain undetected.

**3. Did our custom test suite cover all identified bugs?**

Our findings log records five bugs. Four are explicitly listed in our current custom test inventory. We need to verify whether the empty-cart checkout test is also included in `tests/test_bookstore.py` before claiming that our custom suite covers all five bugs.

**4. What will you check before trusting a generated test in future?**

We will check whether the test covers the intended behavior and fails against the buggy version of the code. We will then run it against the fixed version to confirm that it passes. This helps us avoid tests that pass without detecting the actual problem.
