from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics, permissions, serializers
from rest_framework.parsers import MultiPartParser, FormParser
import hashlib
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect



from django.views.decorators.csrf import csrf_exempt, csrf_protect
import uuid
from .models import users,driver_detail
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from .serializers import usersSerializer,driver_detailSerializer
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.
# to fetch all users


@api_view(['GET', 'POST', 'DELETE'])
def get_all_users(request):
    if request.method == 'GET':
        tutorials = users.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = usersSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        return render(request,'index.html',{'response':response})

        # 'safe=False' for objects serialization
 
    # elif request.method == 'POST':
        # tutorial_data = JSONParser().parse(request)
        # tutorial_serializer = usersSerializer(data=tutorial_data)
        # if tutorial_serializer.is_valid():
            # tutorial_serializer.save()
            # return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = users.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)








# class usersView(APIView):  
  
#     def get(self, request, *args, **kwargs):  
#         result = users.objects.all()  
#         serializers = usersSerializer(result, many=True)  
#         return Response({'status': 'success', "users":serializers.data}, status=200)  
#         class Meta:
#             model = users
  
#     def post(self, request):  
#        serializer = usersSerializer(data=request.data)  
#        if serializer.is_valid():  
#            serializer.save()  
#            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
#        else:  
#            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# 
@csrf_exempt
def reg_user(request):
    userdata = request.GET
    user = users(
        name = userdata['name'],
        email = userdata['email'],
        phone = userdata['phone'],
        password = hashlib.md5(userdata['password'].encode("utf-8")).hexdigest(),
        age = userdata['age'],
        # Firebase_id = userdata['fire_id'],
        gender = userdata['gender'],
    ) 
    if users.objects.filter(email=userdata['email']).exists():

        return HttpResponse({'register':False},content_type= 'application/json')
    else:
        user.save()
        return HttpResponse({'register':True},content_type= 'application/json')
#///////////////////////////////////////////////////////////////////////////////

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def user_fetchone(request):
    requests = request.GET
    email = requests['email']

    user = users.objects.filter(email = email).values()
    useri = list(user)
    if useri:
        return JsonResponse(useri,safe=False)
    else:
        return JsonResponse({False:"notfound"})

def user_login(request):
    requests = request.GET
    email = requests['email']
    
    user = users.objects.filter(email = request['email'],
    password = hashlib.md5(requests['password'].encode("utf-8")).hexdigest()).values()
    # start_response(
    #     '200 OK',
    #     [
    #     ('Access-control-Allow-Origin','*')
    #     ]
    # )
    if user:
        return JsonResponse({"ok": True})
    else:
        return JsonResponse({"ok": False})
    

def deletesingleuser(request):
    
    email = request.GET['email']
    if(users.objects.filter(email=email).exists()):
        dels = users.objects.filter(email=email).delete()
        if(dels): 
            return HttpResponse({'dlt':True},content_type= 'application/json')
        else:
            return HttpResponse({'dlt':False},content_type= 'application/json')
    else:
        return HttpResponse({'nodata':True},content_type= 'application/json')

def forgotpass(request):
    email=('musafarshakeel@gmail.com')
    
    

# ////////////////////////////////////////////////////////////////////////////////
def reg_driver(request):
    driverdata = request.GET
    driver = driver_detail(
        d_name = driverdata['d_name'],
        d_email = driverdata['d_email'],
        d_phone = driverdata['d_phone'],
        d_password = hashlib.md5(driverdata['password'].encode("utf-8")).hexdigest(),
        # age = driverdata['age'],
        # gender = driverdata['gender'],
    ) 
    if driver_detail.objects.filter(d_email=driverdata['d_email']).exists():

        return HttpResponse({'drivers':False},content_type= 'application/json')
    else:
        driver.save()
        return HttpResponse({'driver':True},content_type= 'application/json')
#/////////////////
def driver_login(request):
    requests = request.GET
    d_email = requests['d_email']
    d_password = requests['d_password']
    # print(d_email)
    # print(make_password(d_password))
    driverlog = driver_detail.objects.filter(d_email = d_email,
    d_password = hashlib.md5(requests['d_password'].encode("utf-8")).hexdigest()).values()
    print(driverlog)
    if driverlog:
        return JsonResponse({"driverlog": True})
    else:
        return JsonResponse({"driverlog": False})
    
@api_view(['GET', 'POST', 'DELETE'])
def get_all_drivers(request):
    if request.method == 'GET':
        tutorials = driver_detail.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = driver_detailSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'DELETE':
        count = driver_detail.objects.all().delete()
        return JsonResponse({'message': '{}  deleted successfully!'.format(count[0])},
                             status=status.HTTP_204_NO_CONTENT)



@csrf_exempt
def save_photo(request):
    print("hello")
  

# def reg_driver(request):
#     userdata = request.GET
#     user = driver_detail(
#         d_name = userdata['fname'],
#         d_email = userdata['email'],
#         d_phone = userdata['phone'],
#         d_password = (userdata['password']),
#         d_age = userdata['age'],
#         # Firebase_id = userdata['fire_id'],
#         d_gender = userdata['gender'],
#         d_photo = userdata['photo']
#     ) 
def driver(self, request, *args, **kwargs):
    form = EmployeeForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
    context = self.get_context_data(form=form)
    return self.render_to_response(context)     
def get(self, request, *args, **kwargs):
    return self.post(request, *args, **kwargs)