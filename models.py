from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from db.db_config import Base

class Item(Base):
    __tablename__  = "items"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    category = Column(String, index=True)