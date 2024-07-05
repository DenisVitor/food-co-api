from django.urls import path
from pizzas.views import PizzaDetailView, PizzaView

urlpatterns = [
    path("pizzas/", PizzaView.as_view()),
    path("pizzas/<str:pizza_id>", PizzaDetailView.as_view()),
]
