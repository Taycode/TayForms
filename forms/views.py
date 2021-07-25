"""Forms View"""

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView
)
from .serializers import (
	CreateFormSerializer,
	CreateResponseSerializer,
	FormModelSerializer,
	QuestionModelSerializer,
	AnswerModelSerializer
)
from .models import Form, Question, Response, Answer

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
			ref_name = 'list_form_api_view'

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
			ref_name = 'retrieve_form_api_view'

	serializer_class = OutputSerializer
	queryset = Form.objects.all()


class CreateResponseAPIView(CreateAPIView):
	"""Creates Response"""
	serializer_class = CreateResponseSerializer

	def perform_create(self, serializer):
		"""Perform Create process"""
		form = Form.objects.get(id=self.kwargs.get('pk'))
		serializer.save(form=form)

	def get_queryset(self):
		"""Filter Query set"""
		return Response.objects.filter(form_id=self.kwargs.get('pk'))


class ListResponseAPIView(ListAPIView):
	"""Lists Responses"""

	class OutputSerializer(serializers.ModelSerializer):
		"""Output Serializer"""
		class Meta:
			"""Meta Class"""
			model = Response
			fields = '__all__'
			ref_name = 'list_response_api_view'

	serializer_class = OutputSerializer

	def get_queryset(self):
		"""Filter Query set"""
		return Response.objects.filter(form_id=self.kwargs.get('pk'))


class RetrieveResponseAPIView(RetrieveAPIView):
	"""Retrieves Response"""

	class OutputSerializer(serializers.ModelSerializer):
		"""Output Serializer"""
		form = FormModelSerializer()
		answers = AnswerModelSerializer(many=True, source='answer_set')

		class Meta:
			"""Meta Class"""
			model = Response
			fields = ('form', 'created_at', 'answers', )
			ref_name = 'retrieve_response_api_view'

	serializer_class = OutputSerializer
	queryset = Response.objects.all()
