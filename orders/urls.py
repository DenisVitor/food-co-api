from django.urls import path
from orders.views import (
    OrderReadView,
    OrderCreateView,
    OrderUpdateView,
    OrderRetrieveView,
    OrderDestroyView
)

urlpatterns = [
    path("orders/", OrderReadView.as_view()),
    path("orders/create/", OrderCreateView.as_view()),
    path("orders/<str:order_id>/", OrderRetrieveView.as_view()),
    path("orders/<str:order_id>/update/", OrderUpdateView.as_view()),
    path("orders/<str:order_id>/delete/", OrderDestroyView.as_view()),
]
