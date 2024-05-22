from django.db import models
from django.utils import timezone

# Create your models here.
class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class JobListing(models.Model):
    job_logo = models.ImageField()
    job_title = models.CharField(max_length=300)
    job_start = models.DateField("Start Date")
    job_end = models.DateField("End Date")
    job_description = models.CharField(max_length=3000)

    def __str__(self):
        return f"'{self.job_title}'"
    
class KeywordList(models.Model):
    kword = models.CharField(max_length=100)
    kword_link = models.CharField(max_length=300)

    def __str__(self):
        return f"'{self.kword}' : '{self.kword_link}'"
    