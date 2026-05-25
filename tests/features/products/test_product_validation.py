"""
Product validation tests.
Tests for validating product data in the ecommerce API.
"""


def test_missing_fields(client):
    """Test that API rejects incomplete product data."""
    incomplete_product = {
        "name": "Laptop"
    }

    response = client.post('/products', json=incomplete_product)

    assert response.status_code == 400


def test_empty_body(client):
    """Test that API handles empty requests."""
    response = client.post('/products', json={})

    assert response.status_code == 400


def test_invalid_price_type(client):
    """Test that API validates price type."""
    invalid_product = {
        "name": "Laptop",
        "price": "abc",  # Wrong! Price should be a number
        "quantity": 5,
        "category": "Electronics"
    }

    response = client.post('/products', json=invalid_product)

    assert response.status_code == 400


def test_negative_price(client):
    """Test that API rejects negative prices."""
    product_with_negative_price = {
        "name": "Laptop",
        "price": -100,  # Wrong! Price cannot be negative
        "quantity": 5,
        "category": "Electronics"
    }

    response = client.post('/products', json=product_with_negative_price)

    assert response.status_code == 400


def test_negative_quantity(client):
    """Test that API rejects negative quantities."""
    product_with_negative_quantity = {
        "name": "Laptop",
        "price": 1000,
        "quantity": -1,  # Wrong! Quantity cannot be negative
        "category": "Electronics"
    }

    response = client.post('/products', json=product_with_negative_quantity)

    assert response.status_code == 400


def test_empty_name(client):
    """Test that API rejects empty product names."""
    product_with_empty_name = {
        "name": "",  # Wrong! Name cannot be empty
        "price": 1000,
        "quantity": 2,
        "category": "Electronics"
    }

    response = client.post('/products', json=product_with_empty_name)

    assert response.status_code == 400
