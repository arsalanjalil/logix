
from django.shortcuts import render
from .models import Service,Order,Product
from .forms import OrderValidaionForm
from django.http import HttpResponse
# Create your views here.


def show_service(request,id):
    products = Product.objects.filter(service_id=id)
    services = Service.objects.filter(id=id)
    context = {'service':services[0],'products':products}
    return render(request,'service/service.html',context)


def detail_service(request,id):
    services = Service.objects.filter(id=id)
    context = {'services': services, }
    return render(request, 'service/detail_service.html', context)


def detail_product(request,id):
    products = Product.objects.filter(id=id)
    context = {'products': products, }
    return render(request, 'service/detail_product.html', context)


def order(request ,id):
    service = Service.objects.get(id=id)
    # return HttpResponse(service.id)
    if request.method == "POST":
        form = OrderValidaionForm(request.POST)
        order = Order()
        if form.is_valid():
            order.file = request.POST['file']
            order.created_at = request.POST['create_at']
            order.state = request.POST['state']
            order.service = Service.objects.get(id=id)

            order.save()

        else:

            return render(request, 'service/detail_service.html', {'form': form ,'services':Service.objects.filter(id=id)})

        return render(request, 'service/detail_service.html', {'message': {'text': "Your request has been successfully registered"}, 'order': order})
    else:

        return render(request, 'service/detail_service.html', {'form': OrderValidaionForm(request.POST).errors,
                                'message': {'text': "لطفا خطا های زیر را برطرف کنید."}})
