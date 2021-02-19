from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    """
    Item model
    """
    CONDITION_TYPE = (
        ('N', 'New'),
        ('U', 'Used')
    )

    AUCTION_STATUS = (
        ('O', 'Open for Offers'),
        ('C', 'Completed')
    )

    # item id unique value
    item_id = models.AutoField(primary_key=True)

    # item title
    title = models.CharField(max_length=100, verbose_name="Title")

    # timestamp of the item registration in the system
    created_at = models.DateTimeField(
        verbose_name="Registration Timestamp",
        auto_now_add=True, null=False,
        editable=True)

    # item condition
    condition = models.CharField(
        choices=CONDITION_TYPE,
        default='N',
        verbose_name="Item Condition",
        max_length=5
        )

    # price of the item
    price = models.IntegerField(null=False, verbose_name="Item Price")

    # item description
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Item Description'
    )

    # item owner
    owner = models.ForeignKey(
        User,
        related_name='owner',
        on_delete=models.CASCADE,
        verbose_name="Owner",
        null=True,
        to_field = 'username'
        #blank=False
    )

    # Auction expiration time
    expire_time = models.DateTimeField(
        verbose_name="Auction Expiration Time",
        auto_now_add=False, null=False,
        editable=True
    )

    # status of auction
    auction_status = models.CharField(
        choices=AUCTION_STATUS,
        default='O',
        verbose_name="Auction Status",
        max_length=20
    )

    # auction winner
    winner = models.ForeignKey(
        User,
        related_name='winner',
        on_delete=models.CASCADE,
        verbose_name="Auction Winner",
        null=True,
        blank=True,
        to_field='username'
    )

    def __str__(self):
        return '{}: Title:{}, Owner:{}'.format(self.item_id, self.title, self.owner)

    class Meta:
        ordering = ['created_at']


class Bid(models.Model):
    """
    Bid model
    """
    # unique key for each bid
    bid_id = models.AutoField(primary_key=True)

    # bid on which auction item
    item = models.ForeignKey(
        Item,
        related_name='bids',
        on_delete=models.CASCADE,
        verbose_name="Auction Item",
        null=False,
        blank=False,
    )

    # bidding amount
    bidding_amount = models.IntegerField(null=False, verbose_name="Bidding Amount")

    # user that bids for the item
    bidder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Bidder",
        null=False,
        blank=False,
        to_field='username'
    )

    # bid creation/updation time
    created_at = models.DateTimeField(
        verbose_name="Bid Timestamp",
        auto_now_add=True, null=False
    )

    def __str__(self):
        return '{}: Bidder: {}, Bid Amount: {}'.format(self.bid_id, self.bidder, self.bidding_amount)

    class Meta:
        ordering = ['created_at']
