"""
Product retrieval tests.
Tests for getting products from the ecommerce API.
"""


def test_get_all_products(client):
    """Test getting all products."""
    # First, add one product
    client.post('/products', json={
        "name": "Tablet",
        "price": 25000,
        "quantity": 4,
        "category": "Electronics"
    })

    # Now get all products
    response = client.get('/products')

    assert response.status_code == 200
    data = response.get_json()
    assert data["count"] == 1


def test_get_single_product(client):
    """Test getting a specific product by ID."""
    # First, add a product
    client.post('/products', json={
        "name": "Mouse",
        "price": 500,
        "quantity": 10,
        "category": "Accessories"
    })

    # Get the first product (ID = 1)
    response = client.get('/products/1')

    assert response.status_code == 200


def test_product_not_found(client):
    """Test getting a non-existent product."""
    # Try to get a product that doesn't exist (ID = 999)
    response = client.get('/products/999')

    assert response.status_code == 404
