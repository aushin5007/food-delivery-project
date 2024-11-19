from datetime import date, timedelta, timezone
from datetime import date,datetime
from multiprocessing import connection
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from flask import redirect
from django.core.files.storage import FileSystemStorage
from flask import redirect
from foodapp.models import *

# Create your views here.




def home(request):
    return render(request,'main_home.html')


def  loginss(request):
    if request.method=="POST":
        uname=request.POST['username']
        pwd=request.POST['Password']
        print(uname,pwd)
        
        try:
            lg=login.objects.get(username=uname,password=pwd)
            print(lg,"........................")
   
            request.session['login_id']=lg.pk
            lid=request.session['login_id']
            if lg.usertype=='admin':
                return HttpResponse("<script>alert('login successfully!');window.location='adminhome';</script>")
            elif lg.usertype=='hotel':
                q=hotels.objects.filter(login_id=lid)
                if q:
                    hotel_id=q[0].id
                    request.session['hid']=hotel_id
                return HttpResponse("<script>alert('login successfully.!');window.location='hotel_home';</script>")
            elif lg.usertype=='user':
                qq=passenger.objects.filter(login_id=lid)
                if qq:
                    p_id=qq[0].id
                    request.session['pid']=p_id
                return HttpResponse("<script>alert('login successfully!');window.location='passenger_home';</script>")
            elif lg.usertype=='dboy':
                qqqq=delivery_boys.objects.filter(login_id=lid)
                if qqqq:
                    db_id=qqqq[0].id
                    request.session['db_id']=db_id
                return HttpResponse("<script>alert('login successfully!');window.location='dboy_home';</script>")
        except:
            return HttpResponse("<script>alert('login Failed...!!!!');window.location='login';</script>")
    return render(request,'login.html')


def hotel_register(request):
    q=station.objects.all()
    if request.method=="POST":
        hname=request.POST['hname']
        place=request.POST['stations']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        q=login.objects.filter(username=username)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='/login';</script>")
        else:
            lg=login(username=username,password=password,usertype='pending')
            lg.save()
            pt=hotels(hotel_name=hname,place=place,phone=phone,email=email,login=lg,status='pending')
            pt.save()
         
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/login';</script>")
    return render(request,'hotel_register.html',{'q':q})


def adminhome(request):
    return render(request,'admin_home.html')


def admin_manage_station(request):
    qry1=station.objects.all()
    if request.method=="POST":
        stations=request.POST['stations']
        place=request.POST['place']
        district=request.POST['district']
        q=station.objects.filter(sname=stations)
        if q:
            return HttpResponse("<script>alert('This category is Already added ');window.location='/admin_manage_stations'</script>")
        else:
            qry=station(sname=stations,place=place,district=district)
            qry.save()
            return HttpResponse("<script>alert('added successfully');window.location='/admin_manage_stations' ;</script>")

    return render(request,'admin_manage_stations.html',{'qry1':qry1})

def delete_station(request,id):
    qry=station.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/admin_manage_stations'</script>")

def update_station(request,id):
    qry1=station.objects.all()
    up=station.objects.get(id=id)
    if request.method=="POST":
        stations=request.POST['stations']
        place=request.POST['place']
        district=request.POST['district']
        up.sname=stations
        up.place=place
        up.district=district
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/admin_manage_stations';</script>")
    return render(request,'admin_manage_stations.html',{'up':up,'qry1':qry1})

def admin_manage_train(request):
    qry1=train.objects.all()
    q=station.objects.all()
    if request.method=="POST": 
        train_name=request.POST['train']
        startstation=request.POST['startstation']
        endstation=request.POST['endstation']
        q=train.objects.filter(train_name=train_name)
        if q:
            return HttpResponse("<script>alert('This category is Already added ');window.location='/admin_manage_train'</script>")
        else:
            qry=train(train_name=train_name,starting_station_id=startstation,ending_station_id=endstation)
            qry.save()
            return HttpResponse("<script>alert('added successfully');window.location='/admin_manage_train' ;</script>")
    return render(request,'admin_manage_train.html',{'qry1':qry1,'q':q})

