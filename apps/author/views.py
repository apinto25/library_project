from django.shortcuts import render
from django.views.generic import ListView

from apps.author.models.author_model import Author


class ListAuthors(ListView):
    context_object_name = "authors_list"
    template_name = "author/list.html"

    def get_queryset(self):
        kword = self.request.GET.get("kword", "")
        return Author.objects.search_authors(kword)
