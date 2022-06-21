from django.contrib import admin

from api.models import User, Hero, Powerstats, Appearance, Biography, Work, Connections, Images


class PowerstatsInline(admin.TabularInline):
    model = Powerstats
    extra = 1


class AppearanceInline(admin.TabularInline):
    model = Appearance
    extra = 1


class BiographyInline(admin.TabularInline):
    model = Biography
    extra = 1


class WorkInline(admin.TabularInline):
    model = Work
    extra = 1


class ConnectionsInline(admin.TabularInline):
        model = Connections
        extra = 1


class ImagesInline(admin.TabularInline):
            model = Images
            extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Hero)
class Hero(admin.ModelAdmin):
    list_display = ['name']
    inlines = [PowerstatsInline,AppearanceInline,BiographyInline,WorkInline,ConnectionsInline,ImagesInline]