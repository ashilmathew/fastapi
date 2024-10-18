from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user_model import User
from database import get_db
from schemas import UserCreate, ChangePassword
from utils import get_password_hash, verify_password
from auth import get_current_user
from auth import create_access_token

router = APIRouter()

@router.post("/register/user/")
def register_normal_user(user: UserCreate, db: Session = Depends(get_db)):
    # Hash the password and create a normal user
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password, is_admin=False)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg": "Normal user created successfully!"}

@router.post("/register/admin/")
def register_admin_user(user: UserCreate, db: Session = Depends(get_db)):
    
    # Hash the password and create an admin user
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password, is_admin=True)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg": "Admin user created successfully!"}

@router.post("/login/")
def login(username: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user or not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.id})  # Use user ID as subject
    return {"access_token": access_token, "token_type": "bearer","msg": "Logged in successfully!"}

@router.post("/change_password/")
def change_password(
    password_data: ChangePassword, 
    db: Session = Depends(get_db), 
    user: User = Depends(get_current_user)
):
    # Verify the current password
    if not verify_password(password_data.current_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Current password is incorrect")

    # Hash the new password and update the user record
    hashed_new_password = get_password_hash(password_data.new_password)
    user.hashed_password = hashed_new_password
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return {"msg": "Password updated successfully!"}
