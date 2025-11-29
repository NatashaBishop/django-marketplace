import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_register_login_refresh_logout():
    client = APIClient()

    # Register
    resp = client.post("/api/auth/register/", {
        "username": "alice",
        "email": "alice@example.com",
        "password": "SuperSecret123!",
        "password2": "SuperSecret123!"
    }, format='json')
    assert resp.status_code == 201
    assert "tokens" in resp.data
    refresh = resp.data["tokens"]["refresh"]

    # Obtain token via token endpoint (using credentials)
    resp2 = client.post("/api/auth/token/", {"username":"alice","password":"SuperSecret123!"}, format='json')
    assert resp2.status_code == 200
    assert "access" in resp2.data and "refresh" in resp2.data
    access = resp2.data["access"]
    refresh2 = resp2.data["refresh"]

    # Refresh access token
    resp3 = client.post("/api/auth/token/refresh/", {"refresh": refresh2}, format='json')
    assert resp3.status_code == 200
    assert "access" in resp3.data

    # Logout (blacklist refresh)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
    resp4 = client.post("/api/auth/logout/", {"refresh": refresh2}, format='json')
    assert resp4.status_code == 205

    # Try to refresh using blacklisted token -> should fail
    resp5 = client.post("/api/auth/token/refresh/", {"refresh": refresh2}, format='json')
    assert resp5.status_code == 401 or resp5.status_code == 401
