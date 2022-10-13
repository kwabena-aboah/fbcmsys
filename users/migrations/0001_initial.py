# Generated by Django 4.0.6 on 2022-07-25 11:44

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberGroups',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Group description')),
            ],
            options={
                'verbose_name': 'Member Group',
                'verbose_name_plural': 'Member Groups',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=10, null=True)),
                ('address_line', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('residence', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('do_not_text', models.BooleanField()),
                ('home_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('do_not_email', models.BooleanField()),
                ('talents_or_hobbies', models.CharField(blank=True, max_length=255, null=True)),
                ('employment_status', models.CharField(blank=True, choices=[('employed', 'employed'), ('unemployed', 'unemployed'), ('student', 'student')], max_length=10, null=True)),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('office_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('place_of_work', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=users.models.upload_image_path)),
                ('fathers_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mothers_name', models.CharField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=50, null=True)),
                ('alergies', models.CharField(blank=True, help_text='Any known perculiar disease', max_length=255, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('married', 'married'), ('divorcee', 'divorcess'), ('widow', 'widow'), ('widower', 'widower'), ('single', 'single')], max_length=10, null=True)),
                ('name_of_spouse', models.CharField(blank=True, help_text='If Married', max_length=255, null=True)),
                ('spouses_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('number_of_children', models.IntegerField(blank=True, null=True)),
                ('other_dependants', models.IntegerField(blank=True, null=True)),
                ('name_of_children', models.TextField(blank=True, help_text='Separate each entry by a comma. Attach ages of kids using brackets.', null=True)),
                ('home_town', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('baptized_church', models.CharField(blank=True, help_text='Name of Church that Baptized you', max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_baptism', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their group.', related_name='user_set', related_query_name='user', to='users.membergroups', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
