from django.contrib import admin
from books.models import Book, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Name', 'AuthorID')
    search_fields = ('Name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('Title',)
    list_filter = ('PublishDate',)
    ordering = ('Title',)
    filter_horizontal = ('AuthorID',)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
#修改admin.py