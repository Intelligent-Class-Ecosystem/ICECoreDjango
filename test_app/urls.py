from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:q_id>/vote/", views.vote, name="vote"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
]
