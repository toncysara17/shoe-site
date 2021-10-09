from  django.urls import path
from .views import create_brand,index

urlpatterns=[
    path("index",index,name="index"),
    path("create",create_brand,name="create")

]