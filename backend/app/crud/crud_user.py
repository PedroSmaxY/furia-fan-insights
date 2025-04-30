from typing import Optional, Dict, Any
from sqlmodel import Session, select
from passlib.context import CryptContext

from app.models.user import User, UserCreate, UserUpdate
from app.crud.base import CRUDBase

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CRUDUser(CRUDBase):
    def get_user(self, db: Session, user_id: int) -> Optional[User]:
        user = self.get(db, user_id)
        return user if user else None

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        statement = select(User).where(self.model.email == email)
        return db.exec(statement).first()  # type: ignore

    def get_by_cpf(self, db: Session, cpf: str) -> Optional[User]:
        statement = select(User).where(self.model.cpf == cpf)
        return db.exec(statement).first()  # type: ignore

    def create(self, db: Session, data: UserCreate) -> User:
        hashed_password = pwd_context.hash(data.password)
        user_data = data.model_dump(exclude={"password"})
        user_data["hashed_password"] = hashed_password
        db_obj = User(**user_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def add_document(self, db: Session, user_id: int, document: Dict[str, Any]) -> Optional[User]:
        user = self.get_user(db, user_id)
        if user is None:
            return None

        if user.documents is None:
            user.documents = []

        user.documents.append(document)
        db.commit()
        db.refresh(user)
        return user

    def add_esports_profile(self, db: Session, user_id: int, profile: Dict[str, Any]) -> Optional[User]:
        user = self.get_user(db, user_id)
        if user is None:
            return None

        if user.esports_profiles is None:
            user.esports_profiles = []

        user.esports_profiles.append(profile)
        db.commit()
        db.refresh(user)
        return user

    def add_social_interaction(self, db: Session, user_id: int, interaction: Dict[str, Any]) -> Optional[User]:
        user = self.get_user(db, user_id)
        if user is None:
            return None

        if user.social_interactions is None:
            user.social_interactions = []

        user.social_interactions.append(interaction)
        db.commit()
        db.refresh(user)
        return user

    def update(self, db: Session, user_id: int, data: UserUpdate) -> Optional[User]:
        user = self.get_user(db, user_id)
        if user is None:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)
        return user


user_crud = CRUDUser(User)
