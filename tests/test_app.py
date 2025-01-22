import pytest
from mentorship_ai.app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_ask_endpoint(client):
    response = client.post('/ask', json={
        "question": "How can I improve my career?",
        "mentorship_area": "frontend-react",
    })
    assert response.status_code == 200
    assert "response" in response.json
