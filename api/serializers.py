from rest_framework import serializers

from api.models import User, Hero, Powerstats, Appearance, Biography, Work, Connections, Images


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name','first_name', 'email')


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'slug')


class PowerstatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerstats
        fields = ('id','intelligence','strength',
                  'speed','durability','power','combat')


class AppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appearance
        fields = ('id','gender','race',
                  'height','weight','eyecolor','haircolor')


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = ('id','fullName','alterEgos',
                  'aliases','placeOfBirth','firstAppearance',
                  'publisher','alignment')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id','occupation','base')


class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connections
        fields = ('id','groupAffiliation','relatives')


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id','xs','sm',
                  'md','lg')


class SearchSerializer(serializers.ModelSerializer):
    powerstats = PowerstatsSerializer(many=True)
    appearance = AppearanceSerializer(many=True)
    biography = BiographySerializer(many=True)
    work = WorkSerializer(many=True)
    connections = ConnectionsSerializer(many=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Hero
        fields = ('id','name', 'slug','powerstats','appearance',
                  'biography','work','connections','images')