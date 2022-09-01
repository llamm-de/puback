from . import db

class Person(db.Model):
    __tablename__ = 'persons'
    firstname = db.Column(db.String(30), primary_key=True)
    lastname = db.Column(db.String(30), primary_key=True)

    def __repr__(self) -> str:
        return f"<Person {self.firstname} {self.lastname}>"

class Publication(db.Model):
    __tablename__ = 'publications'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    journal = db.Column(db.String(100))
    doi = db.Column(db.String(50))

    def __repr__(self) -> str:
        return f"<Publication {self.id}>"

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(100))
    short_title = db.Column(db.String(20))
    project_number = db.Column(db.Integer)
    billing_onject = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"<Project {self.id}: {self.short_title}>"