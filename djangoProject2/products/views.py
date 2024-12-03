from django.shortcuts import render,redirect, get_object_or_404
from .models import CPU,MOBO,CPUCooler,RAM,Storage,GPU,PSU,CASE
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem, Order, OrderItem


@login_required
def order_list(request):
    orders = request.user.orders.all()
    return render(request, "order_list.html", {"orders": orders})

@login_required
def add_to_cart(request, product_type, product_id):
    product_model = {
        "CPU": CPU,
        "GPU": GPU,
        "RAM": RAM,
        "Storage": Storage,
        "PSU": PSU,
        "CASE": CASE,
        "MOBO": MOBO,
        "CPUCooler": CPUCooler,
    }.get(product_type)

    if not product_model:
        messages.error(request, "Invalid product type!")
        return redirect("home")

    product = get_object_or_404(product_model, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product_type=product_type,
        product_id=product_id,
        defaults={"price": product.price, "quantity": 1},
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} added to your cart.")
    return redirect("cart_view")

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.total_price for item in cart_items)
    return render(request, "cart.html", {"cart_items": cart_items, "total_amount": total_amount})

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect("cart_view")

@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        messages.error(request, "Your cart is empty!")
        return redirect("cart_view")

    total_amount = sum(item.total_price for item in cart_items)
    order = Order.objects.create(user=request.user, total_amount=total_amount)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product_type=item.product_type,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
        )
        item.delete()

    messages.success(request, f"Order #{order.id} placed successfully!")
    return redirect("order_details", order_id=order.id)

@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "order_details.html", {"order": order})

def cpu(request):
    cpu= CPU.objects.all()
    return render(request,'products/cpu.html',{'cpu':cpu})

def mobo(request):
    mobo= MOBO.objects.all()
    return render(request,'products/mobo.html',{'mobo':mobo})

def cpucooler(request):
    cpucooler= CPUCooler.objects.all()
    return render(request,'products/cpucooler.html',{'cpucooler':cpucooler})

def ram(request):
    ram= RAM.objects.all()
    return render(request,'products/ram.html',{'ram':ram})

def storage(request):
    storage= Storage.objects.all()
    return render(request,'products/storage.html',{'storage':storage})

def gpu(request):
    gpu= GPU.objects.all()
    return render(request,'products/gpu.html',{'gpu':gpu})

def case(request):
    case= CASE.objects.all()
    return render(request,'products/case.html',{'case':case})

def psu(request):
    psu= PSU.objects.all()
    return render(request,'products/psu.html',{'psu':psu})


def cpu_detail(request, cpu_id):
    cpu = get_object_or_404(CPU, id=cpu_id)
    return render(request, 'products/details.html', {'object': cpu})

def mobo_detail(request, mobo_id):
    mobo = get_object_or_404(MOBO, id=mobo_id)
    return render(request, 'products/details.html', {'object': mobo})

def cpu_cooler_detail(request, cooler_id):
    cooler = get_object_or_404(CPUCooler, id=cooler_id)
    return render(request, 'products/details.html', {'object': cooler})

def ram_detail(request, ram_id):
    ram = get_object_or_404(RAM, id=ram_id)
    return render(request, 'products/details.html', {'object': ram})

def storage_detail(request, storage_id):
    storage = get_object_or_404(Storage, id=storage_id)
    return render(request, 'products/details.html', {'object': storage})

def gpu_detail(request, gpu_id):
    gpu = get_object_or_404(GPU, id=gpu_id)
    return render(request, 'products/details.html', {'object': gpu})

def psu_detail(request, psu_id):
    psu = get_object_or_404(PSU, id=psu_id)
    return render(request, 'products/details.html', {'object': psu})

def case_detail(request, case_id):
    case = get_object_or_404(CASE, id=case_id)
    return render(request, 'products/details.html', {'object': case})