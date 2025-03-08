from django.contrib import admin
from .models import Genre, Author, Book, Member, BorrowingHistory

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(BorrowingHistory)
