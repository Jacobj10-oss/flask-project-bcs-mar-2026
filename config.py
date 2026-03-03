class Config:
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://username:yourpassword@localhost:5432/movies"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True