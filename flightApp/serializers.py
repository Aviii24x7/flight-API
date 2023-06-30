from rest_framework import serializers
from .models import Reservation,Passenger,Flight
import re

#method 3 validators (in Meta)
#def isFlightNumberValid(flightNumber):     #can be this for particular field
def isFlightNumberValid(data):              #data is a dictionary with keys as fieldname
    #give some conditions
    print("IsFlightNumber")

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields="__all__"
        validators=[isFlightNumberValid]
        
    #method 1: custom validators9name should ne VALIDATE _ FIELD NAME
    def validate_flightNumber(self,flightNumber):
        print("validate_flightNumber")
        if(re.match("^[a-zA-Z1-9]*$",flightNumber)==None):
            raise serializers.ValidationError("Invalid flight Number. Make sure it is alph-numeric")
        return flightNumber
    
    #method 2: custom validators
    def validate(self,data):
        print("validate")
        print(data)
        #put customisation on data['fieldname'] e.g if data['flightNumber']==something
        return data
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields="__all__"
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields="__all__"
        