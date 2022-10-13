from tokenize import Token
from rest_framework import serializers
from . models import FollowUp, Notes
from schedule.models import Calendar, Event, Occurrence


class FollowUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = FollowUp
		fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notes 
		fields = '__all__'


class CalendarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Calendar
		fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event 
		fields = '__all__'


class OccurenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Occurrence
		fields = '__all__'