import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.middleware.csrf import get_token

from .models import Organization, Classroom, Cycle, Timetable, Activity, Period

# Create your views here.

class OrganizationDetailView(generic.DetailView):
    model = Organization
    template_name = 'ICE_Organization/organization_detail.html'

def temp_get_token(request):
    token = get_token(request)
    return HttpResponse(json.dumps({"csrf_token":token}), content_type="application/json,charset=utf-8")

def create_organization(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        organization = Organization.objects.create(name=name, description=description)
        return redirect('organization_detail', pk=organization.id)
    else:
        return None