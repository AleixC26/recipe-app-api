"""
Test for models
"""
from django.core.exceptions import ValidationError
from django.test import TestCase

from core.factories import UserFactory


class UserTest(TestCase):
    """Test models"""

    def setUp(self):
        self.user = UserFactory.build()

    # factory is defined correctly
    def test_is_valid(self):
        try:
            self.user.full_clean()
        except ValidationError as error:
            self.fail("user factory should be valid")
            print(error)

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_email = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected in sample_email:
            user = UserFactory.create(email=email)
            self.assertEqual(user.email, expected)
