import datetime

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView,ListView
# import generic UpdateView
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import *
from .forms import *
class DashboardView(TemplateView):
    template_name = "shop/index.html"

class AdminTemplate(TemplateView):
    template_name = "shopadmin/base.html"

class itemcreateview(CreateView):
    # model = item
    template_name = "shopadmin/itemcreate.html"
    form_class = itemcreateform
    success_url = reverse_lazy('myapp:itemcreateview')



class itemview(View):
    def get(self, request):
        itm = item.objects.all()
        form = itemcreateform()
        context = {'itm':itm, 'form':form}
        return render(request, 'shopadmin/itemcreate.html', context)

    def post(self, request):
        itemname = request.POST.get('itemname')
        cat = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        photo1 = request.FILES['photo1']
        photo2 = request.FILES['photo2']
        photo3 = request.FILES['photo3']
        photo4 = request.FILES['photo4']

        cate = category.objects.get(id=int(cat))

        itm = item(itemname=itemname, category=cate, price=price, description=description, photo1=photo1, photo2=photo2, photo3=photo3, photo4=photo4)
        itm.save()
        
        return redirect('myapp:itemview')