from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = (
        ('ML', 'Milk'),
        ('CR', 'Curd'),
        ('MS', 'Milk Shake'),
        ('LS', 'Lassi'),
        ('GH', 'Ghee'),
        ('PN', 'Paneer'),
        ('CH', 'Cheese'),
        ('IC', 'Ice Cream'),
    )

    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title