"""Checkout input validation tests."""


def test_checkout_missing_product_id(client):
    """Test checkout with missing product_id."""
    checkout_data = {
        "quantity": 2,
        "total_price": 100000
        # Missing product_id
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400


def test_checkout_missing_quantity(client):
    """Test checkout with missing quantity."""
    checkout_data = {
        "product_id": 1,
        "total_price": 100000
        # Missing quantity
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400


def test_checkout_missing_total_price(client):
    """Test checkout with missing total_price."""
    checkout_data = {
        "product_id": 1,
        "quantity": 2
        # Missing total_price
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400


def test_checkout_invalid_quantity_type(client):
    """Test checkout with invalid quantity type."""
    checkout_data = {
        "product_id": 1,
        "quantity": "invalid",  # Should be number
        "total_price": 100000
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400


def test_checkout_invalid_price_type(client):
    """Test checkout with invalid price type."""
    checkout_data = {
        "product_id": 1,
        "quantity": 2,
        "total_price": "invalid"  # Should be number
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400


def test_checkout_negative_quantity(client):
    """Test checkout with negative quantity."""
    checkout_data = {
        "product_id": 1,
        "quantity": -2,  # Cannot be negative
        "total_price": 100000
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400


def test_checkout_negative_price(client):
    """Test checkout with negative price."""
    checkout_data = {
        "product_id": 1,
        "quantity": 2,
        "total_price": -100000  # Cannot be negative
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400


def test_checkout_zero_quantity(client):
    """Test checkout with zero quantity."""
    checkout_data = {
        "product_id": 1,
        "quantity": 0,  # Cannot be zero
        "total_price": 100000
    }
    response = client.post('/checkout', json=checkout_data)
    assert response.status_code == 400


def test_checkout_empty_body(client):
    """Test checkout with empty request body."""
    response = client.post('/checkout', json={})
    assert response.status_code == 400
