from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


UserModel = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


@python_2_unicode_compatible
class UserFitbit(models.Model):
    user = models.OneToOneField(UserModel, related_name='user_model1')
    fitbit_user = models.CharField(max_length=32, unique=True)
    access_token = models.TextField()
    auth_secret = models.TextField()
    refresh_token = models.TextField()

    def __str__(self):
        return self.user.__str__()

    def get_user_data(self):
        return {
            'user_id': self.fitbit_user,
            'access_token': self.access_token,
            'refresh_token': self.refresh_token
        }


class TimeSeriesDataType(models.Model):
    """
    This model is intended to store information about Fitbit's time series
    resources, which can be found here:
    https://wiki.fitbit.com/display/API/API-Get-Time-Series
    """

    foods = 0
    activities = 1
    sleep = 2
    body = 3
    CATEGORY_CHOICES = (
        (foods, 'foods'),
        (activities, 'activities'),
        (sleep, 'sleep'),
        (body, 'body'),
    )
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    resource = models.CharField(max_length=128)

    def __str__(self):
        return self.path()

    class Meta:
        unique_together = ('category', 'resource',)
        ordering = ['category', 'resource']

    def path(self):
        return '/'.join([self.get_category_display(), self.resource])


class TimeSeriesData(models.Model):
    """
    The purpose of this model is to store Fitbit user data obtained from their
    time series API (https://wiki.fitbit.com/display/API/API-Get-Time-Series).
    """

    user = models.ForeignKey(UserModel, related_name='user_model')
    resource_type = models.ForeignKey(TimeSeriesDataType)
    date = models.DateField()
    value = models.CharField(null=True, default=None, max_length=32)

    class Meta:
        unique_together = ('user', 'resource_type', 'date')

    def string_date(self):
        return self.date.strftime('%Y-%m-%d')

class Cuisine(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)

class Restaurent(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	zip_code = models.CharField(max_length=10, blank=True)
	city = models.CharField(max_length=30)
	cuisine_id = models.ForeignKey(Cuisine)

class Menu(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	calories = models.IntegerField()
	veg = models.BooleanField(null=False, default=True)
	restaurent_id = models.ForeignKey(Restaurent)
	cuisine_id = models.ForeignKey(Cuisine)

class User(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	zip_code = models.CharField(max_length=10, blank=True)

class Health_Stat(models.Model):
	id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User)
	weight = models.PositiveIntegerField()
	height = models.PositiveIntegerField()
	age = models.IntegerField(max_length=3)

class Diet_Preference(models.Model):
	id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User)
	calories = models.PositiveIntegerField()
	prefered_food = models.CharField(max_length=10, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)