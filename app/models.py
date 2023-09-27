from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Output(Base):
    __tablename__ = "Output"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String)
    output = Column(String)
    reviewed = Column(Boolean, index=True)
    reviewer = Column(String, index=True)
    review_date = Column(String)
    rating = Column(Integer)
    bad_content = Column(Boolean)
    bad_content_type = Column(String)
