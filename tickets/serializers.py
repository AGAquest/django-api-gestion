from rest_framework import serializers
from .models import TicketSoporte

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketSoporte
        fields = '__all__'