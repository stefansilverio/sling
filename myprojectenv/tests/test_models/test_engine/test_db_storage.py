#!/usr/bin/python3
"""
unit tests for db_storage class
"""
import unittest
import models
from models.engine.db_storage import DBstorage

class TestBaseModel(unittest.TestCase):
    """
    this will test the DBstorage class
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

    def test_create_engine(self):
        """
        test engine gets created
        """
        new_db = DBstorage()
        self.assertIn('_DBstorage__engine', new_db.__dict__.keys())

if __name__ == "__main__":
    unittest.main()
