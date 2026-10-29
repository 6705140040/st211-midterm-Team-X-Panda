# AI Usage Declaration and Audit

*Group:* Team X-Panda

*Members:*

- Aung Myo Hlaing (Olary) - 6705140040
- Hein Zaw Lin (Hubert) - 6705140038
- Hein Thura Naung (Ivan) - 6705140056
- Chan Myae Thaw Tar (Chan) - 6705140048
- Aye Than Tin (Aye) - 6705140074

*Part D3 of the midterm — 20 marks.* Part 1 is required but carries no marks;
its absence is an academic-honesty matter. Part 2 is worth 16 (2 per test).
Parts 3 and 4 together are worth 4.

Before you submit, check all eight boxes:

- [x] Part 1 declaration complete.
- [x] All eight tests appear in the summary table with a verdict.
- [x] All eight tests have evidence from shipped and fixed code.
- [x] Part 3 coverage table filled in against `FINDINGS.md`.
- [x] Part 4 verdict written, under 400 words.
- [x] Every audit entry names the member who did it.
- [x] Claims are supported by the pytest runs recorded below.
- [x] File committed as `AI_USAGE.md` in the repository root.

---

## Part 1 — AI usage declaration (required, unmarked)

Every AI tool any member used anywhere in this project should be declared.
Using AI is allowed. Not declaring it is not.

| Tool | What we used it for | Where in the project | How we checked it before relying on it |
|---|---|---|---|
| Codex / LLM Assistant | Helped plan catalog smoke and regression tests, review search fixes and workflow scripts, and structure test-audit documentation. | `tests/test_bookstore.py`, `FINDINGS.md`, `AI_USAGE.md`, `REPORT.md` | Reviewed suggestions manually and ran pytest against the original and fixed application versions to check regression behavior. |
| GitHub Copilot (Copilot SDK) | Helped format and organize this audit and compare supplied test results across original and fixed revisions. | `AI_USAGE.md`, `templates/AI_USAGE.md`, `ai_review/test_ai_generated.py` | Compared the audit with repository history and project findings, and ran each supplied test individually against the original and fixed versions. |

If any AI tools were used but are not listed here, add them before submission.

---

## Part 2 — Audit of the supplied test set (16 marks)

The supplied tests are in `ai_review/test_ai_generated.py`. The shipped-code
run used an isolated extraction of original commit `53beb74`. The fixed-code
run used the current project checkout.

### Summary table

| # | Test | What it claims to catch | Shipped | Fixed | Verdict | Auditor |
|---|---|---|---|---|---|---|
| 1 | `test_cart_total_sums_items` | Checks that the cart total includes all items. | FAIL | PASS | Genuine detection | Hein Thura Naung (Ivan) |
| 2 | `test_login_rejects_wrong_password` | Checks that login rejects an incorrect password. | PASS | PASS | Detects nothing | Aung Myo Hlaing (Olary) |
| 3 | `test_search_finds_exact_title` | Search finds a product by its exact title. | PASS | PASS | Detects nothing | Hein Zaw Lin (Hubert) |
| 4 | `test_import_returns_count` | Checks that bulk import returns the number of products imported. | FAIL | PASS | Genuine detection | Chan Myae Thaw Tar (Chan) |
| 5 | `test_register_duplicate_returns_false` | Checks that registering a duplicate username returns `False`. | PASS | PASS | Detects nothing | Aye Than Tin (Aye) |
| 6 | `test_checkout_empty_returns_none` | Checks that checking out an empty cart returns `None`. | FAIL | PASS | Genuine detection | Hein Thura Naung (Ivan) |
| 7 | `test_add_to_cart_returns_true_for_known_product` | Checks that adding a known product to the cart returns `True`. | PASS | PASS | Detects nothing | Aung Myo Hlaing (Olary) |
| 8 | `test_search_is_limited_to_ten_results` | Claims that catalog search should return no more than ten matches. | FAIL | PASS | Genuine detection | Hein Zaw Lin (Hubert) |

### Detail entries

#### Test: `test_cart_total_sums_items` (`ai_review/test_ai_generated.py:10`)

*Audited by:* Hein Thura Naung — Ivan

