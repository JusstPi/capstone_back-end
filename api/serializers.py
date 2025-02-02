import datetime
from rest_framework import serializers
from api.models import Booking,Venue,Attendee,User

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=('__all__')

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Venue
        fields=('__all__')
class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendee
        fields=('__all__')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','id')
class BookingRequestSerializer(serializers.ModelSerializer):
    attendees=AttendeeSerializer(many=True)
    class Meta:
        model=Booking
        fields=('purpose','description','venue','date','startTime','endTime','computers','coins','points','user','attendees','officeName','user_id')
    def create(self, validated_data):
        attendees=validated_data.pop('attendees')
        booking=Booking(**validated_data)        
        booking.save()
        serializer= AttendeeSerializer(data=attendees,many=True)
        if serializer.is_valid(raise_exception=True):
            attendees=serializer.save(booking=booking)
        return booking
    