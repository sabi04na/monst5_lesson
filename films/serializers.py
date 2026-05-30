from rest_framework import serializers
from .models import Film, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id first_name last_name'.split()



class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    genres = serializers.SerializerMethodField()



    class Meta:
        model = Film
        fields = 'id title rating created director genres genre_list'.split()
        # depth = 1

    def get_genres(self, film):
        list_ =[]
        for i in film.genres.all():
            list_.append(i.name)
        return list_