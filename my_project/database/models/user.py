from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from database.database import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Article", back_populates='user')