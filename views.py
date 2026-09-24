from rest_framework import viewsets
from .models import TicketSoporte
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver, crear, editar o eliminar tickets.
    """
    queryset = TicketSoporte.objects.all().order_by('-fecha_creacion')
    serializer_class = TicketSerializer
