from .models import Article
from django.forms import ModelForm, TextInput, Textarea

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'body', 'author' ]

		widgets = {
			'title': TextInput(attrs={
					'class': 'form-control',
					'placeholder': 'Мақала тақырбы',

				}),
			'body': Textarea(attrs={
					'class': 'form-control',
					'placeholder': 'Жазыңыз...',
					
				}),
			'author': TextInput(attrs={
					'class': 'form-control',
					'placeholder': 'Есіміңіз',	
				}),
		}