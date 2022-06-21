from django.urls import path

from api.views import DataUpdate, HeroView, SearchView, PowerstatsView

urlpatterns = [
    path('data/update/', DataUpdate.as_view(), name='dataupdate'),
    path('search/<str:name>', SearchView.as_view(),name='search'),
    path('hero/<int:pk>', HeroView.as_view(), name='hero'),
    path('powerstats/<int:pk>',PowerstatsView.as_view(),name='powerstats'),
    # path('appearance/<int:id>'),
    # path('biography/<int:id>'),
    # path('connections/<int:id>'),
    # path('work/<int:id>'),
    # path('images/<int:id>'),
]

# /all.json
# /id
# /powerstats
# /appearance
# /biography
# /connections
# /work
