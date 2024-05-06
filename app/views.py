from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Product, Shipping
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    shippings = Shipping.objects.all()
    return render(request, 'home.html', {'customers': customers, 'products': products, 'shippings': shippings})

from django.contrib.auth import logout
from django.shortcuts import redirect
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login page

# def dashboard(request):
#     customers = Customer.objects.all()
#     customer_list_html = [f'<li>{Customer.name}']
#     return HttpResponse(f"<ul>{''.join(customer_list_html)}</ul>")



def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')
        Customer.objects.create(name=name, email=email, mobile_number=mobile, city=city)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        Product.objects.create(name=name, quantity=quantity, price=price)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


def add_shipping(request):
    if request.method == 'POST':
        recipient_name = request.POST.get('recipient_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postal_code = request.POST.get('postal_code')
        Shipping.objects.create(recipient_name=recipient_name, address=address, city=city, country=country, postal_code=postal_code)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

