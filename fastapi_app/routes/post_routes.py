from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.post_model import Post
from models.comment_model import Comment
from database import get_db
from schemas import PostBase, CommentBase
from auth import get_current_user
from models.user_model import User  # Import User model

router = APIRouter()

@router.post("/create_post/")
def create_post(
    post: PostBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can create posts")

    db_post = Post(title=post.title, content=post.content, user_id=current_user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return {"msg": "Post created successfully!"}

@router.get("/posts/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@router.post("/posts/{post_id}/comments/")
def add_comment(
    post_id: int,
    comment: CommentBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Create a new comment associated with the post
    db_comment = Comment(content=comment.content, post_id=post_id, user_id=current_user.id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return {"msg": "Comment added successfully!"}

@router.get("/posts/{post_id}/comments/")
def get_comments(post_id: int, db: Session = Depends(get_db)):
    # Retrieve all comments for the specified post
    comments = db.query(Comment).filter(Comment.post_id == post_id).all()
    return comments  # Return comments as a list of Comment objects
