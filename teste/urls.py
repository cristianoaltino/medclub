
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

app_name='teste'

# URLs para a API e autenticação
urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration', include('rest_auth.registration.urls')),
    path('api/', include('api.urls')),
]

# URL administrativo django
urlpatterns += [
    path('admin/', admin.site.urls),
]
