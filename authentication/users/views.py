from django.shortcuts import render,redirect
from django.views import View




class Home(View):
    def get(self,request):
        return render(request,'home.html')


from users.forms import SignupForm,LoginForm
from django.contrib.auth.forms import UserCreationForm


    # def post(self,request):
    #     form_instance=SignupForm(request.POST)
    #     if form_instance.is_valid():
    #         form_instance.save()
    #         return redirect('login')
    #



class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('userlogin')  # or any success URL
        else:
            print('error')
            return render(request, 'register.html', {'form': form_instance})


    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)


from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

class Userlogin(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():

            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)

            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'invalid user')
                return render(request, 'login.html', {'form': form_instance})



    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)

class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
