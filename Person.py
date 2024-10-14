class Character:
    
    REQUIRED_FIELDS = ["name", "height", "mass", "hair_color", "skin_color", "eye_color",
                    "birth_year", "gender", "homeworld", "films", "species", "vehicles",
                    "starships", "created", "edited", "url"]
    
    VALID_GENDERS = ("male", "female", "n/a")
    
    def __init__(self, character_data):
        self.character_data = character_data
        
    def has_required_fields(self):
        return all(field in self.character_data for field in self.REQUIRED_FIELDS)

    def validate_fields(self):
        missing_fields = [field for field in self.REQUIRED_FIELDS if field not in self.character_data]
        if missing_fields:
            raise AssertionError(f"Character is missing the following fields: {missing_fields}")
    
    def validate_gender(self):
        gender = self.character_data.get("gender")
        if gender not in self.VALID_GENDERS:
            raise AssertionError(f"Invalid gender value '{gender}' for character {self.character_data.get('name')}")