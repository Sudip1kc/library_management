from rest_framework import serializers
from .models import Genre, Author, Book, Member, BorrowingHistory
from django.contrib.auth.models import User

# Serializer for Genre
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# Serializer for Author
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# Serializer for Book
class BookSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to accept only IDs
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())  # Accept genre ID
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)  # Accept a list of author IDs

    class Meta:
        model = Book
        fields = '__all__'

# Serializer for User (for Member registration)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}  # Correct indentation

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Serializer for Member
class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = ['user', 'phone', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract user data
        user = User.objects.create_user(**user_data)  # Create user with password hashing
        user.is_staff = False  # Regular members should have is_staff = False
        user.save()  # Save the user
        member = Member.objects.create(user=user, **validated_data)  # Create Member instance
        return member



# Serializer for BorrowingRecord
class BorrowingHistorySerializer(serializers.ModelSerializer):
    # Nested serializers for the book and member involved in the record
    book = BookSerializer()
    member = MemberSerializer()

    class Meta:
        model = BorrowingHistory
        fields = '__all__'

