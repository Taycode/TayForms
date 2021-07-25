"""Form Models"""

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Form(models.Model):
	"""Form"""
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)


class Response(models.Model):
	"""Response"""
	form = models.ForeignKey(Form, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
	"""Question"""
	form = models.ForeignKey(Form, on_delete=models.CASCADE)
	question = models.CharField(max_length=255)
	description = models.TextField(blank=True)


class Answer(models.Model):
	"""Answer"""
	response = models.ForeignKey(Response, on_delete=models.CASCADE)
	answer = models.CharField(max_length=255)

