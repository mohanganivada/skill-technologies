from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
	phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_("Enter a valid international mobile phone number starting with +(country code)"))
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date_of_birth = models.DateField(verbose_name=_("Date of birth"), blank=True, null=True)
	gender = models.CharField(verbose_name=_("Gender"), max_length=10, choices=(("male", "Male"), ("female", "Female"), ("other", "Other")), blank=True, null=True)
	father_name = models.CharField(verbose_name=_("Father name"), max_length=30, help_text=_("Will be shown e.g. when commenting"))
	emergency_contact_name1=models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"))
	emergency_contact_relation1=models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"))
	passport_number= models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"))
	#present address
	address1 = models.CharField(verbose_name=_("Address line 1"), max_length=1024, blank=True, null=True)
	pin_code = models.CharField(verbose_name=_("Postal Code"), max_length=12, blank=True, null=True)
	city = models.CharField(verbose_name=_("City"), max_length=1024, blank=True, null=True)
	state = models.CharField(verbose_name=_("State"),max_length=6,blank=True, null=True)
	country = CountryField(blank=True, null=True,default="India",max_length=5)
	#permanant address
	address3 = models.CharField(verbose_name=_("Address line 1"), max_length=1024, blank=True, null=True)
	pin_code1 = models.CharField(verbose_name=_("Postal Code"), max_length=12, blank=True, null=True)
	city1 = models.CharField(verbose_name=_("City"), max_length=1024, blank=True, null=True)
	state1 = models.CharField(verbose_name=_("State"),  max_length=6,blank=True, null=True)
	mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17, blank=True, null=True)
	aadhar_no=models.CharField(max_length=12, default='000000000000')
	marital_status = models.BooleanField(default=False)
	pan_no =models.CharField(verbose_name=_("PAN"), max_length=10, help_text=_("Will be shown e.g. when commenting"))
	accountnumber = models.CharField(max_length=13, default='0000000000000')
	accounttype = models.CharField(max_length=13, default='abc')
	bank_name=models.CharField(verbose_name=_("Display name"), max_length=250, help_text=_("Will be shown e.g. when commenting"))
	ifsc_code=models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"))
	nationality=models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"),default='Indian')
	religion=models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"),default='NA')
		
	def __str__(self):
		return str(self.user)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        # Check if a profile already exists before creating a new one
        if not hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)


class Client(models.Model):
    client_id = models.AutoField(primary_key=True, verbose_name='Client ID', editable=False)
    # Name of the client
    name = models.CharField(max_length=100, verbose_name='Client')
    # Client logo (an image field)
    logo = models.ImageField(upload_to='client_logos/', blank=True, null=True, verbose_name='Logo')
    # On Board Date
    on_board_date = models.DateField(verbose_name='On Board Date')
    # Price (assuming a decimal field, you can change it to suit your requirements)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    # Choices for the status field
    STATUS_CHOICES = [
        ('On Boarded', 'On Boarded'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    # Default status will be 'on_boarded'
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='on_boarded', verbose_name='Status')

    def __str__(self):
        return f"{self.client_id} - {self.name}"            

class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True, verbose_name='Testimonial ID', editable=False)
    name = models.CharField(max_length=100, verbose_name='Name')
    designation = models.CharField(max_length=100, verbose_name='Designation')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='testimonials/', verbose_name='Image')

    def __str__(self):
        return f"{self.testimonial_id} - {self.name}"        




class JobApplication(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    resume = models.FileField(upload_to='applications/')
    # Other fields related to the job application

    def __str__(self):
        return self.full_name




class PortfolioItem(models.Model):
    portfolio_id = models.AutoField(primary_key=True, verbose_name='Portfolio ID', editable=False)
    name = models.CharField(max_length=100, verbose_name='Name')
    featured_image = models.ImageField(upload_to='ourportfolio/', verbose_name='Featured Image')

    def __str__(self):
        return f"{self.portfolio_id} - {self.name}"
    



class Blog(models.Model):
   
    blog_title = models.CharField(max_length=200, verbose_name='Blog Title')
    author = models.CharField(max_length=100, verbose_name='Author')
    date = models.TextField(verbose_name='Date')
    featured_image = models.ImageField(upload_to='blogs/', verbose_name='Featured Image')
    description = models.TextField(verbose_name='Job Description')

    def __str__(self):
        return self.blog_title



class Career(models.Model):
    JOB_TYPES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    )

    job_title = models.CharField(max_length=100, verbose_name='Job Title')
    employee_type = models.CharField(max_length=20, choices=JOB_TYPES, verbose_name='Employee Type')
    job_location = models.CharField(max_length=100, verbose_name='Job Location')
    required_qualification = models.CharField(max_length=200, verbose_name='Required Qualification')
    required_experience = models.CharField(max_length=50, verbose_name='Required Experience')
    salary = models.CharField(max_length=100, verbose_name='Salary')
    skills = models.CharField(max_length=200, verbose_name='Skills')
    job_description = models.TextField(verbose_name='Job Description')
    roles_responsibilities = models.TextField(verbose_name='Roles and Responsibilities')

    def __str__(self):
        return self.job_title
        



class Package(models.Model):
    PACKAGE_TYPES = (
        ('Free', 'Free'),
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    )

    package_name = models.CharField(max_length=100, verbose_name='Package Name')
    package_type = models.CharField(max_length=20, choices=PACKAGE_TYPES, verbose_name='Package Type')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    package_details = models.TextField(verbose_name='Package Details')

    def __str__(self):
        return self.package_name

