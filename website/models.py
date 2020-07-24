from django.db import models

# Create your models here.
class sender(models.Model):
    sender_email = models.CharField(max_length=200)
    reciver_email = models.CharField(max_length=200)
    otp = models.CharField(max_length=4)
    file = models.FileField(upload_to='media/am/')

    def __self__(self):
        return self.sender_email
