from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe
from . models import User, MemberGroups
from import_export.admin import ImportExportActionModelAdmin


class UserAdmin(ImportExportActionModelAdmin, BaseUserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mobile_phone', 'email', 'is_active', 'is_admin')
    list_filter = list_filter = ('do_not_text', 'do_not_email','is_admin',)
    search_fields = ('first_name', 'last_name', 'email',)
    fieldsets = (
        ("Personal Information", {
            'fields': ('email', 'password', 'first_name', 'last_name','middle_name', 'picture', 'mobile_phone',
                'groups','birthdate', 'gender', 'passport_picture')
            }
        ),
        ("Addresses", {
            'fields': ('address_line', 'address_line_2', 'residence', 'gps_address',
                'city', 'do_not_text', 'home_phone', 'do_not_email', 'talents_or_hobbies')
            }
        ),
        ("Education & Profession", {
            'fields': ('employment_status', 'profession', 'office_phone', 'place_of_work', 'position')
            }
        ),
        ("Baptism", {
            'fields': ('baptized_church', 'location', 'date_of_baptism')
            }
        ),
        ("Relations", {
            'fields': ('marital_status',
                'name_of_spouse','spouses_phone_number', 'number_of_children', 'other_dependants', 'name_of_children', 
                'home_town', 'region', 'fathers_name', 'mothers_name')
            }
        ),
        ("Health", {
            'fields': ('blood_group', 'alergies')
            }
        ),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2'),
        }),
    )

    ordering = ('email',)
    filter_horizontal = ()
    readonly_fields = ['passport_picture']
    list_per_page = 100

    def passport_picture(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'. format(
            url=obj.picture.url,
            width=100,
            height=100,
            )
        )


class MemberGroupAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'description',)
    list_per_page = 25


admin.site.register(MemberGroups, MemberGroupAdmin)

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

