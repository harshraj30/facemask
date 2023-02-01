from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


class Landing(View):
    def get(self, r):
        return render(r, "landing.html")

    def post(self, r):
        username = r.POST.get("full-name")
        password = r.POST.get("password")

        user = authenticate(username = username, password = password)

        if user:
            login(r, user)
            return redirect("dashboard")


        # print(username, password)
        
        return redirect("landingpage")


class dashboard(View):
    def get(self, r):
        return render(r, "dashboard.html", {
            'user': User.objects.get(username=r.user),
        })


class signUp(View):
    def get(self, r):
        return render(r, "signUp.html")

    def post(self, r):
        Fname = r.POST.get("Fname")
        Lname = r.POST.get("Lname")
        Email = r.POST.get("Email")
        username = r.POST.get("Username")
        DOB = r.POST.get("DOB")
        Gender = r.POST.get("Gender")
        password = r.POST.get("password")
        conPassword = r.POST.get("conPassword")


        if password == conPassword:
            user = User()
            user.first_name = Fname
            user.last_name = Lname
            user.username = username
            user.email = Email
            user.set_password(password)
            user.is_superuser = False
            user.is_staff = False
            user.is_active = True
            user.save()


            login(r, user)

            return redirect("dashboard")
        
         
        # print(Fname, Lname, Email, Contact, DOB, Gender, password, conPassword)


        return redirect("landingpage")