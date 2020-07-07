"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics.
    path('topic/', views.topics, name='topics')
]
