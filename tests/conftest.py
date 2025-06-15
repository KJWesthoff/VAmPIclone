import os
import tempfile
from pathlib import Path
from typing import Generator, Dict, Any

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_config() -> Dict[str, Any]:
    """Provide mock configuration for testing."""
    return {
        "DEBUG": True,
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "SECRET_KEY": "test-secret-key",
        "JWT_SECRET_KEY": "test-jwt-secret",
    }


@pytest.fixture
def sample_user_data() -> Dict[str, Any]:
    """Provide sample user data for testing."""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123",
    }


@pytest.fixture
def sample_book_data() -> Dict[str, Any]:
    """Provide sample book data for testing."""
    return {
        "book_title": "Test Book",
        "secret": "This is a test book secret",
        "owner": "testuser",
    }


@pytest.fixture
def capture_logs(caplog):
    """Capture log messages during tests."""
    with caplog.at_level("DEBUG"):
        yield caplog