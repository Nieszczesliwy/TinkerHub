from TinkerHub.settings import PAGINATION_COUNT
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Article


def renderHomePage(request):
    if request.method == "GET":
        req_page = int(request.GET.get('page', 1))
            
        all_articles = Article.objects.all().order_by('-published_date')
        
        paginated_articles = Paginator(all_articles, per_page=PAGINATION_COUNT)
        get_page = paginated_articles.get_page(req_page)
        
        payload = [elem.serializer_all() for elem in get_page.object_list]
        
        response = {
            "page": {
                "current": get_page.number,
                "has_next": get_page.has_next(),
                "has_previous": get_page.has_previous(),
                "total": paginated_articles.num_pages
            },
            "articles": payload,
        }

        return render(request, 'articles/homepage.html', {'context' : response})
        

def renderSingleArticle(request, aID):
    if request.method == "GET":
        get_article = Article.objects.get(pk=aID)
        
        return render(request, 'articles/article_detail.html', {"context": get_article.serializer_single()})


def createArticle(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return render(request, 'articles/article_creation.html')
        else:
            return redirect('homepage')