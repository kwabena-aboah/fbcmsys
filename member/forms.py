from django import forms 
from . models import FollowUp, Notes


class FollowUpForm(forms.ModelForm):
	class Meta:
		model = FollowUp
		fields = [
			'people', 'responsible', 'follow_up_date', 'follow_up_type',
			'from_time', 'to_time', 'action', 'done', 'notes'
		]


class NotesForm(forms.ModelForm):
	model = Notes
	fields = ['note', 'mark_as_private']