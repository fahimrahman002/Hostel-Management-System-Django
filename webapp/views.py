import imp
from turtle import title
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from webapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# For email validation
from django.forms import EmailField
from django.core.exceptions import ValidationError
# For django-cleanup
from django.apps import apps
apps.get_models()


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'login.html')

    def post(self, request):
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(username=email, password=password)
            member = Member.objects.filter(user=user).first()

            if member is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                messages.error(request, "User is not valid.")
                return redirect('login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('login')


class SignUp(View):
    def isEmailValid(self, email):
        try:
            EmailField().clean(email)
            return True
        except ValidationError:
            return False

    def validateUserInput(self, email, password, confirm_password):
        if password != confirm_password:
            return "Confirm Password is not matching."
        elif len(password) < 6:
            return "Password must be at lease 6 charecters long"
        elif self.isEmailValid(email) == False:
            return "Please enter a valid email."
        return None

    def get(self, request):

        context = {

        }
        return render(request, 'register.html', context)

    def post(self, request):
        try:
            hostel_title = request.POST['hostel_title']
            full_name = request.POST['full_name']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            check_user_input = self.validateUserInput(
                email, password, confirm_password)

            if check_user_input != None:
                messages.error(request, check_user_input)
                return render(request, 'register.html')

            if User.objects.filter(email=email).first():
                messages.error(request, 'Email already exists.')
                return render(request, 'register.html')

            new_hostel = Hostel(title=hostel_title)
            new_hostel.save()

            new_user = User.objects.create_user(
                username=email, email=email, first_name=full_name, password=password)
            new_user.save()

            new_member = Member(
                user=new_user,
                hostel=new_hostel,
                admin_privilege=True,
            )
            new_member.save()

            messages.success(
                request, 'Account is created with new hostel')
        except Exception as e:
            print(e)
            if type(e).__name__ == "IntegrityError":
                messages.error(
                    request, "Account already exists with the email.")
            else:
                messages.error(request, "Something went wrong")
            return render(request, 'register.html')

        return redirect('login')


@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    def get(self, request):
        context = {

        }
        return render(request, 'dashboard.html', context)

    def post(self, request):
        if 'bazar_details_save' in request.POST:
            date=request.POST['bazar_date']
            details=request.POST['bazar_details']
            expense=request.POST['bazar_expense']
            
            # bazar_detail=BazarDetail.objects.filter()
            
        context = {

        }
        return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def profile(request):
    context = {
    }

    return render(request, 'profile.html', context)


def settings(request):
    context = {
    }

    return render(request, 'settings.html', context)


def manage_members(request):
    context = {
    }

    return render(request, 'manage-members.html', context)


def monthly_accounting(request):
    context = {
    }

    return render(request, 'monthly-accounting.html', context)

def all_investments(request):
    context = {
    }

    return render(request, 'all-investmens.html', context)


def my_investments(request):
    context = {
    }

    return render(request, 'my-investments.html', context)



def all_bazar_details(request):
    context = {
    }

    return render(request, 'all-bazar-details.html', context)


def my_bazar_details(request):
    context = {
    }

    return render(request, 'my-bazar-details.html', context)


def my_meal_records(request):
    context = {
    }

    return render(request, 'my-meal-records.html', context)
