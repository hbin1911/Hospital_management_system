from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('book', views.book, name='book'),
    path('deletee/<str:id>', views.Deletee, name='deletee'),
    path('delete/<str:id>', views.Delete, name='delete'),
    path('contact', views.contact, name='contact'),
    path('muscleinfo', views.muscleinfo, name='muscleinfo'),
    path('getplans', views.getplans, name='getplans'),
    path('login', views.handleLogin, name='handelLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('signup', views.handleSignup, name='handleSignup'), 
    path('index1', views.index1, name='index1'),
    path('addpatient', views.addpatient, name='addpatient'), 
    path('updatee/<str:id>', views.Updatee, name='updatee'),
    path('update/<str:id>', views.Update, name='update'),
    path('editpatient', views.editpatient, name='editpatient'), 
    path('patients', views.patients, name='patients'), 
    path('aboutpatient', views.aboutpatient, name='aboutpatient'), 
    
    path('aboutdoctor', views.aboutdoctor, name='aboutdoctor'),
    
    path('adddoctor', views.adddoctor, name='adddoctor'),
  
    path('appointments', views.appointments, name='appointments'),
   
    path('doctors', views.doctors, name='doctors'),

    path('gateway', views.gateway, name='gateway'),
    
    path('pop', views.pop, name='pop'),
   
    path('editdoctor', views.editdoctor, name='editdoctor'),
    # path('rooms', views.rooms, name='rooms'),
   
    path('payments', views.payments, name='payments'),
   
    path('rooms', views.rooms, name='rooms'),
    path('addroom', views.addroom, name='addroom'),
    path('editroom', views.editroom, name='editroom'),
    path('updateroom/<str:id>', views.updateroom, name='updateroom'),
    path('deleteroom/<str:id>', views.deleteroom, name='deleteroom'),


]
