from typing import Sequence, Optional, Type
from sqlmodel import SQLModel, Session, select


class CRUDBase:
    def __init__(self, model: Type[SQLModel]):
        self.model = model

    def get(self, db: Session, id: int) -> Optional[SQLModel]:
        return db.get(self.model, id)

    def get_multi(self, db: Session, limit: int = 100) -> Sequence[SQLModel]:
        return db.exec(select(self.model).limit(limit)).all()

    def create(self, db: Session, data: dict) -> SQLModel:
        db_obj = self.model(**data)
        db.add(db_obj)
        db.commit()
        return db_obj

    def update(self, db: Session, id: int, data: dict) -> Optional[SQLModel]:
        db_obj = self.get(db, id)
        if db_obj:
            for key, value in data.items():
                setattr(db_obj, key, value)
            db.commit()
        return db_obj

    def delete(self, db: Session, id: int) -> bool:
        db_obj = self.get(db, id)
        if db_obj:
            db.delete(db_obj)
            db.commit()
            return True
        return False
