from django.shortcuts import  render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login as lin ,logout as lout
from .models import * 
from django.contrib.auth.models import User

                             
def home(request):
    if request.user.is_authenticated:
        name = request.user.username
        count = len(Cart.objects.filter(username = request.user.username))
        return render(request,"foodmenu.html",{"name":name,"len":count})
    else:
        return render(request,"foodmenu.html")
def contactus(request):
    return render(request,"contactus.html")
def logout(request):
    lout(request)
    return redirect('home')
def viewcart(request):
    obj = Cart.objects.filter(username = request.user.username)
    price = 0
    for i in obj:
       price+=float(i.price)
    print(len(obj))
    return render(request,'cart.html',{"detial":obj,"name":request.user.username,"price":price}) 

def remove(request,id):
    Cart.objects.get(id=id).delete()
    return redirect("view")   
    
def signup(request):
    if request.method=="POST":
        
        Name = request.POST["Username"]
        password = request.POST["Password"]
        Obj = Signup()
        Obj.username = Name
        Obj.password = password
        user = User.objects.create_user(username=Name,password=password)
        user.save()
        Obj.save()
        print(Name)
        print(password)
        user = authenticate(username = Name,password = password)
        lin(request,user)
        return redirect("home")
    else:
        return render(request,"signup.html")
    
def login(request):
        if request.method=="POST":
            Name = request.POST["Username"]
            password = request.POST["Password"]
            user = authenticate(username = Name,password = password)
            if user is not None:
                lin(request,user)
                count = len(Cart.objects.filter(username = request.user.username))
                return render(request,"foodmenu.html",{"name":Name,"len":count})
            else:
                return render(request,"login.html",{"msg":"invalid username or password"})
        else:
            return render(request,"login.html")   


def breakfast(request,food):
    context = {}
    if food == "breakfast":
        context['breakfasts']= Breakfast.objects.all()
        context["title"] = "BREAKFAST"
    if food == "combo":
        context['breakfasts'] = ComboOffer.objects.all()
        context["title"] = "COMBO OFFERS"
    if food == "dailyspecial":
        context['breakfasts']= DailySpecial.objects.all()
        context["title"] = "DIALY SPECIAL"
    if food == "lunch":
        context['breakfasts'] = Lunch.objects.all()
        context["title"] = "LUNCH"
    if food == "fastfood":
        context['breakfasts']= FastFood.objects.all()
        context["title"] = "FAST FOOD"
    if food == "chatitems":
        context['breakfasts'] = ChatItems.objects.all()
        context["title"] = "CHAT ITEMS"
    if food == "freshjuice":
        context['breakfasts']= FreshJuice.objects.all()
        context["title"] = "FRESH JUICE"
    
    if request.user.is_authenticated:
        count = len(Cart.objects.filter(username = request.user.username))
        context["len"] = count


    
    context["name"]=request.user.username
    return render(request,"breakfast.html",context )

def addcart(request,food,name,price,quantity):
    obj = Cart()
    obj.username = request.user.username
    obj.product = name
    obj.price = float(price)
    obj.quantity = int(quantity)
    print(food)
    if food == "breakfast":
        breakfasts= Breakfast.objects.get(name = name)
   
    if food == "combo":
        breakfasts = ComboOffer.objects.get(name = name)
   
    if food == "dailyspecial":
        breakfasts= DailySpecial.objects.get(name = name)
        
    if food == "lunch":
        breakfasts = Lunch.objects.get(name = name)

    if food == "fastfood":
        breakfasts= FastFood.objects.get(name = name)
        
    if food == "chatitems":
        breakfasts = ChatItems.objects.get(name = name)

    if food == "freshjuice":
        breakfasts= FreshJuice.objects.get(name = name)
  
    obj.image = breakfasts.bimage.url
    obj.save()
    return redirect("home")




