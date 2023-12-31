# Generated by Django 4.2.4 on 2023-08-05 04:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True, verbose_name='Gender')),
                ('father_name', models.CharField(help_text='Will be shown e.g. when commenting', max_length=30, verbose_name='Father name')),
                ('emergency_contact_name1', models.CharField(help_text='Will be shown e.g. when commenting', max_length=30, verbose_name='Display name')),
                ('emergency_contact_relation1', models.CharField(help_text='Will be shown e.g. when commenting', max_length=30, verbose_name='Display name')),
                ('passport_number', models.CharField(help_text='Will be shown e.g. when commenting', max_length=30, verbose_name='Display name')),
                ('address1', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 1')),
                ('pin_code', models.CharField(blank=True, max_length=12, null=True, verbose_name='Postal Code')),
                ('city', models.CharField(blank=True, max_length=1024, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=6, null=True, verbose_name='State')),
                ('country', django_countries.fields.CountryField(blank=True, default='India', max_length=5, null=True)),
                ('address3', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 1')),
                ('pin_code1', models.CharField(blank=True, max_length=12, null=True, verbose_name='Postal Code')),
                ('city1', models.CharField(blank=True, max_length=1024, null=True, verbose_name='City')),
                ('state1', models.CharField(blank=True, max_length=6, null=True, verbose_name='State')),
                ('mobile_phone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Mobile phone')),
                ('aadhar_no', models.CharField(default='000000000000', max_length=12)),
                ('marital_status', models.BooleanField(default=False)),
                ('pan_no', models.CharField(help_text='Will be shown e.g. when commenting', max_length=10, verbose_name='PAN')),
                ('accountnumber', models.CharField(default='0000000000000', max_length=13)),
                ('accounttype', models.CharField(default='abc', max_length=13)),
                ('bank_name', models.CharField(help_text='Will be shown e.g. when commenting', max_length=250, verbose_name='Display name')),
                ('ifsc_code', models.CharField(help_text='Will be shown e.g. when commenting', max_length=30, verbose_name='Display name')),
                ('nationality', models.CharField(default='Indian', help_text='Will be shown e.g. when commenting', max_length=30, verbose_name='Display name')),
                ('religion', models.CharField(default='NA', help_text='Will be shown e.g. when commenting', max_length=30, verbose_name='Display name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
