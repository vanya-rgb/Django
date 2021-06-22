from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import events.views
#управление любыми медиа файлами

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', events.views.home, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
