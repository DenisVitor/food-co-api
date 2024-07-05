from django.urls import path
from burgers.views import BurguerView, BurgerDetailView

urlpatterns = [
    path("burgers/", BurguerView.as_view()),
    path("burgers/<str:burger_id>", BurgerDetailView.as_view()),
]
