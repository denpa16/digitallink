from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator

class Phone(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)


class File(models.Model):
    file = models.FileField(blank=False, null=False, validators=[FileExtensionValidator(allowed_extensions=['xlsx'])])
    title = models.CharField(max_length=100, blank=True)