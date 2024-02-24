from django.test import TestCase
from django.urls import reverse

# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self):
#         print("setUp: Run once for every test method to set up clean data.")
#         pass

#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)

#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)


#python3 manage.py test
#python3 manage.py test --verbosity 2    to get more info
#python3 manage.py test --parallel auto     run in parallel if independ 
        
from catalog.models import Author, Book, BookInstance

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')
#check verbose name, but not direclty so use _meta
    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'Died')  #updated to match

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')


class BookModelTest(TestCase):
    @classmethod
    #TypeError: BookModelTest.setUpTestData() missing 1 required positional argument: 'cls'
    def setUpTestData(cls):
        Book.objects.create(title="Born a Crime",summary="words words words", isbn="1234567890123")
        # first_name="Trevor", last_name="Noah", 
        #TypeError: Book() got unexpected keyword arguments: 'first_name', 'last_name'
        #not sure how to handle fk and m2m relationships...
        #https://www.valentinog.com/blog/testing-django/#testing-a-many-to-many-relationship

    def test_title_label(self):
        book = Book.objects.get(id=1)
        #get specific instance to check
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
    
    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)    #select specific object
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')


# how can it be used to test expected_info for relations?
# def test_relation(self):
#     author = Author.objects.get(id=1)
#     book = Book.objects.get(id=1)



# py manage.py test catalog.tests  runs whole folder
# py manage.py test catalog.tests  specific file
        # py manage.py test catalog.tests.test_models.BookModelTest.test_get_absolute_url
        