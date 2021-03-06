"""Party_maker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from all_authentication import views

urlpatterns = [
    path("", views.home, name="home"),
    path('partners/', include('partners.urls')),
    path('event/', include('event.urls')),

    path('admin/', admin.site.urls),
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name="signup"),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/', include('django.contrib.auth.urls'))
    # path('social-auth/', include('social_django.urls', namespace="social")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
