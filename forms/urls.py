"""Forms URL PAtterns"""


from django.urls import path
from .views import (
	CreateFormAPIView,
	ListFormAPIView,
	RetrieveFormAPIView
)

urlpatterns = [
	path('', CreateFormAPIView.as_view()),
	path('fetch/', ListFormAPIView.as_view()),
	path('<int:pk>/', RetrieveFormAPIView.as_view())
]
