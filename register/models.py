from django.db import models
#register models
# Create your models here.
# Create your models here.
class User(models.Model):
	uname = models.CharField(max_length=20)
	uemail = models.EmailField(max_length=40)
	unumber = models.IntegerField()
	upassword = models.CharField(max_length=20)
    
    
class Meta:
	db_table = "user"