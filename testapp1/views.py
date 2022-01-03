from django.shortcuts import render

from testapp1.models import Student109qwe
# Create your views here.
def home(request):
    qs=Student109qwe.objects.all()
    print(qs)
    return render(request,'home.html',{'qs':qs})

def delete_data(request,id):
    qs=Student109qwe.objects.get(id=id)
    qs.delete()
    qs=Student109qwe.objects.all()
    return render(request,'home.html',{'qs':qs})

