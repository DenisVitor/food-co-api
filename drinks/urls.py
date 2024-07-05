from django.urls import path
from drinks.views import DrinkView, DrinkDetailView

urlpatterns = [
    path("drinks/", DrinkView.as_view()),
    path("drinks/<str:drink_id>", DrinkDetailView.as_view()),
]
