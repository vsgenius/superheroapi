import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User, Hero, Powerstats, Appearance, Biography, Work, Connections, Images
from api.serializers import UserSerializer, HeroSerializer, SearchSerializer, PowerstatsSerializer


class UserView(APIView):
    def get(self, request):
        if not request.user.is_superuser:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class HeroView(APIView):
    def get(self, request, pk=None):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)
        hero = Hero.objects.filter(id=pk)
        serializer = HeroSerializer(hero, many=True)
        return Response(serializer.data)


class SearchView(APIView):
    def get(self, request, name=None):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)
        hero = Hero.objects.filter(name=name)
        serializer = SearchSerializer(hero, many=True)
        return Response(serializer.data)


class PowerstatsView(APIView):
    def get(self, request, pk=None):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)
        powerstats = Powerstats.objects.filter(hero_id_id=pk)
        serializer = PowerstatsSerializer(powerstats, many=True)
        return Response(serializer.data)


class DataUpdate(APIView):
    """
    Класс для обновления прайса от поставщика
    """

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)
        url = request.data.get('url')
        with open(url, 'r') as stream:
            try:
                with open(url, 'r') as file:
                    data = json.load(file)
            except:
                print('Ошибка чтения')
            for category in data:
                filter = len(Hero.objects.filter(id=category['id']))
                if filter == 0:
                    Hero.objects.create(id=category['id'], name=category['name'], slug=category['slug'])
                    Powerstats.objects.create(intelligence=category['powerstats']['intelligence'],
                                              strength=category['powerstats']['strength'],
                                              speed=category['powerstats']['speed'],
                                              durability=category['powerstats']['durability'],
                                              power=category['powerstats']['power'],
                                              combat=category['powerstats']['combat'],
                                              hero_id_id=category['id'], )
                    Appearance.objects.create(gender=category['appearance']['gender'],
                                              race=category['appearance']['race'],
                                              height=category['appearance']['height'],
                                              weight=category['appearance']['weight'],
                                              hero_id_id=category['id'], )
                    Biography.objects.create(fullName=category['biography']['fullName'],
                                             alterEgos=category['biography']['alterEgos'],
                                             aliases=category['biography']['aliases'],
                                             placeOfBirth=category['biography']['placeOfBirth'],
                                             publisher=category['biography']['publisher'],
                                             alignment=category['biography']['alignment'],
                                             hero_id_id=category['id'], )
                    Work.objects.create(occupation=category['work']['occupation'],
                                        base=category['work']['base'],
                                        hero_id_id=category['id'], )
                    Connections.objects.create(groupAffiliation=category['connections']['groupAffiliation'],
                                               relatives=category['connections']['relatives'],
                                               hero_id_id=category['id'], )
                    Images.objects.create(xs=category['images']['xs'],
                                          sm=category['images']['sm'],
                                          md=category['images']['md'],
                                          lg=category['images']['lg'],
                                          hero_id_id=category['id'], )

            return JsonResponse({'Status': True})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})
