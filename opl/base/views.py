from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Calendar, Blog, Admission
from datetime import datetime
from .forms import BlogForm, AdmissionForm
# Create your views here.


def home(request):
    calendars = Calendar.objects.all().order_by('-id')
    ctx = {'calendars' : calendars[:3]}
    return render(request, 'base/index.html', ctx)


def login_staff(request):
    error = ''
    if request.user.is_authenticated:
        return redirect('dash')

    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            error = 'User does not exist!'

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
           error = 'Username or password is not correct'

    ctx = {'error': error}
    return render(request, 'base/staff-login.html', ctx)


def logout_staff(request):
    logout(request)
    return redirect('login')


def register(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        pword1 = request.POST.get('password1')
        pword2 = request.POST.get('password2')
        if pword1 == pword2:
            username = username.lower()
            user = User.objects.create_user(username, '', pword2)
            user.save()
            login(user)
        else: 
            error = "Passwords don't match"

    ctx = {'error': error}
    return render(request, 'base/register.html', ctx)


def services(request):
    ctx = {}
    return render(request, 'base/services.html', ctx)


def events(request):
    calendars = Calendar.objects.all().order_by('-id')
    ctx = {'calendars': calendars}
    return render(request, 'base/events.html', ctx)


def addcalendar(request):
    error = ''
    if request.method == 'POST':
        name = request.POST.get('calendar-name')
        date = request.POST.get('calendar-date')
        if name and date:
            calendar = Calendar.objects.create(
                name = name,
                date = date
            )
            calendar.save()
            return redirect('events')
        else: 
            error = 'An Error occured'
    
    ctx = {'error': error}
    return render(request, 'base/add_events.html', ctx)



def delete_calendar(request, pk):
    calendar = Calendar.objects.get(id=pk)
    print(calendar)
    if request.method == "POST":
        calendar.delete()
        return redirect('events')

    ctx = {'obj': calendar}
    return render(request, 'base/delete.html', ctx)


def dash(request):
    ctx = {}
    return render(request, 'base/dash.html', ctx)


def blog_feed(request):
    blog = Blog.objects.all()
    ctx = {'blogs': blog}
    return render(request, 'base/blog_feed.html', ctx)


def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    ctx = {'blog': blog}
    return render(request, 'base/blog.html', ctx)

def create_blog(request):
    error = ''
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            error = 'Blog has been successfully sent'
            return redirect('blog-feed')
        else:
            error = 'An error occured'
    else:
        form = BlogForm()

    ctx = {'form': form, 'error': error}
    return render(request, 'base/create-blog.html', ctx)



def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    
    if request.method == "POST":
        blog.delete()
        return redirect('blog-feed')

    ctx = {'obj': blog}
    return render(request, 'base/delete.html', ctx)



def admission(request):
    msg = ''
    form = AdmissionForm()
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Data has been sent successfully'
            return redirect('home')
        else:
            msg = 'An error occured'
    ctx = {'form': form, 'msg': msg}
    return render(request, 'base/admission.html', ctx)


def see_enrollment(request):
    enrolled_list = Admission.objects.all().order_by('-id')
    ctx = {'lists': enrolled_list}
    return render(request, 'base/enrollment.html', ctx)