"""User Model"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
	"""Custom User Model"""
	email = models.EmailField(_('email address'), unique=True)

	def __str__(self):
		return self.email
