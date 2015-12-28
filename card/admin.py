from django.contrib import admin

# Register your models here.
from card.models import Card, PlayerCard


class PlayerCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cal', 'order', 'flavour')
    list_filter = ('cal', 'order', 'flavour')

admin.site.register(Card)
admin.site.register(PlayerCard, PlayerCardAdmin)
