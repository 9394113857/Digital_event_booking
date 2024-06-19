from django.shortcuts import render, redirect
from eventapp.forms import CustomerForm,EventmanagerForm,AddeventForm,AdministrationForm,BookForm,ReviewForm
from eventapp.models import Customer,Eventmanager,Addevent,Administration,Bookevent,Review

# Create your views here.

def index(request):
    return render(request, "index.html", {})
def about(request):
    return render(request, "about.html", {})
def contact(request):
    return render(request, "contact.html", {})


#Customer Views
def customer(request):
    return render(request, "customer_login.html", {})



def customerhome(request):
    return render(request, "customer.html", {})


def administrationhome(request):
    return render(request, "administration.html", {})

def eventmanagerhome(request):
    return render(request, "eventmanager.html", {})


def regpage(request):
    return render(request, "reg.html", {})

def reg(request):
    if request.method == "POST":
        email = request.POST["email"]
        print("hello")
        if Customer.objects.filter(email=email).exists():
            print("email already taken")
            return render(request,"reg.html",{"msg":"This email is already taken"})
        else:
            form = CustomerForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return render(request, "customer_login.html", {"msg": "REGISTER SUCCESS"})
                except Exception as e:
                    print(e)
            return render(request, "reg.html", {"msg": "REGISTER IS FAIL"})


def is_customer_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False
def customer_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        customer = Customer.objects.filter(email=email, password=password)
        if customer.exists():
            request.session["email"] = email
            return render(request, "customer.html", {"msg": email})
        else:
            return render(request, "customer_login.html", {"msg": "email or password not exist"})
    return render(request, "customer_login.html", {"msg": ""})

