# AI Usage Declaration and Test Audit

**Group:** Team X-Panda

**Members:**

- Aung Myo Hlaing (Olary) — 6705140040
- Hein Zaw Lin (Hubert) — 6705140038
- Hein Thura Naung (Ivan) — 6705140056
- Chan Myae Thaw Tar (Chan) — 6705140048
- Aye Than Tin (Aye) — 6705140074

**Part D3 of the midterm — 20 marks.** Part 1 is required but unmarked.
Part 2 is worth 16 marks, and Parts 3 and 4 together are worth 4 marks.

## Submission checklist

- [x] Part 1 AI usage declaration completed.
- [x] All eight supplied tests are listed with a verdict and auditor.
- [x] Complete pytest output for both code versions is included below.
- [x] Part 3 cross-referenced against the five findings.
- [x] Part 4 completed in under 400 words.
- [x] The audit identifies the member responsible for each test.
- [x] Completed submission copy saved as `AI_USAGE.md` in the repository root.

> **Evidence note:** Both complete pytest runs are included in the Evidence
> section below. The shipped run uses an isolated extraction of original commit
> `53beb74`; the fixed run uses the current working tree.

## Part 1 — AI usage declaration

Every AI tool used by any team member should be declared, including tools used
for planning, code, tests, or documentation.

| Tool | What it was used for | Where it was used | How its output was checked |
|---|---|---|---|
| Codex / LLM Assistant | Helped plan catalog smoke and regression tests, review search fixes and workflow scripts, and structure the test-audit documentation. | `tests/test_bookstore.py`, `FINDINGS.md`, `AI_USAGE.md`, `REPORT.md` | Reviewed suggestions manually and used pytest to check regression behavior against the shipped and fixed code. |
| GitHub Copilot (Copilot SDK) | Helped organize and format this audit and verify the supplied test set against the original and fixed revisions. | `AI_USAGE.md`, `templates/AI_USAGE.md`, `ai_review/test_ai_generated.py` | Checked the report against repository history, project findings, and actual pytest output for both code versions. |

If no AI tools were used, replace the table with:

> No AI tools were used in this project. All tests, bug investigation, and fixes
> were produced by the group.

## Part 2 — Audit of the supplied test set

The supplied tests are in `ai_review/test_ai_generated.py`. Each was compared
against the shipped and fixed versions. The pair of outcomes determines the
verdict:

| Shipped code | Fixed code | Verdict |
|---|---|---|
| FAIL | PASS | **Genuine detection** — the test detects a defect that was fixed. |
| PASS | PASS | **Detects nothing** — the test passes without detecting the defect. |
| PASS | FAIL | **Locks in the bug** — the test expects the buggy behavior. |
| FAIL | FAIL | **Invented requirement or unrelated failure** — investigate whether the asserted behavior is actually required. |

### Summary

| # | Test | What it claims to catch | Shipped | Fixed | Verdict | Auditor |
|---|---|---|---|---|---|---|
| 1 | `test_cart_total_sums_items` | Cart total includes every item. | FAIL | PASS | Genuine detection | Hein Thura Naung (Ivan) |
| 2 | `test_login_rejects_wrong_password` | Login rejects an incorrect password. | PASS | PASS | Detects nothing | Aung Myo Hlaing (Olary) |
| 3 | `test_search_finds_exact_title` | Search finds a product by its exact title. | PASS | PASS | Detects nothing | Hein Zaw Lin (Hubert) |
| 4 | `test_import_returns_count` | Bulk import returns the number of products imported. | FAIL | PASS | Genuine detection | Chan Myae Thaw Tar (Chan) |
| 5 | `test_register_duplicate_returns_false` | Registering a duplicate username returns `False`. | PASS | PASS | Detects nothing | Aye Than Tin (Aye) |
| 6 | `test_checkout_empty_returns_none` | Checking out an empty cart returns `None`. | FAIL | PASS | Genuine detection | Hein Thura Naung (Ivan) |
| 7 | `test_add_to_cart_returns_true_for_known_product` | Adding a known product returns `True`. | PASS | PASS | Detects nothing | Aung Myo Hlaing (Olary) |
| 8 | `test_search_is_limited_to_ten_results` | Catalog search returns no more than ten matches. | FAIL | PASS | Genuine detection | Hein Zaw Lin (Hubert) |

> **Correction to the supplied notes:** They reported that test 8 failed against
> both versions. The actual fixed-code run in this workspace passes test 8.
> The team's findings and regression suite also record the ten-result limit as
> expected behavior, so the verified outcome pair is FAIL then PASS.

### Test details

#### 1. `test_cart_total_sums_items` — audited by Hein Thura Naung (Ivan)

