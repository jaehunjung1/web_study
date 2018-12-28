from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.CharField(max_length=480)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    