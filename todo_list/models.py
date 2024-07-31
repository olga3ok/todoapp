from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    content = models.TextField(blank=True)

    created = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, default="general", on_delete=models.PROTECT)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
