from django.db import models


def function(instance, filename):
	return 'profile/user_{0}/{1}'.format(instance.id, filename)


class User(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField(max_length=100, default='peri@gmail.com')
	telephone = models.CharField(max_length=100, default=2)
	password = models.CharField(max_length=100, default='nopassword')
	pub_date = models.DateTimeField('create date')
	userlevel = models.CharField(max_length=50, default='User')
	model_pic = models.ImageField(upload_to = function, default = 'pic_folder/None/no-img.jpg', null=True, blank=True)

	def __str__(self):
	    return self.username

def gamespic(instance, filename):
	return 'games/name_{0}/{1}'.format(instance.name, filename)

class Game(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=5000, default="")
	pub_date = models.DateField('release date')
	genre = models.CharField(max_length=50)
	developer = models.CharField(max_length=50)
	publisher = models.CharField(max_length=50)
	pic = models.ImageField(upload_to = gamespic, default = 'pic_folder/None/no-img.jpg')

	def __str__(self):
	    return self.name

class HypeRatio(models.Model):
	id_game = models.IntegerField()
	like_votes = models.IntegerField(default=0)
	dislike_votes = models.IntegerField(default=0)

	def __str__(self):
	    return self.id_game


class Votes(models.Model):
	id_game = models.IntegerField()
	id_user = models.IntegerField()



