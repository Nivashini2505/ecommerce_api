"""
Category validation tests.
Tests for validating product categories in the ecommerce API.
"""


def test_invalid_category_type(client):
    """Test that API rejects non-string categories."""
    invalid_product = {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": 123  # Wrong! Category should be text
    }

    response = client.post('/products', json=invalid_product)

    assert response.status_code == 400


def test_empty_category(client):
    """Test that API rejects empty categories."""
    product_with_empty_category = {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": ""  # Wrong! Category cannot be empty
    }

    response = client.post('/products', json=product_with_empty_category)

    assert response.status_code == 400


def test_missing_category_field(client):
    """Test that API requires category field."""
    response = client.post('/products', json={
        "name": "Laptop",
        "price": 50000,
        "quantity": 5
    })

    assert response.status_code == 400


def test_category_with_whitespace(client):
    """Test that category whitespace is trimmed."""
    response = client.post('/products', json={
        "name": "Phone",
        "price": 30000,
        "quantity": 3,
        "category": "  Mobile Devices  "
    })

    assert response.status_code == 201

    data = response.get_json()
    assert data["product"]["category"] == "Mobile Devices"
