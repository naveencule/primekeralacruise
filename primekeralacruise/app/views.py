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
            else:
                return HttpResponse(f"<script>alert('Invalid user...!');window.location='/login'</script>")
        else:
            return HttpResponse(f"<script>alert('Username or password incorrect...!');window.location='/login'</script>")
    return render(request,'public/login.html')


# -----------------------------------Admin functions----------------------------------

def admin_home(request):
    return render(request,'admin/admin_home.html')

def admin_view_package(request):
    packages = Package.objects.all()
    return render(request, 'admin/admin_view_package.html', {'packages': packages})

def admin_add_package(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        photo = request.FILES.get('photo')
        description = request.POST.get('description')
        Package.objects.create(
            title=title,
            photo=photo,
            description=description
        )
        return redirect('admin_view_package')
    return render(request, 'admin/admin_add_package.html')

def admin_edit_package(request, id):
    package = Package.objects.get(id=id)
    if request.method == 'POST':
        package.title = request.POST.get('title')
        package.description = request.POST.get('description')
        if 'photo' in request.FILES:
            package.photo = request.FILES['photo']
        package.save()
        return redirect('admin_view_package')
    return render(request, 'admin/admin_edit_package.html', {'package': package})

def admin_delete_package(request, id):
    package = Package.objects.get(id=id)
    package.delete()
    return redirect('admin_view_package')