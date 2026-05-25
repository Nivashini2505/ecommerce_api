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


def test_duplicate_product(client):
    """Test that duplicate products are rejected."""
    product_data = {
        "name": "Phone",
        "price": 30000,
        "quantity": 2,
        "category": "Electronics"
    }
    client.post('/products', json=product_data)

    # Try to add the same product again
    response = client.post('/products', json=product_data)

    assert response.status_code == 409


def test_add_product_with_valid_category(client):
    """Test adding product with valid category."""
    response = client.post('/products', json={
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": "Electronics"
    })

    assert response.status_code == 201
