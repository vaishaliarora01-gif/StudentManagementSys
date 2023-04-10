"""
URL patterns for the Student app.
"""

from django.urls import path
from Student import views

app_name = 'Student'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('signup/', views.signupview, name='signup'),
    path('list/', views.student_view, name='list'),
    path('add/', views.student_add, name='add'),
    path('<int:id>/', views.student_delete, name='delete'),
    path('<int:id>/update', views.student_update, name='update'),
    path('about/', views.student_about, name='about'),
    path('contact/', views.student_contact, name='contact'),
    path('home/', views.student_home, name='home'),
    path('privacy/', views.student_privacy, name='privacy'),
    path('<int:id>/', views.student_show, name='show'),
]
