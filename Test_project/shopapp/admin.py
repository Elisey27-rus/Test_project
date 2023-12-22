from .models import Item
from django.contrib import admin

@admin.register(Item)
class Item_admin(admin.ModelAdmin):
  list_display = ('name','descriptions', 'price')#внутри админки выдает столбцы с наименование
  list_display_links = ('name','descriptions', 'price') #названия которые открывают продукт
  ordering=('name','descriptions', 'price')#Устанавливаем поля по которым можно будет делать сортировки
  serch_fields = ('name','descriptions', 'price')#выходит графа поиска по полям

  def __str__(self):
    return f"Item(id={self.id},name={self.name}"
