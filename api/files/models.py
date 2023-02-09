import os

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.storage import DefaultStorage


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class FileModel(models.Model):
    file = models.FileField(upload_to="files/", storage=S3Boto3Storage(bucket_name="dspskateshop"))
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=64, null=False, default="Patrocinado")

    active = ActiveManager()

    def __str__(self):
        return self.file.name
