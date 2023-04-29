from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "사용자에게 특정 권한이 있습니까?"
        # 가장 간단한 대답: 네, 항상.
        return True

    def has_module_perms(self, app_label):
        "사용자에게 'app_label' 앱을 볼 수 있는 권한이 있습니까?"
        # 가장 간단한 대답: 네, 항상.
        return True

    @property
    def is_staff(self):
        "사용자가 직원입니까?"
        # 가장 간단한 대답: 모든 관리자는 직원입니다
        return self.is_admin