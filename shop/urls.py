from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("register/", v.register, name="register"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


