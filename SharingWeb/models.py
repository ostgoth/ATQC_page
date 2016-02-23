from django.db import models

# Base model

#################################################################################
# UserInfo classes
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
    email = models.EmailField()
    phoneMain = models.PositiveIntegerField()
    socailNetworks = models.ForeignKey(SocialNetworks)

# Rate - possible negative and positive values
# For UserInfo class
class UserRating(models.Model):
    rate = models.IntegerField()


#################################################################################
# ShareItem classes
#################################################################################
# Rent prices
# For ShareItem class
class RentPrices(models.Model):
    totalPrice = models.PositiveIntegerField()
    hourPrice = models.PositiveIntegerField()
    dayPrice = models.PositiveIntegerField()
    weekPrice = models.PositiveIntegerField()
    monthPrice = models.PositiveIntegerField()
    yearPrice = models.PositiveIntegerField()

# Item condition
# From zero till 10 ?????
# For ShareItem class
class Condition(models.Model):
    condition = models.IntegerField()

# Calendar - needs some research
# For ShareItem class
class Calendar(models.Model):
    date = models.DateField()

# Pictures - needs some research
# For ShareItem class
# For now: title for picture and web link
class Pictures(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField() # or ImageField() ??

# UserInfo - main item description class
class ShareItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    rent = models.ForeignKey(RentPrices)
    condition = models.ForeignKey(Condition)
    calendar = models.ForeignKey(Calendar)
    pictures = models.ForeignKey(Pictures)
    creationYear = models.IntegerField()
    color = models.CharField(max_length=20)
    size = models.IntegerField() # any kind of size....
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    weight = models.IntegerField()

#################################################################################
# UserInfo - main user profile and all user's item class
#################################################################################
class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    realName = models.CharField(max_length=50)
    passoword = models.CharField(max_length=50)
    contacts = models.ForeignKey(Contacts)
    delivery = models.ForeignKey(DeliveryInfo)
    location = models.ForeignKey(Location)
    rate = models.ForeignKey(UserRating)
    items = models.ForeignKey(ShareItem) # all users items will be here
    registrationData = models.DateTimeField()
# pay method (cash, card, paypal... ) - ????
# settings for user notification ??
