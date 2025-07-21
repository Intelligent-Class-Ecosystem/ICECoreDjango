from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views
from .views import OrganizationAPIViewSet

app_name = "ICE_Organization"

router = DefaultRouter()
router.register('organization', OrganizationAPIViewSet)

urlpatterns = [
    # path("", views.index, name="index"),
    path('', include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("temp_get_token/", views.temp_get_token, name="temp_get_token"),
    path("create_organization/", views.create_organization, name="create_organization"),
    path("create_classroom/", views.create_classroom, name="create_classroom"),
    path("create_timetable/", views.create_timetable, name="create_timetable"),
    path("create_activity/", views.create_activity, name="create_activity"),
    path("create_period/", views.create_period, name="create_period"),
    path("create_cycle/", views.create_cycle, name="create_cycle"),
    path("classroom_list/", views.classroom_list, name="classroom_list"),
    path("classroom_detail/", views.classroom_detail, name="classroom_detail"),
    path("activity_list/", views.activity_list, name="activity_list"),
    path("activity_detail/", views.activity_detail, name="activity_detail"),
    path("timetable_list/", views.timetable_list, name="timetable_list"),
    path("timetable_detail/", views.timetable_detail, name="timetable_detail"),
    path("period_list/", views.period_list, name="period_list"),
    path("period_detail/", views.period_detail, name="period_detail"),
    path("cycle_list/", views.cycle_list, name="cycle_list"),
    path("cycle_detail/", views.cycle_detail, name="cycle_detail"),
]