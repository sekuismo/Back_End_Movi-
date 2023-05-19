from django.urls import path,include
from miapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',views.UserView,'users')

urlpatterns=[
    
    path('api/v1/',include(router.urls))

]