def delete_train(request,id):
    qry=train.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/admin_manage_train'</script>")

def update_train(request,id):
    qry1=train.objects.all()
    q=station.objects.all()
    up=train.objects.get(id=id)
    if request.method=="POST":
        train_name=request.POST['train']
        startstation=request.POST['startstation']
        endstation=request.POST['endstation']
        up.train_name=train_name
        up.starting_station_id=startstation
        up.ending_station_id=endstation
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/admin_manage_train';</script>")
    return render(request,'admin_manage_train.html',{'up':up,'qry1':qry1,'q':q})


def admin_manage_schedule(request,id):
    qry1=schedule.objects.all()
    q=station.objects.all()
    if request.method=="POST": 
        at=request.POST['at']
        dt=request.POST['dt']
        stopstation=request.POST['stopstation']

        qry=schedule(arrivaltime=at,departuretime=dt,stopstation_id_id=stopstation,train_id_id=id)
        qry.save()
        return HttpResponse("<script>alert('added successfully');window.location='/admin_manage_train' ;</script>")
    return render(request,'admin_manage_schedule.html',{'qry1':qry1,'q':q})

def delete_schedule(request,id):
    qry=schedule.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/admin_manage_train'</script>")

def update_schedule(request,id):
    qry1=train.objects.all()
    q=station.objects.all()
    up=schedule.objects.get(id=id)
    if request.method=="POST":
        at=request.POST['at']
        dt=request.POST['dt']
        stopstation=request.POST['stopstation']
        up.arrivaltime=at
        up.departuretime=dt
        up.stopstation_id=stopstation
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/admin_manage_train';</script>")
    return render(request,'admin_manage_train.html',{'up':up,'qry1':qry1,'q':q})


def admin_view_passengers(request):
    p=passenger.objects.all()
    return render(request, 'admin_view_passengers.html',{'p':p} )


def admin_manage_category(request):
    qry1=food_category.objects.all()
    if request.method=="POST": 
        cat=request.POST['category']
        qry=food_category(category=cat)
        qry.save()
        return HttpResponse("<script>alert('added successfully');window.location='/admin_manage_category' ;</script>")
    return render(request,'admin_mange_food_category.html',{'qry1':qry1})

def delete_category(request,id):
    qry=food_category.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/admin_manage_category'</script>")

def update_category(request,id):
    qry1=food_category.objects.all()
    up=food_category.objects.get(id=id)
    if request.method=="POST":
        cat=request.POST['category']
        up.category=cat
        return HttpResponse("<script>alert('updated successfully');window.location='/admin_manage_category';</script>")
    return render(request,'admin_mange_food_category.html',{'up':up,'qry1':qry1})

def admin_view_menu(request):
    qry1=menu.objects.all()
    return render(request,'admin_view_menu_and_price.html',{'qry1':qry1})

def admin_view_hotels_on_station(request):
    hotel = hotels.objects.all()   
    return render(request, 'admin_view_hotels_on_station.html', {'h':hotel})


def admin_view_hotels_on_station_accept(request, id):
    q = get_object_or_404(login, id=id)
    q.usertype = 'hotel'
    q.save()
    up = get_object_or_404(hotels, login=q)
    up.status = 'accept'
    up.save()
    return HttpResponse("<script>alert('Unblocked');window.location='/admin_view_hotels_on_station';</script>")


def admin_view_hotels_on_station_reject(request, id):
    q = get_object_or_404(login, id=id)
    q.delete()
    up = get_object_or_404(hotels, login=q)
    up.delete()
    return HttpResponse("<script>alert('blocked');window.location='/admin_view_hotels_on_station';</script>")



def admin_view_reported_hotels(request):
    qry1=reported_hotel.objects.all()
    return render(request,'admin_view_reported_hotel.html',{'qry1':qry1})

def update_hotel_blocked(request,id):
    up=hotels.objects.get(id=id)
    up.status='block'
    up.save()
    return HttpResponse("<script>alert('Blocked');window.location='/admin_view_reported_hotel';</script>")

