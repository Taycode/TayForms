"""Form Serializers"""

from rest_framework import serializers
from .models import Form, Question


class CreateQuestionSerializer(serializers.Serializer):
	"""Serializer for Creating Questions"""
	question = serializers.CharField(required=True)
	description = serializers.CharField(required=False)

	def update(self, instance, validated_data):
		"""Update Method"""
		pass

	def create(self, validated_data):
		"""Create Method"""
		return Question.objects.create(**validated_data)


class CreateFormSerializer(serializers.Serializer):
	"""Serializer for Creating forms"""
	title = serializers.CharField(required=True)
	description = serializers.CharField(required=False)
	questions = CreateQuestionSerializer(many=True, source='question_set')

	def update(self, instance, validated_data):
		"""Update Method"""
		pass

	def create(self, validated_data):
		"""Create Method"""
		questions = validated_data.pop('question_set')
		form = Form.objects.create(**validated_data)
		questions_serializer = CreateQuestionSerializer(data=questions, many=True)
		questions_serializer.is_valid(raise_exception=True)
		questions_serializer.save(form=form)
		return form
