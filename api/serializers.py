from rest_framework import serializers

from api.models import User, Hero, Powerstats, Appearance, Biography, Work, Connections, Images


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class PowerstatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerstats
        fields = '__all__'


class AppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appearance
        fields = '__all__'


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connections
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


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