def update_hotel_unblocked(request, id):
    hotel = get_object_or_404(hotels, id=id)
    hotel.status = 'active'
    hotel.save()
    return HttpResponse("<script>alert('Unblock');window.location='/admin_view_reported_hotel';</script>")

def admin_view_hotel_rating(request):
    qry1=rating.objects.all()
    return render(request,'admin_view_hotel_rating.html',{'qry1':qry1})

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def hotel_home(request):
    q=hotels.objects.all()
    return render(request,'hotel_home.html',{'q':q})


def hotel_view_food_category(request):
    q=food_category.objects.all()
    return render(request,'hotel_view_food_category.html',{'q':q})

def hotel_manage_menu_and_price(request):
    hid=request.session['hid']
    qry1=menu.objects.filter(hotel=hid)
    q=food_category.objects.all()
    if request.method=="POST": 
        category=request.POST['category']
        food_name=request.POST['food_name']
        image=request.FILES['image']
        price=request.POST['price']
        quantity=request.POST['quantity']
        fs=FileSystemStorage()
        fns=fs.save(image.name,image)
        qry=menu(category_id=category,food_name=food_name,price=price,quantity=quantity,image=fns,status='pending',hotel_id=hid)
        qry.save()
        return HttpResponse("<script>alert('added successfully');window.location='/hotel_manage_menu_and_price' ;</script>")
    return render(request,'hotel_manage_menu_and_price.html',{'qry1':qry1,'q':q})

def delete_hotel_manage_menu_and_price(request,id):
    qry=menu.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/hotel_manage_menu_and_price'</script>")

def update_hotel_manage_menu_and_price(request,id):
    hid=request.session['hid']
    qry1=menu.objects.filter(hotel=hid)
    up=menu.objects.get(id=id)
    if request.method=="POST":
        category=request.POST['category']
        food_name=request.POST['food_name']
        image=request.FILES['image']
        price=request.POST['price']
        quantity=request.POST['quantity']
        fs=FileSystemStorage()
        fn=fs.save(image.name,image)
        up.food_name=food_name
        up.image=fn
        up.price=price
        up.quantity=quantity
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/hotel_manage_menu_and_price';</script>")
    return render(request,'hotel_manage_menu_and_price.html',{'up':up,'qry1':qry1})


