from fastapi import FastAPI
from sqlalchemy import Select
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from apps.server.core.database import Base, engine, DATABASE_URL
from apps.server.models import User

app = FastAPI()
print("Database Url: ", DATABASE_URL)

Base.metadata.create_all(bind=engine)
# session = Session(bind=engine)

@app.get("/")
def home():

    with Session(bind=engine) as session:
        stmt = Select(User)
        names = []

        for user in session.scalars(stmt).all():
            names.append(user.username)
            print(user.username)
    return {"message": "API Running", 'created':names.__str__()}

@app.post('/new_user')
def new_user():

    with Session(bind=engine) as session:
        user = User(
            username='user2',
            email='somthing 2',
            password='new123',
            bio="User2"
        )

        try:
            session.add(user)
            session.commit()

            # created_user = session.query(User).first()
            return {"message": "User Added", "created_user": None}
        except DatabaseError as e:
            session.rollback()
            return {"message": "User Not Created", "error": e}
#
# 5d091ef2-b61e-402a-aa7e-72b4f35c5d0f