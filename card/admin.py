from django.contrib import admin

# Register your models here.
from card.models import PlayerCard, KingCard


class PlayerCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cal', 'order', 'flavour')
    list_filter = ('cal', 'order', 'flavour')


class KingCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cal', 'number_of_firsts', 'number_of_seconds', 'number_of_desserts', 'today_eat',
                    'action')


admin.site.register(PlayerCard, PlayerCardAdmin)
admin.site.register(KingCard, KingCardAdmin)
