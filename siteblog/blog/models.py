from django.db import models

class Category (models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self): #служебный метод для вывода title объектов
        return self.title

    class Meta:
        ordering = ['title']
class Tag (models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)#уникальное

    def __str__(self): #служебный метод для вывода title объектов
        return self.title

    class Meta:
        ordering = ['title']

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, verbose_name='Url', unique=True)
    author = models.CharField(max_length=50)
    content = models.TextField(blank=True) #необязательное поле
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')# автоматически заполняется текущей датой и не подлежит измению
    photo = models.ImageField(upload_to='photo/%Y/%M/%D/', blank=True)# место хранения фото
    viwes =models.IntegerField(default=0, verbose_name='Количество просмотров')# значение по умолчанию =0
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags =models.ManyToManyField(Tag,blank=True, related_name='posts')

    def __str__(self): #служебный метод для вывода title объектов
        return self.title

    class Meta:
        ordering = ['-created_at']