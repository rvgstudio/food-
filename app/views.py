from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Product,Address,Contact
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages 
# Create your views here.

def index(request):

    return render(request, 'index.html')

def login(request):
    return render(request,"login.html")

@login_required
def product_view(request):
    products = Product.objects.all().order_by('?')
    paginator = Paginator(products, 8)  # Show 25 contacts per page.

    page_list = request.GET.get("page")
    page_obj = paginator.get_page(page_list)
    context = {
        'products' : products,
        'page_obj' : page_obj,
    }
    return render(request,"Product.html",context)

@login_required
def single_product(request,id):
    singleproduct = Product.objects.filter(id = id).first()
    details = {
        'prod' : singleproduct,
    }
    return render(request,"single_product.html",details)


@login_required
def about(request):
    return render(request,"about.html")

@login_required
def services(request):
    return render(request,"services.html")

@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact = Contact(Name=name, Email=email, Phone=phone, Subject=subject,Message=message)
        contact.save()
       
        messages.success(request,"Successfully Contacted")
        return redirect("contactus")
    return render(request,"contactus.html")

@login_required
def address(request):
    if request.method == "POST":
        addresstype = request.POST.get("addresstype")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        house = request.POST.get("house")
        society = request.POST.get("society")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zip")

        address1 = Address(user=request.user,Address_type = addresstype,Name=name,Phone=phone,Apartment=house,Society=society,City=city,State=state,Zip=zipcode)

        address1.save()
        return redirect("address")

    if request.user.is_authenticated:
        show = Address.objects.filter(user=request.user)
        context = {
            "show" : show,
        }
    return render(request,"address.html",context)

def test(request):
    return render(request,'test.html')



# cart code

@login_required
def cart_add(request, id):
    cart = Cart(request)
    print("done")
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required






































































def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
