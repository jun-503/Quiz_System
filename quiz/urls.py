from django.urls import path
from . import views

urlpatterns = [
    path('quiz/',views.quiz_view,name = 'quiz_view'),
     path('score/', views.score_view, name='score_view'),
]

