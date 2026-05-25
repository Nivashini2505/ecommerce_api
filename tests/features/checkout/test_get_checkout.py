"""Checkout retrieval and status tests."""


def test_get_checkout_status(client):
    """Test retrieving checkout/order status."""
    # First create a checkout
    product_data = {
        "name": "Product",
        "price": 1000,
        "quantity": 10,
        "category": "General"
    }
    product_response = client.post('/products', json=product_data)
    product_id = product_response.get_json()["product"]["id"]
    
    checkout_data = {
        "product_id": product_id,
        "quantity": 2,
        "total_price": 2000
    }
    checkout_response = client.post('/checkout', json=checkout_data)
    order_id = checkout_response.get_json()["order"]["id"]
    
    # Get checkout status
    response = client.get(f'/checkout/{order_id}')
    assert response.status_code == 200
    assert response.get_json()["status"] == "pending"


def test_get_checkout_not_found(client):
    """Test retrieving non-existent checkout."""
    response = client.get('/checkout/999')
    assert response.status_code == 404


def test_get_all_checkouts(client):
    """Test retrieving all checkouts/orders."""
    response = client.get('/checkout')
    assert response.status_code == 200
    assert "orders" in response.get_json()
    assert "count" in response.get_json()


def test_checkout_status_transitions(client):
    """Test checkout status changes (pending -> confirmed -> completed)."""
    # Create checkout
    product_data = {
        "name": "Test Product",
        "price": 500,
        "quantity": 10,
        "category": "Test"
    }
    product_response = client.post('/products', json=product_data)
    product_id = product_response.get_json()["product"]["id"]
    
    checkout_data = {
        "product_id": product_id,
        "quantity": 1,
        "total_price": 500
    }
    checkout_response = client.post('/checkout', json=checkout_data)
    order_id = checkout_response.get_json()["order"]["id"]
    
    # Initial status should be pending
    response = client.get(f'/checkout/{order_id}')
    assert response.get_json()["status"] == "pending"
    
    # Confirm checkout
    confirm_response = client.post(f'/checkout/{order_id}/confirm', json={})
    assert confirm_response.status_code == 200
    assert confirm_response.get_json()["status"] == "confirmed"
