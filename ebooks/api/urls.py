from django.urls import path
from ebooks.api.views import EBookListCreateAPIView, EbookDetailAPIView,ReviewCreateAPIView,ReviewDetailAPIView

urlpatterns = [
    path("ebooks/",EBookListCreateAPIView.as_view(),name="ebook-list"),
    path("ebooks/<int:pk>/",EbookDetailAPIView.as_view(),name="ebook-detail"),
    path("ebooks/<int:ebook_pk>/review/", ReviewCreateAPIView.as_view(), name="review-ebook"),
    path("reviews/<int:pk>/", ReviewDetailAPIView.as_view(), name="review-detail")
]