"""Cats serializers."""
from rest_framework import serializers

from .models import Cat, Owner, AchievementCat, Achievement


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ('id', 'name')


class CatSerializer(serializers.ModelSerializer):
    """Cat serializer."""

    achievements = AchievementSerializer(many=True)

    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'owner', 'achievements')

    def create(self, validated_data):
        """Create cat."""
        # Уберём список достижений из словаря validated_data и сохраним его
        achievements = validated_data.pop('achievements')

        # Создадим нового котика пока без достижений, данных нам достаточно
        cat = Cat.objects.create(**validated_data)

        # Для каждого достижения из списка достижений
        for achievement in achievements:
            # Создадим новую запись или получим существующий экземпляр из БД
            current_achievement, status = Achievement.objects.get_or_create(
                **achievement)
            # Поместим ссылку на каждое достижение во вспомогательную таблицу
            # Не забыв указать к какому котику оно относится
            AchievementCat.objects.create(
                achievement=current_achievement, cat=cat)


class OwnerSerializer(serializers.ModelSerializer):
    """Owner serializer."""

    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        """Meta class."""

        model = Owner
        fields = ('first_name', 'last_name', 'cats')
