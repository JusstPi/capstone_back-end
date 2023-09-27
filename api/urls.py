from django.urls import path
from .views import *
from api.controllers.calendarControl import CalendarControl

urlpatterns = [
    path('booking/',BookingDetail.as_view(),name='creation'),
    # path('currentBookings/',CurrentBookings.as_view(),name='currentBookings'),
    # path('getBookingByVenue/<id>/',BookingByVenue.as_view(),name='bookingsByVenue'),
    path('createBooking/',CalendarControl.saveBooking,name='create booking'),
    path('currentBookings/',CalendarControl.getCurrentBookings,name='current bookings'),
    path('getAttendees/<id>/',AttendeeDetail.as_view(),name='getBookingAttendees'),
    path ('cancelBooking/<id>/', CancelBooking.as_view, name='cancel booking'),
    path('users/',Users.as_view(),name='getAllUsers'),
    path('login/',login,name='login')
]