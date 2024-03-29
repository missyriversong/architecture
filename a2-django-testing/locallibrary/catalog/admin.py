from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.

class BooksInline(admin.TabularInline):
   model = Book

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
  inlines = [BooksInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    #can be used with Book, see below, so can edit all related for Book at one time

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')
  inlines = [BooksInstanceInline]
  #since genre is m2m, need to add def display_genre to Book model
  #can add BookInstance since Book is FK 

# class BooksInline(admin.TabularInline):
#    model = Book

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_display = ('book', 'status', 'due_back')
  list_filter = ( 'status', 'due_back')
  fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
  # inlines = [BooksInline]

# admin.site.register(Book)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)