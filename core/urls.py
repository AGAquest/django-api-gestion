from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # 1. Importamos la vista de redirección
from rest_framework.routers import DefaultRouter
from tickets.views import TicketViewSet

router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/api/tickets/')),  # 2. Redirigimos la raíz vacía hacia tu API
]
