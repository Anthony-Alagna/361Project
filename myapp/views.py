from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(
            User_LogName=username, User_LogPass=password)
        if user:
            return redirect('index')
        else:
            return redirect('login')


class AccountBase(View):
    def get(self, request):
        return render(request, 'accountbase.html')

    def searchUser(self):
        pass

    def filterUser(self):
        pass

    def deleteUser(self):
        pass
