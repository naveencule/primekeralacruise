from django.shortcuts import render, redirect, HttpResponse
from .models import *
# Create your views here.


# -----------------------------------Public functions----------------------------------

def index(request):
    return render(request,'public/index.html')

def login(request):
    if 'submit' in request.POST:
        uname=request.POST['username']
        password=request.POST['password']
        if Login.objects.filter(uname=uname,password=password).exists():
            s=Login.objects.get(uname=uname,password=password)
            request.session["lid"]=s.pk
            lid=request.session.get('lid')
            if s.user_type == "admin":
                request.session['log']="in"
                return HttpResponse(f"<script>alert('Welcome Admin');window.location='/admin_home'</script>")
            # elif s.user_type == "doctor":
            #     request.session['log']="in"
            #     q=Doctor.objects.get(LOGIN=lid)
            #     request.session["doc_id"]=q.pk
            #     return HttpResponse(f"<script>alert('Welcome doctor');window.location='/doctorhome'</script>")
            # elif s.user_type == "staff":
            #     request.session['log']="in"
            #     q=Staff.objects.get(LOGIN=lid)
            #     request.session["staff_id"]=q.pk
            #     return HttpResponse(f"<script>alert('Welcome staff');window.location='/staffhome'</script>")
            else:
                return HttpResponse(f"<script>alert('Invalid user...!');window.location='/login'</script>")
        else:
            return HttpResponse(f"<script>alert('Username or password incorrect...!');window.location='/login'</script>")
    return render(request,'public/login.html')


# -----------------------------------Admin functions----------------------------------

def admin_home(request):
    return render(request,'admin/admin_home.html')