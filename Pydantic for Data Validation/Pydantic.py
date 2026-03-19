from pydantic import BaseModel, EmailStr, Field, ValidationError

class UserRegister(BaseModel):
    username: str = Field(..., min_length=5)
    email: EmailStr
    age: int = Field(..., ge=18)

# Sample data (provided by me)
data = {
    "username": "Sanskriti Jain",
    "email": "sanskritijain47@gmail.com",
    "age": 23
}

try:
    user = UserRegister(**data)
    print("Registration successful!")
    print(user)

except ValidationError as error:
    print("Invalid input")
    print(error)