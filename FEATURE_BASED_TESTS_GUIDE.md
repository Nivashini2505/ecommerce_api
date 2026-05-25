# Feature-Based Test Structure Guide

## Overview

This document explains the feature-based test organization structure for the ecommerce API. Tests are organized by **business features** rather than by type (unit, integration, etc.).

---

## 📁 Directory Structure

```
ecommerce_api/
├── app.py
├── models.py
├── requirements.txt
│
└── tests/                          # Root tests directory
    ├── __init__.py
    ├── conftest.py                 # Shared fixtures (client, app_context)
    ├── pytest.ini                  # pytest configuration
    │
    └── features/                   # Features directory
        ├── __init__.py
        │
        ├── products/               # 🛍️ PRODUCT FEATURE
        │   ├── __init__.py
        │   ├── conftest.py         # Product-specific fixtures (optional)
        │   ├── test_add_product.py          (Add/create products)
        │   ├── test_get_products.py         (Retrieve products)
        │   ├── test_update_product.py       (Modify products)
        │   ├── test_delete_product.py       (Remove products)
        │   └── test_product_validation.py   (Input validation)
        │
        ├── categories/             # 🏷️ CATEGORY FEATURE
        │   ├── __init__.py
        │   ├── conftest.py         # Category-specific fixtures (optional)
        │   └── test_category_validation.py  (Category rules)
        │
        └── checkout/               # 💳 CHECKOUT FEATURE (Future)
            ├── __init__.py
            ├── conftest.py         # Checkout-specific fixtures (optional)
            └── test_checkout.py     (Order processing, payment, etc.)
```

---

## 🎯 Features Explained

### 1. **Products Feature** (🛍️)
Everything related to product management:
- **test_add_product.py**: Creating new products
- **test_get_products.py**: Retrieving products
- **test_update_product.py**: Modifying existing products
- **test_delete_product.py**: Removing products
- **test_product_validation.py**: Input validation (price, quantity, name)

### 2. **Categories Feature** (🏷️)
Everything related to product categories:
- **test_category_validation.py**: Category validation rules
- Tests ensure categories are properly validated
- Tests ensure whitespace is trimmed

### 3. **Checkout Feature** (💳)
(Placeholder for future implementation)
- Order creation and processing
- Payment handling
- Order history and status
- Refunds and cancellations

---

## 🚀 Running Tests

### Run All Tests
```bash
pytest tests/
```

### Run Tests for Specific Feature
```bash
# Products feature only
pytest tests/features/products/

# Categories feature only
pytest tests/features/categories/

# Checkout feature only
pytest tests/features/checkout/
```

### Run Specific Test File
```bash
pytest tests/features/products/test_add_product.py
```

### Run Tests with Verbose Output
```bash
pytest tests/ -v
```

### Run Tests by Marker
```bash
# Run all product tests
pytest tests/ -m products

# Run all validation tests
pytest tests/ -m validation
```

---

## 📊 Test Statistics

| Feature | Test Files | Test Cases | Status |
|---------|------------|-----------|--------|
| Products | 5 files | 13 tests | ✅ Ready |
| Categories | 1 file | 4 tests | ✅ Ready |
| Checkout | 1 file | 1 placeholder | 🚧 TODO |
| **Total** | **7 files** | **18 tests** | ✅ |

---

## 🔧 How to Add New Tests for a Feature

### Example: Adding a "Orders" Feature

1. **Create directory structure**:
   ```bash
   mkdir -p tests/features/orders
   ```

2. **Create `__init__.py`**:
   ```python
   """Orders feature tests."""
   ```

3. **Create `conftest.py`** (if needed):
   ```python
   """Orders feature fixtures."""
   import pytest
   
   @pytest.fixture
   def order_data():
       return {
           "product_id": 1,
           "quantity": 2,
           "total_price": 10000
       }
   ```

4. **Create test files by test type**:
   - `test_create_order.py` - Creating orders
   - `test_get_orders.py` - Retrieving orders
   - `test_order_validation.py` - Validation rules

