from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
    default=timezone.now)
    published_date= models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Job(models.Model):
    applicant=models.ForeignKey('auth.User')
    job_title=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    application_date=models.DateField()
    salary=models.IntegerField()
