"""
Database models
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django_extensions.db.models import TimeStampedModel
from django.db import models


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, username):
        """Create and return a new superuser"""
        user = self.create_user(email, password, username=username)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractUser, TimeStampedModel):
    """User in the system"""

    email = models.EmailField(blank=True, unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta(AbstractUser.Meta):
        ordering = ["-date_joined"]
