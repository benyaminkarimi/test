from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models import signals

User = get_user_model()

class CategoryModel(models.Model):
    parent_category = models.ForeignKey('self',related_name='child_category_list',on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("the `name` of the category."),
        max_length=128,

    )

class ProductModel(models.Model):
    user = models.ForeignKey(
        verbose_name=_("user"),
        help_text=_("The user who added the product"),
        to=User,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("the `name` of the product."),
        max_length=128,

    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("the `description` of the product."),
        max_length=1000,
    )
    price = models.PositiveIntegerField(
        verbose_name=_("price"),
        help_text=_("the `price` of the product."),
    )
    salesNumber = models.PositiveIntegerField(
        verbose_name=_("number of sales"),
        help_text=_("the `sales number` of the product."),
        default=0,
    )
    stock = models.PositiveIntegerField(
        verbose_name=_("stock"),
        help_text=_("the `stock` of the product."),
    )
    createAt = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(CategoryModel)


# def create_customer(sender, instance, created, **kwargs):
#     print ("///////////////////////////////////")
#     print("saveeed!!!!!!!!!!!!")
#     print ("///////////////////////////////////")


# signals.post_save.connect(receiver=create_customer, sender=ProductModel)
