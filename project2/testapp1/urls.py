from django.urls import path
from . import views

urlpatterns=[
    path("home/", views.home_view),
    path("python/", views.python_view),
    path("java/", views.java_view),
    path("sform/", views.students_form_view),
    path("sdata/", views.students_display_view),
    path("sdelete/<no>", views.students_delete_view),
    path("supdate/<no>", views.students_update_view),
    path("signup/", views.signup_view),
    path("logout/", views.login_view),
    path("demo/", views.demo_view),
]