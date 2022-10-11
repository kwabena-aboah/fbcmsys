import os, random
from users.models import User
from django.db import models
from users.get_usernames import current_request
from tinymce.models import HTMLField


FOLLOW_UP_TYPE = (
	('visit', 'visit'),
	('text', 'text'),
	('call', 'call'),
	('email', 'email'),
)

ACTION = (
	('care', 'care'),
	('ceremony', 'ceremony'),
	('other', 'other'),
)

class FollowUp(models.Model):
	people = models.ManyToManyField(
		User, 
		verbose_name=('members'), 
		blank=True,
		help_text="Select one or more members to make follow up on. Could be new members, sick members etc",
		related_name="members_set",
		related_query_name="members")
	responsible = models.CharField(max_length=255, blank=True, null=True)
	follow_up_date = models.DateField(auto_now_add=False, blank=True, null=True)
	follow_up_type = models.CharField(max_length=6, null=True, blank=True, choices=FOLLOW_UP_TYPE)
	from_time = models.TimeField(auto_now_add=False, null=True, blank=True)
	to_time = models.TimeField(auto_now_add=False, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION)
	done = models.BooleanField(default=False)
	notes = HTMLField(blank=True, null=True, default="")

	def __str__(self):
		return f'{self.responsible}'

	class Meta:
		verbose_name = 'Follow Up'
		verbose_name_plural = 'Follow Ups'


# 	def save(self, *args, **kwargs):
# 		'''Automatically save user'''
# 		if not self.id:
# 			self.user = current_request().user
# 		return super(Person, self).save(*args, **kwargs)


class Notes(models.Model):
	note = HTMLField(blank=True, null=True, default="")
	mark_as_private = models.BooleanField(default=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.note}'

	class Meta:
		verbose_name = 'Note'
		verbose_name_plural = 'Notes'

	def save(self, *args, **kwargs):
		"""Automatically save user on entry """
		if not self.id:
			self.user = current_request().user 
		return super(Notes, self).save(*args, **kwargs)