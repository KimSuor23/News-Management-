from django.test import TestCase
from django.utils import timezone
from .models import Category, News
from .forms import NewsForm
from django.core.exceptions import ValidationError


# Create your tests here.

class CategoryModelTest(TestCase):
    def test_category_str(self):
        category = Category(name="Tech")
        self.assertEqual(str(category), "Tech")

    def test_category_unique_name(self):
        Category.objects.create(name="Science")
        with self.assertRaises(Exception):
            # Attempt to create duplicate category name
            Category.objects.create(name="Science")


class NewsModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="World")

    def test_news_str(self):
        news = News(title="Big Event", category=self.category, source="News Corp", published_date=timezone.now(),
                    content="Details...")
        self.assertEqual(str(news), "Big Event")


class NewsFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Business")

    def test_news_form_valid(self):
        form_data = {
            'title': 'Economy improves',
            'category': self.category.id,
            'source': 'Global Times',
            'published_date': timezone.now().date(),
            'content': 'The economy is growing steadily.'
        }
        form = NewsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_news_form_invalid_empty_title(self):
        form_data = {
            'title': '  ',  # Spaces only
            'category': self.category.id,
            'source': 'Global Times',
            'published_date': timezone.now().date(),
            'content': 'Content here'
        }
        form = NewsForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
