from django.urls import path, include
from miapp import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'users')
router.register('peliculas', views.PeliculasViewSet, basename='peliculas')
router.register('listas', views.ListaDePeliculasViewSet, basename='listas')

urlpatterns = [
    path('api/v1/users/create/', views.CreateUserView.as_view({'post': 'create'}), name='create-user'),
    path('api/v1/', include(router.urls)),
    path('api/v1/login/', views.LoginView.as_view({'post': 'login'}), name='login'),
    path('api/v1/logout/', views.LogoutView.as_view(), name='logout'),
    path('api/v1/protected_view/', views.UserView.as_view({'get': 'protected_view'}), name='protected_view'),
    path('docs/', include_docs_urls(title="movieApp api")),
]
