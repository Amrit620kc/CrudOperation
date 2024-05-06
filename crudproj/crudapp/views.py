from django.shortcuts import render,redirect
from django.contrib import messages
from crudapp.models import Student

# Create your views here.
def home(request):
    students=Student.objects.all()
    context={
        "students":students,
    }
    return render(request, "home/index.html",context)

def add(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        roll=request.POST.get('roll')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')

        data=Student(first_name=firstname, last_name=lastname, roll=roll, phone=phone, email=email, address=address)
        data.save()
        messages.success(request,"successfully sent!")
    return render(request, "home/add.html")

def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def update(request,id):
    student=Student.objects.get(id=id)
    context={
        "student":student
    }
    return render(request,"home/update.html",context)
def do_update(request, id):
    if request.method=="POST":
       first_name=request.POST.get('firstname') 
       last_name=request.POST.get('lastname')
       phone=request.POST.get('phone')
       email=request.POST.get('email')
       address=request.POST.get('address')

       student=Student.objects.get(id=id)
       student.first_name=first_name
       student.last_name=last_name
       student.phone=phone
       student.email=email
       student.address=address
       student.save()
       return redirect('/')
    
def search(request):
    search=request.GET['search']
    
    if len(search)>20:
        student=Student.objects.none()
    else:
        firstname=Student.objects.filter(first_name__icontains=search)
        lastname=Student.objects.filter(last_name__icontains=search)
        roll=Student.objects.filter(roll__icontains=search)
        student=firstname.union(lastname,roll)
    if student.count()==0:
        messages.warning(request,"No search results!")
    context={
        "students":student,
        "search":search,
    }

    return render(request,"home/search.html",context)



    