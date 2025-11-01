from django.shortcuts import render
from .models import Service, Gallery, Testimonial
from datetime import datetime
def home(request):
    # Fetch limited data for homepage
    services = Service.objects.all()[:3]        # Only 3 services
    gallery_items = Gallery.objects.all()[:4]   # Only 4 gallery images
    testimonials = Testimonial.objects.all()[:3] # Only 3 testimonials

    context = {
        'services': services,
        'gallery_items': gallery_items,
        'testimonials': testimonials,
        'year': datetime.now().year
    }
    return render(request, 'home.html', context)


def gallery(request):
    gallery_items = Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery_items': gallery_items, 'year': datetime.now().year})

# Frontend page
def services_frontend(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services, 'year': datetime.now().year})




def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials, 'year': datetime.now().year})

def contact(request):
    return render(request, 'contact.html', {'year': datetime.now().year})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_login.html')


@login_required(login_url='admin_login')
def dashboard(request):
    return render(request, 'dashboard.html')


def admin_logout(request):
    logout(request)
    return redirect('admin_login')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service

@login_required(login_url='admin_login')
def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

@login_required(login_url='admin_login')
def service_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES.get('image')
        Service.objects.create(title=title, description=description, image=image)
        return redirect('service_list')
    return render(request, 'service_form.html', {'action': 'Add'})

@login_required(login_url='admin_login')
def service_edit(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        service.title = request.POST['title']
        service.description = request.POST['description']
        if request.FILES.get('image'):
            service.image = request.FILES['image']
        service.save()
        return redirect('service_list')
    return render(request, 'service_form.html', {'service': service, 'action': 'Edit'})

@login_required(login_url='admin_login')
def service_delete(request, id):
    service = get_object_or_404(Service, id=id)
    service.delete()
    return redirect('service_list')


from .models import Gallery
from django.shortcuts import get_object_or_404

@login_required(login_url='admin_login')
def gallery_list(request):
    items = Gallery.objects.all()
    return render(request, 'gallery_list.html', {'items': items})

@login_required(login_url='admin_login')
def gallery_add(request):
    if request.method == 'POST':
        description = request.POST['description']
        image = request.FILES.get('image')
        Gallery.objects.create(description=description, image=image)
        return redirect('gallery_list')
    return render(request, 'gallery_form.html', {'action': 'Add'})

@login_required(login_url='admin_login')
def gallery_edit(request, id):
    item = get_object_or_404(Gallery, id=id)
    if request.method == 'POST':
        item.description = request.POST['description']
        if request.FILES.get('image'):
            item.image = request.FILES['image']
        item.save()
        return redirect('gallery_list')
    return render(request, 'gallery_form.html', {'item': item, 'action': 'Edit'})

@login_required(login_url='admin_login')
def gallery_delete(request, id):
    item = get_object_or_404(Gallery, id=id)
    item.delete()
    return redirect('gallery_list')

from .models import Testimonial

@login_required(login_url='admin_login')
def testimonial_list(request):
    items = Testimonial.objects.all()
    return render(request, 'testimonial_list.html', {'items': items})

@login_required(login_url='admin_login')
def testimonial_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        photo = request.FILES.get('photo')
        Testimonial.objects.create(name=name, message=message, photo=photo)
        return redirect('testimonial_list')
    return render(request, 'testimonial_form.html', {'action': 'Add'})

@login_required(login_url='admin_login')
def testimonial_edit(request, id):
    item = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.message = request.POST['message']
        if request.FILES.get('photo'):
            item.photo = request.FILES['photo']
        item.save()
        return redirect('testimonial_list')
    return render(request, 'testimonial_form.html', {'item': item, 'action': 'Edit'})

@login_required(login_url='admin_login')
def testimonial_delete(request, id):
    item = get_object_or_404(Testimonial, id=id)
    item.delete()
    return redirect('testimonial_list')


from django.shortcuts import render, redirect
from .models import Contact
from datetime import datetime

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        Contact.objects.create(name=name, email=email, message=message)
        success = "Your message has been sent successfully!"
        return render(request, "contact.html", {'success': success, 'year': datetime.now().year})

    return render(request, "contact.html", {'year': datetime.now().year})

from .models import Contact
from django.contrib.auth.decorators import login_required

@login_required(login_url='admin_login')
def contact_list(request):
    messages = Contact.objects.all().order_by('-created_at')
    return render(request, 'contact_list.html', {'messages': messages})

from django.contrib.auth import logout
from django.shortcuts import redirect

def admin_logout(request):
    logout(request)
    return redirect('home')  # redirect to your login page

