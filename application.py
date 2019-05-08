from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pymssql://username@sqlpythondb:Password1@sqlpythondb.database.windows.net:1433/SQLPythonDB?charset=UTF-8"
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


db.session.add(Person(id=6,username="Flask", email="example@example.com"))
db.session.commit()

users = Person.query.all()