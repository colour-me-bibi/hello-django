"""shapes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('rectangle/area/', views.rectangle_area_params),
    path('rectangle/perimeter/', views.rectangle_perimeter_params),
    path('circle/area/', views.circle_area_params),
    path('circle/perimeter/', views.circle_perimeter_params),

    path('rectangle/area/<int:height>/<int:width>', views.rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>', views.rectangle_perimeter),
    path('circle/area/<int:radius>', views.circle_area),
    path('circle/perimeter/<int:radius>', views.circle_perimeter),
]
