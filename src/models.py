import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, ForeignKey
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    firtsname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    mail: Mapped[str] = mapped_column(nullable=False)
    posts=relationship("Post",back_populates="user")
    comments=relationship("Comment",back_populates="author")
    follower=relationship("Follower",back_populates="follower")
    following=relationship("Follower",back_populates="following")


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    # relacion con la tabla Usuario
    userid: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user=relationship("User",back_populates="posts")
    # relacion con la tabla Comments
    comments=relationship("Comment",back_populates="post")
    media=relationship("Media",back_populates="post")

class Media(Base):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post=relationship("Post",back_populates="media")

class Follower(Base):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_from=relationship("User",back_populates="follower")
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to=relationship("User",back_populates="following")
    

   

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(nullable=False)
    # relacion con la tabla Usuario
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author=relationship("User",back_populates="comments")
    # relacion con la tabla Post
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post=relationship("Post",back_populates="comments")

# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
