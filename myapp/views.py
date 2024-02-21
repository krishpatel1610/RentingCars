from django.contrib import messages
from django.shortcuts import render, redirect
from .models import usertable, contactus, vehicle_table,booking_table, feedback
# Create your views here.
def index(request):
    getcar = vehicle_table.objects.all()
    context = {
        "data": getcar
    }
    print(context)
    return render(request, 'index.html', context)
def contact(request):
    return render(request,'contact.html')

def checkout(request,id):
    get = vehicle_table.objects.get(id=id)
    context = {
        'data': get
    }
    return render(request,'checkout.html',context)

def checkoutform(request):
    return render(request,'checkoutform.html')

def book(request):
    return render(request,'book.html')

def service(request):
    return render(request,'services.html')

def vehicles(request):
    getcar = vehicle_table.objects.all()
    context = {
        "data": getcar
    }
    print(context)
    return render(request,'vehicles.html', context)

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone =request.POST.get("phone")
        pw = request.POST.get("pass")
        repass = request.POST.get("repass")
        licence_no = request.POST.get("licence_no")
        address = request.POST.get("address")

        if pw==repass:
            user = usertable(name=name, emailid=email, phoneno=phone, password=pw, licence_no=licence_no, address=address, role=1, status=1)
            user.save()
            return render(request,'index.html')
        else:
            messages.error(request,"both password are not same")
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        pw = request.POST.get("pass")

        try:
            user = usertable.objects.get(emailid=email, password=pw)
            request.session['log_user'] = user.emailid
            request.session['log_id'] = user.id
            request.session.save()
        except:
            user=None

    if user is not None:
        return redirect(index)
    else:
        messages.info(request,"NOT EXIST")
    return render(request,'vehicles.html')

def lgout(request):
    try:
        del request.session['log_id']
        del request.session['log_user']
    except:
        print("sorry")
    return redirect(index)

def contactfill(request):
    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        msg = request.POST.get("msg")
        name= request.POST.get("name")
        user = contactus(name=name, message=msg, phone=phone, email=email)
        user.save()
        messages.success(request, "insertion done")
    return render(request,'index.html')

def displayvehical(request):
    getcar = vehicle_table.objects.all()
    context ={
        "data":getcar
    }
    print(context)
    return render(request,'index.html',context)

def bookcar(request):
    if request.method == "POST":
        from_duration = request.POST.get("from_duration")
        to_duration = request.POST.get("to_duration")
        uid =request.session['log_id']
        ssd = request.FILES['ss']
        vid = request.POST.get("vid")
        rent = request.POST.get("rent")

        from datetime import datetime
        date_format = "%Y-%m-%d"
        a = datetime.strptime(str(from_duration),date_format)
        b = datetime.strptime(str(to_duration),date_format)
        delta = b-a
        print(delta.days)
        amount = int(delta.days) * int(rent)
        booker = booking_table(amount=amount, from_duration=from_duration, from_to=to_duration, login_id=usertable(id=uid), vehicle_id = vehicle_table(id=vid), paystatus=1, reciept=ssd)
        booker.save()
        messages.success(request,"booking done")
    else:
        messages.success(request, "booking not done")
    return render(request,'index.html')

def history(request):
    uid = request.session['log_id']
    getcar = booking_table.objects.filter(login_id_id=uid)
    context = {
        "data": getcar
    }
    return render(request,'history.html',context)

def feedback1(request):
    return render(request,'feedback.html')

def feedbackfill(request):
    if request.method == "POST":
        uid =request.session['log_id']
        name = request.POST.get("name")
        msg = request.POST.get("msg")
        rate = request.POST.get("rate")

        feed = feedback(l_id=usertable(id=uid),ratings=rate,name=name,comments=msg)
        feed.save()
        messages.success(request, "Feedback done done")
        return render(request,'feedback.html')
