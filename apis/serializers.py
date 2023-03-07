from rest_framework import serializers
from .models import users,driver_detail

class usersSerializer(serializers.ModelSerializer):
      class Meta:
        model =users
        fields =  (
                "user_id",
                "name",
                "email", 
                "phone",
                "password",
                "age",
                "gender", 
                # "fire_id",
                "created_on"
        
        
        )
        class Meta:

                fields = '__all__'


    
    # fname = serializers.CharField(max_length=200,required = True)
    # lname = serializers.CharField(max_length=200,required = True)
    # email = serializers.CharField(max_length=200,required = True)
    # phone = serializers.CharField(max_length=200,required = True)
    # password = serializers.CharField(
    #     write_only = True,
    #     required = True,
    #     help_text  ='leave empty is no changes needed',
    #     style = {'input_type':'password','placeholder':'password'}
    # )
    # age = serializers.IntegerField()
    # gender = serializers.CharField(max_length=100,required=True)
    # Firebase_id = serializers.CharField(max_length=200,required=True)

    # class Meta:
    #     model = users

class driver_detailSerializer(serializers.ModelSerializer):

       class Meta:
        model =driver_detail
        fields =  (
                "driver_id",
                "d_name",
                "d_email", 
                "d_phone",
                "d_password",
                # "age",
                "gender", 
                # "fire_id",
                "created_on"
        
        
        )
        class Meta:

                fields = '__all__'
