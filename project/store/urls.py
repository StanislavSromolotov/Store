from django.urls import path

from project.store import views


app_name = "main"

urlpatterns = [
    path("", views.store, name="mystore"),
    path("phones/", views.phones, name="phones"),
    path("cases/", views.cases, name="cases"),
    path("basket/", views.basket, name="basket"),
]
