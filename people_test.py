import pytest
import requests

API_URL = "https://swapi.dev/api/people"

@pytest.fixture
def api_response():
    response = requests.get(API_URL)
    assert response.status_code == 200, f"Expected Status Code 200, but received Status Code {response.status_code}"
    return response.json()

def test_maximum_characters(api_response):
    results = api_response["results"]
    assert len(results) <= 82, f"Expected maximum 82 characters, but received {len(results)}"