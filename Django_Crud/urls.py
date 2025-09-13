from django.contrib import admin
from django.urls import path
from Tasks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("Tasks/", views.tasks, name="Tasks"),
    path ("signin/", views.signin, name="signin"),
    path ("signout/", views.signout, name="signout"),
    path ("tasks/create/", views.create_task, name="create_task"),

]