"""
Product update tests.
Tests for updating product information in the ecommerce API.
"""


def test_update_product(client):
    """Test successful product update."""
    # First, add a product
    client.post('/products', json={
        "name": "Keyboard",
        "price": 1500,
        "quantity": 5,
        "category": "Accessories"
    })

    # Update the price of first product
    response = client.put('/products/1', json={
        "price": 2000
    })

    assert response.status_code == 200
    data = response.get_json()
    assert data["product"]["price"] == 2000


def test_update_non_existing_product(client):
    """Test updating a product that doesn't exist."""
    response = client.put('/products/999', json={
        "price": 2000
    })

    assert response.status_code == 404
