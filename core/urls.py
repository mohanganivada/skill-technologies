from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('',views.home,name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('contactus/', views.contactus, name='contactus'),
    path('login/', views.login, name='login'),
    path('careers/', views.careers, name='careers'),
    path('clients/', views.clients, name='clients'),
    path('ourportfolio/', views.our_portfolio, name='our_portfolio'),
    path('pricepackage/', views.pricing_packages, name='pricing_packages'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('add_client/', views.add_client, name='add_client'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
    path('all/', views.all, name='all'),
    path('application/', views.application, name='application'),
    path('submit_application/', views.submit_application, name='submit_application'),
    path('export/', views.export, name='export'),
    path('add_portfolio/', views.add_portfolio, name='add_portfolio'),
    path('add_career/', views.add_career, name='add_career'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('add_package/', views.add_package, name='add_package')

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)