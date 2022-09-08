from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, first_name, middle_name, last_name, email, phone, username, password=None, ):
        if not email:
            raise ValueError('Users require an email field')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name,
                          middle_name=middle_name,
                          last_name=last_name,
                          email=self.normalize_email(email),
                          phone=phone,
                          username=username
                          )
        user.set_password(password)
        user.is_expert = False
        user.is_staff = True
        user.is_active = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, middle_name, last_name, email, phone, password, username):
        user = self.create_user(first_name, middle_name, last_name, email, phone, username, password)
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name="email", max_length=220, unique=True)
    phone = models.CharField(max_length=210, blank=False, null=False)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login joined", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    is_expert = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'middle_name', 'last_name', 'phone']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
