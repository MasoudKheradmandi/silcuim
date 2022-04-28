from django.shortcuts import render,get_object_or_404
from .models import Article,Category
from django.core.paginator import Paginator

# Create your views here.

def home(request ,page_number=1):

	articles_list = Article.objects.filter(status="Publish")
	paginator = Paginator(articles_list,3) 
	page_obj = paginator.get_page(page_number)

	context = {
	'articles': page_obj ,
 	'category':Category.objects.filter(status=True),
	}
	return render(request,"blog/home.html",context)

def detailview(request,slug):
	context={
	'article':get_object_or_404(Article, slug=slug , status='Publish'),
 	'category':Category.objects.filter(status=True),
	}
	return render(request,"blog/detail.html",context)

def category(request,slug):
    context = {
        'articles':Article.objects.filter(status='Publish'),
        'category':Category.objects.filter(status=True),
		'categorys':get_object_or_404(Category,slug=slug,status=True),
	}
    return render(request,'blog/category.html',context)

# def authorlist(request,pk):
#     context = {
#     'articles':Article.objects.filter(status='Publish'),
#     'authors':Article.objects.get(pk='author')
# 	}
#     return render(request,'blog/author_list.html',context)