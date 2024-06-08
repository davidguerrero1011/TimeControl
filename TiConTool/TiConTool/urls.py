"""
URL configuration for TiConTool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings

from adminapp.views import welcome, validateCredentials, index, show, create, edit, storeTimeUser, showTimeRegisters, \
    storeUsers, processFileRegisters, deleteRegisters, logoutSession, showRegister, changePassword, update, \
    updateTimeRegister

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('', welcome, name="login"),
    path('validate/', validateCredentials),
    path('logout/', logoutSession, name="logout"),
    path('index/', index, name='index'),
    path('show/<int:id>', show, name='show'),
    path('create/', create, name='create'),
    path('update/', update, name='update'),
    path('edit/<int:id>', edit, name='edit'),
    path('change/', changePassword, name='change'),
    path('store/', storeTimeUser),
    path('time_registers/<int:id>', showTimeRegisters, name="registers"),
    path('showRegister', showRegister, name='showRegister'),
    path('storeEmployee/', storeUsers),
    path('proccess_file/', processFileRegisters),
    path('updateRegister/<int:id>/', updateTimeRegister, name='updateRegister'),
    path('delete/<int:id>', deleteRegisters, name='delete'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
