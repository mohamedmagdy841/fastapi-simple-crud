from sqlalchemy import Integer, String, Boolean, DateTime, func, Text
from sqlalchemy import Column, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String, nullable=False)
    content = Column(Text)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    user = relationship("User", back_populates='articles')
