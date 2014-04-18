from django.db import models
from admin_resumable.fields import ModelAdminResumableFileField

class Foo(models.Model):
    bar = models.CharField(max_length=200)
    foo = ModelAdminResumableFileField()
