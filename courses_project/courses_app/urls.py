from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirHome),
    path('courses', views.homePage),
    path('courses/create', views.createCourse),
    path('courses/<int:id>/destroyConfirmation', views.destroyConfirmation),
    path('courses/<int:id>/destroy', views.destroyCourse)
]