from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    
    
# Frontend Services page
path('services/', views.services_frontend, name='services_frontend'),

# Admin Services CRUD
path('services-admin/', views.service_list, name='service_list'),   # admin dashboard
path('services-admin/add/', views.service_add, name='service_add'),
path('services-admin/edit/<int:id>/', views.service_edit, name='service_edit'),
path('services-admin/delete/<int:id>/', views.service_delete, name='service_delete'),


    # Gallery, Testimonials, Contact
    path('gallery/', views.gallery, name='gallery'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('contacts/', views.contact_list, name='contact_list'),


    # Admin login
    path('admin-login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.admin_logout, name='admin_logout'),
    
    # Gallery CRUD
path('gallery-admin/', views.gallery_list, name='gallery_list'),
path('gallery-admin/add/', views.gallery_add, name='gallery_add'),
path('gallery-admin/edit/<int:id>/', views.gallery_edit, name='gallery_edit'),
path('gallery-admin/delete/<int:id>/', views.gallery_delete, name='gallery_delete'),

# Testimonials CRUD
path('testimonials-admin/', views.testimonial_list, name='testimonial_list'),
path('testimonials-admin/add/', views.testimonial_add, name='testimonial_add'),
path('testimonials-admin/edit/<int:id>/', views.testimonial_edit, name='testimonial_edit'),
path('testimonials-admin/delete/<int:id>/', views.testimonial_delete, name='testimonial_delete'),

path('logout/', views.admin_logout, name='logout'),



]
