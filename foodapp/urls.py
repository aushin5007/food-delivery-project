"""foodfortrain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('login',views.loginss),
    path('stall_register',views.hotel_register),
    path('adminhome',views.adminhome),

    
    path('admin_manage_stations',views.admin_manage_station),
    path('delete_station/<id>',views.delete_station),
    path('update_station/<id>',views.update_station),
    path('admin_manage_train',views.admin_manage_train),
    path('delete_train/<id>',views.delete_train),
    path('update_train/<id>',views.update_train),

    path('admin_manage_schedule/<id>',views.admin_manage_schedule),
    path('delete_schedule/<id>',views.delete_schedule),
    path('update_schedule/<id>',views.update_schedule),
    path('admin_view_passengers',views.admin_view_passengers),
    path('admin_manage_category',views.admin_manage_category),
    path('delete_category/<id>',views.delete_category),
    path('update_category/<id>',views.update_category),
    path('admin_view_passengers',views.admin_view_passengers),
    path('admin_view_menu_and_price',views.admin_view_menu),
    path('admin_view_hotels_on_station',views.admin_view_hotels_on_station),
    path('admin_view_reported_hotel',views.admin_view_reported_hotels),
    path('update_hotel_blocked/<id>',views.update_hotel_blocked),
    path('update_hotel_unblocked/<id>',views.update_hotel_unblocked),
    path('admin_view_hotel_rating',views.admin_view_hotel_rating),
    path('admin_view_hotels_on_station_accept/<id>',views.admin_view_hotels_on_station_accept),
    path('admin_view_hotels_on_station_reject/<id>',views.admin_view_hotels_on_station_reject),
    path('adminview_payment',views.adminview_payment),
    path('adminview_booking',views.adminview_booking),
    path('purschase_report',views.purschase_report),

    #====================================================================

    path('hotel_home',views.hotel_home),
    path('hotel_view_food_category',views.hotel_view_food_category),
    path('hotel_manage_menu_and_price',views.hotel_manage_menu_and_price),
    path('delete_hotel_manage_menu_and_price/<id>',views.delete_hotel_manage_menu_and_price),
    path('update_hotel_manage_menu_and_price/<id>',views.update_hotel_manage_menu_and_price),
    path('hotel_mange_delivery_boys',views.dboy_register),
    path('delete_dboy_register/<id>',views.delete_dboy_register),
    path('update_dboy_register/<id>',views.update_dboy_register),
    path('hotel_view_booking_and_accept/<id>',views.hotel_view_booking_and_accept),
    path('hotel_view_booking_and_accepts/<id>',views.hotel_view_booking_and_accepts),
    path('hotel_view_booking_and_reject/<id>',views.hotel_view_booking_and_reject),
    path('passenger_details/<id>',views.hotel_view_passenger),
    path('hotel_view_payment',views.hotel_view_payment),
    path('hotel_assign_delivery_boy/<pid>/<bid>',views.hotel_assign_delivery_boy),
    path(' hotel_view_rating_and_review',views. hotel_view_rating_and_review),
    # path('admin_view_hotel_rating',views.admin_view_hotel_rating),
    path('hotel_report',views.hotel_report),
    path('food_report',views.food_report),



    #================================================================================
    path('passenger_registration',views.passenger_registration),
    path('passenger_home',views.passenger_home),
    path('manage_trip',views.manage_trip),
    path('delete_manage_trip/<id>',views.delete_manage_trip),
    path('update_manage_trip/<id>',views.update_manage_trip),
    path('passenger_view_hotel',views.passenger_view_hotel),
    path('user_send_rating1',views.user_send_rating1),
    path('passenger_view_hotel_on_station',views.passenger_view_hotel_on_station),
    path('view_menu/<id>',views.view_menu),
    path('order/<id>/<price>',views.order),
    path('passenger_view_booking',views.view_booking),
    path('payment/<id>/<amt>',views.payments),
    path('report',views.reported_hotel),
    path('reported_hotel',views.reported_hotels),
    path('passenger_view_deliveryboy/<id>',views.passenger_view_deliveryboy),
    path('usermakepayment_hotel',views.usermakepayment_hotel),
    path('usermakepayment',views.usermakepayment),
    path('usermake_payment/<user_id>',views.usermake_payment),
    path('u_makepayment',views.u_makepayment),
    path('passenger_view_category/<id>',views.passenger_view_category),
    path('get_food_items',views.get_food_items),
  
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  path('dboy_home',views.dboy_home),
  path('dboy_view_orders',views.dboy_view_orders),
  path('dboy_view_pickuporder',views.dboy_view_pickuporder),

]
