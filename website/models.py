from django.db import models
from django.contrib.auth.models import User

#from django.contrib.admin.widgets import AdminDateWidget
#from django import forms
#from django.forms.fields import DateField
from datetime import datetime
import datetime

# Create your models here.
Cat_choices=(
('E-COM','E-COM'),
('NEWS','NEWS'),
('SOCIAL','SOCIAL'),
('SPORTS','SPORTS'),
('ACADAMIC','ACADAMIC'),
('OTHER','OTHER'),
)
class website(models.Model):
    website_name=models.CharField(max_length=50)
    website_url=models.CharField(max_length=100)
    website_category=models.CharField(max_length=100,choices=Cat_choices)
    website_description=models.TextField()
    website_logo=models.FileField(upload_to='static/uploads/')
    def __str__(self):
        return self.website_name
class Comment(models.Model):
    now = datetime.datetime.now()
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    coment=models.TextField()
    webid=models.ForeignKey(website,on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.datetime.now)
    polar=models.FloatField(default=0,max_length=8)
    rating=models.IntegerField(default=0)
    def __str__(self):
        return self.coment
