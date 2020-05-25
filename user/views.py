from django.shortcuts import render, redirect
from .forms import UserRegisteration
# Create your views here.
def signup(request):
    if(request.method=="POST"):
        form = UserRegisteration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegisteration()
    context =  {"form" : form}
    return render(request,"user/signup.html",context)