from django.db import models


class CityInfo(models.Model):
    url = models.CharField(max_length=900, blank=True, null=True)
    id_from_page = models.IntegerField(unique=True)
    city_name = models.CharField(max_length=500, verbose_name="Город")
    okato = models.IntegerField(verbose_name="ОКАТО")
    population = models.BigIntegerField(verbose_name="Населения")
    founded_in = models.IntegerField(verbose_name="Основание")
    status_of_city = models.IntegerField(verbose_name="Статус города")

    def __str__(self):
        return f"{self.city_name}"

    class Meta:
        verbose_name = "Городские населённые пункты Московской области"
        verbose_name_plural = "Городские населённые пункты Московской области"
