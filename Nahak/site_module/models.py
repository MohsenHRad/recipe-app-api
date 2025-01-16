from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True, db_index=True, null=False, blank=False,
                                verbose_name='نام کاربری')
    email = models.EmailField(max_length=200, unique=True, null=False, blank=False, verbose_name='ایمیل')
    email_active_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="کد فعالسازی ایمیل")
    mobile = models.CharField(max_length=13, null=True, blank=True, verbose_name='شماره تماس')
    avatar = models.ImageField(upload_to='uploads/avatars', null=True, blank=True, verbose_name='عکس پروفایل')
    about_author = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.username
