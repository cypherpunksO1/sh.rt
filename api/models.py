from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _  # Переводит строки на англ.
from api.base.validators import *


# Create your models here.

class CustomUser(AbstractUser):
    ...


class Link(models.Model):
    link = models.TextField(help_text=_('Ссылка для сокращения вида https://domen.com/path/.'),
                            validators=[validate_link],
                            verbose_name='ссылка')
    key = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')

    passed = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'ссылка'
        verbose_name_plural = 'ссылки'