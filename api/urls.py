from django.urls import path

from api.views import DataUpdate, HeroView, SearchView, PowerstatsView, AppearanceView, BiographyView, ConnectionsView, \
    WorkView, ImagesView

urlpatterns = [
    path('data/update/', DataUpdate.as_view(), name='dataupdate'),
    path('search/<str:name>', SearchView.as_view(), name='search'),
    path('hero/<int:pk>', HeroView.as_view(), name='hero'),
    path('powerstats/<int:pk>', PowerstatsView.as_view(), name='powerstats'),
    path('appearance/<int:pk>', AppearanceView.as_view(), name='appearance'),
    path('biography/<int:pk>', BiographyView.as_view(), name='biography'),
    path('connections/<int:pk>', ConnectionsView.as_view(), name='connections'),
    path('work/<int:pk>', WorkView.as_view(), name='work'),
    path('images/<int:pk>', ImagesView.as_view(), name='images'),
]
