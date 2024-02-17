from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)