- **Claim:** The cart total includes the prices of all items.
- **Shipped evidence:** The full run below shows `FAILED`; assertion was `10 == 30`.
- **Fixed evidence:** The full run below shows `PASSED`.
- **What it demonstrates:** The shipped loop omitted the last cart item; after the fix, the total includes both items.
- **Verdict:** **Genuine detection — FAIL then PASS.**

#### 2. `test_login_rejects_wrong_password` — audited by Aung Myo Hlaing (Olary)

- **Claim:** Login rejects an incorrect password.
- **Shipped evidence:** The full run below shows `PASSED`.
- **Fixed evidence:** The full run below shows `PASSED`.
- **What it demonstrates:** A normal wrong-password attempt is rejected in both versions. It does not exercise the special-character password bug.
- **Verdict:** **Detects nothing — PASS then PASS.**

#### 3. `test_search_finds_exact_title` — audited by Hein Zaw Lin (Hubert)

- **Claim:** Search finds a product when given its exact title.
- **Shipped evidence:** The full run below shows `PASSED`.
- **Fixed evidence:** The full run below shows `PASSED`.
- **What it demonstrates:** Exact-title search worked before and after the fixes; this test does not detect a defect.
- **Verdict:** **Detects nothing — PASS then PASS.**

#### 4. `test_import_returns_count` — audited by Chan Myae Thaw Tar (Chan)

- **Claim:** Bulk import returns the number of products imported.
- **Shipped evidence:** The full run below shows `FAILED`; assertion was `3 == 2`.
- **Fixed evidence:** The full run below shows `PASSED`.
- **What it demonstrates:** The shipped implementation returned a count one too high; removing the extra increment corrected it.
- **Verdict:** **Genuine detection — FAIL then PASS.**

#### 5. `test_register_duplicate_returns_false` — audited by Aye Than Tin (Aye)

- **Claim:** Registering a duplicate username returns `False`.
- **Shipped evidence:** The full run below shows `PASSED`.
- **Fixed evidence:** The full run below shows `PASSED`.
- **What it demonstrates:** Duplicate registration was already rejected in the shipped version, so this test does not detect a defect.
- **Verdict:** **Detects nothing — PASS then PASS.**

#### 6. `test_checkout_empty_returns_none` — audited by Hein Thura Naung (Ivan)

- **Claim:** Checking out an empty cart returns `None`.
- **Shipped evidence:** The full run below shows `FAILED`; assertion was `[] is None`.
- **Fixed evidence:** The full run below shows `PASSED`.
- **What it demonstrates:** The shipped implementation returned an empty list instead of the documented `None`; the empty-cart check fixed this.
- **Verdict:** **Genuine detection — FAIL then PASS.**

#### 7. `test_add_to_cart_returns_true_for_known_product` — audited by Aung Myo Hlaing (Olary)

- **Claim:** Adding a known product to the cart returns `True`.
- **Shipped evidence:** The full run below shows `PASSED`.
- **Fixed evidence:** The full run below shows `PASSED`.
- **What it demonstrates:** Normal cart addition worked in both versions; the test does not detect a defect.
- **Verdict:** **Detects nothing — PASS then PASS.**

#### 8. `test_search_is_limited_to_ten_results` — audited by Hein Zaw Lin (Hubert)

- **Claim:** Catalog search returns no more than ten results.
- **Shipped evidence:** The full run below shows `FAILED`; assertion was `20 <= 10`.
- **Fixed evidence:** The full run below shows `PASSED`.
- **What it demonstrates:** The shipped implementation returned more than ten matches, while the fixed implementation enforces the documented ten-result limit.
- **Verdict:** **Genuine detection — FAIL then PASS.**

## Part 3 — Coverage against the team's bug hunt

| Bug recorded in `FINDINGS.md` | Team found it | Supplied set catches it | Test and evidence |
|---|---|---|---|
| Cart total skips the final item. | Yes | Yes | `test_cart_total_sums_items` fails on the shipped version and passes on the fixed version. |
| Bulk import returns a count one too high. | Yes | Yes | `test_import_returns_count` fails on the shipped version and passes on the fixed version. |
| Empty-cart checkout returns `[]` instead of `None`. | Yes | Yes | `test_checkout_empty_returns_none` fails on the shipped version and passes on the fixed version. |
| Login strips special characters from passwords. | Yes | No | `test_login_rejects_wrong_password` passes on both versions. The team's `test_regression_user_login_with_symbols` covers the special-character case. |
| Catalog search does not limit results to ten. | Yes | Yes | `test_search_is_limited_to_ten_results` fails on the shipped version and passes on the fixed version. The team's `test_regression_catalog_search_limit` also covers this behavior. |

