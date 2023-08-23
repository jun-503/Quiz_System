
from django.contrib import admin
from django.urls import path,include

from authentication import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('quiz/',include('quiz.urls'))

]
