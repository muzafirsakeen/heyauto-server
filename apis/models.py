from django.db import models

# Create your models here.
class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)

class driver_detail(models.Model):
    driver_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=200)
    d_email = models.EmailField(max_length=200)
    d_phone = models.BigIntegerField()
    d_password = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    # d_photo=models.ImageField(upload_to='driversphoto',max_length=255, null=True, blank=True,default='images/None/No0img.jpg')
    created_on = models.DateTimeField(auto_now_add=True)
    

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)    

# no editing needed

class driver_photo(models.Model):

    photo_id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey(driver_detail,on_delete=models.CASCADE,)
    d_photo=models.ImageField(upload_to='driversphoto',max_length=255, null=True, blank=True,default='images/None/No0img.jpg')


