from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('keeru.urls')),
    path('api/', include('keeru.urls')),

]
