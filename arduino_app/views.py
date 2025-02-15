from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from .models import ProgrammingLanguage, Update
import json
import os
from django.http import JsonResponse
from django.templatetags.static import static  # Import static here
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth import logout
from django.core.mail import send_mail
from .forms import SendEmailForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage



def home(request):
    return render(request, 'home.html', {'user': request.user})

def language_detail(request, language_name):
    language = get_object_or_404(ProgrammingLanguage, name=language_name)
    return render(request, 'language_detail.html', {'language': language})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'home.html', {
                'modal': 'login',
                'error_message': 'Invalid username or password.'
            })

# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'home.html', {
                'modal': 'register',
                'error_message': 'Passwords do not match.'
            })

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'home.html', {
                'modal': 'register',
                'error_message': 'Username already taken.'
            })

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'home.html', {
                'modal': 'register',
                'error_message': 'Email already registered.'
            })

        # Create the new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        """
        # Send a welcome email
        send_mail(
            'Welcome to GEINOTECH!',
            'Thank you for registering with us. We are excited to have you onboard!',
            'from@example.com',  # Replace with your sender's email address
            [user.email],  # The email address of the user
            fail_silently=False,  # This will raise an error if the email fails to send
        )
        """
        # Display success message and redirect
        messages.success(request, 'Registration successful.')
        return redirect('main')  # Replace 'main' with the appropriate view name if needed



def logout_user(request):
    logout(request)  # This logs out the user
    return redirect('main')

def prolan(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'prolan.html', {'languages': languages})

def privacy_policy(request):
    return render(request, 'privacy policy.html')

def update(request):
    updates = Update.objects.all()  # Fetch all updates from the database
    return render(request, "update.html", {"updates": updates}) 



def python_programming(request, language_name):
    try:
        # Determine which JSON file to load
        if 'LED' in language_name:
            file_name = 'ard_LED.json'
            template_name = 'ard_LED.html'  # Render the LED template
        elif 'LCD ' in language_name:
            file_name = 'ard_LCD.json'
            template_name = 'ard_LCD2.html'  # Render the LCD template
        elif 'Buzzers' in language_name:
            file_name = 'ard_Buzzers.json'
            template_name = 'ard_Buzzers.html'  # Render the LCD template
        elif 'Servo motors' in language_name:
            file_name = 'ard_servomotor.json'
            template_name = 'ard_servomotor.html'  # Render the LCD template
        elif 'DC Motor' in language_name:
            file_name = 'ard_dcmotor.json'
            template_name = 'ard_dcmotor.html'  # Render the LCD template
        elif '7 segment' in language_name:
            file_name = 'ard_7 segment.json'
            template_name = 'ard_7 segment.html'  # Render the LCD template
        elif 'RGB Led' in language_name:
            file_name = 'ard_rgb led.json'
            template_name = 'ard_rgb led.html'  # Render the LCD template
        elif 'Buttons' in language_name:
            file_name = 'ard_buttons.json'
            template_name = 'ard_buttons.html'  # Render the LCD template
        elif '8x8 Led' in language_name:
            file_name = 'ard_8x8 Led.json'
            template_name = 'ard_8x8 Led.html'  # Render the LCD template
        elif 'Water Sensor' in language_name:
            file_name = 'ard_watersensor.json'
            template_name = 'ard_watersensor.html'  # Render the LCD template
        elif 'Temp and Hum sensor' in language_name:
            file_name = 'ard_temphum.json'
            template_name = 'ard_temphum.html'  # Render the LCD template


        else:
            return JsonResponse({"error": "Language not Found"}, status=404)

        # Construct the file path
        file_path = os.path.join(settings.BASE_DIR, 'static', 'data', file_name)
        print(f"File path: {file_path}")  # Debugging

        # Read the JSON file
        with open(file_path, 'r') as json_file:
            content = json.load(json_file)

        # Render the correct template
        return render(request, template_name, {'language_name': language_name, 'content': content})

    except FileNotFoundError:
        return JsonResponse({"error": f"Content for {language_name} not found."}, status=404)
    


def send_bulk_email_view(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Get all registered users' email addresses
            users = User.objects.all()
            email_addresses = [user.email for user in users if user.email]

            # Modify the sender name to be in uppercase
            from_email = f"{settings.EMAIL_SENDER_NAME} <{settings.EMAIL_HOST_USER}>"

            # Create an email message object
            email = EmailMessage(
                subject,
                message,
                from_email,
                [],  # Empty To field as we're using BCC
                bcc=email_addresses,  # Add BCC recipients here
            )

            # Send the email
            email.send(fail_silently=False)

            return render(request, 'email_sent_success.html', {'subject': subject})

    else:
        form = SendEmailForm()

    return render(request, 'send_email_form.html', {'form': form})


    
def tech_updates(request, update_name):
      return render(request, 'update.html', {'update_name': update_name})    

"""
file_name = "user_data.json"
file_path = os.path.join(settings.BASE_DIR, 'static', 'data', file_name)
print(file_path)

from django.http import JsonResponse
import os
import json
from django.conf import settings

def load_config(request):
    try:
        file_name = "config.json"
        file_path = os.path.join(settings.BASE_DIR, 'static', 'conf', file_name)
        with open(file_path, 'r') as json_file:
            config_data = json.load(json_file)
        return JsonResponse(config_data)
    except FileNotFoundError:
        return JsonResponse({'error':'File not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid json format in configuration file'}, status=404)
    
    
def save_user_preferences(request):
     user_preferences = {"theme": "light", "notifications": True}
     file_name = "preferences"
     file_path = os.path.join(settings.BASE_DIR, 'static', 'data', file_name)
     with open(file_path, 'w') as json_file:
         json.dump(user_preferences, json_file, indent=4)

save_user_preferences()

from django.shortcuts import render
from django.http import JsonResponse
import os
import json

def load_content(request):
    try:
        tutorial_name = "HELLO"
        file_path = os.path.join(settings.BASE_DIR, 'static', 'tutorials' f"{tutorial_name}.json")
        with open(file_path, 'r') as json_file:
            tutorial_content = json.load(json_file)
        
        return render(request, 'tutorial.html', {'content': tutorial_content})
    except FileNotFoundError:
        return JsonResponse({'error':'File not found'}, status=404)
    
def load_data(request):
    file_name = request.GET.get('file', '') + '.json'
    format_type = request.GET.get('format', 'json') 

    try:
        file_path = os.path.join(settings.BASE_DIR, 'static', 'data', file_name)
        with open(file_path, "r") as json_file:
            tutorial_content = json.load(json_file)
        
        if format_type == 'html':
            return render(request, 'tutorial.html', {'content': tutorial_content})
        return JsonResponse(tutorial_content)
    
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=404)
    
"""