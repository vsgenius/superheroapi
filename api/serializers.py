from rest_framework import serializers

from api.models import User, Hero, Powerstats


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name','first_name', 'email')


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'slug')


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id')


class PowerstatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerstats
        fields = ('hero_id_id','intelligence','strength',
                  'speed','durability','power','combat')