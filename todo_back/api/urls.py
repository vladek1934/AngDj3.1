from django.urls import path
from api import views

urlpatterns = [

    path('api/task_lists/', views.Tasklists.as_view()),
    path('api/task_lists/<int:pk>/', views.TasklistDetail.as_view()),
    path('api/task_lists/<int:pk>/tasks', views.Tasks.as_view()),
    path('api/tasks/<int:pk>', views.TaskDetail.as_view()),

    path('api/login/', views.login),
    path('api/logout/', views.logout)
]
