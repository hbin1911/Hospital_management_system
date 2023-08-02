#main id/pass=admin
#user id=akash123 , pass=akash
from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime
from home.models import Contact
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Patient
from home.models import Book
from home.models import Doctor
from home.models import Room


# Create your views here.
def index(request):
    
    return render(request, 'index.html')
    #return HttpResponse("This is Home Page")

def about(request):
    return render(request, 'about.html')
   
#Id/pass=fitness
def contact(request):
   # messages.success(request, 'Welcome to Contact')
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        date=request.POST['date']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "please fill the message Correctly !!!")
        else:
            contact=Contact(name=name,email=email,phone=phone,desc=desc,date=date)
            contact.save()
            messages.success(request, "Your messages has been Successfully Send.")

    return render(request, 'contact.html')
  

def muscleinfo(request):
    return render(request, 'muscle_info.html')
    

def getplans(request):
    return render(request, 'get_plans.html')
    
def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully Logged In.")
            return redirect('home')
        else:
            messages.error(request, "Fail to Logged In.")
            return redirect('home')

    return HttpResponse('404 -Not Found')
    
def handleLogout(request):  
    logout(request)
    messages.success(request, "successfully Logged out.")
    return redirect('home')

    

def handleSignup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myUser=User.objects.create_user(username, email, pass1)
        myUser.first_name=fname
        myUser.last_name=lname
        myUser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('/')
    else:
        return HttpResponse('404 -Not Found')
    
def index1(request):
   
    
    return render(request, 'index1.html')


def aboutpatient(request):
   return render(request, 'aboutpatient.html')

def editpatient(request):
    pat = Patient.objects.all()

    context = {
        'pat':pat,
    }

    return redirect(request, 'patients.html', context)

def patients(request):
    pat = Patient.objects.all()

    context = {
        'pat':pat,
    }
    return render(request, 'patients.html', context)

def Update(request, id):
    if request.method == "POST":
        patient_Name = request.POST.get('patient_Name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        pat = Patient(
            id = id,
           patient_Name = patient_Name,
           age = age,
           phone = phone,
           email = email,
           gender = gender,
           address = address
        )
        pat.save()
        return redirect('patients')

    return redirect(request, 'patients.html')
    
    
def addpatient(request):    
    if request.method == "POST":
        patient_Name = request.POST.get('patient_Name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        pat = Patient(
           patient_Name = patient_Name,
           age = age,
           phone = phone,
           email = email,
           gender = gender,
           address = address
        )
        pat.save()
        return redirect('patients')   
    return render(request, 'patients.html')

def Delete(request, id):
    pat = Patient.objects.filter(id = id)
    pat.delete()

    context = {
        'pat':pat,
    }
    return redirect('patients')


def about(request):
    return render(request, 'about.html')

def book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        age = request.POST.get('age')
        desc = request.POST.get('desc')
        date = request.POST.get('date')

        if len(name)<2 or len(email)<3 or len(number)<10 or len(desc)<4:
            messages.error(request, "please fill the message Correctly !!!")
        else:
            book=Book(name=name,email=email,number=number,desc=desc,date=date)
            book.save()
            messages.success(request, "Your messages has been Successfully Send.")

    return render(request, 'book.html')   
       
        
    

def aboutappointment(request):
    return render(request, 'aboutappointment.html')

def aboutdoctor(request):
    return render(request, 'aboutdoctor.html')

def aboutpayment(request):
    return render(request, 'aboutpayment.html')

def accordions(request):
    return render(request, 'accordions.html')

def addappointment(request):
    return render(request, 'addappointment.html')



def addpayment(request):
    return render(request, 'addpayment.html')

def addroom(request):
    return render(request, 'addroom.html')

def appointments(request):
    return render(request, 'appointments.html')

def blankpage(request):
    return render(request, 'blankpage.html')

def buttons(request):
    return render(request, 'buttons.html')

def cards(request):
    return render(request, 'cards.html')

def carousel(request):
    return render(request, 'carousel.html')

def gateway(request):
    return render(request, 'gateway.html')

def pop(request):
    return render(request, 'pop.html')

def charts1(request):
    return render(request, 'charts1.html')

def charts2(request):
    return render(request, 'charts2.html')



# 
# 
# 
# 
# 
def doctors(request):
    doc = Doctor.objects.all()

    context = {
        'doc':doc,
    }
    return render(request, 'doctors.html', context)
    

def editdoctor(request):
    doc = Doctor.objects.all()

    context = {
        'doc':doc,
    }

    return redirect(request, 'doctors.html', context)

