from django.urls import include, path
from rest_framework import routers 
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from rest_framework_simplejwt import views as jwt_views



from django.contrib import admin
from service.views import HelloView
from posts import views 

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/asosiy', include('asosiy.urls')),
    path('admin/', admin.site.urls),
    path('',include('service.urls')),
    path('api/portfolio/', include('portfolio.urls')),
    path('api/services/', include('service.urls')),
    path('hello/', HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


]