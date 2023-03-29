from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def products_count(self):
        return self.product_set.count()

    @property
    def products_list(self):
        return [product.title for product in self.product_set.all()]


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def category_n(self):
        try:
            return self.category.name
        except:
            ''

    @property
    def rating(self):
        all_stars = [review.stars for review in self.reviews.all()]
        return round(sum(all_stars) / len(all_stars), 2) if len(all_stars) > 0 else 0


class Review(models.Model):
    CHOICES = ((i, '* ' * i) for i in range(1, 6))
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews', null=True)
    stars = models.IntegerField(default=1, choices=CHOICES)

    def __str__(self):
        return self.text

    def product_title(self):
        return self.product.title
