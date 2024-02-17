from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Author, Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class MainPage(View):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['authors'] = Author.objects.all()
        context['books'] = Book.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)


class AuthorDetailView(View):
    template_name = 'author_detail.html'

    def get(self, request, pk, *args, **kwargs):
        author = get_object_or_404(Author, pk=pk)
        return render(request, self.template_name, {'author': author})


class BookDetailView(View):
    template_name = 'book_detail.html'

    def get(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        return render(request, self.template_name, {'book': book})


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_form.html'
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('main')


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author_form.html'
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('main')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('main')


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'publication_year', 'genres', 'rating']
    success_url = reverse_lazy('main')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'publication_year', 'genres', 'rating']
    success_url = reverse_lazy('main')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('main')



