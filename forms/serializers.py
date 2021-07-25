"""Form Serializers"""

from rest_framework import serializers
from .models import (
	Form,
	Question,
	Answer,
	Response
)


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


class FormModelSerializer(serializers.ModelSerializer):
	"""Serializer for Form Model"""
	class Meta:
		"""Meta Class"""
		model = Form
		fields = '__all__'


class CreateAnswerSerializer(serializers.Serializer):
	"""Serializer for creating Answers"""

	answer = serializers.CharField()
	question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

	def update(self, instance, validated_data):
		"""Update Method"""
		pass

	def create(self, validated_data):
		"""Create Method"""
		return Answer.objects.create(**validated_data)


class CreateResponseSerializer(serializers.Serializer):
	"""Serializer for creating responses"""
	answers = CreateAnswerSerializer(many=True, source='answer_set')
	form = FormModelSerializer(read_only=True)

	def update(self, instance, validated_data):
		"""Update Method"""
		pass

	def create(self, validated_data):
		"""Create Method"""
		def convert_question_to_question_id(answer):
			"""Converts question to question id"""
			answer['question'] = answer['question'].id
			return answer

		answers = validated_data.pop('answer_set')
		answers = list(map(convert_question_to_question_id, answers))
		response = Response.objects.create(**validated_data)
		answer_serializer = CreateAnswerSerializer(data=answers, many=True)
		answer_serializer.is_valid(raise_exception=True)
		answer_serializer.save(response=response)
		return response


class QuestionModelSerializer(serializers.ModelSerializer):
	"""Question Model Serializer"""
	class Meta:
		"""Meta Class"""
		model = Question
		exclude = ('form', )


class ResponseModelSerializer(serializers.ModelSerializer):
	"""Response Model Serializer"""
	class Meta:
		"""Meta Class"""
		model = Response
		exclude = ('form', )


class AnswerModelSerializer(serializers.ModelSerializer):
	"""Answer Serializer"""
	question = QuestionModelSerializer()

	class Meta:
		"""Meta Class"""
		model = Answer
		fields = ('answer', 'question', )
