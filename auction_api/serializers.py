from rest_framework import serializers
from .models import Item, Bid
from django.utils import timezone
from api_users.serializers import UserSerializer


class ItemSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Check that create is before expiration.
        """
        now = timezone.now()
        if data['expire_time'] < now:
            raise serializers.ValidationError("expire_time must occur after creation_time")
        return data

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['item_id', 'owner', 'created_at', 'winner', 'auction_status']


class ItemDetailSerializer(serializers.ModelSerializer):
    bids = serializers.StringRelatedField(many=True)

    class Meta:
        model = Item
        fields = ['item_id', 'title', 'owner', 'created_at', 'condition',
                  'price', 'description', 'winner', 'auction_status', 'expire_time', 'bids']


class BidSerializer(serializers.ModelSerializer):
    bidder = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    item_id = serializers.IntegerField()
    class Meta:
        model = Bid
        fields = ['item_id', 'bidding_amount', 'bidder']
        read_only_fields = ['bid_id']

    def validate(self, data):
        """
        validate data.
        """
        try:
            item = Item.objects.get(item_id=data['item_id'])
        except Item.DoesNotExist:
            raise serializers.ValidationError("Invalid item_id")
        
        if item.auction_status != 'O':
            raise serializers.ValidationError("Item not open for Auction")
        user_value = self.context['request'].user

        if item.owner == user_value:
            raise serializers.ValidationError("Can't bid on your own item")

        return data
