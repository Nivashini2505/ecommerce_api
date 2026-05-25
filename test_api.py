# test_api.py
# This file contains all the test cases for the ecommerce API
# We use pytest to test if our API works correctly

import pytest
from app import app, db


# =========================
# TEST FIXTURE (Setup for each test)
# =========================
# A fixture is like a setup function that runs before each test
# It creates a test database in memory so tests don't affect real data

@pytest.fixture
def client():
    # Tell Flask we're testing
    app.config['TESTING'] = True
    # Use an in-memory database so tests don't touch the real database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    # Create a test client to make requests
    with app.test_client() as client:
        # Create all database tables
        with app.app_context():
            db.create_all()

        yield client  # Give the test this client to use

        # Clean up after test by dropping all tables
        with app.app_context():
            db.drop_all()


# =========================
# TEST: Add Product Successfully
# =========================
# This test checks if we can add a new product successfully
# Expected: API should return status code 201 (Created)

def test_add_product_success(client):
    # Prepare product data
    new_product = {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": "Electronics"
    }
    
    # Send POST request to add product
    response = client.post('/products', json=new_product)
    
    # Check if product was created successfully (201 = Created)
    assert response.status_code == 201
    
    # Get the response data
    data = response.get_json()
    
    # Verify that the product name is saved correctly
    assert data["product"]["name"] == "Laptop"


# =========================
# TEST: Missing Required Fields
# =========================
# This test checks if API rejects incomplete product data
# Expected: API should return status code 400 (Bad Request)

def test_missing_fields(client):
    # Try to add a product with only name (missing price, quantity, category)
    incomplete_product = {
        "name": "Laptop"
    }
    
    response = client.post('/products', json=incomplete_product)
    
    # Should fail because required fields are missing
    assert response.status_code == 400


# =========================
# TEST: Empty Request Body
# =========================
# This test checks if API handles empty requests
# Expected: API should return status code 400 (Bad Request)

def test_empty_body(client):
    # Send an empty JSON object
    response = client.post('/products', json={})
    
    # Should fail because no data was provided
    assert response.status_code == 400


# =========================
# TEST: Invalid Price Type
# =========================
# This test checks if API validates that price is a number, not text
# Expected: API should return status code 400 (Bad Request)

def test_invalid_price_type(client):
    # Try to add product with price as text instead of number
    invalid_product = {
        "name": "Laptop",
        "price": "abc",  # Wrong! Price should be a number
        "quantity": 5,
        "category": "Electronics"
    }
    
    response = client.post('/products', json=invalid_product)
    
    # Should fail because price is not a number
    assert response.status_code == 400


# =========================
# TEST: Negative Price
# =========================
# This test checks if API rejects negative prices
# Expected: API should return status code 400 (Bad Request)

def test_negative_price(client):
    # Try to add product with negative price
    product_with_negative_price = {
        "name": "Laptop",
        "price": -100,  # Wrong! Price cannot be negative
        "quantity": 5,
        "category": "Electronics"
    }
    
    response = client.post('/products', json=product_with_negative_price)
    
    # Should fail because price is negative
    assert response.status_code == 400


# =========================
# TEST: Negative Quantity
# =========================
# This test checks if API rejects negative quantities
# Expected: API should return status code 400 (Bad Request)

def test_negative_quantity(client):
    # Try to add product with negative quantity
    product_with_negative_quantity = {
        "name": "Laptop",
        "price": 1000,
        "quantity": -1,  # Wrong! Quantity cannot be negative
        "category": "Electronics"
    }
    
    response = client.post('/products', json=product_with_negative_quantity)
    
    # Should fail because quantity is negative
    assert response.status_code == 400


# =========================
# TEST: Empty Product Name
# =========================
# This test checks if API rejects empty product names
# Expected: API should return status code 400 (Bad Request)

def test_empty_name(client):
    # Try to add product with empty name
    product_with_empty_name = {
        "name": "",  # Wrong! Name cannot be empty
        "price": 1000,
        "quantity": 2,
        "category": "Electronics"
    }
    
    response = client.post('/products', json=product_with_empty_name)
    
    # Should fail because name is empty
    assert response.status_code == 400


# =========================
# TEST: Duplicate Product
# =========================
# This test checks if API prevents adding same product twice
# Expected: First add should succeed, second add should fail with 409 (Conflict)

def test_duplicate_product(client):
    # First, add a product
    product_data = {
        "name": "Phone",
        "price": 30000,
        "quantity": 2,
        "category": "Electronics"
    }
    client.post('/products', json=product_data)
    
    # Now try to add the same product again
    response = client.post('/products', json=product_data)
    
    # Should fail because product already exists
    assert response.status_code == 409


# =========================
# TEST: Get All Products
# =========================
# This test checks if API can retrieve all products
# Expected: API should return status code 200 (OK) and show product count

def test_get_all_products(client):
    # First, add one product
    client.post('/products', json={
        "name": "Tablet",
        "price": 25000,
        "quantity": 4,
        "category": "Electronics"
    })
    
    # Now get all products
    response = client.get('/products')
    
    # Should succeed
    assert response.status_code == 200
    
    # Get the response data
    data = response.get_json()
    
    # Should show 1 product in the list
    assert data["count"] == 1


# =========================
# TEST: Get Single Product
# =========================
# This test checks if API can retrieve a specific product by ID
# Expected: API should return status code 200 (OK)

