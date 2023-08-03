from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView, View
from .models import Text
from django.core.paginator import Paginator
import random
from django.db.models import Q


class MainView(View):
    def get(self, request, *args, **kwargs):
        texts = Text.objects.all()
        for text in texts:
            text = Text.objects.filter(id=text.id)

        posts = Text.objects.get_queryset().order_by('date_created')
        paginator = Paginator(posts, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Number of visits to this view, as counted in the session variable.
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1

        img_position = random.choice(('left', 'right'))
        return render(request, 'page/index.html', context={'texts': texts,
            'page_obj': page_obj, 'num_visits':num_visits, 'img_position':img_position,})


class SearchResultView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = Text.objects.filter(
                Q(text__icontains=query)
            )
        paginator = Paginator(results, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'page/search.html', context={
           # 'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })