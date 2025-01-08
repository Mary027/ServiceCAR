from django.contrib import admin
from django.http import HttpResponse
import openpyxl
from .models import User, Car, Order

@admin.action(description="Экспортировать в Excel")
def export_to_excel(modeladmin, request, queryset):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = modeladmin.model.__name__

    # Заголовки
    headers = [field.verbose_name for field in modeladmin.model._meta.fields]
    sheet.append(headers)

    # Данные
    for obj in queryset:
        row = [str(getattr(obj, field.name)) for field in modeladmin.model._meta.fields]
        sheet.append(row)

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = f'attachment; filename={modeladmin.model.__name__}.xlsx'
    workbook.save(response)
    return response

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)
    actions = [export_to_excel]

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'model', 'series', 'year')
    search_fields = ('model','series')
    list_filter = ('client', 'year')
    actions = [export_to_excel]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'service_date', 'description', 'cost')
    search_fields = ('description',)
    list_filter = ('service_date', 'car')
    actions = [export_to_excel]