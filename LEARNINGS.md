# Dynamic Test-Subset Routing — Assignment Learnings

## Objective

The goal was to run only the tests related to changed files. This can save time in larger projects because unrelated tests do not need to run after every change.

## Steps completed

1. **Created the project structure**  
   I organized the project into `src` for application code and `tests` for test files.

2. **Added application code**  
   I created pricing, inventory, and cart modules. The cart uses the pricing functions, and the inventory module checks whether an item is in stock.

3. **Added tests**  
   I wrote tests for pricing, inventory, and cart behavior. These tests check expected results, including cart totals with a discount.

4. **Ran the full test suite**  
   I used `python3 -m pytest -v` to run all tests. The output showed **4 tests passed**.

5. **Created the test router**  
   The router maps changed source files to their related test files. For example, a change to `src/pricing.py` selects `tests/test_pricing.py`.

6. **Checked targeted test runs**  
   I ran the router with a changed file path and confirmed that it selected and ran the matching test. If no matching test is found, the router can run the full test suite as a fallback.

7. **Published the project**  
   I pushed the project to GitHub so the code and assignment work can be reviewed.

## What I learned

Dynamic test-subset routing connects changed files to relevant tests. It can make feedback faster while keeping the full test suite available as a fallback. I also learned how to organize Python source and test files, run tests with pytest, and publish a project using Git and GitHub.

## Repository

https://github.com/drutika6/dynamic-test-subset-routing