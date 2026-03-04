from sqlalchemy import Column, String, Numeric,Integer, Identity
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer,Identity(always = False), primary_key  = True) #always true is only autoincrement, always false is we can also add id
    name = Column(String(100),nullable = False)
    poster = Column(String(500))
    summary = Column(String(1000))
    rating = Column(Numeric(3,1))
    trailer = Column(String(500))

    def to_dict(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "poster": self.poster,
            "summary": self.summary,
            "rating":self.rating,
            "trailer":self.trailer
        }



