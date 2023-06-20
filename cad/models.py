from django.db import models

class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.BigInteger(max_length=50)
    password = models.CharField(max_length=50)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class driver_detail(models.Model):
    driver_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=50)
    d_email = models.EmailField(max_length=50)
    d_phone = models.BigInteger()
    d_password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    d_photo=models.CharField(max_length=100)
    d_lat = models.CharField(max_length=100)
    d_long = models.CharField(max_length=100)
    d_status = models.models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class admin(models.Model):
        admin_id = models.AutoField(primary_key=True)
        username = models.CharField(max_length=50)
        password = models.CharField(max_length=50)