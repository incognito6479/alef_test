from django.contrib import admin
from mainapp.models import CityInfo


@admin.register(CityInfo)
class CityInfoModelAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'okato', 'population', 'founded_in', 'status_of_city')
    search_fields = ('city_name',)
