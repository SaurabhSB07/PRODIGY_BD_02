from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDeleteView

urlpatterns = [
    path('users/', UserListCreateView.as_view()),
    path('users/<uuid:pk>/', UserRetrieveUpdateDeleteView.as_view()),
]