*1. What it claims to catch.*

The cart total should include the prices of all items.

*2. Evidence — against the shipped code*

Run location: isolated extraction of original commit `53beb74`.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_cart_total_sums_items`

```text
F                                                                        [100%]
E   assert 10 == 30
FAILED ai_review/test_ai_generated.py::test_cart_total_sums_items - assert 10...
1 failed in 0.17s
```

*3. Evidence — against your fixed code*

Run location: current project checkout.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_cart_total_sums_items`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*4. What that pair proves.*

The test fails on the shipped code because the final cart item was omitted
from the total. It passes after the total loop was fixed.

*5. Verdict*

- [x] Genuine detection — FAIL then PASS

---

#### Test: `test_login_rejects_wrong_password` (`ai_review/test_ai_generated.py:17`)

*Audited by:* Aung Myo Hlaing — Olary

*1. What it claims to catch.*

Login should reject an incorrect password.

*2. Evidence — against the shipped code*

Run location: isolated extraction of original commit `53beb74`.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_login_rejects_wrong_password`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*3. Evidence — against your fixed code*

Run location: current project checkout.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_login_rejects_wrong_password`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*4. What that pair proves.*

The test passes on both versions. It uses a completely different password and
does not detect the special-character password bug.

*5. Verdict*

- [x] Detects nothing — PASS then PASS

---

#### Test: `test_search_finds_exact_title` (`ai_review/test_ai_generated.py:25`)

*Audited by:* Hein Zaw Lin — Hubert

*1. What it claims to catch.*

Search should find a product when given its exact title.

*2. Evidence — against the shipped code*

Run location: isolated extraction of original commit `53beb74`.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_search_finds_exact_title`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*3. Evidence — against your fixed code*

Run location: current project checkout.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_search_finds_exact_title`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*4. What that pair proves.*

The exact-title search passes on both versions. It does not expose the separate
search-limit defect, which is tested by `test_search_is_limited_to_ten_results`.

*5. Verdict*

- [x] Detects nothing — PASS then PASS

---

#### Test: `test_import_returns_count` (`ai_review/test_ai_generated.py:31`)

*Audited by:* Chan Myae Thaw Tar — Chan

*1. What it claims to catch.*

Bulk import should return the number of products imported.

*2. Evidence — against the shipped code*

Run location: isolated extraction of original commit `53beb74`.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_import_returns_count`

```text
F                                                                        [100%]
E   AssertionError: assert 3 == 2
FAILED ai_review/test_ai_generated.py::test_import_returns_count - AssertionE...
1 failed in 0.16s
```

*3. Evidence — against your fixed code*

Run location: current project checkout.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_import_returns_count`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*4. What that pair proves.*

The test fails on the shipped code and passes after the extra increment was
removed. The shipped implementation reported one more product than it imported.

*5. Verdict*

- [x] Genuine detection — FAIL then PASS

---

#### Test: `test_register_duplicate_returns_false` (`ai_review/test_ai_generated.py:38`)

*Audited by:* Aye Than Tin — Aye

*1. What it claims to catch.*

Registering a duplicate username should return `False`.

*2. Evidence — against the shipped code*

Run location: isolated extraction of original commit `53beb74`.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_register_duplicate_returns_false`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*3. Evidence — against your fixed code*

Run location: current project checkout.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_register_duplicate_returns_false`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*4. What that pair proves.*

Duplicate registration already returned `False` in the shipped version. This
test passes on both versions and does not detect a bug fixed by the group.

*5. Verdict*

- [x] Detects nothing — PASS then PASS

---

#### Test: `test_checkout_empty_returns_none` (`ai_review/test_ai_generated.py:44`)

*Audited by:* Hein Thura Naung — Ivan

*1. What it claims to catch.*

Checking out an empty cart should return `None`.

*2. Evidence — against the shipped code*

Run location: isolated extraction of original commit `53beb74`.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_checkout_empty_returns_none`

```text
F                                                                        [100%]
E   assert [] is None
FAILED ai_review/test_ai_generated.py::test_checkout_empty_returns_none - ass...
1 failed in 0.14s
```

*3. Evidence — against your fixed code*

Run location: current project checkout.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_checkout_empty_returns_none`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*4. What that pair proves.*

