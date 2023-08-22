from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price',  'auction', 'created_date', 'updated_date', 'photo']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('общее' , {
            'fields' : ('title', 'description', 'image'),
        }),
        ('финансы' , {
            'fields' : ('price' , 'auction'),
            'classes' : ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, reqest, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, reqest, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
