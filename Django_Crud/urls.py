from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("tasks/", views.tasks, name="tasks"),
    path ("signin/", views.signin, name="signin"),
    path ("signout/", views.signout, name="signout"),
    path ("tasks/create/", views.create_task, name="create_task"),
     path('tasks/select/<int:task_id>/', views.seleccionar, name='seleccionar'),
    path('tasks/edit/<int:task_id>/', views.editar_task, name='editar_task'),
    path('tasks/delete/<int:task_id>/', views.eliminar, name='eliminar')
    

]