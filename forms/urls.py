"""Forms URL PAtterns"""


from django.urls import path
from .views import (
	CreateFormAPIView,
	ListFormAPIView,
	RetrieveFormAPIView,
	CreateResponseAPIView,
	ListResponseAPIView,
	RetrieveResponseAPIView
)

urlpatterns = [
	path('', CreateFormAPIView.as_view()),
	path('fetch/', ListFormAPIView.as_view()),
	path('<int:pk>/', RetrieveFormAPIView.as_view()),
	path('<int:pk>/response/create/', CreateResponseAPIView.as_view()),
	path('<int:pk>/response/fetch/', ListResponseAPIView.as_view()),
	path('response/<int:pk>/', RetrieveResponseAPIView.as_view()),
]
