from django.shortcuts import render
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . models import Profile,Client,Testimonial,JobApplication,Blog,Career,Package,PortfolioItem
from django.http import JsonResponse
from datetime import datetime
import pandas as pd
from django.http import HttpResponse
import os
import zipfile
from django.conf import settings
import re
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def is_ajax(request):
	return request.headers.get('x-requested-with') == 'XMLHttpRequest'   

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')  # Replace 'home' with the name of your dashboard view URL
		else:
			error_message = "Invalid username or password. Please try again."
			return render(request, 'login.html', {'error_message': error_message})
	return render(request, 'login.html')



def dashboard(request):
	c=Client.objects.all()
	context = {
		'name': 'V Kalyan Ram Kalipatnapu',
		'dsg': 'Sr. Developer',
		'c':c
	}
	return render(request, 'dashboard.html', context)

def home(request):
	
	return render(request, 'home.html')

def contactus(request):
	
	return render(request, 'contactus.html')	

def application(request):
	
	context = {
		'name': 'V Kalyan Ram Kalipatnapu',
		'dsg': 'Sr. Developer'
		
	}
	return render(request, 'application.html', context)	

def blogs(request):
	context = {
		'name': 'V Kalyan Ram Kalipatnapu',
		'dsg': 'Sr. Developer'
	}
	return render(request, 'blogs.html', context)

def careers(request):
	context = {
		'name': 'V Kalyan Ram Kalipatnapu',
		'dsg': 'Sr. Developer'
	}
	return render(request, 'careers.html', context)

def clients(request):
	context = {
		'name': 'V Kalyan Ram Kalipatnapu',
		'dsg': 'Sr. Developer'
	}
	return render(request, 'clients.html', context)

def our_portfolio(request):
	context = {
		'name': 'V Kalyan Ram Kalipatnapu',
		'dsg': 'Sr. Developer'
	}
	return render(request, 'our-portfolio.html', context)

def pricing_packages(request):
	context = {
		'name': 'V Kalyan Ram Kalipatnapu',
		'dsg': 'Sr. Developer'
	}
	return render(request, 'pricing-packages.html', context)

def testimonials(request):
	context = {
		'name': 'V Kalyan Ram Kalipatnapu',
		'dsg': 'Sr. Developer'
	}
	return render(request, 'testimonials.html', context)


def all(request):
	c=Client.objects.all()
	t=Testimonial.objects.all()
	context = {
		'name': 'V Kalyan Ram Kalipatnapu',
		'dsg': 'Sr. Developer',
		'c':c,
		't':t
	}
	return render(request, 'all.html', context)	

def is_ajax(request):
	return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def add_client(request):
	if request.method == 'POST':
		if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			client_img = request.FILES.get('client_img')
			client_name = request.POST.get('client_name')
			on_board_date = datetime.now().date()  # Current date
			price = '1500'

			# Create a new Client object
			new_client = Client(name=client_name, logo=client_img, status='On Boarded',price=price,on_board_date=on_board_date)
			new_client.save()
		
			message = f"Hi Admin {new_client.name.capitalize()} Client Added"
		
			return JsonResponse({'status': 'success', 'data': message})
		else:
			return JsonResponse({'status': 'error'})
	else:
		return JsonResponse({'status': 'error'})


def add_testimonial(request):
	if request.method == 'POST':
		if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			img = request.FILES.get('img')
			name = request.POST.get('name')
			description=request.POST.get('description')
			designation=request.POST.get('designation')
			
			# Create a new Client object
			new_testimonial = Testimonial(name=name, image=img, designation=designation,description=description)
			new_testimonial.save()
		
			message = f"Hi Admin new testimonial was added by {new_testimonial.name.capitalize()} "
		
			return JsonResponse({'status': 'success', 'data': message})
		else:
			return JsonResponse({'status': 'error'})
	else:
		return JsonResponse({'status': 'error'})



def submit_application(request):
	if request.method == 'POST':
		if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			cv = request.FILES.get('cv')
			name = request.POST.get('name')
			email=request.POST.get('email')
			title=request.POST.get('title')
			phonenumber=request.POST.get('phonenumber')
			
			# Create a new Client object
			new_application = JobApplication(full_name=name,title=title, email=email, phone_number=phonenumber,resume=cv)
			new_application.save()
		
			message = f"Hi {name.capitalize()} your application submitted successfully !! "
		
			return JsonResponse({'status': 'success', 'data': message})
		else:
			return JsonResponse({'status': 'error'})
	else:
		return JsonResponse({'status': 'error'})




	

