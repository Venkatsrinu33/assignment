from django.urls import path,include
from .views import *
urlpatterns = [
    path('create/', Creategateway.as_view(),name ="Create"),
    path('create/<int:id>', Creategateway.as_view(),name ="Get"),
    path('route/', route.as_view(),name ="route"),
    path('route/<int:id>', route.as_view(),name ="getroute"),
    path('number/<int:number>', Search.as_view(),name ="number"),
]