from django.shortcuts import render, HttpResponseRedirect,Http404

# Create your views here.

from .forms import ProfileForm, ProfileForm2 #import the Profile form from forms.py
from .models import Profile
import uuid

def scan_ip(request):
    try:
        http_x_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if http_x_for:
            ipAdd = http_x_for.split(",")[0]
        else:
            ipAdd = request.META.get("REMOTE_ADDR")
    except:
        ipAdd = ""
    return ipAdd

def set_unique_id():
    unique_id = str(uuid.uuid4())[:15].replace('-', '').upper()
    try:#if id exists
        id_taken = Profile.objects.get(unique_id=unique_id)
        set_unique_id()
    except: #if id doesnt exist make one
        return unique_id

def profile_page(request, unique_id): #set uniqueid as link
    #custom_url = "http://website.com/%s" %()
    context = {"unique_id": unique_id}
   # context2 = {"first_name": first_name}
    template = "profile.html"
    return render(request, template, context)

def about(request): #set uniqueid as link
    context = {}
    template = "about.html"
    return render(request, template, content)


def home(request):
    try:
        profile_id = request.session['profile_id_ref']
        obj = Profile.objects.get(id = profile_id)
        print "The obj is %s" %(obj.email)
    except:
        obj = None
    

    
    #Using regular forms:
    #print request.POST.get('first_name', False), request.POST.get('last_name', False), request.POST.get('email', False)
    #form = ProfileForm(request.POST or None)
    #if form.is_valid():
    #    fname = form.cleaned_data['first_name'],
    #    lname = form.cleaned_data['last_name'],
    #    email = form.cleaned_data['email'] #collecting first name last name and email
    #    new_profile, created = Profile.objects.get_or_create(first_name=fname)
    
    #using modal forms:
    form = ProfileForm2(request.POST or None)
    if form.is_valid():
        new_profile = form.save(commit=False)
        email = form.cleaned_data['email'] 
        chk_profile, created = Profile.objects.get_or_create(email=email)
        if created:
            chk_profile.unique_id = set_unique_id()
            chk_profile.ip_address = scan_ip(request)
            chk_profile.save()
        return HttpResponseRedirect("/%s" %(chk_profile.unique_id))
            
            
        #new_profile.ip_address = scan_ip(request)
        #new_profile.save()
    context = {"form": form}
    template = "home.html"
    return render(request, template, context)



