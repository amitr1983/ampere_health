from __future__ import unicode_literals

from django.db import models

# Create your models here.
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