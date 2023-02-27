from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # Создание модели, по сути - основной класс
    # Перечисляем свойства нашего класса (нашей модели) и определяем их тип

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Сmodels.ForeignKey — ссылка на другую модель
    title = models.CharField(max_length=200) # models.CharField — так мы определяем текстовое поле с ограничением на количество символов
    text = models.TextField() # models.TextField — так определяется поле для неограниченно длинного текста. Выглядит подходящим для содержимого поста
    created_date = models.DateTimeField(default=timezone.now) # models.DateTimeField — дата и время
    published_date = models.DateTimeField(blank=True, null=True) # models.DateTimeField — дата и время

    # Перечисляем методы нашего класса (нашей модели)

    def publish(self): # метод публикации записи
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # Метод, возвращающий текст, с заголовком записи
        return self.title
