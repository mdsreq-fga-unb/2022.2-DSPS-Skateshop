from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel  # Model with created and modified columns
from autoslug import AutoSlugField
from django.urls import reverse

class User(AbstractUser):
    pass