The shipped code returned an empty list rather than `None`. The test passes
after the empty-cart check was added.

*5. Verdict*

- [x] Genuine detection — FAIL then PASS

---

#### Test: `test_add_to_cart_returns_true_for_known_product` (`ai_review/test_ai_generated.py:51`)

*Audited by:* Aung Myo Hlaing — Olary

*1. What it claims to catch.*

Adding a known product to the cart should return `True`.

*2. Evidence — against the shipped code*

Run location: isolated extraction of original commit `53beb74`.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_add_to_cart_returns_true_for_known_product`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*3. Evidence — against your fixed code*

Run location: current project checkout.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_add_to_cart_returns_true_for_known_product`

```text
.                                                                        [100%]
1 passed in 0.02s
```

*4. What that pair proves.*

Adding a known product works in both versions. The test checks normal cart
behavior but does not detect a bug fixed by the group.

*5. Verdict*

- [x] Detects nothing — PASS then PASS

---

#### Test: `test_search_is_limited_to_ten_results` (`ai_review/test_ai_generated.py:58`)

*Audited by:* Hein Zaw Lin — Hubert

*1. What it claims to catch.*

Catalog search should return no more than ten results.

*2. Evidence — against the shipped code*

Run location: isolated extraction of original commit `53beb74`.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_search_is_limited_to_ten_results`

```text
F                                                                        [100%]
E   AssertionError: assert 20 <= 10
FAILED ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results - assert 20...
1 failed in 0.14s
```

*3. Evidence — against your fixed code*

Run location: current project checkout.

Command: `py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_search_is_limited_to_ten_results`

```text
.                                                                        [100%]
1 passed in 0.03s
```

*4. What that pair proves.*

The shipped code returned 20 matching products. The test passes after the
search was limited to ten results, as specified by the catalog search
docstring and the team's findings.

*5. Verdict*

- [x] Genuine detection — FAIL then PASS

---

## Part 3 — Coverage against your own bug hunt

One row per bug recorded in `FINDINGS.md`.

| Bug (from `FINDINGS.md`) | We found it | The supplied set catches it | Which test, and how you established that |
|---|---|---|---|
| Cart total skips the final item. | Yes | Yes | `test_cart_total_sums_items` fails on shipped code (10 instead of 30) and passes on fixed code. |
| Bulk import returns a count one too high. | Yes | Yes | `test_import_returns_count` fails on shipped code (3 instead of 2) and passes on fixed code. |
| Empty-cart checkout returns `[]` instead of `None`. | Yes | Yes | `test_checkout_empty_returns_none` fails on shipped code and passes on fixed code. |
| Login strips special characters from passwords. | Yes | No | `test_login_rejects_wrong_password` passes on both versions. The team's `test_regression_user_login_with_symbols` checks the affected password case. |
| Catalog search does not limit results to ten. | Yes | Yes | `test_search_is_limited_to_ten_results` fails with 20 results on shipped code and passes on fixed code. The team's `test_regression_catalog_search_limit` also covers this behavior. |

Every “Yes” in the supplied-set column points to a test classified as a
genuine detection above.

---

## Part 4 — Verdict (4 marks, 400 words maximum)

1. *Which failure mode was most common?*

   “Detects nothing” was the most common verdict: 4 of 8 tests (tests 2, 3, 5,
   and 7).
2. **Why is a test that passes against buggy code more dangerous than one that
   crashes?**

   A crashing test draws attention to a problem. A test that passes against
   buggy code creates false confidence and can let a defect go unnoticed.
3. *Did the supplied set catch anything you had missed?*

   No. The genuine detections correspond to bugs the team had already found
   and recorded in `FINDINGS.md`.
4. *What will you check before trusting a generated test in future?*

   The team will run each test against both the original shipped code and the
   fixed code, then check whether the failure and pass results support the
   claimed defect.

---

## Appendix (optional)

Note on AI Use: AI tools were used exclusively for brainstorming test file structures, checking pytest syntax, and organizing markdown formatting. No core application logic or bug-fixing code was generated by AI without manual team review and empirical verification via pytest.
