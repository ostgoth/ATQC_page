from SharingWeb.models import ItemUser
from SharingWeb.models import Category
from SharingWeb.models import Item
from SharingWeb.models import ItemComment
from SharingWeb.models import Reference
from django.utils import timezone

ItemUser.objects.create(username="antony", first_name = "Anton", last_name = "Ryabko", email = "anto@rybko.com")
ItemUser.objects.create(username="maxI", first_name = "Maxim", last_name = "Row", email = "max@imena.com")
ItemUser.objects.create(username="maxII", first_name = "Максим", last_name = "Hadoop", email = "maxii@imena.com")
ItemUser.objects.create(username="maxIII", first_name = "Maxim", last_name = "Low", email = "maxiii@imena.com")
ItemUser.objects.create(username="maxIV", first_name = "Максим", last_name = "High", email = "high@imena.com")

writer = ItemUser.objects.first()
recipient = ItemUser.objects.filter(username="maxIII").first()

Reference.objects.create(UserWriter=writer, UserRecipient=recipient, reference="Нурмальний паца")

Category.objects.create(name="snowboards", description="Used snowboards", attr_format={})
Category.objects.create(name="sleepbag", description="Used sleepbag", attr_format={})

category_snowboards = Category.objects.first()
category_sleepbag = Category.objects.first()

Item.objects.create( name="snowboard", description="Найкращий борд в світі", price = 50, condition = 5, attributes={
    'style': ['universal', 'freeride'],
    'height': 157,
}, category = category_snowboards)
Item.objects.create( name="snowboard2", description="Just board", price = 30, condition = 5, attributes={
    'style': ['freestyle'],
    'height': 127,
}, category = category_snowboards)
Item.objects.create( name="snowboard3", description="Найкращий борд в світі - 2", price = 70, condition = 5, attributes={
    'style': ['universal'],
    'height': 180,
}, category = category_snowboards)

Item.objects.create( name="sleepbag1", description="Кому Спальник?", price = 70, condition = 5, attributes={
    'weight': 1000,
}, category = category_sleepbag)

item = Item.objects.first()
author = ItemUser.objects.first()
ItemComment.objects.create(item=item, author=author,body = "Непоганий борд", stars=4, created_at=timezone.now())
ItemComment.objects.create(item=item, author=author,body = "Так собі", stars=2, created_at=timezone.now())
ItemComment.objects.create(item=item, author=author,body = "Середнячок", stars=3, created_at=timezone.now())
