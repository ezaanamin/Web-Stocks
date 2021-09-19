from django.contrib import admin
from django.urls import path,include
app='stocksmarkets'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('stocksmarket.urls')),
]

