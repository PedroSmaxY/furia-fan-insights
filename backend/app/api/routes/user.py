from typing import Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Query
from sqlmodel import Session, select
from datetime import datetime

from app.core.db import get_session
from app.models.user import UserCreate, UserRead, UserUpdate, User
from app.crud.crud_user import user_crud

router = APIRouter()


@router.post("/", response_model=UserRead)
def create_user(user_data: UserCreate, db: Session = Depends(get_session)):
    db_user = user_crud.get_by_email(db, user_data.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")

    db_user = user_crud.get_by_cpf(db, user_data.cpf)
    if db_user:
        raise HTTPException(status_code=400, detail="CPF já registrado")

    return user_crud.create(db, user_data)


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_session)):
    db_user = user_crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_session)):
    db_user = user_crud.update(db, user_id, user_data)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.post("/{user_id}/documents", response_model=UserRead)
async def upload_document(
        user_id: int,
        document_type: str = Form(...),
        document: UploadFile = File(...),
        db: Session = Depends(get_session)
):
    document_data = {
        "document_type": document_type,
        "filename": document.filename,
        "content_type": document.content_type,
        "upload_date": datetime.now().isoformat(),
        "is_verified": False,
        "verification_status": "pendente"
    }

    db_user = user_crud.add_document(db, user_id, document_data)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return db_user


@router.post("/{user_id}/esports-profiles", response_model=UserRead)
def add_esports_profile(
        user_id: int,
        profile_data: Dict[str, Any],
        db: Session = Depends(get_session)
):
    profile_data["added_date"] = datetime.now().isoformat()
    profile_data["is_verified"] = False

    db_user = user_crud.add_esports_profile(db, user_id, profile_data)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return db_user


@router.post("/{user_id}/social-interactions", response_model=UserRead)
def add_social_interaction(
        user_id: int,
        interaction_data: Dict[str, Any],
        db: Session = Depends(get_session)
):
    interaction_data["interaction_date"] = datetime.now().isoformat()

    db_user = user_crud.add_social_interaction(db, user_id, interaction_data)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return db_user


@router.get("/", response_model=List[UserRead])
def list_users(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_session)
):
    users = db.exec(select(User).offset(skip).limit(limit)).all()
    return users
