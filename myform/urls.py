from django.urls import path
from . import views

urlpatterns = [
   path('api/', views.MyFormListCreate.as_view(), name='myform-list-create'),
   path('api2/', views.UserSchemaListCreate.as_view(), name='user-schema-create'),
]