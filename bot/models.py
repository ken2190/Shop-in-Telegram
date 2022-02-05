from django.db import models


class Profile(models.Model):
    level_client = [
        (1, 'Didn\'t buy'),
        (2, 'Regular client'),
        (3, 'Regular customer'),
        (4, 'Wholesaler 1'),
        (5, 'Wholesaler 2'),
    ]
    external_id = models.PositiveIntegerField(verbose_name="User ID")
    name = models.CharField(verbose_name="User Nickname", max_length=200)
    level = models.IntegerField("Client level", choices=level_client, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class MessageText(models.Model):
    message = models.TextField(verbose_name="Message")

    class Meta:
        verbose_name = "Bot Messages"
        verbose_name_plural = "Bot Messages"


class MenuText(models.Model):
    button = models.TextField(verbose_name="Menu button")

    class Meta:
        verbose_name = "Bot menu buttons"
        verbose_name_plural = "Bot Menu Buttons"


class Category(models.Model):
    text = models.TextField(verbose_name="Category")
    parent = models.ForeignKey('self', default=None, null=True, blank=True, related_name='nested_category',
                               on_delete=models.CASCADE, verbose_name="Parent")
    nesting_level = models.IntegerField(default=1, verbose_name="Nested Level")
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Product Categories"
        verbose_name_plural = "Product Categories"


class Product(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
    price1 = models.PositiveIntegerField(verbose_name="Price for non-buyer")
    price2 = models.PositiveIntegerField(verbose_name="Normal user price")
    price3 = models.PositiveIntegerField(verbose_name="Loyalty Price")
    price4 = models.PositiveIntegerField(verbose_name="Price for wholesaler 1")
    price5 = models.PositiveIntegerField(verbose_name="Price for wholesaler 2")
    text = models.TextField(verbose_name="Description", null=True)
    img = models.ImageField(verbose_name="Product Image", null=True, upload_to='image/')
    description = models.TextField(verbose_name="Detailed description (split into separate messages ';')", null=True,
                                   blank=True)
    ask = models.TextField(verbose_name="Questions for the product (separated into separate messages ';')", null=True,
                           blank=True)
    data = models.TextField(verbose_name="Purchase data required", null=True)
    сat = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        related_name="products"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"


class Order(models.Model):
    step_order = [
        (1, 'Customer enters data'),
        (2, 'Not paid'),
        (3, 'Paid'),
        (4, 'Sent to supplier'),
        (5, 'Ready'),
        (6, 'Canceled'),
        (7, 'Operator failure')

    ]
    step = models.IntegerField("Order Status", choices=step_order)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="order"
    )
    data_kol = models.IntegerField(verbose_name="Amount of data loaded", default=0)
    data_have = models.TextField(verbose_name="User Input", default="", null=True)
    date_create = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name="Update Date", auto_now=True)
    code = models.TextField(verbose_name="Payment code", default="", null=True)
    pay = models.IntegerField(verbose_name="Sum", default=0)
    comment = models.TextField(verbose_name="Comment for user", default="", null=True, blank=True)
    phone = models.CharField(verbose_name="Phone number", max_length=15, null=True)
    fio = models.CharField(verbose_name="Name", max_length=200, null=True)

    class Meta:
        verbose_name = "Purchase Request"
        verbose_name_plural = "Purchase Requests"


class FileOrder(models.Model):
    file_order = models.FileField(verbose_name="Loading data", null=True, upload_to='documents/')
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=True

    )

    class Meta:
        verbose_name = "Files"
        verbose_name_plural = "Files"
