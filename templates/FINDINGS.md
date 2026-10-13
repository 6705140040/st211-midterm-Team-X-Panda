# Bug-Hunt Findings Log

**Group:** Team X-Panda
**Members:**
- Aung Myo Hlaing (Olary) - 6705140040
- Hein Zaw Lin (Hubert) - 6705140038
- Hein Thura Naung (Ivan) - 6705140056
- Chan Myae Thaw Tar (Chan) - 6705140048
- Aye Than Tin (Aye) - 6705140074

---

## Bug 1
- **Module / function:** `cart.py -> total()`
- **What we suspected and why:** Our test `test_regression_cart_total_sums_all_items` failed. We had two items, priced 10 and 20. The total was 10, not 30. We thought the loop was missing one item.
- **What we did:** We checked the loop in `total()`. First we thought the price dictionary was wrong. Then we traced the loop and found the problem was with the indices.
- **What we observed:** The total only counted the first item. It skipped the last one (`assert 10 == 30`).
- **What we expected instead:** The sum of all items in the cart, which is 30.
- **The fix:** The loop was `for i in range(len(self.items) - 1):`. It stopped one item too early. We changed it to `for pid in self.items:`.
- **Author of this finding:** Ivan

---

## Bug 2
- **Module / function:** `cart.py -> import_products()`
- **What we suspected and why:** Our bulk-import test loaded 50 products and expected a count of 50. It returned 51. We thought an extra number was being added.
- **What we did:** We looked at the end of `import_products`. We followed the `count` variable through the loop to find the extra one.
- **What we observed:** The method returned `51`. The test `assert count == 50` failed.
- **What we expected instead:** The exact number of items that were processed.
- **The fix:** The return line had a hardcoded `+ 1`. We changed `return count + 1` to `return count`.
- **Author of this finding:** Olary

---

## Bug 3
- **Module / function:** `cart.py -> checkout()`
- **What we suspected and why:** The AI-generated test `test_checkout_empty_returns_none` failed. Checking out an empty cart gave `[]`, not `None`.
- **What we did:** We read the `checkout()` code and compared it with the docstring. The docstring says it returns the order list, or None if the cart is empty.
- **What we observed:** An empty cart returned `[]`. This caused `AssertionError: assert [] is None`.
- **What we expected instead:** `None` for an empty cart.
- **The fix:** We added a check at the start of the method: `if not self.items: return None`.
- **Author of this finding:** Chan & Aye

---

## Bug 4
- **Module / function:** `users.py -> login()`
- **What we suspected and why:** Our test registered a user with the password `p@ssword123!`. Login failed, even though the password was saved correctly.
- **What we did:** We opened `users.py` and compared how passwords are handled in register and in login. We found a line in login that changes the password text.
- **What we observed:** Login removed all non-letter and non-number characters with `.isalnum()`. So passwords with symbols never matched.
- **What we expected instead:** Login should work with passwords that have symbols.
- **The fix:** We removed the `cleaned` variable that stripped the characters. Now the original password is compared with the saved one.
- **Author of this finding:** Chan

---

## Bug 5
- **Module / function:** `catalog.py -> search()`
- **What we suspected and why:** The AI-generated test and our own test both expected at most 10 search results. But a search with 20 matches returned all 20.
- **What we did:** We looked at the loop in `search()`. We also tried returning the full list first. The tests that check for a 10-item limit failed.
- **What we observed:** Search returned every match, with no limit (`len = 20` when `<= 10` was expected).
- **What we expected instead:** A maximum of 10 results.
- **The fix:** We cut the list of product IDs with `[:10]`.
- **Author of this finding:** Ivan & Hubert
