from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Blog_data(models.Model):

        Blog_Id=models.UUIDField(max_length=60,default=uuid.uuid4, editable=False)
        User_Name=models.CharField(max_length=30,null=False,editable=False)
        Blog_Name=models.CharField(max_length=30,null=False)
        Blog=models.TextField(null=False)
        Blog_Image=models.ImageField(upload_to='media/blogimg',max_length=250,null=True,default=None)
        Blog_Date=models.DateField(null=True)
        Id=models.AutoField(primary_key=True)
        Favourite=models.ManyToManyField(User)
        def __str__(self):
                return self.Blog_Name
                





    
