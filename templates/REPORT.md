# REPORT.md

Group: Team X-Panda  
Members: 
- Aung Myo Hlaing (Olary) - 6705140040
- Hein Zaw Lin (Hubert) - 6705140038
- Hein Thura Naung (Ivan) - 6705140056
- Chan Myae Thaw Tar (Chan) - 6705140048
- Aye Than Tin (Aye) - 6705140074

## Part A -- Test types

1. **Smoke Testing (`@pytest.mark.smoke`)**
   * **Definition:** A rapid, minimal verification test designed to check basic system stability and core functionality. 
   * **When it runs:** Executed immediately after a new build or deployment to determine if the software is stable enough for deeper testing.
   * **Bookstore Examples:** 
     - Verifying that the catalog initializes and successfully adds a single product.
     - Checking that instantiating an empty shopping cart works without errors.

2. **Regression Testing (`@pytest.mark.regression`)**
   * **Definition:** Targeted testing executed to ensure that recent code modifications, bug fixes, or refactoring have not broken existing, previously working features.
   * **When it runs:** Run before every code commit or merge, and automatically triggered in CI/CD pipelines upon pushing updates.
   * **Bookstore Examples:** 
     - Verifying that the cart total calculation correctly sums all items without skipping the final index.
     - Confirming that user login successfully authenticates passwords containing special symbols.

3. **Slow Testing (`@pytest.mark.slow`)**
   * **Definition:** Resource-intensive or time-consuming tests (involving large data arrays, loops, or artificial delays) that simulate performance limits or heavy load.
   * **When it runs:** Typically excluded from rapid local pre-commit cycles; executed during nightly builds, staging pipelines, or full test suite evaluations.
   * **Bookstore Examples:** 
     - Bulk importing a large batch of 50+ products into the catalog in a single operation.
     - Simulating heavy database searches across extensive product catalogs.

---

## Part B -- Scenario classification

1. **Catalog Search & Result Limiting**
   * **Classification:** Regression
   * **Justification:** This scenario guards against search constraint bugs where queries returned unconstrained matches rather than capping results at 10. Running this test during pre-commit checks ensures search pagination and filtering logic remain intact.

2. **Shopping Cart Total Calculation**
   * **Classification:** Regression
   * **Justification:** It directly targets fixed defects like the loop index bug that previously skipped the final item in price aggregations. Running this test ensures multi-item arithmetic stays accurate across future code changes.

3. **User Authentication with Special Characters**
   * **Classification:** Regression
   * **Justification:** It verifies that password validation correctly handles alphanumeric and special punctuation symbols after code fixes related to strict character stripping. It prevents regressions when modifying authentication security modules.

4. **Checkout Processing (Empty vs. Populated Carts)**
   * **Classification:** Smoke / Regression
   * **Justification:** It serves as a fundamental sanity check (smoke) to ensure checkout execution doesn't crash the application, while also testing edge cases like empty carts safely returning None (regression). This dual role makes it critical for both build stability and data integrity.

5. **Bulk Product Import Performance**
   * **Classification:** Slow
   * **Justification:** Processing large datasets and bulk database insertions takes extra execution time and system resources. Decoupling this from fast local test loops prevents developer workflow slowdowns during rapid prototyping.

6. **Item Removal from Shopping Cart**
   * **Classification:** Smoke
   * **Justification:** It performs a rapid sanity check on primary cart interactions to confirm basic item deletion works before deep integration testing begins. A failure here indicates fundamental cart state corruption.

---

## Part F -- Team reflection
1. Why is running only regression tests before every commit inefficient?
2. Why do smoke tests usually run first in a CI/CD pipeline?
3. What risks arise if slow tests are never run?
4. Can one test belong to two categories? Give an example.
5. Bug-finders and bug-fixers are often different people in a real QA team.
   What does that separation change about how a bug report must be written?
