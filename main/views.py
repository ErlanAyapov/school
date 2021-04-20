from django.shortcuts import render
from .forms import ArticleForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Article


# class MainView(ListView):
# 	model = 'Article'
# 	template_name = 'main/index.html'

def main(request):
	news = Article.objects.all()
	context = {
		'news': news,
	}
	return render(request, 'main/index.html', context)

def ArticleAddView(request):
	error = ''
	if request.method == 'POST':
		news_form = ArticleForm(request.POST)
		
		# self.instance.author = self.request.user
		if news_form.is_valid():
			news_form = news_form.save(commit=False)
			news_form.save()
			return HttpResponseRedirect('/')
		else:
			error = 'Дұрыс толтырылмады!'

	news_form = ArticleForm()
	data = {
		'form':news_form,
		'error':error,
	}
	return render(request, 'main/add.html', data)