from django.db import models

# Base model

#################################################################################
# Location - for UserInfo class
# Alternative Name - Address
class Location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.PositiveIntegerField()
    apartment = models.PositiveIntegerField()
    additionInfo = models.CharField(max_length=200)

# Delivery services - list of delivery services
# For DeliveryInfo class
class DeliveryServices(models.Model):
    deliveryServiceName = models.CharField(max_length=50)

# Delivery method
# deliveryService - Nova Poshta
# deliveryServiceDepartment - Viddilennia #250
# For UserInfo class
class DeliveryInfo(models.Model):
    deliveryService = models.ForeignKey(DeliveryServices)
    deliveryServiceDepartment = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.PositiveIntegerField()
    apartment = models.PositiveIntegerField()
    additionInfo = models.CharField(max_length=200)

# Social networks list
# For Contacts list
class SocialNetworks(models.Model):
    socialNetworksName = models.CharField(max_length=50)
    socialNetworksLink = models.CharField(max_length=200)

# Contacts
# For UserInfo class
class Contacts(models.Model):
    email = models.CharField(max_length=50)
    phoneMain = models.PositiveIntegerField()
    socailNetworks = models.ForeignKey(SocialNetworks)

# Rate - possible negative and positive values
# For UserInfo class
class UserRating(models.Model):
    rate = models.IntegerField()

# Rent prices
# For ShareItem class
class RentPrices(models.Model):
    totalPrice = models.PositiveIntegerField()
    hourPrice = models.PositiveIntegerField()
    dayPrice = models.PositiveIntegerField()
    weekPrice = models.PositiveIntegerField()
    monthPrice = models.PositiveIntegerField()
    yearPrice = models.PositiveIntegerField()

# Item name
# Price
# Rent prices
# Item description
# Condition
# Calendar
# Text Description
# Pictures
class ShareItem(models.Model):
    rent = models.ForeignKey(RentPrices)

# UserInfo
class UserInfo(models.Model):
    delivery = models.ForeignKey(DeliveryInfo)
    location = models.ForeignKey(Location)
    contacts = models.ForeignKey(Contacts)
    rate = models.ForeignKey(UserRating)
    items = models.ForeignKey(ShareItem)
# login
# password
# real naim
# pay method