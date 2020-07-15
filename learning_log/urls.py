"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from lists import views as list_views
from lists import urls as list_urls
from accounts import urls as accounts_urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('learninglog/users/', include('users.urls', namespace='users')),
    path('learninglog/', include('learning_logs.urls', namespace='learning_logs')),

    path('superlists/', list_views.home_page, name='home'),
    path('superlists/lists/', include(list_urls), name='lists'),
    path('superlists/accounts/', include(accounts_urls), name='accounts'),
]
