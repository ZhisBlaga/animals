from django.db import models
from django.utils import timezone
# Create your models here.

#Модель животных

class Animal (models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    age =  models.CharField(max_length=50, default='не известен')
    created_date = models.DateTimeField(default=timezone.now)
    SEX_CHOICES = [
            ('Муж', 'Муж'),
            ('Жен', 'Жен'),
            ('Не определен', 'Не определен'),
        ]


    sex = models.CharField( max_length=12, choices=SEX_CHOICES,default='Не определен') 
    KIND_CHOICES = [
            ('Кошка', 'Cat'),
            ('Собака', 'Dog'),
            ('Попугай', 'Parrot'),
        ]
    king = models.CharField( max_length=7, choices=KIND_CHOICES,default='')
    photo = models.ImageField(upload_to='img/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name+' '+self.breed

    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
