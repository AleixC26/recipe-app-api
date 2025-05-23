"""
Database models
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django_cryptography.fields import encrypt
from django_extensions.db.models import TimeStampedModel


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser, TimeStampedModel):
    """User in the system"""

    first_name = encrypt(AbstractUser._meta.get_field("first_name"))
    last_name = encrypt(AbstractUser._meta.get_field("last_name"))
    email = encrypt(AbstractUser._meta.get_field("email"))

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        ordering = ["-date_joined"]
