from django.urls import path
from . import views

app_name = "ICE_Organization"

urlpatterns = [
    # path("", views.index, name="index"),
    path("temp_get_token/", views.temp_get_token, name="temp_get_token"),
    path("create_organization/", views.create_organization, name="create_organization"),
    path("<int:pk>/", views.OrganizationDetailView.as_view(), name="organization_detail"),
]