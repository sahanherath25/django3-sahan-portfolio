from django.urls import path
from portfolio import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home_page,name="main"),
    path("<int:content_id>/", views.contents, name="content"),
]
