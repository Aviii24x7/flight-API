#username:avinash
#password:chauhan
#userno3= Avinash@123

from django.shortcuts import render
from flightApp.models import Passenger,Flight,Reservation
from flightApp.serializers import PassengerSerializer, FlightSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# @api_view(['GET','POST'])
# def reservation_operations(request):
    
#     if request.method == "POST":
@api_view(['POST'])     
def find_flights(request):
    flights=Flight.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'] )
    serializer=FlightSerializer(flights,many=True)
    return Response(serializer.data)


class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    filter_backends=[filters.SearchFilter]
    search_fields= ['departureCity','arrivalCity','dateOfDeparture']
    permission_classes=(IsAuthenticated,)
    
class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer
    permission_classes=(IsAuthenticated,)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    permission_classes=(IsAuthenticated,)