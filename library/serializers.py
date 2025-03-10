from rest_framework import serializers
from .models import Genre, Author, Book, Member, BorrowingHistory
from django.contrib.auth.models import User


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name'] 



class BookSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['genre'] = GenreSerializer(instance.genre).data

        representation['authors'] = AuthorSerializer(instance.authors.all(), many=True).data

        return representation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = ['id', 'user', 'phone', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user') 
        user = User.objects.create_user(**user_data) 
        user.is_staff = False  
        user.save() 
        member = Member.objects.create(user=user, **validated_data)  
        return member



# Serializer for BorrowingRecord
class BorrowingHistorySerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all()) 
    member = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())  



    class Meta:
        model = BorrowingHistory
        fields = '__all__'

