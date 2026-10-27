# AI Usage Declaration and Test Audit

**Group:** Team X-Panda

**Members:**

- Aung Myo Hlaing (Olary) - 6705140040
- Hein Zaw Lin (Hubert) - 6705140038
- Hein Thura Naung (Ivan) - 6705140056
- Chan Myae Thaw Tar (Chan) - 6705140048
- Aye Than Tin (Aye) - 6705140074

**Part D3 of the midterm - 20 marks.** Part 1 is required but unmarked.
Part 2 is worth 16 marks, and Parts 3 and 4 together are worth 4 marks.

## Part 1 - AI usage declaration

| AI tool | What it was used for | Where it was used | How the output was checked |
|---|---|---|---|
| Codex / LLM Assistant | Helped plan catalog smoke and regression tests, review search fixes and workflow scripts, and structure test-audit documentation. | `tests/test_bookstore.py`, `FINDINGS.md`, `AI_USAGE.md`, `REPORT.md` | Suggestions were reviewed manually. Regression tests were checked with pytest against the original and fixed application versions. |
| GitHub Copilot (Copilot SDK) | Helped organize and format this audit and verify the supplied test set against the original and fixed revisions. | `AI_USAGE.md`, `templates/AI_USAGE.md`, `ai_review/test_ai_generated.py` | The report was checked against the repository history, project findings, and actual pytest output for both code versions. |

## Part 2 - Audit of the supplied test set

The supplied tests are in `ai_review/test_ai_generated.py`. Each test was run
against the original application from commit `53beb74` and against the fixed
application in the current working tree. The complete pytest outputs are
included in the Evidence section below.

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

### Test-by-test findings

1. **`test_cart_total_sums_items` - Hein Thura Naung (Ivan).** The shipped code
   returned 10 instead of 30, omitting the last item's price. It passes after
   the total loop was fixed. **Genuine detection (FAIL then PASS).**
2. **`test_login_rejects_wrong_password` - Aung Myo Hlaing (Olary).** A regular
   incorrect password is rejected in both versions. This does not exercise the
   special-character password bug. **Detects nothing (PASS then PASS).**
3. **`test_search_finds_exact_title` - Hein Zaw Lin (Hubert).** Exact-title
   search works in both versions, so the test detects no defect.
   **Detects nothing (PASS then PASS).**
4. **`test_import_returns_count` - Chan Myae Thaw Tar (Chan).** The shipped
   code returned 3 for two imported products. It passes after the extra count
   increment was removed. **Genuine detection (FAIL then PASS).**
5. **`test_register_duplicate_returns_false` - Aye Than Tin (Aye).** Duplicate
   registration already returned `False` in the shipped version.
   **Detects nothing (PASS then PASS).**
6. **`test_checkout_empty_returns_none` - Hein Thura Naung (Ivan).** The shipped
   code returned `[]` instead of `None`; it passes after the empty-cart check
   was added. **Genuine detection (FAIL then PASS).**
7. **`test_add_to_cart_returns_true_for_known_product` - Aung Myo Hlaing
   (Olary).** Adding a known product works in both versions.
   **Detects nothing (PASS then PASS).**
8. **`test_search_is_limited_to_ten_results` - Hein Zaw Lin (Hubert).** The
   shipped code returned 20 matching products. It passes after the search limit
   was implemented. The team's findings and regression suite also treat the
   ten-result limit as expected behavior. **Genuine detection (FAIL then PASS).**

## Part 3 - Coverage against the team's bug hunt

| Bug recorded in `FINDINGS.md` | Team found it | Supplied set catches it | Test and evidence |
|---|---|---|---|
| Cart total skips the final item. | Yes | Yes | `test_cart_total_sums_items` fails on shipped code (10 instead of 30) and passes on fixed code. |
| Bulk import returns a count one too high. | Yes | Yes | `test_import_returns_count` fails on shipped code (3 instead of 2) and passes on fixed code. |
| Empty-cart checkout returns `[]` instead of `None`. | Yes | Yes | `test_checkout_empty_returns_none` fails on shipped code and passes on fixed code. |
| Login strips special characters from passwords. | Yes | No | `test_login_rejects_wrong_password` passes on both versions. The team's `test_regression_user_login_with_symbols` checks the affected password case. |
| Catalog search does not limit results to ten. | Yes | Yes | `test_search_is_limited_to_ten_results` fails with 20 results on shipped code and passes on fixed code. The team's `test_regression_catalog_search_limit` also covers this behavior. |

## Part 4 - Verdict

**1. Which failure mode was most common?**
“Detects nothing” was the most common verdict: 4 of 8 tests (tests 2, 3, 5,
and 7).

**2. Why is a test that passes against buggy code more dangerous than one that
crashes?**
A crashing test draws attention to a problem. A test that passes against buggy
code creates false confidence and can let a defect go unnoticed.

**3. Did the supplied set catch anything the team had missed?**
No. The genuine detections correspond to bugs the team had already found and
recorded in `FINDINGS.md`.

**4. What will the team check before trusting a generated test in future?**
The team will run each test against both the original shipped code and the
fixed code, then check whether the failure and pass results support the claimed
defect.

## Evidence - pytest output

Both runs execute all eight tests. The shipped run uses an isolated extraction
of the original repository commit `53beb74`; the fixed run uses the current
working tree. The failing assertions below are the observed results, not
retyped summaries.

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
