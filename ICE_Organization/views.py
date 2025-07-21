import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.middleware.csrf import get_token

# noinspection PyUnresolvedReferences
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.

class OrganizationAPIViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def temp_get_token(request):
    response = HttpResponse(status=200)
    response["X-CSRFToken"] = get_token(request)
    return response

def get_post_or_400(request):
    if request.method != 'POST':
        return HttpResponse(status=400)
    return None

def create_organization(request):
    if get_post_or_400(request) is not None: return get_post_or_400(request)
    name = request.POST['name']
    description = request.POST['description']
    organization = Organization.objects.create(name=name, description=description)
    organization.save()
    return HttpResponse(status=200)

def create_classroom(request):
    if get_post_or_400(request) is not None: return get_post_or_400(request)
    name = request.POST['name']
    description = request.POST['description']
    organization_id = request.POST['organization_id']
    organization = get_object_or_404(Organization, pk=organization_id)
    classroom = Classroom.objects.create(name=name, description=description, organization=organization)
    classroom.save()
    return HttpResponse(status=200)

def create_timetable(request):
    if get_post_or_400(request) is not None: return get_post_or_400(request)
    name = request.POST['name']
    description = request.POST['description']
    periods = [get_object_or_404(Period, pk=period_id) for period_id in request.POST['periods_id']]
    timetable = Timetable.objects.create(name=name, description=description, periods=periods)
    timetable.save()
    return HttpResponse(status=200)

def create_activity(request):
    if get_post_or_400(request) is not None: return get_post_or_400(request)
    name = request.POST['name']
    description = request.POST['description']
    activity = Activity.objects.create(name=name, description=description)
    activity.save()
    return HttpResponse(status=200)

def create_period(request):
    if get_post_or_400(request) is not None: return get_post_or_400(request)
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    activity_id = request.POST['activity_id']
    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        activity = EMPTY_ACTIVITY
    period = Period.objects.create(start_time=start_time, end_time=end_time, activity=activity)
    period.save()
    return HttpResponse(status=200)

def create_cycle(request):
    if get_post_or_400(request) is not None: return get_post_or_400(request)
    name = request.POST['name']
    description = request.POST['description']
    cycle = Cycle.objects.create(name=name, description=description)
    timetables = [get_object_or_404(Timetable,pk=timetable_id) for timetable_id in request.POST['timetable_id']]
    for timetable in timetables:
        timetable.belong_cycle = cycle
    return HttpResponse(status=200)

def classroom_list(request):
    ret = [clsrm.get_dict() for clsrm in Classroom.objects.all()]
    return HttpResponse(json.dumps(ret), content_type="application/json")

def classroom_detail(request, classroom_id):
    ret = get_object_or_404(Classroom, pk=classroom_id).get_dict()
    return HttpResponse(json.dumps(ret), content_type="application/json")

def timetable_list(request):
    ret = [timetable.get_dict() for timetable in Timetable.objects.all()]
    return HttpResponse(json.dumps(ret), content_type="application/json")

def timetable_detail(request, timetable_id):
    ret = get_object_or_404(Timetable, pk=timetable_id).get_dict()
    return HttpResponse(json.dumps(ret), content_type="application/json")

def period_list(request):
    ret = [period.get_dict() for period in Period.objects.all()]
    return HttpResponse(json.dumps(ret), content_type="application/json")

def period_detail(request, period_id):
    ret = get_object_or_404(Period, pk=period_id).get_dict()
    return HttpResponse(json.dumps(ret), content_type="application/json")

def activity_list(request):
    ret = [activity.get_dict() for activity in Activity.objects.all()]
    return HttpResponse(json.dumps(ret), content_type="application/json")

def activity_detail(request, activity_id):
    ret = get_object_or_404(Activity, pk=activity_id).get_dict()
    return HttpResponse(json.dumps(ret), content_type="application/json")

def cycle_list(request):
    ret = [cycle.get_dict() for cycle in Cycle.objects.all()]
    return HttpResponse(json.dumps(ret), content_type="application/json")

def cycle_detail(request, cycle_id):
    ret = get_object_or_404(Cycle, pk=cycle_id).get_dict()
    return HttpResponse(json.dumps(ret), content_type="application/json")

