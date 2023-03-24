from django.urls import path
from . import views
## localhost/abts/index
urlpatterns=[
path('index',views.index)

]