from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, User, PermissionsMixin
from django.db import models

# Admin Email: admin@localhost.com
# Admin Password: goshev135


# This is my custom user model

# objects.all(), objects.get(), object.create(), etc...
# are called managers


class CustomerUserManagerModel(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)




# Extending the user model
class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    # In users model we will find the is_staff and is_superuser attributes above
    is_staff = models.BooleanField(
        default=False,
    )

    # Choosing which field to be used as a username to login
    USERNAME_FIELD = 'email'
    # Overriding objects (managers) so we can access admin-panel with email address
    # and be able to create a superuser
    objects = CustomerUserManagerModel()