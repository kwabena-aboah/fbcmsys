from django.contrib import admin
from . models import FollowUp, Notes 
from . forms import FollowUpForm, NotesForm
from import_export.admin import ImportExportActionModelAdmin


admin.site.site_header = "FBCMSYS Admin"
admin.site.site_title = "FBCMSYS Admin Portal"
admin.site.index_title = "Welcome to FBCMSYS Portal"


class FollowUpAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
	list_display = ('responsible', 'follow_up_date', 'follow_up_type', 'done')
	list_filter = ('done', 'action',)
	search_fields = ('responsible',)
	ordering = ('follow_up_type',)
	filter_horizontal = ()
	form = FollowUpForm
	list_per_page = 100

	# def save_model(self, request, obj, form, change):
	# 	'''Automatically save user on submit'''
	# 	if getattr(obj, 'id', True) is not None:
	# 		self.user = request.user
	# 		obj.save()
	# 	super().save_model(request, obj, form, change)


class NotesAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
	list_display = ('note', 'mark_as_private', 'user')
	list_filter = ('mark_as_private',)
	search_fields = ('user',)
	ordering = ('user',)
	exclude = ['user']
	filter_horizontal = ()
	form = NotesForm
	fieldsets = [
		("Header", {'fields': ["note"]}),
		("Security", {'fields': ['mark_as_private']})
	]
	list_per_page = 50

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'id', True) is not None:
			self.user = request.user
			obj.save()
		super().save_model(request, obj, form, change)


admin.site.register(Notes, NotesAdmin)
admin.site.register(FollowUp, FollowUpAdmin)