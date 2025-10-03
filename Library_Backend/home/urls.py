from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index_view, name='index'),
    path('request_retrieval/', views.request_retrieval, name='request_retrieval'),

    path('admin_shelves/', views.admin_shelves, name='admin_shelves'),
    path('approve_assignment/', views.approve_assignment, name='approve_assignment'),
    path('confirm_retrieval/', views.confirm_retrieval, name='confirm_retrieval'),
]
