from django.urls import path

from . import views


app_name = 'shibousuitei'
urlpatterns = [
    path("", views.select, name="select"),
]