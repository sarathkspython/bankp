from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import District
from .models import regf
from .models import Branch
from .forms import location


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, "reg.html")
        else:
            messages.info('invalid credentials')
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')


            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:

                user = User.objects.create_user(username=username, password=password, email=email)
                user.save();
                return redirect('login')
                print("new user created")

        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def reg(request):
    return render(request, "reg.html")


def form(request):
    form = location()
    return render(request, "forms.html", {"form": form})
    print("new user created")
def dependantfield(request):
    districtid = request.GET.get('district',None)
    branchid = request.GET.get('branch',None)
    branch = None
    district = None
    if districtid:
        getdistrict =District.objects.get(id=districtid)
        branch = Branch.objects.filter(district=getdistrict)
    if branchid:
        getbranch = Branch.objects.get(id=branchid)
        district = District.objects.filter(branch=getbranch)
    district = District.objects.all()
    return render(request,"dependantfield.html",locals())
#
#
# # def branch(request):
# #     district_id = request.Get.get("District")
# #     branchs = Branch.objects.filter(district_id=district_id).order_by('name')
# #     return render(request, "branch.html", {"branchs": branchs})
# #
# # class regfListView(ListView):
# #     model = regf
# #     context_object_name = 'people'
# # class regfCreateView(CreateView):
# #     model = regf
# #     fields = ('district', 'branch')
# #     success_url = reverse_lazy('regf_changelist')
# #
# # class regfUpdateView(UpdateView):
# #     model = regf
# #     fields = ('district', 'branch')
# #     success_url = reverse_lazy('regf_changelist')
#
# #
# # class regfCreateView(CreateView):
# #     model = regf
# #     form_class = location
# #     success_url = reverse_lazy('regf_changelist')
# #
# # class regfUpdateView(UpdateView):
# #     model = regf
# #     form_class = location
# #     success_url = reverse_lazy('regf_changelist')

def get_branch(request):
    district_id = request.GET("district_id")
    get_district = District.objects.get(id=district_id)
    branch = Branch.objects.filter(district=get_district)
    return render(request,'branch.html', locals())
