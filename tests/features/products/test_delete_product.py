"""
Product deletion tests.
Tests for deleting products from the ecommerce API.
"""


def test_delete_product(client):
    """Test successful product deletion."""
    # First, add a product
    client.post('/products', json={
        "name": "Monitor",
        "price": 12000,
        "quantity": 2,
        "category": "Electronics"
    })

    # Delete the first product
    response = client.delete('/products/1')

    assert response.status_code == 200


def test_delete_non_existing_product(client):
    """Test deleting a product that doesn't exist."""
    response = client.delete('/products/999')

    assert response.status_code == 404
