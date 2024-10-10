from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from miniproj.forms import ArticleForm
from .models import Article

# Create your views here.
def viewArticles(request):
    articles = Article.objects.all()
    return render(request, 'articleList.html', {'articles': articles})

def openArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', {'article': article})

def createArticle(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articleList')
    else:
        form = ArticleForm()
    return render(request, 'form.html', {'form': form})

def UpdateArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articleList')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'form.html', {'form': form})

def deleteArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articleList')
    return render(request, 'delete.html', {'article': article})