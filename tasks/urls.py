from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('task/<int:pk>/update/', views.update_task, name='update_task'),
    path('delete/<int:pk>', views.delete_task, name='delete_task'),
    path('label_list/', views.label_list, name='label_list'),
    path('create_label/', views.create_label, name='create_label'),
    path('label/<int:pk>/update/', views.update_label, name='update_label')
]
