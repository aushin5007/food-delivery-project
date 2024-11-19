from django.db import models
# Create your models here.


class login(models.Model):
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)

class station(models.Model):
    sname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    district=models.CharField(max_length=225)

class train(models.Model):
    train_name = models.CharField(max_length=225)
    starting_station = models.ForeignKey(station, related_name='starting_trains', on_delete=models.CASCADE)
    ending_station = models.ForeignKey(station, related_name='ending_trains', on_delete=models.CASCADE)
 
class schedule(models.Model):
    train_id=models.ForeignKey(train,on_delete=models.CASCADE)
    stopstation_id=models.ForeignKey(station,on_delete=models.CASCADE)
    arrivaltime=models.CharField(max_length=225)
    departuretime=models.CharField(max_length=225)

class passenger(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    hname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    pincode=models.CharField(max_length=225)
    gender=models.CharField(max_length=225)
    age=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)

class hotels(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    #station=models.ForeignKey(station,on_delete=models.CASCADE)
    hotel_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    # place=models.CharField(max_length=225)

class food_category(models.Model):
    category=models.CharField(max_length=225)

class menu(models.Model):
    hotel=models.ForeignKey(hotels,on_delete=models.CASCADE)
    category=models.ForeignKey(food_category,on_delete=models.CASCADE)
    food_name=models.CharField(max_length=225)
    image=models.CharField(max_length=225)
    price=models.CharField(max_length=225)
    quantity=models.CharField(max_length=225)
    status=models.CharField(max_length=225)

class reported_hotel(models.Model):
    hotel=models.ForeignKey(hotels,on_delete=models.CASCADE)
    passenger=models.ForeignKey(passenger,on_delete=models.CASCADE)
    reason_details=models.CharField(max_length=225)
    date_time=models.CharField(max_length=225)
    status=models.CharField(max_length=225)

class rating(models.Model):
    hotel=models.ForeignKey(hotels,on_delete=models.CASCADE)
    passenger=models.ForeignKey(passenger,on_delete=models.CASCADE)
    rate=models.CharField(max_length=225)
    review=models.CharField(max_length=225)
    date_time=models.CharField(max_length=225)

class delivery_boys(models.Model):
    hotel=models.ForeignKey(hotels,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    hname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
  
class trips(models.Model):
    passenger=models.ForeignKey(passenger,on_delete=models.CASCADE)
    train=models.ForeignKey(train,on_delete=models.CASCADE)
    tdate=models.CharField(max_length=225)


class booking(models.Model):
    passenger=models.ForeignKey(passenger,on_delete=models.CASCADE)
    trip=models.ForeignKey(trips,on_delete=models.CASCADE)
    menu=models.ForeignKey(menu,on_delete=models.CASCADE)
    qty=models.CharField(max_length=225)
    date_time=models.CharField(max_length=225)
    price=models.CharField(max_length=225)
    status=models.CharField(max_length=225)

class assign(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    delivery_boys=models.ForeignKey(delivery_boys,on_delete=models.CASCADE)
    date_time=models.CharField(max_length=225)
    status=models.CharField(max_length=225)


class payment(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    tdate=models.CharField(max_length=225)

# class Payments(models.Model):
#     bookings = models.ForeignKey(booking, on_delete=models.CASCADE)
#     tdate = models.CharField(max_length=225)

class payment_sub(models.Model):
    user=models.ForeignKey(passenger,on_delete=models.CASCADE)
    Amount=models.CharField(max_length=225)
    payment_date=models.DateField(max_length=225)	 
    payment_for=models.CharField(max_length=225)
 
class subscription(models.Model):
    subscription_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(passenger,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225)
    from_date=models.CharField(max_length=225)
    to_date=models.CharField(max_length=225)
    sub_status=models.CharField(max_length=225)