def customer_change(request):
    if is_customer_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]

            try:
                customer = Customer.objects.get(email=email, password=password)
                customer.password = newpassword
                customer.save()
                msg = "password updated successfully"
                return render(request, "customer_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "customer_change.html", {"msg": msg})
        return render(request, "customer_change.html", {})
    else:
        return render(request, "customer_change.html", {})
def customer_display(request):
    email = request.session["email"]
    customer = Customer.objects.filter(email=email)
    print("hello")
    return render(request, "customer_display.html", {"customer": customer})

def customer_viewevent(request):
    addevent = Addevent.objects.all()
    return render(request, "customer_viewevent.html", {"addevent": addevent})

# def customer_viewreview(request,id):
#     addevent = Addevent.objects.get(id=id)
#     print("hello")
#     review = Review.objects.filter(addevent_id=addevent.id)
#     return render(request, "customer_viewreview.html", {"reviews": review})


def customer_delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/regpage")

def customer_edit(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "customer_edit.html", {"customer": customer})

def customer_viewbook(request):
    email = request.session["email"]
    customer = Customer.objects.get(email=email)
    book = Bookevent.objects.filter(customer_id=customer.id)
    print("hello")
    return render(request, "customer_viewbook.html", {"book": book})

def customer_viewreview(request,id):
    addevent=Addevent.objects.get(id=id)
    review=Review.objects.filter(addevent_id=addevent.id)
    print("hello")
    return render(request, "customer_viewreview.html", {"review": review})


def customer_update(request):
    if request.method == "POST":
        customerid = request.POST["id"]
        customer = Customer.objects.get(id=customerid)
        customer = CustomerForm(request.POST, instance=customer)
        if customer.is_valid():
            customer.save()
        return redirect("/customer_display",{"msg":"Update Successfully"})
    return redirect("/customer_display",{"msg":"update failed"})

def customer_logout(request):
     if request.session.has_key("email"):
        email = request.session["email"]
        return render(request, "customer_login.html", {"email": email})

#Eventmanager Views
def eventmanager(request):
    return render(request, "eventmanager_login.html", {})
def eventmanager_registerpage(request):
    return render(request, "eventmanager_reg.html", {})
def eventmanager_reg(request):
    if request.method == "POST":
        email = request.POST["email"]
        print("hello")
        if Eventmanager.objects.filter(email=email).exists():
            print("email already taken")
            return render(request, "eventmanager_reg.html", {"msg": "This email is already taken"})
        else:
            form = EventmanagerForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return render(request, "eventmanager_login.html", {"msg": "REGISTER SUCCESS"})
                except Exception as e:
                    print(e)
            return render(request, "eventmanager_reg.html", {"msg": "REGISTER IS FAIL"})

def eventmanager_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        eventmanager = Eventmanager.objects.filter(email=email, password=password)
        if eventmanager.exists():
            request.session["email"] = email
            return render(request, "eventmanager.html", {"msg": email})
    else:
        return render(request, "eventmanager_login.html", {"msg": "email or password not exist"})
    return render(request, "eventmanager_login.html", {"msg": "email or password not exist"})

def is_eventmanager_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False

def eventmanager_change(request):
    if is_eventmanager_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]

            try:
                eventmanager = Eventmanager.objects.get(email=email, password=password)
                eventmanager.password = newpassword
                eventmanager.save()
                msg = "password updated successfully"
                return render(request, "eventmanager_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "eventmanager_change.html", {"msg": msg})
        return render(request, "eventmanager_change.html", {})
    else:
        return render(request, "eventmanager_change.html", {})

def eventmanager_display(request):
    email = request.session["email"]
    eventmanager = Eventmanager.objects.filter(email=email)
    print("hello")
    return render(request, "eventmanager_display.html", {"eventmanager": eventmanager})

def eventmanager_viewevent(request):
    email = request.session['email']
    addevent = Addevent.objects.filter(email=email)
    return render(request, "eventmanager_viewevent.html", {"addevent": addevent})


def accept_book(request, booking_id):
    accept = Bookevent.objects.get(id=booking_id)
    accept.status = 1
    accept.save()
    return redirect("/eventmanager_viewevent")


def reject_book(request, booking_id):
    reject = Bookevent.objects.get(id=booking_id)
    reject.status = 2
    reject.save()
    return redirect("/eventmanager_viewevent")


def cancel_book(request, booking_id):
    reject = Bookevent.objects.get(id=booking_id)
    reject.status = 3
    reject.save()
    return redirect("/customer_bookings")

def eventmanager_viewbook(request,id):
    addevent = Addevent.objects.get(id=id)
    book = Bookevent.objects.filter(addevent_id=addevent.id)
    return render(request, "eventmanager_viewbook.html", {"book": book})


def eventmanager_viewreview(request,id):
    addevent = Addevent.objects.get(id=id)
    review = Review.objects.filter(addevent_id=addevent.id)
    print("hello")
    return render(request, "eventmanager_viewreview.html", {"review": review})

def eventmanager_logout(request):
     if request.session.has_key("email"):
        email = request.session["email"]
        return render(request, "eventmanager_login.html", {"email": email})

def manager_edit(request,id):
    eventmanager = Eventmanager.objects.get(id=id)
    return render(request, "eventmanager_edit.html", {"eventmanager": eventmanager})

def manager_update(request):
    if request.method == "POST":
        addeventid = request.POST["id"]
        print("hii")
        addevent = Eventmanager.objects.get(id=addeventid)
        addevent = EventmanagerForm(request.POST, instance=addevent)
        if addevent.is_valid():
            addevent.save()
        return redirect("/eventmanager_display")
    return redirect("/eventmanager_display")


def eventmanager_edit(request,id):
    addevent = Addevent.objects.get(id=id)
    return render(request, "addevent_edit.html", {"addevent": addevent})

def eventmanager_update(request):
    if request.method == "POST":
        addeventid = request.POST["id"]
        print("hii")
        addevent = Addevent.objects.get(id=addeventid)
        addevent = AddeventForm(request.POST, instance=addevent)
        if addevent.is_valid():
            addevent.save()
        return redirect("/eventmanager_viewevent")
    return redirect("/eventmanager_viewevent")

def post_event(request):
    email = request.session['email']
    return render(request, "add_event.html", {'email1': email})

def add_event(request):
    if request.method == "POST":
        addevent = AddeventForm(request.POST, request.FILES)
        # print("error",addevent.error)
        if addevent.is_valid():
            addevent.save()
        return render(request, "add_event.html", {"msg": "successfully add event"})
    return render(request, "add_event.html", {})

def addevent_update(request):
    if request.method == "POST":
        addeventid = request.POST["id"]
        addevent = Addevent.objects.get(id=addeventid)
        addevent = AddeventForm(request.POST,request.FILES, instance=addevent)
        print("error:",addevent.errors)

        if addevent.is_valid():
            addevent.save()
        return redirect("/eventmanager_viewevent")
    return redirect("/eventmanager_viewevent")

def addevent_edit(request,id):
    addevent = Addevent.objects.get(id=id)
    return render(request, "addevent_edit.html", {"addevent": addevent})
def addevent_delete(request,id):
    addevent = Addevent.objects.get(id=id)
    addevent.delete()
    return redirect("/addevent")

def view_event(request):
    addevent = Addevent.objects.all()
    return render(request, "view_event.html", {"addevent": addevent})

#Admin Views
def administration(request):
    return render(request,"admin_login.html",{})

def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        administration = Administration.objects.filter(email=email,password=password)
        if administration.exists():
            print("hello")
            request.session["email"] = email
            return render(request, "administration.html", {"msg": email})
        else:
            return render(request, "admin_login.html", {"msg": "email or password not exist"})
    return render(request, "admin_login.html", {"msg": ""})



def admin_viewevent(request):
    addevent = Addevent.objects.all()
    return render(request, "admin_viewevent.html", {"addevent": addevent})


def admin_viewreview(request):
    review = Review.objects.all()
    print("hello")
    return render(request, "admin_viewreview.html", {"review": review})

def admin_logout(request):
     if request.session.has_key("email"):
        email = request.session["email"]
        return render(request, "admin_login.html", {"email": email})


def admin_book(request, id):
    email = request.session["email"]
    customer = Customer.objects.get(email=email)
    addevent = Addevent.objects.get(id=id)
    if request.method == "POST":
        print("hii")
        book = BookForm(request.POST)
        print("error",book.errors)
        if book.is_valid():
            print("hello")
            book.save()
        return render(request, "book.html", {"msg": "success", "id": addevent.id, "customer": customer.id})
    return render(request, "book.html", {"id": addevent.id, "email": customer.id})


def book(request, id):
    email = request.session["email"]
    customer = Customer.objects.get(email=email)
    addevent = Addevent.objects.get(id=id)
    if request.method == "POST":
        print("hii")
        book = BookForm(request.POST)
        print("error",book.errors)
        if book.is_valid():
            print("hello")
            book.save()
        return render(request, "book.html", {"msg": "success", "id": addevent.id, "customer": customer.id,"cost":addevent.entryfee, "title":addevent.title,"datatime":addevent.datatime})
    return render(request, "book.html", {"id": addevent.id, "email": customer.id,"cost":addevent.entryfee, "title":addevent.title,"datatime":addevent.datatime})

def admin_viewbook(request):
    book = Bookevent.objects.all()
    return render(request, "admin_viewbook.html", {"book": book})

def review(request, id):
    email = request.session["email"]
    customer = Customer.objects.get(email=email)
    addevent = Addevent.objects.get(id=id)
    if request.method == "POST":
        print("hii")
        review = ReviewForm(request.POST)
        print("error",review.errors)
        if review.is_valid():
            print("hello")
            review.save()
        return render(request, "review.html", {"msg": "sent review successfully", "id": addevent.id, "customer": customer.id,"title":addevent.title})
    return render(request, "review.html", {"id": addevent.id, "email": customer.id,"title":addevent.title})

def admin_viewcustomer(request):
    customer = Customer.objects.all()
    print("hello")
    return render(request, "admin_viewcustomer.html", {"customer": customer})


def admin_viewcontact(request):
    contact = Contact.objects.all()
    print("hello")
    return render(request, "admin_viewcontact.html", {"contact": contact})


def admin_vieweventmanager(request):
    eventmanager = Eventmanager.objects.all()
    print("hello")
    return render(request, "admin_vieweventmanager.html", {"eventmanager": eventmanager})


def customer_bookings(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    epass = Bookevent.objects.filter(customer_id=customer.id)
    return render(request, "customer_viewbook.html", {"books": epass})

def Admin_customer_delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/admin_viewcustomer")


def Admin_manager_delete(request, id):
    customer = Eventmanager.objects.get(id=id)
    customer.delete()
    return redirect("/admin_vieweventmanager")

def Admin_event_delete(request, id):
    customer = Addevent.objects.get(id=id)
    customer.delete()
    return redirect("/admin_viewevent")