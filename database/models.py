from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Text
from sqlalchemy import Column, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Article", back_populates='user')

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String, nullable=False)
    content = Column(Text)
    is_published = Column(Boolean, default=False)

    user = relationship("User", back_populates='items')
