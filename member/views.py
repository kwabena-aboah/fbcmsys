from django.shortcuts import render
from . serializer import FollowUpSerializer, NotesSerializer, CalendarSerializer, EventSerializer, OccurenceSerializer
from users.permissions import AdminOrAuthorCanEdit
from . models import FollowUp, Notes
from django.views.generic import TemplateView
from schedule.models import Calendar, Event, Occurrence
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated, IsAdminUser, SAFE_METHODS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from yaml import serialize



class IndexViewset(TemplateView):
    template_name = 'index.html'


class FollowUpViewset(viewsets.ModelViewSet):
    queryset = FollowUp.objects.all()
    serializer_class = FollowUpSerializer
    permission_classes = (IsAuthenticated, AdminOrAuthorCanEdit,)


class NotesViewset(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = (IsAuthenticated, AdminOrAuthorCanEdit,)


class CalendarViewset(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = (IsAuthenticated, AdminOrAuthorCanEdit,)


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, AdminOrAuthorCanEdit,)


class OccurenceViewset(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurenceSerializer
    permission_classes = (IsAuthenticated, AdminOrAuthorCanEdit,)