def Deletee(request, id):
    doc = Doctor.objects.filter(id = id)
    doc.delete()

    context = {
        'doc':doc,
    }
    return redirect('doctors')

def adddoctor(request):
    if request.method == "POST":
        doctor_Name = request.POST.get('doctor_Name')
        agee = request.POST.get('agee')
        phonee = request.POST.get('phonee')
        emaill = request.POST.get('emaill')
        genderr = request.POST.get('genderr')
        addresss = request.POST.get('addresss')
        roless = request.POST.get('roless')

        doc = Doctor(
            doctor_Name = doctor_Name,
            agee = agee,
            phonee = phonee,
            emaill = emaill,
            genderr = genderr,
            addresss = addresss,
            roless = roless
        )
        doc.save()
        return redirect('doctors')   
    return render(request, 'doctors.html')

def Updatee(request, id):
    if request.method == "POST":
        doctor_Name = request.POST.get('doctor_Name')
        agee = request.POST.get('agee')
        phonee = request.POST.get('phonee')
        emaill = request.POST.get('emaill')
        genderr = request.POST.get('genderr')
        addresss = request.POST.get('addresss')
        roless = request.POST.get('roless')

        doc = Doctor(
           id = id,
           doctor_Name = doctor_Name,
           agee = agee,
           phonee = phonee,
           emaill = emaill,
           genderr = genderr,
           addresss = addresss,
           roless = roless
        )
        doc.save()
        return redirect('doctors')

    return redirect(request, 'doctors.html')


    
    

def editappointment(request):
    return render(request, 'editappointment.html')



# def rooms(request):
#     return render(request, 'rooms.html')

def faq(request):
    return render(request, 'faq.html')

def fontawesome(request):
    return render(request, 'fontawesome.html')

def forms(request):
    return render(request, 'forms.html')

def grid(request):
    return render(request, 'grid.html')

def invoice(request):
    return render(request, 'invoice.html')

def lists(request):
    return render(request, 'lists.html')

def map1(request):
    return render(request, 'map1.html')

def map2(request):
    return render(request, 'map2.html')

def modals(request):
    return render(request, 'modals.html')

def notificationsalerts(request):
    return render(request, 'notificationsalerts.html')

def pagination(request):
    return render(request, 'pagination.html')

def payments(request):
    return render(request, 'payments.html')

def pricing(request):
    return render(request, 'pricing.html')

def progressbars(request):
    return render(request, 'progressbars.html')

def rooms(request):
    rm = Room.objects.all()

    context = {
        'rm': rm,
    }
    return render(request, 'rooms.html', context)

def addroom(request):
    if request.method == 'POST':
        roomnumber = request.POST.get('roomnumber')
        roomtype = request.POST.get('roomtype')
        patientname = request.POST.get('patientname')
        allotmentdte = request.POST.get('allotmentdte')
        dischargedte = request.POST.get('dischargedte')
        docname = request.POST.get('docname')


        rm = Room(
            roomnumber = roomnumber,
            roomtype = roomtype,
            patientname = patientname,
            allotmentdte = allotmentdte,
            dischargedte = dischargedte,
            docname = docname

        )
        rm.save()
        return redirect('rooms')
    return render(request, 'rooms.html')

def editroom(request):
    rm = Room.objects.all()

    context = {
        'rm':rm,
    }



    return render(request, 'rooms.html', context)

def updateroom(request, id):
    if request.method == 'POST':
        roomnumber = request.POST.get('roomnumber')
        roomtype = request.POST.get('roomtype')
        patientname = request.POST.get('patientname')
        allotmentdte = request.POST.get('allotmentdte')
        dischargedte = request.POST.get('dischargedte')
        docname = request.POST.get('docname')

        rm = Room(
            id = id,
            roomnumber = roomnumber, 
            roomtype = roomtype,
            patientname = patientname,
            allotmentdte = allotmentdte,
            dischargedte = dischargedte,
            docname = docname
        )
        rm.save()
        return redirect('rooms')

    return render(request, 'rooms.html')

def deleteroom(request, id):
    rm = Room.objects.filter(id = id)
    rm.delete()     

    context = {
        'rm':rm
    }
    return redirect('rooms')

def tables(request):
    return render(request, 'tables.html')

def tabs(request):
    return render(request, 'tabs.html')

def themify(request):
    return render(request, 'themify.html')

def typography(request):
    return render(request, 'typography.html')

    
   
    

    