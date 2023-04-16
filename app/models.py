from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name
    
class webpg(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    webpage=models.URLField()
    email=models.EmailField()
    def __str__(self):
        return self.name
    
class accessrec(models.Model):
    name=models.ForeignKey(webpg,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return self.author