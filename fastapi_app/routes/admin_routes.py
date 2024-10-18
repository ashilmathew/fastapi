from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user_model import User
from models.post_model import Post
from models.comment_model import Comment
from database import get_db
from auth import get_current_user

router = APIRouter()

@router.get("/admin/posts/{post_id}/comments/")
def get_comments_for_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:  # Check if the user is an admin
        raise HTTPException(status_code=403, detail="Only admins can access this resource")
    
    # Fetch the post to check if it belongs to the admin
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == current_user.id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found or does not belong to the current user")
    
    # Fetch comments for the specified post
    comments = db.query(Comment).filter(Comment.post_id == post_id).all()
    
    return comments  # Return the list of comments for the post