def dboy_register(request):
    hid=request.session['hid']
    qry1=delivery_boys.objects.filter(hotel=hid)
    if request.method=="POST": 
        fname=request.POST['fname']
        lname=request.POST['lname']
        hname=request.POST['hname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        q=login.objects.filter(username=username)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='/login';</script>")
        else:
            lg=login(username=username,password=password,usertype='dboy')
            lg.save()
            qry=delivery_boys(fname=fname,lname=lname,hname=hname,place=place,phone=phone,email=email,hotel_id=hid,login =lg)
            qry.save()
            return HttpResponse("<script>alert('added successfully');window.location='/hotel_mange_delivery_boys' ;</script>")
    return render(request,'hotel_mange_delivery_boys.html',{'qry1':qry1})

def delete_dboy_register(request,id):
    qry=delivery_boys.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/hotel_mange_delivery_boys'</script>")

def update_dboy_register(request,id):
    up=delivery_boys.objects.get(id=id)
    qry1=delivery_boys.objects.all()
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        hname=request.POST['hname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email'] 
        up.fname=fname
        up.lname=lname
        up.hname=hname
        up.place=place
        up.phone=phone
        up.email=email
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/hotel_mange_delivery_boys';</script>")
    return render(request,'hotel_mange_delivery_boys.html',{'up':up,'qry1':qry1})

def hotel_view_booking_and_accept(request,id):
    q=booking.objects.filter(menu=id)
    return render(request,'hotel_view_booking_and_accept.html',{'q':q})

def hotel_view_booking_and_accepts(request, id):
    booking_instance = get_object_or_404(booking, id=id)
    booking_instance.status = 'accept'
    booking_instance.save()
    return HttpResponse("<script>alert('Booking Accepted');window.location='/hotel_manage_menu_and_price';</script>")

def hotel_view_booking_and_reject(request, id):
    booking_instance = get_object_or_404(booking, id=id)
    booking_instance.status = 'reject'
    booking_instance.save()
    return HttpResponse("<script>alert('Booking Rejected');window.location='/hotel_manage_menu_and_price';</script>")

def hotel_view_passenger(request,id):
    q=passenger.objects.filter(id=id)
    return render(request,'hotel_view_passenger_details.html',{'q':q})

# def  hotel_view_rating_and_review(request):
#         h=request.session['hid']
#         q=rating.objects.get(id=h)
#         return render(request,'hotel_view_rating_and_review.html',{'q':q})

def hotel_view_rating_and_review(request):
    hid=request.session['hid']
    qry1=rating.objects.filter(id=hid)
    return render(request,'admin_view_hotel_rating.html',{'qry1':qry1})

def hotel_view_payment(request):
    hid = request.session['hid']
    payments = payment.objects.filter(booking__menu__hotel_id=hid).select_related('booking__passenger', 'booking__menu')
    return render(request, 'hotel_view_payment.html', {'p':payments})


def hotel_assign_delivery_boy(request,pid,bid):
    ad = assign.objects.filter(booking=bid)
    db = delivery_boys.objects.all()
    # asign_details = assign.objects.select_related('booking', 'delivery_boy').filter(booking_id=bid)
    if request.method == 'POST':
        name = request.POST['name']
        assigns = assign(booking_id=bid, delivery_boy_id=name, date_time=timezone.now(), assign_status='accept')
        assigns.save()
        messages.success(request, 'Assignment successful')
        return redirect('hotel_assign_delivery_boy', pid=pid, bid=bid)

    return render(request, 'hotel_assign_delivery_boy.html', {'db':db,'ad':ad})

def hotel_view_payment(request):
    hid = request.session.get('hid')
    payments = payment.objects.filter(booking__menu__hotel_id=hid).select_related('booking__passenger', 'booking__menu')
    data = {'payment': payments}
    return render(request, 'hotel_view_payment.html', data)


#==========================================================================================================================



def passenger_registration(request):
    if request.method == 'POST':
        # Get form data
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        hname = request.POST.get('hname')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        pin = request.POST.get('pin')
        gen = request.POST.get('gen')
        age = request.POST.get('age')
        username = request.POST.get('username')
        password = request.POST.get('password')
        q=login.objects.filter(username=username)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='/login';</script>")
        else:
            lg=login(username=username,password=password,usertype='user')
            lg.save()
            hotel = passenger(fname=fname,lname=lname,hname=hname,place=place,phone=phone,email=email,pincode=pin,gender=gen,age=age,login=lg)
            hotel.save()
            user_id=hotel.id          
            return HttpResponseRedirect("/usermake_payment/%s"%user_id)
    return render(request, 'passenger_reg.html')


def usermake_payment(request,user_id):
    total=199
    cdate=date.today()
    to_date = cdate + timedelta(days=90)
    if request.method == "POST":
        q = payment_sub(Amount=total, payment_date=cdate, user_id=user_id, payment_for='subscription')
        q.save()
        f=subscription(amount=total,from_date=cdate,to_date=to_date,user_id=user_id,sub_status='subscribed')
        f.save()
        return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/login';</script>")
    return render(request, 'usermakepayment.html', {'total': total})

def passenger_home(request):
    cdate = date.today()
    data = []
    bata = []
    try:
        s = subscription.objects.get(user_id=request.session.get('pid'))
        to_date_str = s.to_date 
        to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date() 
        if cdate <= to_date:
            data = [s]  # Add subscription to data list if it's still active
        else:
            bata = [s]  # Add subscription to bata list if it's expired
    except subscription.DoesNotExist:
        print("***** Subscription not found for this user")
    
    return render(request, 'passenger_home.html', {'data': data, 'bata': bata})

def u_makepayment(request):
    total=199
    cdate=date.today()
    to_date = cdate + timedelta(days=90)
    if request.method == "POST":
        q = payment_sub(Amount=total, payment_date=cdate, user_id=request.session['pid'], payment_for='subscription')
        q.save()
        f=subscription.objects.get(user_id=request.session['pid'])
        f.to_date=to_date
        f.from_date=cdate
        f.save() 
        return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/passenger_home';</script>")
    return render(request, 'usermakepayment.html', {'total': total})


def manage_trip(request):
    pid=request.session['pid']
    q=train.objects.all()
    qry=trips.objects.filter(passenger=pid)
    cdate=date.today()
    if request.method == 'POST':  
        trains = request.POST.get('train')
        trip = trips(tdate=cdate,passenger_id=pid,train_id=trains)
        trip.save()
        return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/manage_trip';</script>")
    return render(request,'manage_trip.html',{'qry':qry,'q':q})


def delete_manage_trip(request,id):
    qry=trips.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/manage_trip'</script>")


def update_manage_trip(request,id):
    up=trips.objects.get(id=id)
    pid=request.session['pid']
    q=train.objects.all()
    qry=trips.objects.filter(passenger=pid)
    if request.method=="POST":
        trains = request.POST.get('train')
        up.train_id=trains
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/manage_trip';</script>")
    return render(request,'manage_trip.html',{'up':up,'qry':qry,'q':q})

def passenger_view_hotel(request):
    hotel = hotels.objects.all()
    return render(request,'passenger_view_hotel.html',{'h':hotel})

def user_send_rating1(request):
    hotel = hotels.objects.all()
    cdate = date.today()
    cus_id = request.session.get('pid')  
    if request.method == 'POST':
        if 'button' in request.POST:
            try:
                turf_id = request.POST['turf'] 
                rate = request.POST['rate']
                review = request.POST['review']
                r = rating(passenger_id=cus_id, hotel_id=turf_id, rate=rate,date_time=cdate,review=review)
                r.save()
                return HttpResponse("<script>alert('Rated successfully');window.location='/user_send_rating1'</script>")
            except KeyError:
                return HttpResponse("<script>alert('Error: Please fill out all fields.');window.location='/user_send_rating1'</script>")
    return render(request, 'userrate.html', {'q': hotel})


def passenger_view_hotel_on_station(request):
    hotel = hotels.objects.all()
    return render(request,'passenger_view_hotel_on_station.html',{'h':hotel})


def view_menu(request,id):
    qry = menu.objects.filter(hotel=id)
    return render(request,'passenger_view_menu.html',{'qry':qry})

def order(request, id, price):
    # q = trips.objects.all()
    cdate = date.today()
    pid = request.session['pid']
    if request.method == "POST":
        # trip = request.POST['trip']
        qty = request.POST['qty']
        total=request.POST['total']
        price=float(price)
        q = booking(qty=qty, date_time=cdate, status="pending", menu_id=id, passenger_id=pid, trip_id='01',price=total)
        q.save()
        return HttpResponse("<script>alert('Booked Successfully');window.location='/passenger_view_hotel_on_station'</script>")
    return render(request, 'passenger_order.html', { 'price': price})

# def order(request, id, price):
#     q = trips.objects.all()
#     cdate = date.today()
#     pid = request.session.get('pid') 
#     if request.method == "POST":
#         trip = request.POST.get('trip') 
#         qty = request.POST.get('qty')
#         total = request.POST.get('total')
#         if trip != 'Select' and qty and total:
#             menu_id = int(id)
#             passenger_id = int(pid)
#             price = float(price)  
#             booking_obj = booking.objects.create(qty=qty, date_time=cdate, status="pending",
#                                                   menu_id=menu_id, passenger_id=passenger_id,
#                                                   trip_id=int(trip), price=total)
#             booking_obj.save()
#             return HttpResponse("<script>alert('Booked Successfully');window.location='/passenger_view_hotel_on_station'</script>")
#         else:
#             return HttpResponse("<script>alert('Invalid input');window.location='/passenger_order.html'</script>") 
#     return render(request, 'passenger_order.html', {'q': q, 'price': price})


def view_booking(request):
    pid=request.session['pid']
    q=booking.objects.filter(passenger=pid)
    return render(request,'passenger_view_booking.html',{'q':q})

# def payment(request, id):
#     if request.method == 'POST':
#         cdate = date.today()
#         q = payment(date_time=today,booking_id=id)
#         q.save()
#         return HttpResponse("<script>alert('Payment Completed Successfully');window.location='/view_booking'</script>")
#     return render(request, 'user_product_payment.html')

def payments(request,id,amt):
    today=date.today()
    print(today)
    if request.method=="POST":
        q=payment(tdate=today,booking_id=id)
        q.save()
        q1=booking.objects.get(id=id)
        q1.status='paid'
        q1.save()    
        return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/passenger_home';</script>")
    return render(request,'user_product_payment.html')


def reported_hotels(request):
    q = hotels.objects.all()
    cdate = date.today()
    pid = request.session['pid']
    if request.method == 'POST':
        reasonss = request.POST['reasonss']
        hotel_id = request.POST['hotel']
        reported_hotel_instance = reported_hotel(reason_details=reasonss, date_time=cdate, hotel_id=hotel_id, passenger_id=pid,status='Block')
        reported_hotel_instance.save()
        return HttpResponse("<script>alert('Successfully');window.location='/reported_hotel'</script>")
    
    return render(request, 'reported.html', {'q': q})


def passenger_view_deliveryboy(request,id):
    hotel = delivery_boys.objects.get(hotel=id)
    return render(request,'def passenger_view_deliveryboy.html',{'h':hotel})
  
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def dboy_home(request):
    q=hotels.objects.all()
    return render(request,'dboyhome.html',{'q':q})


# def view_order(request):
#     bookings = booking.objects.filter(status='Paid')
#     return render(request, 'dboy_view_orders.html', {'q': bookings})

def dboy_view_orders(request):
    bookings = booking.objects.filter(status='Paid').select_related('menu', 'passenger')
    res = bookings

    if 'action' in request.GET:
        action = request.GET['action']
        bid = request.GET['bid']

        if action == 'deliver':
            bookings = booking.objects.get(pk=bid)
            bookings.status = 'Delivery Completed'
            bookings.save()
            return HttpResponse("<script>alert('Delivery Completed');window.location='/dboy_view_orders'</script>")

        elif action == 'pickedup':
            bookings = booking.objects.get(pk=bid)
            bookings.status = 'Picked Up'
            bookings.save()
            return HttpResponse("<script>alert('Pickup Completed ');window.location='/dboy_view_orders'</script>")

    return render(request, 'dboy_view_orders.html', {'res':res})


def dboy_view_pickuporder(request):
   
    res = booking.objects.filter(status='Picked Up')

    if 'action' in request.GET:
        action = request.GET['action']
        bid = request.GET['bid']
    else:
        action = None

    if action == "deliver":
        bookings = booking.objects.get(id=bid)
        bookings.status = 'Delivery Completed'
        bookings.save()
        return HttpResponse("<script>alert('Delivery Completed');window.location='/dboy_view_pickuporder'</script>")

    return render(request, "dboy_view_pickuporder.html", {'res':res})



# def dboy_view_train(request):
#     data = {}
#     res = train.objects.all()
#     return render(request, "trainview.html", res)


def usermakepayment_hotel(request,physician_id):
    total=int(199)
    if request.method=="POST":
        today = date.today()
        user_id = request.session['user_ids'] 
        p=payment(Amount=total, payment_date=today, payment_for='subscribePhysician', user_id=user_id)
        p.save()
        q=subscription(physician_id=physician_id,user_id=user_id)
        q.save()
        return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/userhome';</script>")
    return render(request,'usermakepayment_physician.html',{'total':total})


def adminview_payment(request):
    qry1=payment.objects.all()
    return render(request,'adminview_payment.html',{'qry1':qry1})

def adminview_booking(request):
    qry1=booking.objects.all()
    return render(request,'adminview_booking.html',{'qry1':qry1})

def purschase_report(request):
    p = booking.objects.filter(status='paid')
    return render(request,'admin_purchase_report.html',{'p':p})


def hotel_report(request):
    v=booking.objects.filter(menu__hotel_id= request.session['hid'])
    print("==========",v)
    if request.method == 'POST':
        from_date = request.POST.get('fd')
        to_date = request.POST.get('td')

        print("From Date:", from_date)
        print("To Date:", to_date)

        if from_date and to_date:  # Check if both dates are provided
            # Filter queryset to get payments between from_date and to_date
            v = booking.objects.filter(date_time__range=[from_date, to_date])
    return render(request,'hotel_report.html',{'v':v})
  
# def food_report(request):
#     if request.method == "POST":     
#         category_id = request.POST.get("category_id")
#         try:
#             if category_id:
#                 v = booking.objects.filter(menu__category_id=category_id)
#             else:
#                 v = booking.objects.all()
#         except booking.DoesNotExist:
#             v = []
#         except Exception as e:
#             v = []
#     else:
#         v = booking.objects.all()
#     q = food_category.objects.all()
#     return render(request, 'food_report.html', {'v': v, 'q': q})

from django.db.models import Sum
def food_report(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        try:
            if category_id:
                v = booking.objects.filter(menu__category_id=category_id)
                total_price = v.aggregate(total_price=Sum('price'))['total_price'] or 0
            else:
                v = booking.objects.all()
                total_price = v.aggregate(total_price=Sum('price'))['total_price'] or 0
        except booking.DoesNotExist:
            v = []
            total_price = 0
        except Exception as e:
            v = []
            total_price = 0
    else:
        v = booking.objects.all()
        total_price = v.aggregate(total_price=Sum('price'))['total_price'] or 0
    
    q = food_category.objects.all()
    return render(request, 'food_report.html', {'v': v, 'q': q, 'total_price': total_price})

from django.core.exceptions import ObjectDoesNotExist
def usermakepayment(request):
    today = date.today()
    user_id = request.session.get('pid') 
    total = int(199)
    if request.method == "POST":
        if user_id:
            try:
                payment_record = payment_sub.objects.filter(user_id=user_id).latest('payment_date')
                payment_date = payment_record.payment_date
                if today <= payment_date:
                    return HttpResponse("<script>alert('You have already made a payment for this month.');window.location='/passenger_home' ;</script>")
                else:
                    new_payment = payment_sub(Amount=total, payment_date=today, payment_for='subscription', user_id=user_id)
                    new_payment.save()
                    return HttpResponse("<script>alert('Payment Successfull');window.location='/passenger_home' ;</script>")
            
            except ObjectDoesNotExist:
                total_amount = 199
                new_payment = payment_sub(Amount=total_amount, payment_date=today, payment_for='subscription', user_id=user_id)
                new_payment.save()
                return HttpResponse("<script>alert('Payment Successfull.');window.location='/passenger_home' ;</script>")
                
            except payment_sub.DoesNotExist:
                total_amount = 199
                new_payment = payment_sub(Amount=total_amount, payment_date=today, payment_for='subscription', user_id=user_id)
                new_payment.save()
                return HttpResponse("<script>alert('Payment Successfull.');window.location='/passenger_home' ;</script>")
    
    return render(request, 'usermakepayment.html', {'total': total})



def passenger_view_category(request,id):
    # q= menu.objects.select_related('hotel', 'category').all()
    q = menu.objects.select_related('category').filter(hotel_id=id)
    return render(request,'passenger_view_category.html',{'q':q})


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import menu, food_category

def get_food_items(request, category_name):
    # Get the food category object based on the category name
    food_cat = get_object_or_404(food_category, category_name=category_name)

    # Filter food items based on the selected category
    food_items = menu.objects.filter(category=food_cat)

    # Serialize the queryset to JSON
    data = [{'food_name': item.food_name, 'price': item.price} for item in food_items]

    return JsonResponse(data, safe=False)











