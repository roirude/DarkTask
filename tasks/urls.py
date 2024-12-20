from django.urls import path

from tasks import views


urlpatterns = [
    path('tasks/', views.TaskListAPIView.as_view(), name='task_list'),
    path('tasks/<int:pk>/status/', views.TaskDetailAPIView.as_view(), name='task_status_update'),
    path('tasks/<int:pk>/', views.TaskDetailAPIView.as_view(), name='task_detail'),
]
