from django.core.management.base import BaseCommand, CommandError
from auction_api.models import Item as Auction
from auction_api.models import Bid
from django.utils import timezone


class Command(BaseCommand):
    help = 'Closes the auctions for bidding & declare auction winner'

    def __chose_winner(self, auction):

        bids = Bid.objects.filter(item=auction)
        if len(bids) == 0:
            return None
        maximum_bid = bids[0]
        for bid in bids:
            if bid.bidding_amount > maximum_bid.bidding_amount:
                maximum_bid = bid
        return maximum_bid.bidder

    def handle(self, *args, **options):

        auctions = Auction.objects.filter(auction_status='O')

        for auction in auctions:
            if auction.expire_time < timezone.now():
                auction.auction_status = 'C'
                winner = self.__chose_winner(auction)
                auction.winner = winner
                auction.save()
                msg = 'Successfully closed auction for item: {}:{}, winner:{}'.format(
                    auction.item_id, auction.title, winner)
                self.stdout.write(self.style.SUCCESS(msg))
