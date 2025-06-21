from pydantic import BaseModel, EmailStr, field_validator

class User_Profile(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator("age", mode="before")
    @classmethod
    def validate_age(cls, value):
        if not (18 <= value <= 100):
            raise ValueError(f"Age must be in range of (18-100): {value}")
        return value
    
user_profile = User_Profile(name="Amit", email="amitpandey551.hyd@gmail.com", age=28)
print(f"Name: {user_profile.name}")
print(f"Email: {user_profile.email}")
print(f"Age: {user_profile.age}")