## Part 4 — Verdict

**1. Which failure mode was most common?**
“Detects nothing” was the most common verdict: 4 of the 8 tests (tests 2, 3,
5, and 7).

**2. Why is a test that passes against buggy code more dangerous than one that
crashes?**
A crashing test draws attention to a problem. A test that passes against buggy
code can create false confidence, allowing a defect to go unnoticed.

**3. Did the supplied set catch anything the team had missed?**
No. The genuine detections in the supplied set correspond to bugs the team had
already found and recorded in `FINDINGS.md`.

**4. What will the team check before trusting a generated test in future?**
The team will run each test against both the original shipped code and the
fixed code, then compare the outcomes to confirm that the test fails for the
defect and passes after the fix.

## Appendix (optional)

Add relevant prompts or brief notes about AI use here. Do not paste entire
conversations.

## Evidence - pytest output

The shipped run uses an isolated extraction of original commit `53beb74`. The
fixed run uses the current working tree. Each run executes all eight tests.

### Original shipped application

Command (run from an extracted copy of commit `53beb74`):

```powershell
py -m pytest -v --no-header --tb=short ai_review\test_ai_generated.py
```

```text
============================= test session starts =============================
collecting ... collected 8 items

ai_review/test_ai_generated.py::test_cart_total_sums_items FAILED        [ 12%]
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED [ 25%]
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED     [ 37%]
ai_review/test_ai_generated.py::test_import_returns_count FAILED         [ 50%]
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED [ 62%]
ai_review/test_ai_generated.py::test_checkout_empty_returns_none FAILED  [ 75%]
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED [ 87%]
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED [100%]

================================== FAILURES ===================================
_________________________ test_cart_total_sums_items __________________________
ai_review\test_ai_generated.py:16: in test_cart_total_sums_items
    assert c.total() == 30
E   assert 10 == 30
E    +  where 10 = total()
E    +    where total = <bookstore_app.cart.Cart object at 0x000002434B189A90>.total
__________________________ test_import_returns_count __________________________
ai_review\test_ai_generated.py:34: in test_import_returns_count
    assert c.import_products([(1, "A", 5), (2, "B", 6)]) == 2
E   AssertionError: assert 3 == 2
E    +  where 3 = import_products([(1, 'A', 5), (2, 'B', 6)])
E    +    where import_products = <bookstore_app.cart.Cart object at 0x000002434B152AD0>.import_products
______________________ test_checkout_empty_returns_none _______________________
ai_review\test_ai_generated.py:45: in test_checkout_empty_returns_none
    assert Cart(Catalog()).checkout() is None
E   assert [] is None
E    +  where [] = checkout()
E    +    where checkout = <bookstore_app.cart.Cart object at 0x000002434B153250>.checkout
E    +      where <bookstore_app.cart.Cart object at 0x000002434B153250> = Cart(<bookstore_app.catalog.Catalog object at 0x000002434B164C30>)
E    +        where <bookstore_app.catalog.Catalog object at 0x000002434B164C30> = Catalog()
____________________ test_search_is_limited_to_ten_results ____________________
ai_review\test_ai_generated.py:60: in test_search_is_limited_to_ten_results
    assert len(cat.search("match")) <= 10
E   AssertionError: assert 20 <= 10
E    +  where 20 = len([0, 1, 2, 3, 4, 5, ...])
E    +    where [0, 1, 2, 3, 4, 5, ...] = search('match')
E    +      where search = <bookstore_app.catalog.Catalog object at 0x000002434B1A1EB0>.search
=========================== short test summary info ===========================
FAILED ai_review/test_ai_generated.py::test_cart_total_sums_items - assert 10...
FAILED ai_review/test_ai_generated.py::test_import_returns_count - AssertionE...
FAILED ai_review/test_ai_generated.py::test_checkout_empty_returns_none - ass...
FAILED ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results
========================= 4 failed, 4 passed in 0.23s =========================
```

### Fixed application

Command (run from the repository root):

```powershell
py -m pytest -v --no-header --tb=short ai_review\test_ai_generated.py
```

```text
============================= test session starts =============================
collecting ... collected 8 items

ai_review/test_ai_generated.py::test_cart_total_sums_items PASSED        [ 12%]
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED [ 25%]
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED     [ 37%]
ai_review/test_ai_generated.py::test_import_returns_count PASSED         [ 50%]
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED [ 62%]
ai_review/test_ai_generated.py::test_checkout_empty_returns_none PASSED  [ 75%]
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED [ 87%]
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results PASSED [100%]

============================== 8 passed in 0.04s ==============================
```
