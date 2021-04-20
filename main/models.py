from django.db import models


class Article(models.Model):
	title  = models.CharField('Тақырыбы', max_length = 250)
	author = models.CharField('Есіміңіз', max_length = 250)
	body   = models.TextField('Мақаланы жазыңыз')

	def __str__(self):
		return self.author