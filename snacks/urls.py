from django.urls import path
from snacks.views import SnackView, SnackDetailView

urlpatterns = [
    path("snacks/", SnackView.as_view()),
    path("snacks/<str:snack_id>/", SnackDetailView.as_view()),
]
