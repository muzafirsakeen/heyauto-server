from django.urls import path, include,re_path

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'phone','password','age','gender']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   #working.....................
    re_path('get_all_users$', views.get_all_users),
    path('reg_user/',views.reg_user,name='reg_user'),
    path('user_login/',views.user_login),
    path('user_fetchone/',views.user_fetchone),
    path('user_deleteone/',views.deletesingleuser),
    


    path('driver_reg/',views.reg_driver),
    path('driver_login/',views.driver_login),
    path('get_all_drivers/',views.get_all_drivers),



#    .............................................
    
      

]