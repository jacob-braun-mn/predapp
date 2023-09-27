from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import pandas as pd
from datasets import load_dataset
import models

# Only run this for initial setup to load data


class OutputBase(BaseModel):
    prompt: str
    output: str
    reviewed: bool
    reviewer: str
    review_date: str
    rating: int
    bad_content: bool
    bad_content_type: str


class OutputModel(OutputBase):
    id: int

    class Config:
        orm_mode = True


# COMMENTING BELOW SO DUPLICATE DATA IS NOT ADDED ACCIDENTALLY
# UNCOMMENT AND RUN FOR FIRST TIME DB SETUP

# models.Base.metadata.create_all(bind=engine)

# df = pd.DataFrame(load_dataset("TIGER-Lab/MathInstruct", split="train[:1%]"))
# df = df.rename({"instruction": "prompt"}, axis=1)
# df = df[["prompt", "output"]]
# df["reviewed"] = False
# df["reviewer"] = None
# df["review_date"] = None
# df["rating"] = None
# df["bad_content"] = None
# df["bad_content_type"] = None

# df.to_sql("Output", con=engine, if_exists="append", index=False)
