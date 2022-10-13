import os, random
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, Group
)
# from .validators import validate_image_extension
from . get_usernames import current_request
from tinymce.models import HTMLField


def filename_ext(filepath):
    file_base = os.path.basename(filepath)
    filename, ext = os.path.splitext(file_base)
    return filename, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9498594795)
    name, ext = filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "pictures/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

GENDER = (
    ('male', 'male'),
    ('female', 'female'),
)

EMPLOYMENT_STATUS = (
    ('employed', 'employed'),
    ('unemployed', 'unemployed'),
    ('student', 'student'),
)

MARITAL_STATUS = (
    ('married', 'married'),
    ('divorcee', 'divorcess'),
    ('widow', 'widow'),
    ('widower', 'widower'),
    ('single', 'single'),
)


class MemberGroups(Group):
    description = models.TextField(null=True, blank=True, verbose_name="Group description")

    def __str__(self):
        return self.description or self.name 

    class Meta:
        verbose_name = "Member Group"
        verbose_name_plural = "Member Groups"


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def active(self):
        qs = self.get_queryset().filter(active=True)
        return qs

    def deleted(self):
        return self.get_queryset().filter(active=False)

    def do_not_text(self):
        return self.active().filter(do_not_text=False)

    def do_not_email(self):
        return self.active().filter(do_not_email=False)


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True,)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateField(auto_now_add=False, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER)
    address_line = models.CharField(max_length=255, null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    residence = models.CharField(max_length=255, null=True, blank=True)
    gps_address = models.CharField(max_length=12, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    mobile_phone = models.CharField(max_length=15, null=True, blank=True)
    do_not_text = models.BooleanField(default=False)
    home_phone = models.CharField(max_length=15, null=True, blank=True)
    do_not_email = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        MemberGroups,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions granted to each of their group.'),
        related_name="user_set",
        related_query_name="user",
    )
    talents_or_hobbies = models.CharField(max_length=255, null=True, blank=True)
    employment_status = models.CharField(max_length=10, null=True, blank=True, choices=EMPLOYMENT_STATUS)
    profession = models.CharField(max_length=255, null=True, blank=True)
    office_phone = models.CharField(max_length=15, null=True, blank=True)
    place_of_work = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    fathers_name = models.CharField(max_length=255, null=True, blank=True)
    mothers_name = models.CharField(max_length=255, null=True, blank=True)
    blood_group = models.CharField(max_length=50, null=True, blank=True)
    alergies = models.CharField(max_length=255, null=True, blank=True, help_text='Any known perculiar disease')
    marital_status = models.CharField(max_length=10, null=True, blank=True, choices=MARITAL_STATUS)
    name_of_spouse = models.CharField(max_length=255, null=True, blank=True, help_text='If Married')
    spouses_phone_number = models.CharField(max_length=15, null=True, blank=True)
    number_of_children = models.IntegerField(null=True, blank=True)
    other_dependants = models.IntegerField(null=True, blank=True)
    name_of_children = HTMLField(null=True, blank=True, default="")
    home_town = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    baptized_church = models.CharField(max_length=255, null=True, blank=True, help_text='Name of Church that Baptized you')
    location = models.CharField(max_length=255, null=True, blank=True)
    date_of_baptism = models.DateField(auto_now_add=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.first_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    # def __str__(self):
    #     return f'{self.name_on_id} {self.national_id_number}'

