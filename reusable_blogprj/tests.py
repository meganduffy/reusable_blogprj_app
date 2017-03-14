from django.test import TestCase
from .models import Post  # . denotes that the models file is in the same directory as models.py


# Create your tests here.
class PostTests(TestCase):
    """
    Here we'll define the tests that we'll run against our Post model
    """

    def test_str(self):
        test_title= Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title),
                         'My Latest Blog Post')