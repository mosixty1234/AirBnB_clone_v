#!/usr/bin/python3
""" Unittest script """
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
import os


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db',
                 "test is not for db storage")


class TestDBStorage(unittest.TestCase):
    """ Unittest """
    @classmethod
    def setUpClass(cls):
        """ Initialize the database connection and create tables"""
        storage.reload()

    def test_add_and_get(self):
        """ Test adding and getting objects from the database"""
        user = User(email="test@example.com", password="testpwd")
        user.save()

        retrieved_user = storage.get(User, user.id)
        self.assertEqual(retrieved_user, user)

    def test_update(self):
        """ Test updating objects in the database"""
        user = User(email="test@example.com", password="testpwd")
        user.save()

        user.email = "updated@example.com"
        user.save()

        retrieved_user = storage.get(User, user.id)
        self.assertEqual(retrieved_user.email, "updated@example.com")

    def test_delete(self):
        """ Test deleting objects from the database """
        user = User(email="test@example.com", password="testpwd")
        user.save()

        user.delete()

        retrieved_user = storage.get(User, user.id)
        self.assertIsNone(retrieved_user)


if __name__ == '__main__':
    unittest.main()
