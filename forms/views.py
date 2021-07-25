"""Forms View"""

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView
)
from .serializers import (
	CreateFormSerializer
)
from .models import Form, Question

from rest_framework import serializers


class CreateFormAPIView(CreateAPIView):
	"""Creates Form"""
	serializer_class = CreateFormSerializer

	def perform_create(self, serializer):
		"""Perform Create method"""
		serializer.save(user=self.request.user)


class ListFormAPIView(ListAPIView):
	"""Lists Forms"""
	class OutputSerializer(serializers.ModelSerializer):
		"""Output Serializer"""
		class Meta:
			"""Meta Class"""
			model = Form
			fields = '__all__'
	serializer_class = OutputSerializer
	queryset = Form.objects.all()


class RetrieveFormAPIView(RetrieveAPIView):
	"""Retrieve Form"""

	class OutputSerializer(serializers.ModelSerializer):
		"""Retrieve Form Serializer"""

		class OutputQuestionSerializer(serializers.ModelSerializer):
			"""Retrieve Question Serializer"""

			class Meta:
				"""Meta Class"""
				model = Question
				exclude = ('form', )

		questions = OutputQuestionSerializer(source='question_set', many=True)

		class Meta:
			"""Meta Class"""
			model = Form
			fields = ('id', 'title', 'description', 'questions', 'user', )

	serializer_class = OutputSerializer
	queryset = Form.objects.all()
