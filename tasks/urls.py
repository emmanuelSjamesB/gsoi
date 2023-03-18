
from django.urls import  path
from tasks import views
urlpatterns = [


path(
    '', views.home, name='Home' ),
    path('signup/', views.signup, name='SignUp'),
    path('task/', views.tasks, name='Tasks'),
    path('tasks_completed/', views.tasks_completed, name='Tasks_completed'),
    path('logout/', views.cerrarSession, name='Logout'),
    path('login/', views.signin, name='Login'),
    path('task/create/', views.create_task, name='Create_task'),
    path('task/<int:task_id>/', views.task_detail, name='Task_detail'),
    path('task/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('task/<int:task_id>/delete', views.delete_task, name='delete_task'),

]