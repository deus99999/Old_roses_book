from django.urls import path
from .views import MainView, SearchResultView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('search/', SearchResultView.as_view(), name='search_results'),

]