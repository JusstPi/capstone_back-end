import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import *
from rest_framework.views import APIView
from rest_framework import status
from api.models import Booking,Venue,User as user,Attendee
from api.serializers import BookingSerializer, VenueSerializer,BookingRequestSerializer,UserSerializer,AttendeeSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from api.jwt_util import decode_user
from datetime import datetime, date, timedelta
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class CalendarControl():
    @api_view(['GET'])
    def getAllBooking(request):        
        obj = Booking.objects.all()
        serializer = BookingSerializer(obj,many=True)
        return JsonResponse(serializer.data,status=status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getCurrentBookings(request):
        # auth_header=request.META['HTTP_AUTHORIZATION']
        # # pra mawa ang word na Bearer
        # token=auth_header[7:len(auth_header)+1]
        # print(token)
        # user=decode_user(token)
        # owner=user['user_id']
        week_start = date.today()
        week_start -= timedelta(days=week_start.weekday())
        week_end = week_start + timedelta(days=14)        
        obj = Booking.objects.filter(date__gte=week_start,date__lt=week_end,status="Booked",)
        serializer = BookingSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @api_view(['POST'])
    def saveBooking(request):       
        if request.method=='POST':
            serializer= BookingRequestSerializer(data=request.data)   
                
            if serializer.is_valid():
                date=serializer.validated_data['date']
                # calculate hours_difference
                startTime=serializer.validated_data['startTime']
                endTime=serializer.validated_data['endTime']
                duration=datetime.combine(date,endTime)-datetime.combine(date,startTime)
                hours_difference = (duration).total_seconds()/3600.0
                serializer._validated_data['duration']=hours_difference
                # set status to booked
                serializer._validated_data['status']='Booked'
                serializer.save()
                response_data={
                    'message':'Succesfully booked'
                }
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
# class CurrentBookings(APIView):
#     # permission_classes=[IsAuthenticated,]
#     # api to get bookings within 2 weeks ra   
    
# class BookingByVenue(APIView):
#     def get(self,request,id):
#         print(id)
#         obj=Booking.objects.filter(venue=id)
#         serializer=BookingSerializer(obj,many=True)    
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
# class Users(APIView):
#     def get(self,request):
#         users=user.objects.all()
#         serializer=UserSerializer(users,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
# class AttendeeDetail(APIView):
#     def get(self,request,id):
#         obj = Attendee.objects.filter(booking=id)
#         serializer = AttendeeSerializer(obj,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    