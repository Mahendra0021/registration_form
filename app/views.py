from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='login')
def SignupPage(requset):
    if requset.method=='POST':
        print('your data is add')
        print(requset.method)
        if requset.method=='POST':
            uname=requset.POST.get('email')
            pass1=requset.POST.get('pass1')
            log=User.objects.create_user(uname,pass1)
            log.save()
            return HttpResponse("your data rasiter")

    return render(requset,'loginn.html')



    
def LoginPage(requset):
    return render(requset,'Newlogin.html')
def Home(requset):
    print('mahendra')
    print(requset.method)
    if requset.method=='POST':
        username=requset.POST.get('name')
        ddate=requset.POST.get('date')
        ccity=requset.POST.get('City')
        sstate=requset.POST.get('State')
        ccountry=requset.POST.get('Country')
        Experience=requset.POST.get('Experience')
        Cost=requset.POST.get('Cost')
      #  ECTC=requset.POST.get('ECTC')
      #  lag=requset.POST.get('lag')
       # cityy=requset.POST.get('cityy')
      #  yes=requset.POST.get('yes')
        my_user=User.objects.create_user(username)
        my_user.save()
        return HttpResponse("user has been created successfully")
        print(name,date,city,State,Country)
        
    return render(requset,'submit.html')