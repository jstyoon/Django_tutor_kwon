from django.shortcuts import render, redirect #redirect를 추가해줍니다
import random
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')


# dinner views
def dinner(request, name):
    menus = [{"name":'족발',"price":30000}, {"name":'햄버거',"price":5000}, 
             {"name":'치킨',"price":20000}, {"name":'초밥',"price":15000}]
    pick = random.choice(menus)
    #articles = Article.objects.all() #모든Article불러옵니다
    articles = Article.objects.order_by('-pk') #pk의 역순(즉 게시id역순)
    context = {
        'pick': pick,
        'name': name,
        'menus': menus,
        'articles': articles,
    }
    return render(request, 'dinner.html', context)

def review(request):
    return render(request, 'review.html')

def create_review(request):
    content = request.POST.get('content')
    title = request.POST.get('title')
    article = Article(title=title, content=content)
    article.save()
    
#context는 DB 모델을 활용하면 필요하지 않습니다
#    context = {
#        'content': content,
#    }
    
#     return render(request, 'review_result.html') 
#리뷰작성이 완료되면 list 페이지를 보여주기위해 redirect로 바꾸어줍니다
    return redirect('/articles/dinner/무언가/')