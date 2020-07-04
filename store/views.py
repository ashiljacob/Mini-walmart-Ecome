from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Item,BillItem
from datetime import datetime
from django.http import HttpResponse
from django.db.models import Sum,F,FloatField


# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Item

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name','price','quantityofproduct','quantityAvailable','category']

def delete(request,id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect("/")

def edit(request,id):
    item = Item.objects.get(id=id)

    print(item)
    return render(request,'edit.html',{'item':item})

def save_item(request,id):

    if request.method == "POST":

        i = Item.objects.get(pk=id)

        

        
        i.name=request.POST['title']
        i.price=float(request.POST['price'])
        i.quantityofproduct=request.POST['quantityofproduct']
        i.quantityAvailable=request.POST['quantityAvailable']
        i.category=request.POST['category']
        i.UpdatedDate = datetime.now()
        i.save()
    return redirect("/")
   
def add(request): 
    
    return render(request,'create.html')

def add_item(request):
    if request.method == "POST":
        item = Item(name=request.POST['title'],
                price=float(request.POST['price']),quantityofproduct=request.POST['quantityofproduct'],
                quantityAvailable=request.POST['quantityAvailable'],
                category=request.POST['category'])
        item.save()
        return redirect("/")
    else:
        return HttpResponse("Something Went Wrong")

def bill_page(request):
    
    item= BillItem.objects.all() 
    # Getting Total of Order########
    # total = 0
    # for i in item:
    #     total += i.price * i.quantity
    total = BillItem.objects.aggregate(p=Sum(F('price') * F('quantity'),output_field= FloatField()))
    
    return render(request,'bill.html',{'item':item,'total':total['p']})

def add_to_cart(request,id):
    if request.method == "POST":
        i = Item.objects.get(id=id)
        # # Decresing Available Items
        # i.quantityAvailable -=1
        # i.save()
        # # Creating bill of items
        if BillItem.objects.filter(item = i.name).exists():
            obj = BillItem.objects.get(item=i.name)
            obj.quantity +=1
            obj.save()
            
           
        else:
            BillItem.objects.create(item=i.name,quantity=1,price=i.price)

        return redirect("/")
    else:
        return HttpResponse("<h1>Error While Adding to Cart</h1>")
    
def delete_bill_item(request,id):
    item = BillItem.objects.get(id=id)
    item.delete()
    return redirect('bill')
