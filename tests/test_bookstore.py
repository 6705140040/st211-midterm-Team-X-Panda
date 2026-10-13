"""Your test suite. Write smoke, regression, and slow tests here.

Every test MUST carry exactly one marker (@pytest.mark.smoke / regression /
slow) and name its author in the docstring, e.g.:

    @pytest.mark.smoke
    def test_login_works():
        '''Author: <name>. Smoke test for login.'''

Run:  pytest             (all)     pytest -m smoke     pytest -m regression
"""
import time
import pytest
from bookstore_app import Users, Catalog, Cart


@pytest.mark.smoke
def test_example_register():
    """Author: <example>. Smoke: a new user can register."""
    assert Users().register("newuser", "password123") is True


# ---- YOUR SMOKE TESTS (at least 5) ----

@pytest.mark.smoke
def test_smoke_catalog_add():
    """Author: Ivan. Smoke: can add a product to catalog."""
    cat = Catalog()
    cat.add_product(1, "Python Programming", 500)
    assert 1 in cat.products

@pytest.mark.smoke
def test_smoke_cart_add():
    """Author: Hubert. Smoke: can add valid product to cart."""
    cat = Catalog()
    cat.add_product(1, "Book A", 100)
    c = Cart(cat)
    assert c.add(1) is True

@pytest.mark.smoke
def test_smoke_user_login():
    """Author: Olary. Smoke: registered user can log in."""
    u = Users()
    u.register("alice", "secret123")
    assert u.login("alice", "secret123") is True

@pytest.mark.smoke
def test_smoke_cart_history_empty():
    """Author: Chan. Smoke: order history starts empty."""
    c = Cart(Catalog())
    assert c.history() == []

@pytest.mark.smoke
def test_smoke_cart_remove_item():
    """Author: Aye. Smoke: can remove an existing item from the cart."""
    cat = Catalog()
    cat.add_product(1, "Book A", 150)
    c = Cart(cat)
    c.add(1)
    assert c.remove(1) is True

    
# ---- YOUR REGRESSION TESTS (the bug hunt) ----

@pytest.mark.regression
def test_regression_cart_total_sums_all_items():
    """Author: Ivan, HUbert. Regression: cart total should sum all items, not skip the last one."""
    cat = Catalog()
    cat.add_product(1, "Book 1", 10)
    cat.add_product(2, "Book 2", 20)
    c = Cart(cat)
    c.add(1)
    c.add(2)
    # This will fail on the buggy code because of the -1 index skip bug!
    assert c.total() == 30

@pytest.mark.regression
def test_regression_catalog_search_limit():
    """Author: Olary. Regression: catalog search should limit results to a maximum of 10."""
    cat = Catalog()
    for i in range(15):
        cat.add_product(i, "Python Book", 100)
    # This will fail on the buggy code because it returns all 15 results!
    assert len(cat.search("Python")) <= 10


# ---- YOUR SLOW TESTS (at least 2) ----

@pytest.mark.slow
def test_slow_bulk_import_performance():
    """Author: Olary. Slow: tests performance of bulk importing many products."""
    time.sleep(1.0) # Simulating a slow operation
    cat = Catalog()
    c = Cart(cat)
    products = [(i, f"Book {i}", 10) for i in range(50)]
    count = c.import_products(products)
    assert count == 50

@pytest.mark.slow
def test_slow_catalog_heavy_search():
    """Author: Chan, Aye. Slow: simulates heavy catalog search filtering."""
    time.sleep(1.0)
    cat = Catalog()
    for i in range(100):
        cat.add_product(i, f"Item {i}", 10)
    results = cat.search("Item")
    assert len(results) == 100