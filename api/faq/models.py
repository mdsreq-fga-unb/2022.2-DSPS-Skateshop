from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'faq'