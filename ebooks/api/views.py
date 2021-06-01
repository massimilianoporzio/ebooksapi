from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from ebooks.models import Ebook, Review
from ebooks.api.serializers import ReviewSerializer, EbookSerializer
from django.conf import settings
from django.contrib.auth.models import User


class EBookListCreateAPIView(generics.ListCreateAPIView):

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class ReviewCreateAPIView(generics.CreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook,pk=ebook_pk)
        author = User.objects.first()
        serializer.save(ebook=ebook,review_author=author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
