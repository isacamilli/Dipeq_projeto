
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projeto/', include('projeto_dipeq.urls'))
]
