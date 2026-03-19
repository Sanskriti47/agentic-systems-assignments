from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict

# Address Model

class Address(BaseModel):
    city: str = Field(..., min_length=3)
    pincode: str

# Used to enable Assignment Validation    

    model_config = ConfigDict(validate_assignment=True)

# To ensure/validate that the pincode has exactly 6 digits

    @field_validator("pincode")
    @classmethod
    def check_pincode(cls, value):
        if len(value) != 6:
            raise ValueError("Pincode must be exactly 6 digits")
        return value


# User Model

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(..., ge=18)
    address: Address
    is_premium: bool = False

    model_config = ConfigDict(validate_assignment=True)


# Example data (I have used it only for testing the model)

user = User(
    user_id=1,
    name="Sanskriti Jain",
    email="sanskritijain@gmail.com",
    age=23,
    address={
        "city": "Indore",
        "pincode": "452009"
    }
)

print(user)

# Also without providing the example data 

from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict

# Address Model

class Address(BaseModel):
    city: str = Field(..., min_length=3)
    pincode: str

# Used to enable Assignment Validation    

    model_config = ConfigDict(validate_assignment=True)

# To ensure/validate that the pincode has exactly 6 digits

    @field_validator("pincode")
    @classmethod
    def check_pincode(cls, value):
        if len(value) != 6:
            raise ValueError("Pincode must be exactly 6 digits")
        return value


# User Model

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(..., ge=18)
    address: Address
    is_premium: bool = False

    model_config = ConfigDict(validate_assignment=True)

print("User and Address models created successfully")
