from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

def home(request): 
    context = {'title': 'Articles', 'articles': Article.objects.all()}
    return render(request, 'kb/home.html', context)


def about(request):
    #return HttpResponse('<h1> About knowledge base </h1>')
    context = {'title': 'About KB'}
    return render(request, 'kb/about.html', context)

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']
    success_url = reverse_lazy('kb-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)