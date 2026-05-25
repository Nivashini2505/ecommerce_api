"""Checkout creation tests."""


def test_create_checkout_success(client):
    """Test successful checkout/order creation."""
    # First add a product
    product_data = {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": "Electronics"
    }
    product_response = client.post('/products', json=product_data)
    product_id = product_response.get_json()["product"]["id"]
    
    # Create checkout with product
    checkout_data = {
        "product_id": product_id,
        "quantity": 2,
        "total_price": 100000
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 201
    assert response.get_json()["order"]["status"] == "pending"


def test_checkout_with_invalid_product(client):
    """Test checkout with non-existent product."""
    checkout_data = {
        "product_id": 999,  # Non-existent
        "quantity": 2,
        "total_price": 100000
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400


def test_checkout_insufficient_stock(client):
    """Test checkout when product stock is insufficient."""
    # Add product with low stock
    product_data = {
        "name": "Limited Item",
        "price": 1000,
        "quantity": 2,  # Only 2 available
        "category": "Limited"
    }
    product_response = client.post('/products', json=product_data)
    product_id = product_response.get_json()["product"]["id"]
    
    # Try to checkout more than available
    checkout_data = {
        "product_id": product_id,
        "quantity": 5,  # Request 5 but only 2 available
        "total_price": 5000
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400
