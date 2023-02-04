from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class Landing(View):
    def get(self, r):
        if r.user.is_authenticated:
            return redirect("dashboard")
        return render(r, "landing.html")

    def post(self, r):
        username = r.POST.get("full-name")
        password = r.POST.get("password")

        user = authenticate(username = username, password = password)

        if user:
            login(r, user)
            return redirect("dashboard")

        messages.error(r, '<div><p class="font-semibold">Something was wrong</p><p class="text-sm">Check your username or password</p></div>')
        
        return redirect("landingpage")


class dashboard(View):
    def get(self, r):
        if not r.user.is_authenticated:
            return redirect("landingpage")
        return render(r, "dashboard.html", {
            'user': User.objects.get(username=r.user),
        })

    def post(self, r):
        logout(r)

        messages.success(r, '<div><p class="font-bold">LogOut Successfully</p><p class="text-sm">Your have successfully Logout</p></div>')

        return redirect("landingpage")

        


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


        if password == conPassword and Fname and Lname and username and password and Email:
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