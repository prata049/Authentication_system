from django.contrib import admin
from django.urls import path, include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', view.index, name='index'),
    path('accounts/register/', view.registration_view, name='register')
]
