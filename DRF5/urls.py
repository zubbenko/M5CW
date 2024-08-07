from main import views
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test', views.test_api_view),
    path('api/v1/ads', views.ads_list_api_view),
    path('api/v1/ads/<int:id>', views.ads_detial_api_view),
]