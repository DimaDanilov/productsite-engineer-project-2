from django.db import models
from django.contrib.postgres.validators import (MinValueValidator, MaxValueValidator)


class Brand(models.Model):
    brand_name = models.CharField('Название фирмы', max_length = 80, unique=True)
    rating = models.IntegerField('Рейтинг(1-10)',validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        verbose_name = "Фирма"
        verbose_name_plural = "Фирмы"

    def __str__(self):
        return self.brand_name


class ProductGroup(models.Model):
    group_name = models.CharField('Название отдела', max_length = 70, unique=True)
    products_amount = models.IntegerField('Количество товаров в отделе', validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Отдел продуктов"
        verbose_name_plural = "Отделы продуктов"

    def __str__(self):
        return self.group_name


class Products(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Фирма'
    )
    productGroup = models.ForeignKey(
        ProductGroup,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Отдел продуктов'
    )
    title = models.CharField('Название', max_length = 60)
    description = models.TextField('Описание товара', blank=True)
    price = models.IntegerField('Цена, руб.', validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


class Post(models.Model):
    postcode = models.IntegerField('Код должности', validators=[MinValueValidator(1), MaxValueValidator(9999)])
    postname = models.CharField('Название должности', max_length=250)
    
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.postname


class Salerman(models.Model):
    salercode = models.IntegerField('Код работника', validators=[MinValueValidator(1), MaxValueValidator(9999999)])
    salername = models.CharField('ФИО', max_length=250)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Должность'
    )
    cash = models.IntegerField('Заработная плата, руб.', validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return self.salername


class Customer(models.Model):
    customercode = models.IntegerField('Код покупателя', validators=[MinValueValidator(1), MaxValueValidator(9999999)])
    customername = models.CharField('ФИО', max_length=250)

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    def __str__(self):
        return str(self.customercode)



class Sale(models.Model):
    products = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продукт'
    )
    salecode = models.IntegerField('Код продажи', validators=[MinValueValidator(1), MaxValueValidator(9999999)], unique=True)
    salesumm = models.IntegerField('Сумма товара, руб.',validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"

    def __str__(self):
        return str(self.salecode)


class SaleCheck(models.Model):
    salerman = models.ForeignKey(
        Salerman,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продавец'
    )
    сustomer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Покупатель'
    )
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продажа'
    )
    salecheckcode = models.IntegerField('Код чека', validators=[MinValueValidator(1), MaxValueValidator(9999999)], unique=True)
    salechecksumm = models.IntegerField('Сумма чека, руб.',validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"

    def __str__(self):
        return str(self.salecheckcode)


class Promotion(models.Model):
    promotioncode = models.IntegerField('Код акции', validators=[MinValueValidator(1), MaxValueValidator(9999999)], unique=True)
    promotionname = models.CharField('Название акции', max_length=250)
    description = models.TextField('Описание акции', blank=True)

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return str(self.promotionname)


class Delivery(models.Model):
    deliverycode = models.IntegerField('Код доставки', validators=[MinValueValidator(1), MaxValueValidator(9999999)], unique=True)
    saleCheck = models.ForeignKey(
        SaleCheck,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Чек'
    )
    promotion = models.ForeignKey(
        Promotion,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Акция'
    )
    salerman = models.ForeignKey(
        Salerman,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Курьер'
    )

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"

    def __str__(self):
        return str(self.deliverycode)