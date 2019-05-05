from django.urls import path
from api import views

urlpatterns = [

    path('api/task_lists/', views.Tasklists),
    path('api/task_lists/<int:pk>/', views.TasklistDetail),
    path('api/task_lists/<int:pk>/tasks', views.Tasks.as_view()),
    path('api/tasks/<int:pk>', views.TaskDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
]
