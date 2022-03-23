from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import hydjobs, banglorejobs, chennaijobs, punejobs

# Create your views here.
def index(request):
    return render(request,'testApp/index.html')

def hydjobs_view(request):
    jobs_list=hydjobs.objects.order_by('Date')

    # paginator=Paginator(jobs_list,5)
    # page_number=request.GET.get('page')
    # try:
    #     jobs_list=paginator.page(page_number)
    # except PageNotAnInteger:
    #     jobs_list=paginator.page(1)
    # except EmptyPage:
    #     jobs_list=paginator.page(paginator.num_pages)

    my_dict = {'jobs_list':jobs_list}
    return render(request,'testApp/hydjobs.html',context=my_dict)

def banglorejobs_view(request):
    jobs_list = banglorejobs.objects.order_by('Date')
    my_dict = {'jobs_list': jobs_list}
    return render(request,'testApp/banglorejobs.html',context=my_dict)

def chennaijobs_view(request):
    jobs_list = chennaijobs.objects.order_by('Date')
    my_dict = {'jobs_list': jobs_list}
    return render(request,'testApp/chennaijobs.html',context=my_dict)

def punejobs_view(request):
    jobs_list = punejobs.objects.order_by('Date')
    my_dict = {'jobs_list': jobs_list}
    return render(request,'testApp/punejobs.html',context=my_dict)


