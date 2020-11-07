from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import PlayList , Video


# Create your views here.
def index(request):
    lucky_no = random.randint(1,42)
    fruit = random.choice(["蘋果","鳳梨","香蕉","芭樂","芒果","柚子","橘子","香瓜","西瓜","葡萄"])
    numbers = list()
    for i in range(6):
        numbers.append(random.randint(1,42))
    return render(request,"index.html",locals())
    #return HttpResponse("<h3>您今天的幸運號碼是：{}<h3><h3>您今天的幸運水果是：{}<h3>".format(lucky_no,fruit))

def playlist(request):
    items = PlayList.objects.all()
    return render(request,"playlist.html",locals())

def showlist(request,id):
    titles = Video.objects.filter(plist=id)
    return render(request,"showlist.html",locals())
