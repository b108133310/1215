from django.contrib import admin
from django.urls import path
from mysite.views import homepage, lotto, showpost,mychart, chart


urlpatterns = [
    path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('chartbydate/<int:year>/<int:month>', chart),
    path('', homepage),
]