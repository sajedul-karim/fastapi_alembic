from typing_extensions import Annotated
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db, engine
import models
from schemas import PostCreate, PostResponse, UserCreate, UserResponse
from services import create_post, get_post, get_posts, get_user, get_users, create_user, delete_user, update_post

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users", response_model=list[UserResponse])
async def read_users(db: db_dependency, skip: int = 0, limit: int = 100):
    users = get_users(db, skip=skip, limit=limit)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@app.post("/user", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: db_dependency):
    try:
        # Check if email exists
        db_user = db.query(models.User).filter(models.User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return create_user(db=db, user=user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/user/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: db_dependency):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/user/{user_id}")
async def delete_user_mine(user_id: int, db: db_dependency):
    delete_user(db, user_id)
    return {"message": "User deleted successfully"}


@app.post("/post", response_model=PostResponse)
async def create_new_post(post: PostCreate, db: db_dependency):
    try:
        db_post = await create_post(db=db, post=post)
        return db_post

    except IntegrityError as e:
        raise HTTPException(status_code=500, detail=f"Intrigity error occurred: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"an error occurred: {str(e)}")


@app.get("/posts", response_model=list[PostResponse])
async def read_posts(db: db_dependency, skip: int = 0, limit: int = 100):
    posts = get_posts(db, skip=skip, limit=limit)
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found")
    return posts


@app.get("/post/{post_id}", response_model=PostResponse)
async def read_post(post_id: int, db: db_dependency):
    db_post = get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
