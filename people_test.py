import pytest
import requests
from Person import Character

API_URL = "https://swapi.dev/api/people"

@pytest.fixture
def api_response():
    response = requests.get(API_URL)
    assert response.status_code == 200, f"Expected Status Code 200, but received Status Code {response.status_code}"
    return response.json()

def test_maximum_characters(api_response):
    results = api_response["results"]
    assert len(results) <= 82, f"Expected maximum 82 characters, but received {len(results)}"
    
def test_character_structure(api_response):
    results = api_response["results"]
    for character_data in results:
        character = Character(character_data)
        assert character.has_required_fields(), "Character does not have all required fields"
        
        #Validate required fields
        character.validate_fields()
        
        #Validate gender types and ensure each person contains only “male”, “female” or “n/a” as gender
        character.validate_gender()