from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.models import User


def base(request):
    return render(request,'base.html')
def home(request):
    return render(request, 'components/home.html')


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password1')

        if pw1 != pw2:
            return HttpResponse("passwords do not match")
        else:
            my_user = User.objects.create_user(uname, email, pw1)
            my_user.save()
            return redirect('/')
    else:
        return render(request, 'components/register.html')


def login(request):
    return render(request, 'components/login.html')