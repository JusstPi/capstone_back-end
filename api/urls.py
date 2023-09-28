from django.urls import path
from .views import *
from api.controllers.calendarController import CalendarController
from api.controllers.bookingController import BookingController
from api.controllers.detailsConrtoller import DetailsController
urlpatterns = [
    # path('booking/',BookingDetail.as_view(),name='creation'),
    # path('currentBookings/',CurrentBookings.as_view(),name='currentBookings'),
    # path('getBookingByVenue/<id>/',BookingByVenue.as_view(),name='bookingsByVenue'),
    # path('booking/',BookingDetail.as_view(),name='creation'),
    path('createBooking/',CalendarController.saveBooking,name='create booking'),
    path('currentBookings/',CalendarController.getCurrentBookings,name='current bookings'),
    path('getAttendees/<id>/',AttendeeDetail.as_view(),name='getBookingAttendees'),
    path('users/',Users.as_view(),name='getAllUsers'),
    path('cancelBooking/<id>',DetailsController.cancelBooking,name="cancelbooking"),
    path('calculateCost/',BookingController.calculateCost,name="calculate payment or cost"),
    path('getUsers/',BookingController.getAllUsers,name="get all users"),
    path('login/',login,name='login')
]