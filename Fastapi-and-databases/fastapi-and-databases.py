from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CheckConstraint
from sqlalchemy import insert, select, update, delete

DATABASE_URL = "mysql+pymysql://root:1234@localhost/student_db"

engine = create_engine(DATABASE_URL)

metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("age", Integer, CheckConstraint("age >= 18")),
    Column("city", String(50)),
)

# create table
metadata.create_all(engine)
print("Table created")


# insert
with engine.connect() as conn:

    conn.execute(insert(students), [
        {"name": "Rahul", "age": 20, "city": "Indore"},
        {"name": "Amit", "age": 22, "city": "Delhi"},
        {"name": "Riya", "age": 19, "city": "Mumbai"},
    ])

    conn.commit()

print("Inserted")


# fetch
with engine.connect() as conn:

    result = conn.execute(select(students))

    print("All students:")

    for row in result:
        print(row)


# update
with engine.connect() as conn:

    conn.execute(
        update(students)
        .where(students.c.name == "Rahul")
        .values(city="Bhopal")
    )

    conn.commit()

print("Updated")


# delete
with engine.connect() as conn:

    conn.execute(
        delete(students).where(students.c.age < 20)
    )

    conn.commit()

print("Deleted")