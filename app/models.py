from . import db

applicants = db.Table('applicants',
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True),
    db.Column('project_id', db.String(20), db.ForeignKey('project.id'), primary_key=True)
)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))

    def __repr__(self) -> str:
        return f"<Person {self.firstname} {self.lastname} at {id(self)}>"


class Publication(db.Model):
    __tablename__ = 'publications'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    journal = db.Column(db.String(100))
    doi = db.Column(db.String(50))

    def __repr__(self) -> str:
        return f"<Publication {self.id} at {id(self)}>"


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(100))
    short_title = db.Column(db.String(20))
    project_number = db.Column(db.Integer)
    billing_onject = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"<Project {self.id}: {self.short_title} at {id(self)}>"


class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(30), primary_key=True)
    # To Do: Passhash storage
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.username} at {id(self)}>"


class Role(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    users = db.relationship('User', backref='role')

    def __repr__(self) -> str:
        return f"<Role {self.username} at {id(self)}>"