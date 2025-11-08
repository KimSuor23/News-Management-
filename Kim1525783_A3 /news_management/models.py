from django.db import models


# category table
class Category(models.Model):
    # name of the category, must be unique
    name = models.CharField(max_length=100, unique=True)

    # show name in admin and other views
    def __str__(self):
        return self.name


# news table
class News(models.Model):
    # title for the news article
    title = models.CharField(max_length=200)
    # link to category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # where the news comes from
    source = models.CharField(max_length=200)
    # when the article was made public
    published_date = models.DateField()
    # main text of the news
    content = models.TextField()

    # show title in admin and other views
    def __str__(self):
        return self.title
