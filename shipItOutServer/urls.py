"""shipItOutServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.views import login_user, register_user

# At any point, your urlpatterns can “include” other URLconf modules.
#  This essentially “roots” a set of URLs below other ones.
# Whenever Django encounters include(), it chops off whatever part
#  of the URL matched up to that point and sends the remaining
#  string to the included URLconf for further processing.

# URL namespaces allow you to uniquely reverse named URL patterns
#  even if different applications use the same URL names.
#  It’s a good practice for third-party apps to always use
#  namespaced URLs.
# namespace can have the same name as the app but doesn't have to be.

# may no longer need trailing_slash
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('ship_admin/', admin.site.urls),
    path('', include('api.urls', namespace='api'))
]
