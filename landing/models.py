from django.db import models
import uuid, datetime

def generate_filename(self, filename):
    path = "%s/%s" % ( str(datetime.datetime.now().date().strftime("%d-%m-%Y")), str(uuid.uuid4()) + '-' + filename )
    return path

def generateThumbnail(self):
    return '<a href="/media/%s"><img src="/media/%s" width=80px height=80px /></a>' % (self.image, self.image)

def generateImage(self):
    return '<a href="/media/%s"><img src="/media/%s" width=170px height=170px /></a>' % (self.image, self.image)

class NutType(models.Model):
    label = models.CharField('Тип ореха', max_length=100, blank=True, default='')

    def __str__(self):
        return str('%s' % self.label)

class Product(models.Model):
    class Meta:
        db_table = 'Product'

    def getThubmnail(self):
        return generateThumbnail(self)

    def getImage(self):
        return generateImage(self)

    getThubmnail.short_description = "Картинка"
    getThubmnail.allow_tags = True

    getImage.short_description = "Картинка"
    getImage.allow_tags = True

    nut_type = models.ManyToManyField(NutType, verbose_name='Тип ореха', blank=True, null=True)

    def getNutType(self):
        if self.nut_type.all().count() > 0:
            nut_types = ''

            for nut_type in self.nut_type.all():
                nut_types += nut_type.label + ', '

            return '%s' % nut_types[:-2]

        else:
            return ''

    getNutType.short_description = "Тип ореха"

    label = models.CharField('Название', max_length=100, blank=True, default='')
    in_stock = models.BooleanField('В наличии', editable=True, default=True)
    image = models.FileField('Картинка', upload_to=generate_filename)
    count = models.IntegerField('Количество', default=0)
    price = models.FloatField("Цена(руб/кг)", default=0.0)
    
    FRUIT = 'FRU'
    NUT = 'NUT'
    TYPE_CHOICES=(
        (FRUIT,'Фрукт'),
        (NUT,'Орех'),
    )
    the_type = models.CharField('Тип', max_length=3, choices=TYPE_CHOICES, default=FRUIT)

    def __str__(self):
        return str('%s' % self.label)

class Order(models.Model):
    class Meta:
        db_table = 'Order'

    date_create = models.DateTimeField('Дата создания', default=datetime.datetime.now)
    #date_update = models.DateTimeField('date_update', auto_now=True)

    def getCreateDate(self):
        return str(self.date_create.strftime('%d.%m.%Y %H:%M'))
    getCreateDate.short_description = "Дата создания"

    name = models.CharField('Имя', max_length=200, blank=True, default='')
    street = models.CharField('Улица', max_length=200, blank=True, default='')
    house = models.CharField('Дом', max_length=200, blank=True, default='')
    corps = models.CharField('Корпус', max_length=200, blank=True, default='')
    building = models.CharField('Строение', max_length=200, blank=True, default='')
    number = models.CharField('NO(Номер)', max_length=200, blank=True, default='')
    phone = models.CharField('Телефон', max_length=200, blank=True, default='')
    email = models.CharField('E-mail', max_length=200, blank=True, default='')
    company = models.CharField('Название компании', max_length=200, blank=True, default='')
    order_list = models.TextField('Лист заказа', blank=True, default='')
    complete = models.BooleanField('Выполнен', editable=True, default=False)

    def __str__(self):
        return str('%s' % self.name)
