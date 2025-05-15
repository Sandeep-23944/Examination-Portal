# exam_portal/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include URLs from your core app
    path('', include('core.urls')),

    # Django's built-in login view (points to your login template)
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'  # <-- template path
    ), name='login'),
]
