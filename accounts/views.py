from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm


# Create your views here.
def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    orders_delivered = Order.objects.filter(status='Delivered')
    total_orders_delivered = orders_delivered.count()

    orders_pending = Order.objects.filter(status='Pending')
    total_orders_pending= orders_pending.count()

    contex = {"orders": orders, 'customers': customers, 'total_orders': total_orders, 'total_customers':total_customers, 'total_orders_delivered':total_orders_delivered, 'total_orders_pending': total_orders_pending}
    return render(request, 'accounts/dashboard.html', contex)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {"products":products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()

    individul_orders = order.count() 

    context = {'customer': customer,'order': order, 'individul_orders': individul_orders}
    return render(request, 'accounts/customer.html', context)

def Create_order(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={"customer": customer})
    context = {'form': form}

    if request.method =='POST':
        # print("request post", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'accounts/order.html', context)

def update_form(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method=='POST':
        form = OrderForm(request.POST, instance=order)
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'accounts/order.html', context)

def delete_form(request, pk):
    order = Order.objects.get(id=pk)

    if request.method=='POST':
        order.delete()
        return redirect('home')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)