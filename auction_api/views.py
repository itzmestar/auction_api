from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from .models import Item, Bid
from .serializers import ItemSerializer, BidSerializer, ItemDetailSerializer
# Create your views here.


class ItemList(ListCreateAPIView):
    """
    View to create and List Item
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ItemDetails(ListAPIView):
    """
    View to detail and update Item
    """

    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer


class BidCreate(CreateAPIView):
    """
        View to create bid
    """

    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    def perform_create(self, serializer):
        #serializer.
        serializer.save(bidder=self.request.user)
