from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import Post, User
from schemas import PostCreate, UserCreate
from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int) -> User:
    try:
        return db.query(User).filter(User.id == user_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = pwd_context.hash(user.password)
    db_user = User(name=user.name, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    db.delete(user)
    db.commit()


def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = get_user(db, user_id)
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)


async def create_post(db: Session, post: PostCreate) -> Post:
    post_data = post.model_dump(exclude_unset=True)
    db_post = Post(**post_data)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def get_post(db: Session, post_id: int) -> Post:
    try:
        return db.query(Post).filter(Post.id == post_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Post not found")


def delete_post(db: Session, post_id: int):
    post = get_post(db, post_id)
    db.delete(post)
    db.commit()


def update_post(db: Session, post_id: int, post: PostCreate):
    db_post = get_post(db, post_id)
    for key, value in post.dict().items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
