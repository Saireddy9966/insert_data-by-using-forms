from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def display_form(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse('insert successful')
    return render(request,'display_form.html')

def display_wp(request):
    pp=Topic.objects.all()
    d={'topic':pp}
    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST['n']
        un=request.POST['un']
        em=request.POST['em']
        to=Topic.objects.get(topic_name=tn)
        to.save()
        ko=webpg.objects.get_or_create(topic_name=to,name=n,webpage=un,email=em)[0]
        ko.save()
        return HttpResponse('insert Webpage data Successsfully')

    return render(request,'display_wp.html',d)


def display_ac(request):
    wo=webpg.objects.all()
    d={'webp':wo}
    if request.method=='POST':
        n=request.POST['n']
        au=request.POST['au']
        da=request.POST['da']
        ko=webpg.objects.get_or_create(name=n)[0]
        ko.save()
        po=accessrec.objects.get_or_create(name=ko,author=au,date=da)[0]
        
        po.save()
        return HttpResponse('insert accessrecods data Successsfully')

    return render(request,'display_ac.html',d)




def retrive(request):
    pp=Topic.objects.all()
    d={'topic':pp}
    if request.method=='POST':
        td=request.POST.getlist('tn')
        print(td)
        webquery=webpg.objects.none()
        for i in td:
            webquery=webquery|webpg.objects.filter(topic_name=i)
        d1={'webpage':webquery}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrive.html',d)

def checkbox(request):
    lto=Topic.objects.all()
    d={'topic':lto}
    return render(request,'checkbox.html',d)


def radio(request):
    lto=Topic.objects.all()
    d={'topic':lto}
    return render(request,'radio.html',d)

