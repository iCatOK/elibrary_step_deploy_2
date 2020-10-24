from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=60, blank=True)
    address = models.TextField(max_length=500, blank=True)

class User(AbstractBaseUser, PermissionsMixin):

    class ReaderStatus(models.TextChoices):
        NOBOOK = 'NB', _('Без книги')
        BORROWED = 'BR', _('Пользуется книгу')
        DEBTOR = 'DB', _('Должник')
    

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=2, choices=ReaderStatus.choices, 
        default=ReaderStatus.NOBOOK 
    )

    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=200)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.full_name
