from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    """Define the student model."""
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    # many-to-many relationship with the Subject model
    subjects = relationship('Subject', secondary='student_subject', back_populates='students')


class Subject(Base):
    """Define the subject model."""
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # many-to-many relationship with the Student model
    students = relationship('Student', secondary='student_subject', back_populates='subjects')


# association table for the many-to-many relationship
student_subject = Table('student_subject', Base.metadata,
                        Column('student_id', ForeignKey('students.id'), primary_key=True),
                        Column('subject_id', ForeignKey('subjects.id'), primary_key=True))


# create an engine that will connect to the database
engine = create_engine('sqlite:///example.db')

# create the tables in the database
Base.metadata.create_all(engine)

# create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

germione = Student(name='Germione', age=17)
harry = Student(name='Harry', age=18)
ron = Student(name='Ron', age=22)

math = Subject(name='Math')
english = Subject(name='English')
physics = Subject(name='Physics')

germione.subjects.append(math)
germione.subjects.append(english)
harry.subjects.append(physics)
harry.subjects.append(english)
ron.subjects.append(math)
ron.subjects.append(english)

# add the data to the session
session.add_all([germione, harry, ron, math, english, physics])

# commit the changes to the database
session.commit()

# return all students names that visited english
students = session.query(Student.name)\
    .join(student_subject)\
    .join(Subject)\
    .filter(Subject.name == 'English')\
    .all()

print(f'All students from {Subject.name} class: ')
for student in students:
    print(student[0])