5. **Write tests**:
   ```python
   def test_create_order_success(client, order_data):
       response = client.post('/orders', json=order_data)
       assert response.status_code == 201
   ```

---

## 🏗️ Conftest.py Hierarchy

### Root conftest.py (`tests/conftest.py`)
- **Shared Fixtures**: Available to ALL tests
- Contains: `client`, `app_context`
- Used by: All features

### Feature-Specific conftest.py
- **Optional**: Only create if feature needs unique fixtures
- Example: `tests/features/products/conftest.py`
- Contains: Product-specific factories or data

---

## 📋 Fixtures Available

### From Root `conftest.py`:

**1. `client` fixture**
```python
def test_example(client):
    response = client.post('/products', json={...})
    assert response.status_code == 201
```
- Flask test client
- In-memory SQLite database
- Auto cleanup after each test

**2. `app_context` fixture**
```python
def test_with_context(app_context):
    # Can perform database operations here
    from models import Product
    products = Product.query.all()
```
- Application context for database access
- Useful for setup/assertions

---

## 🎯 Best Practices

### ✅ DO:
1. **Group by Feature**: Keep all tests for one feature in same folder
2. **Organize by Operation**: Separate files for create, read, update, delete
3. **Clear Naming**: Use descriptive test function names
4. **Share Fixtures**: Put common fixtures in conftest.py
5. **Document Intent**: Add docstrings to test functions

### ❌ DON'T:
1. **Don't Mix Features**: Keep products tests separate from orders tests
2. **Don't Repeat Code**: Use fixtures for common setup
3. **Don't Test Everything**: Focus on behavior, not implementation
4. **Don't Ignore Validation**: Test edge cases and error conditions

---

## 📈 Migration Path

### From Old Structure (Single File)
```
test_api.py  (19 tests in one file)
```

### To New Structure (Feature-Based)
```
tests/
├── features/
│   ├── products/ (13 tests across 5 files)
│   ├── categories/ (4 tests in 1 file)
│   └── checkout/ (1 placeholder)
```

**Benefits**:
- ✅ Better organization
- ✅ Easier to find tests
- ✅ Clearer feature separation
- ✅ Easier to add new features
- ✅ Better for team collaboration

---

## 🔍 Example Test Structure

### File: `test_add_product.py`
```python
"""
Product addition tests.
Tests for adding new products to the ecommerce API.
"""

def test_add_product_success(client):
    """Test successful product creation."""
    new_product = {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": "Electronics"
    }
    response = client.post('/products', json=new_product)
    assert response.status_code == 201
    data = response.get_json()
    assert data["product"]["name"] == "Laptop"
```

---

## 📚 Related Commands

```bash
# Run tests with coverage
pytest tests/ --cov=app --cov=models

# Generate coverage report
pytest tests/ --cov --cov-report=html

# Run specific test with output
pytest tests/features/products/test_add_product.py::test_add_product_success -v -s

# Run tests and stop on first failure
pytest tests/ -x

# Run last failed tests
pytest tests/ --lf
```

---

## 🤔 FAQ

**Q: Should I move the old test_api.py?**
A: Yes! Archive it or delete it once all tests are migrated to the new structure.

**Q: How do I handle shared test data?**
A: Use fixtures in `conftest.py`. Create feature-specific fixtures in feature conftest.py.

**Q: Can I have tests outside features/?**
A: Yes! Use `tests/` root for integration tests that span multiple features.

**Q: How do I run just validation tests?**
A: Use pytest markers: `pytest tests/ -m validation`

---

## ✅ Checklist for New Features

- [ ] Create feature directory under `tests/features/`
- [ ] Create `__init__.py`
- [ ] Create `conftest.py` (if needed for feature-specific fixtures)
- [ ] Create test files (`test_*.py`) organized by operation
- [ ] Add docstrings to all test functions
- [ ] Run tests to ensure they pass
- [ ] Add feature marker in `pytest.ini` if needed
- [ ] Update this guide with new feature info

---

Last Updated: 2026-05-25
