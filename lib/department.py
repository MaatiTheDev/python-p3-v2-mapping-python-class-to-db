# lib/department.py
from __init__ import CURSOR, CONN

class Department:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        """Create a table to store Department instances."""
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the departments table."""
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Save the Department instance to the database."""
        if self.id is None:
            # Insert new row
            sql = """
                INSERT INTO departments (name, location)
                VALUES (?, ?)
            """
            CURSOR.execute(sql, (self.name, self.location))
            CONN.commit()
            # Update instance id with the new row's id
            self.id = CURSOR.lastrowid
        else:
            # Update existing row
            sql = """
                UPDATE departments
                SET name = ?, location = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.location, self.id))
            CONN.commit()

    @classmethod
    def create(cls, name, location):
        """Create a new Department instance and save it to the database."""
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """Update the Department instance in the database."""
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the Department instance from the database."""
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
