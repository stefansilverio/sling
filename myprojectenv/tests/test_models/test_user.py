#!/usr/bin/python3
"""
unit tests for user class
"""
import unittest
import models
import MySQLdb
from datetime import datetime
from models.user import User
from sqlalchemy import inspect
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    this will test the User class
    """

    @classmethod
    def setUpClass(cls):
        """
        drop all tables in db
        create new session
        """
        models.storage.close()
        models.storage.drop_all()
        models.storage.reload()

    @classmethod
    def tearDown(cls):
        """
        clean db
        """
        models.storage.clean()


    def test_create_user_no_kwargs(self):
        """
        try creating User object without mandatory args
        """
        new_u = User()
        self.assertIsInstance(new_u, User)

        self.assertIsInstance(new_u.id, str)
        self.assertIsInstance(new_u.created_at, datetime)

        state = inspect(new_u)
        self.assertTrue(state.transient)

    def test_create_user_kwargs(self):
        """
        create User instance with kwargs
        """
        new_u = User(email="silver", password="stef", amount_borrowed=40, amount_lent=30)
        self.assertIsInstance(new_u, User)

        self.assertIsInstance(new_u.email, str)
        self.assertIsInstance(new_u.password, str)
        self.assertIsInstance(new_u.amount_borrowed, int)
        self.assertIsInstance(new_u.amount_lent, int)

        self.assertNotEqual(new_u.password, "stef")
        self.assertNotEqual(new_u.email, "silver")


    def test_all_method(self):
        """
        check that all method returns dict of User obj's
        check save method adds obj to db
        """
        new_u = User(email="silver", password="stef", amount_borrowed=40, amount_lent=30)
        obj = new_u.all()
        self.assertIsInstance(obj, dict)
        self.assertEqual(len(obj), 0)

        new_u.save()
        obj = new_u.all()
        self.assertNotEqual(len(obj), 0)

    def test_save_method(self):
        """
        check that save method changes obj state
        """
        new_u = User(email="silver", password="stef", amount_borrowed=40, amount_lent=30)
        state = inspect(new_u)
        self.assertTrue(state.transient)
        models.storage.new(new_u)
        self.assertTrue(state.pending)
        models.storage.save()
        self.assertTrue(state.persistent)


    def test_delete_method(self):
        """
        check delete method can delete from db
        """
        new_u = User(email="silver", password="stef", amount_borrowed=40, amount_lent=30)
        new_u.save()
        self.assertEqual(len(new_u.all()), 1)
        new_u.delete(User, new_u.id)
        self.assertEqual(len(new_u.all()), 0)


    def test_query_method(self):
        new_u = User(email="silver", password="stef", amount_borrowed=40, amount_lent=30)
        new_u.save()
        dic = new_u.query("User")
        self.assertEqual(len(dic), 1)


    def test_update_method(self):
        """
        check update method can update values in db
        check password and email get encrypted
        """
        db = MySQLdb.connect(host="localhost", user="sling", passwd="s", db="sling")
        cur = db.cursor()
        cur.execute("select * from users;")

        """test row count"""
        self.assertEqual(cur.rowcount, 0)

        new_u = User(email="silver", password="silver", amount_borrowed=40,
                     amount_lent=30, first_name="joe", last_name="roberts")

        new_u.save()

        db = MySQLdb.connect(host="localhost", user="sling", passwd="s", db="sling")
        cur = db.cursor()
        cur.execute("select * from users;")

        """test row count changed"""
        self.assertEqual(cur.rowcount, 1)
        """test attr gets written to db"""
        for tup in cur.__dict__['_rows']:
            if 'joe' in tup:
                self.assertIn('joe', tup)

        new_u.update(User, new_u.id, email="silver@", password="williams", first_name="silver", last_name="silver", amount_borrowed=50, amount_lent=40)

        db = MySQLdb.connect(host="localhost", user="sling", passwd="s", db="sling")
        cur = db.cursor()
        cur.execute("select * from users;")

        self.assertEqual(cur.rowcount, 1)
        """check first_name gets updated"""
        for tup in cur.__dict__['_rows']:
            if 'silver' in tup:
                self.assertIn("silver", tup)

if __name__ == "__main__":
    unittest.main()
