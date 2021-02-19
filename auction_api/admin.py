from django.contrib import admin

# Register your models here.
from .models import Item, Bid


class ItemAdmin(admin.ModelAdmin):
    fields = ['title',
              'condition','price','description',
              'owner','expire_time','auction_status','winner']
    list_display = ['item_id', 'created_at', 'title',
              'condition', 'price', 'description',
              'owner', 'expire_time', 'auction_status', 'winner']


admin.site.register(Item, ItemAdmin)


class BidAdmin(admin.ModelAdmin):
    fields = ['item',
              'bidding_amount','bidder']
    list_display = ['bid_id', 'item', 'bidding_amount',
              'bidder', 'created_at']


admin.site.register(Bid, BidAdmin)