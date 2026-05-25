"""
Shared pytest fixtures for all tests.
This file contains fixtures that are used across all test features.
"""

import pytest

from app import app, db


@pytest.fixture
def client():
    """
    Flask test client fixture.
    Creates an in-memory database for testing.
    Database is cleared after each test.
    """
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


@pytest.fixture
def app_context():
    """Application context fixture for database operations."""
    with app.app_context():
        yield app
