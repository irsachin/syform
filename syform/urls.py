from django.contrib import admin
from django.urls import path, include
from myform.views import index  # Import the index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Use the index view as the root URL
    path('app/', include('myform.urls')),
]

