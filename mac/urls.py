from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')), 
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
