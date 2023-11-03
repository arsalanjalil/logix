
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('service/', include('service.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('industry/', include('industry.urls')),
    path('contact/', include('contact.urls')),
    path('solution/', include('solution.urls')),
    path("accounts/", include("django.contrib.auth.urls")),  # new register
    path("user/sign-up", views.sign_up , name='user_register'), 
]