def export_to_excel():
	job_applications = JobApplication.objects.all()
	
	data = {
		'Full Name': [app.full_name for app in job_applications],
		'Title': [app.title for app in job_applications],
		'Email': [app.email for app in job_applications],
		'Phone Number': [app.phone_number for app in job_applications],
		# Add other fields as needed
	}
	
	df = pd.DataFrame(data)
	excel_path = os.path.join(settings.MEDIA_ROOT, 'export', 'job_applications.xlsx')
	df.to_excel(excel_path, index=False)
	
	return excel_path

def create_zip_file():
    job_applications = JobApplication.objects.all()
    zip_filename = 'resumes.zip'
    zip_path = os.path.join(settings.MEDIA_ROOT, 'export', zip_filename)
    
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for app in job_applications:
            resume_path = os.path.join(settings.MEDIA_ROOT, str(app.resume))
            
            # Extract the file extension
            file_extension = os.path.splitext(app.resume.name)[1]
            
            custom_filename = f"{app.id}-{app.full_name}_{app.phone_number}{file_extension}"
            zipf.write(resume_path, os.path.join('resumes', custom_filename))
            
    return zip_path



def export(request):
    zip_file_path = create_zip_file()  # Generate ZIP file
    excel_file_path = export_to_excel()  # Generate Excel file

    zip_filename = os.path.basename(zip_file_path)
    excel_filename = os.path.basename(excel_file_path)

    # Define URLs for download
    zip_download_url = os.path.join(settings.MEDIA_URL, 'export', zip_filename)
    excel_download_url = os.path.join(settings.MEDIA_URL, 'export', excel_filename)

    context = {
        'excel_download_url': excel_download_url,
        'zip_download_url': zip_download_url,
    }

    return render(request, 'export_success.html', context)



@require_POST
def add_portfolio(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        img = request.FILES.get('img')
        name = request.POST.get('name')
        
        # Create a new PortfolioItem object
        new_portfolio_item = PortfolioItem(name=name, featured_image=img)
        new_portfolio_item.save()
        
        message = f"New portfolio item '{new_portfolio_item.name}' was added."
        
        return JsonResponse({'status': 'success', 'data': message})
    else:
        return JsonResponse({'status': 'error'})





def add_blog(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        blog_title = request.POST.get('blog_title')
        author = request.POST.get('author')
        date = request.POST.get('date')
        featured_image = request.FILES.get('featured_image')
        
        description = request.POST.get('description')
        
        # Create a new Blog object
        new_blog = Blog(
            blog_title=blog_title,
            author=author,
            date=date,
            featured_image=featured_image,
            description=description
        )
        new_blog.save()
        
        message = f"New blog '{new_blog.blog_title}' was added."
        
        return JsonResponse({'status': 'success', 'data': message})
    else:
        return JsonResponse({'status': 'error'})
    


def add_career(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        job_title = request.POST.get('job_title')
        employee_type = request.POST.get('employee_type')
        job_location = request.POST.get('job_location')
        required_qualification = request.POST.get('required_qualification')
        required_experience = request.POST.get('required_experience')
        salary = request.POST.get('salary')
        skills = request.POST.get('skills')
        job_description = request.POST.get('job_description')
        roles_responsibilities = request.POST.get('roles_responsibilities')
        
        # Create a new Career object
        new_career = Career(
            job_title=job_title,
            employee_type=employee_type,
            job_location=job_location,
            required_qualification=required_qualification,
            required_experience=required_experience,
            salary=salary,
            skills=skills,
            job_description=job_description,
            roles_responsibilities=roles_responsibilities
        )
        new_career.save()
        
        message = f"New career opportunity '{new_career.job_title}' was added."
        
        return JsonResponse({'status': 'success', 'data': message})
    else:
        return JsonResponse({'status': 'error'})



@require_POST
def add_package(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        package_name = request.POST.get('package_name')
        package_type = request.POST.get('package_type')
        price = request.POST.get('price')
        package_details = request.POST.get('package_details')
        
        # Create a new Career object for the package
        new_package = Package(
            package_name=package_name,
            package_type=package_type,
            price=price,
            package_details=package_details
        )
        new_package.save()
        
        message = f"New package '{new_package.package_name}' was added."
        
        return JsonResponse({'status': 'success', 'data': message})
    else:
        return JsonResponse({'status': 'error'})
