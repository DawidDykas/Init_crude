from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# ------------------------
# Base User (DRY)
# ------------------------
class BaseUser(BaseModel):
    username: str = Field(
        ...,
        description="Login name chosen by the user",
        min_length=3,
        max_length=50,
        json_schema_extra={"example": "alice_wonder"},
    )

    email: EmailStr = Field(
        ...,
        description="Email address of the user (must be unique)",
        json_schema_extra={"example": "alice@example.com"},
    )


# ------------------------
# Create / Update / Delete / Get Models
# ------------------------
class UserCreate(BaseUser):
    password: str = Field(
        ...,
        description="Password for user account (at least 6 characters)",
        min_length=6,
        max_length=100,
        json_schema_extra={"example": "SuperSecure123!"},
    )

    registration_date: datetime | None = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Date and time when the user registered (auto-set to now)",
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "alice_wonder",
                "email": "alice@example.com",
                "password": "SuperSecure123!",
                "registration_date": "2026-02-11T15:30:00Z",
            }
        }
    )


class UserUpdate(BaseModel):
    id: int = Field(
        ...,
        description="Identifier of the user to modify",
        json_schema_extra={"example": 42},
    )

    username: str | None = Field(
        None,
        min_length=3,
        max_length=50,
        json_schema_extra={"example": "alice_new"},
    )

    email: EmailStr | None = Field(
        None,
        json_schema_extra={"example": "alice.new@example.com"},
    )

    password: str | None = Field(
        None,
        min_length=6,
        max_length=100,
        json_schema_extra={"example": "NewPass456!"},
    )


class UserGetById(BaseModel):
    id: int = Field(
        ...,
        description="ID of the user to retrieve",
        json_schema_extra={"example": 42},
    )


class UserGetByEmail(BaseModel):
    email: EmailStr = Field(
        ...,
        description="Email of the user to retrieve",
        json_schema_extra={"example": "alice@example.com"},
    )


# ------------------------
# Response Models
# ------------------------
class UserResponse(BaseUser):
    id: int = Field(
        ...,
        description="Unique identifier assigned to the user",
        json_schema_extra={"example": 42},
    )

    registration_date: datetime = Field(
        ...,
        description="Timestamp when the user registered",
    )

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 42,
                "username": "alice_wonder",
                "email": "alice@example.com",
                "registration_date": "2026-02-11T15:30:00Z",
            }
        },
    )


class UserListResponse(BaseModel):
    total: int = Field(
        ...,
        description="Total number of users available",
        json_schema_extra={"example": 250},
    )

    skip: int = Field(
        ...,
        description="Number of users skipped in this result",
        json_schema_extra={"example": 0},
    )

    limit: int = Field(
        ...,
        description="Maximum number of users returned",
        json_schema_extra={"example": 50},
    )

    users: list[UserResponse] = Field(
        ...,
        description="Array of user records",
    )


class UserDelete(BaseModel):
    id: int = Field(
        ...,
        description="ID of the user to delete",
        json_schema_extra={"example": 42},
    )

class ForgotPasswordRequest(BaseModel):
    email: EmailStr = Field(
        ...,
        description="Email of the user requesting password reset",
        json_schema_extra={"example": "alice@example.com"},
    )


# ------------------------
# Auth Models
# ------------------------
class UserLogin(BaseModel):
    email: EmailStr = Field(
        ...,
        description="Email used to log in",
        json_schema_extra={"example": "alice@example.com"},
    )

    password: str = Field(
        ...,
        description="User password for login",
        min_length=6,
        json_schema_extra={"example": "SuperSecure123!"},
    )


class UserLogout(BaseModel):
    token: str = Field(
        ...,
        description="JWT token to be invalidated on logout",
    )


class ErrorResponse(BaseModel):
    error: str = Field(
        ...,
        description="Short description of the error",
        json_schema_extra={"example": "Authentication failed"},
    )

    detail: str | None = Field(
        None,
        description="Optional detailed explanation of the error",
        json_schema_extra={"example": "Email or password is incorrect"},
    )