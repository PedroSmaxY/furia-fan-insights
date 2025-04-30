from typing import Optional, List
from datetime import date
from enum import Enum
from sqlmodel import SQLModel, Field, JSON, Column
from pydantic import EmailStr, field_validator
import re


class GamingPlatform(str, Enum):
    PC = "PC"
    PLAYSTATION = "PlayStation"
    XBOX = "Xbox"
    MOBILE = "Mobile"
    NINTENDO = "Nintendo Switch"


class UserBase(SQLModel):
    name: str
    email: EmailStr
    cpf: str
    address: str
    birth_date: date
    phone: str
    is_active: bool = True

    @classmethod
    @field_validator('cpf')
    def validate_cpf(cls, v):
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', v):
            raise ValueError('CPF deve estar no formato XXX.XXX.XXX-XX')
        return v

    @classmethod
    @field_validator('phone')
    def validate_phone(cls, v):
        if not re.match(r'^\(\d{2}\)\s\d{5}-\d{4}$', v):
            raise ValueError('Telefone deve estar no formato (XX) XXXXX-XXXX')
        return v


class User(UserBase, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = Field(...)

    favorite_games: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    favorite_teams: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    gaming_platform: Optional[GamingPlatform] = None

    instagram_profile: Optional[str] = None
    twitter_profile: Optional[str] = None
    twitch_profile: Optional[str] = None
    discord_username: Optional[str] = None

    documents: Optional[List[dict]] = Field(default=None, sa_column=Column(JSON))

    attended_events: Optional[List[dict]] = Field(default=None, sa_column=Column(JSON))

    purchases: Optional[List[dict]] = Field(default=None, sa_column=Column(JSON))

    esports_profiles: Optional[List[dict]] = Field(default=None, sa_column=Column(JSON))

    social_interactions: Optional[List[dict]] = Field(default=None, sa_column=Column(JSON))


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


class UserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    favorite_games: Optional[List[str]] = None
    favorite_teams: Optional[List[str]] = None
    gaming_platform: Optional[GamingPlatform] = None
    instagram_profile: Optional[str] = None
    twitter_profile: Optional[str] = None
    twitch_profile: Optional[str] = None
    discord_username: Optional[str] = None
