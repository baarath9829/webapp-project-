from django.shortcuts import render, redirect
from .models  import notes
from .forms import upload
import datetime
# Create your views here.
def invalid(request):
    return redirect('home')
def home(request):
    context={}
    if(request.method=='POST'):
        data = notes.objects.get(id=request.POST['id'])
        data.views = data.views+1
        data.save()
    context["dataset"] = notes.objects.all()
    return render(request, "noteitdown/home.html", context)

def upload_view(request):
    context = {}
    date = datetime.date.today()
    if (request.method == 'POST'):
        form = upload(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            entry = notes(author_name=data["author_name"], date_of_pub=date, department=data["department"], name=data["name"], file=data["file"])
            entry.save()
            return redirect('home')
        else:
            print(form.errors)
    form = upload()
    context["form"] = form
    return render(request, "noteitdown/upload.html", context)

def about(request):
    return render(request, "noteitdown/about.html")