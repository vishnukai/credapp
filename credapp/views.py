from django.shortcuts import render,redirect
from .models import productdetails
# Create your views here.
def addprod(request):
    return render(request,'product.html')

def displayproduct(request):
    if request.method=='POST':
        pname=request.POST['pname']
        desc=request.POST['desc']
        qty=request.POST['qty']
        price=request.POST['price']

        product=productdetails(pname=pname,desc=desc,qty=qty,price=price)
        product.save()
        return redirect('showproduct')

def showproduct(request):
    products=productdetails.objects.all()
    return render(request,'showproduct.html',{'products':products})

def editpage(request,pk):
    product=productdetails.objects.get(id=pk)
    return render(request,'editpage.html',{'product':product})

def epdetails(request,pk):
    if request.method=='POST':
        product=productdetails.objects.get(id=pk)
        product.pname =request.POST.get('pname')
        product.desc = request.POST.get('desc')
        product.qty = request.POST.get('qty')
        product.price = request.POST.get('price')
        product.save()
        return redirect('showproduct')
    return render(request,'editpage.html')


def deletepage(request,pk):
    product=productdetails.objects.get(id=pk)
    return  render(request,'delete.html',{'product':product})

def deleteproduct(request,pk):
    product=productdetails.objects.get(id=pk)
    product.delete()
    return redirect('showproduct')