def test_get_single_product(client):
    # First, add a product
    client.post('/products', json={
        "name": "Mouse",
        "price": 500,
        "quantity": 10,
        "category": "Accessories"
    })
    
    # Get the first product (ID = 1)
    response = client.get('/products/1')
    
    # Should succeed
    assert response.status_code == 200


# =========================
# TEST: Product Not Found
# =========================
# This test checks if API handles requests for non-existent products
# Expected: API should return status code 404 (Not Found)

def test_product_not_found(client):
    # Try to get a product that doesn't exist (ID = 999)
    response = client.get('/products/999')
    
    # Should fail because product doesn't exist
    assert response.status_code == 404


# =========================
# TEST: Update Product
# =========================
# This test checks if API can update product information
# Expected: API should return status code 200 (OK) with updated data

def test_update_product(client):
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
    
    # Should succeed
    assert response.status_code == 200
    
    # Get the response data
    data = response.get_json()
    
    # Verify that price was updated correctly
    assert data["product"]["price"] == 2000


# =========================
# TEST: Delete Product
# =========================
# This test checks if API can delete a product
# Expected: API should return status code 200 (OK)

def test_delete_product(client):
    # First, add a product
    client.post('/products', json={
        "name": "Monitor",
        "price": 12000,
        "quantity": 2,
        "category": "Electronics"
    })
    
    # Delete the first product
    response = client.delete('/products/1')
    
    # Should succeed
    assert response.status_code == 200


# =========================
# TEST: Delete Non-Existing Product
# =========================
# This test checks if API handles deletion of non-existent products
# Expected: API should return status code 404 (Not Found)

def test_delete_non_existing_product(client):
    # Try to delete a product that doesn't exist
    response = client.delete('/products/999')
    
    # Should fail because product doesn't exist
    assert response.status_code == 404


# =========================
# TEST: Invalid Category Type
# =========================
# This test checks if API validates that category is text, not a number
# Expected: API should return status code 400 (Bad Request)

def test_invalid_category_type(client):
    # Try to add product with category as number instead of text
    invalid_product = {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": 123  # Wrong! Category should be text
    }
    
    response = client.post('/products', json=invalid_product)
    
    # Should fail because category is not text
    assert response.status_code == 400
    
    # Also check the error message
    data = response.get_json()
    assert "Category must be string" in data["error"]


# =========================
# TEST: Empty Category
# =========================
# This test checks if API rejects empty category names
# Expected: API should return status code 400 (Bad Request)

def test_empty_category(client):
    # Try to add product with empty category
    product_with_empty_category = {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": ""  # Wrong! Category cannot be empty
    }
    
    response = client.post('/products', json=product_with_empty_category)
    
    # Should fail because category is empty
    assert response.status_code == 400
    
    # Also check the error message
    data = response.get_json()
    assert "Category cannot be empty" in data["error"]


# =========================
# TEST: Missing Category Field
# =========================
# This test checks if API requires category field
# Expected: API should return status code 400 (Bad Request)

def test_missing_category_field(client):
    # Try to add product without category field
    product_without_category = {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5
        # Missing category field
    }
    
    response = client.post('/products', json=product_without_category)
    
    # Should fail because category is missing
    assert response.status_code == 400
    
    # Check the error message
    data = response.get_json()
    assert "All fields are required" in data["error"]


# =========================
# TEST: Valid Category
# =========================
# This test checks if API accepts valid category and saves it
# Expected: API should return status code 201 (Created) and save category

def test_add_product_with_valid_category(client):
    # Add product with valid category
    product_data = {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": "Electronics"
    }
    
    response = client.post('/products', json=product_data)
    
    # Should succeed
    assert response.status_code == 201
    
    # Get the response data
    data = response.get_json()
    
    # Verify that category was saved correctly
    assert data["product"]["category"] == "Electronics"


# =========================
# TEST: Category with Whitespace
# =========================
# This test checks if API trims extra spaces from category names
# Expected: Extra spaces should be removed automatically

def test_category_with_whitespace(client):
    # Add product with category that has extra spaces
    product_data = {
        "name": "Phone",
        "price": 30000,
        "quantity": 3,
        "category": "  Mobile Devices  "  # Has spaces before and after
    }
    
    response = client.post('/products', json=product_data)
    
    # Should succeed
    assert response.status_code == 201
    
    # Get the response data
    data = response.get_json()
    
    # Verify that spaces were trimmed correctly
    assert data["product"]["category"] == "Mobile Devices"


# =========================
# MISSING CATEGORY FIELD
# =========================

def test_missing_category_field(client):

    response = client.post('/products', json={
        "name": "Laptop",
        "price": 50000,
        "quantity": 5
    })

    assert response.status_code == 400

    data = response.get_json()
    assert "All fields are required" in data["error"]


# =========================
# VALID CATEGORY TEST
# =========================

def test_add_product_with_valid_category(client):

    response = client.post('/products', json={
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "category": "Electronics"
    })

    assert response.status_code == 201

    data = response.get_json()
    assert data["product"]["category"] == "Electronics"


# =========================
# CATEGORY WITH WHITESPACE
# =========================

def test_category_with_whitespace(client):

    response = client.post('/products', json={
        "name": "Phone",
        "price": 30000,
        "quantity": 3,
        "category": "  Mobile Devices  "
    })

    assert response.status_code == 201

    data = response.get_json()
    assert data["product"]["category"] == "Mobile Devices"