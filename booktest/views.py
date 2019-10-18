from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.core.paginator import *
from .models import *
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import os
from booktest.task import *
# Create your views here.
def index(request):
    return render(request,'booktest/index.html')
def myexp(request):
    return HttpResponse('hello')
def uploadPic(request):
    return render(request,'booktest/uploadPic.html')
def uploadHandle(request):
    pic1=request.FILES['pic1']
    picName=os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(picName,'wb')as f:
        for i in pic1.chunks():
            f.write(i)
    return HttpResponse('<img src="/static/media/%s"/>'%pic1.name)
def herolist(request,pindex):
    if pindex=='':
        pindex='1'
    list=BookInfo.objects.all()
    paginator=Paginator(list,3)
    page=paginator.page(int(pindex))
    context={'page':page}
    return render(request, 'booktest/herolist.html',context)
def area(request):
    return render(request,'booktest/area.html')
def area2(request,id):
    id1=int(id)
    if id1==0:
        data=AreaInfo.objects.filter(parea__isnull=True)
        # print(data,'sdafgklak;')
    else:
        data=[{}]
    list1=[]
    for a in data:
        list1.append([a.id,a.title])
    return JsonResponse({'data':list1})
def pr(request):
    return render(request, 'booktest/pro.html')
def pro(request):
    prolist=AreaInfo.objects.filter(parea__isnull=True)
    list=[]
    for item in prolist:
        list.append([item.id,item.title])
    return JsonResponse({'data': list})
def city(request,id):
    citylist=AreaInfo.objects.filter(parea_id=id)
    list=[]
    for item in citylist:
        list.append({'id':item.id,'title':item.title})
    return JsonResponse({'data': list})
def htmlEditor(request):
    return render(request,'booktest/htmlEditor.html')
def htmlEditorHandle(request):
    html=request.POST['hcontent']
    test1=Test1.objects.get(pk=1)
    test1.content=html
    test1.save()
    content={'content':html}
    return render(request,'booktest/htmlShow.html',content)
@cache_page(60*1)
def cache1(request):
    # return HttpResponse('hello world')
    # return HttpResponse('hello2')
    # cache.set('ke1','valuelfgfdsgk',60*10)
    print(cache.get('ke1'),'sdjfkg')
    print('sdgjlkajakdslkasdal')
    # cache.clear()
    return render(request,'booktest/cache1.html')
def mysearch(request):
    return render(request,'booktest/mysearch.html')
def celeryTest(request):
    # show()
    show.delay()
    return HttpResponse('ok')
