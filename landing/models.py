from django.db import models
import uuid, datetime

def generate_filename(self, filename):
    path = "%s/%s" % ( str(datetime.datetime.now().date().strftime("%d-%m-%Y")), str(uuid.uuid4()) + '-' + filename )
    return path

class Product(models.Model):
    label = models.CharField('Название', max_length=100, blank=True, default='')
    in_stock = models.BooleanField('В наличии', editable=True, default=True)
    image = models.FileField(upload_to=generate_filename)
    count = models.IntegerField('Количество', default=0)
    price = models.FloatField("Цена", default=0.0)
    
    FRUIT = 'FRU'
    NUT = 'NUT'
    TYPE_CHOICES=(
        (FRUIT,'Фрукт'),
        (NUT,'Орех'),
    )
    the_type = models.CharField(max_length=3, choices=TYPE_CHOICES, default=FRUIT)

    def __str__(self):
        return str('%s, %s, %s, кол-во: %s, цена: %s' % (self.label, self.get_the_type_display(), 'в наличии' if self.in_stock else 'закончились', self.count, self.price))

class Order(models.Model):
    name = models.CharField('Имя', max_length=200, blank=True, default='')
    street = models.CharField('Улица', max_length=200, blank=True, default='')
    house = models.CharField('Дом', max_length=200, blank=True, default='')
    corps = models.CharField('Корпус', max_length=200, blank=True, default='')
    building = models.CharField('Строение', max_length=200, blank=True, default='')
    number = models.CharField('NO(Номер)', max_length=200, blank=True, default='')
    phone = models.CharField('Телефон', max_length=200, blank=True, default='')
    email = models.CharField('E-mail', max_length=200, blank=True, default='')
    company = models.CharField('Название компании', max_length=200, blank=True, default='')

    def __str__(self):
        return str('%s, %s, %s, %s' % (self.name, self.email, self.phone, self.company))
