from rest_framework import serializers
from .models import Tour, TourCategory, Review, Booking, User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["url", "username", "password", "avatar"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        avatar = validated_data.pop('avatar', None)
        user = User(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()

        if avatar:
            user.avatar = avatar
            user.save()

        return user

    def update(self, instance, validated_data):
        avatar = validated_data.pop('avatar', None) # извлекаем значение из validate
        for attr, value in validated_data.items(): # для каждого атрибута устанавливает значения
            setattr(instance, attr, value)
        if avatar:
            instance.avatar = avatar
        instance.save()
        return instance

class TourCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCategory
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'