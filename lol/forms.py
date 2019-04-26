from django import forms
from .models import User
from .models import Game
import datetime

class UserForm(forms.ModelForm):
	username = forms.CharField(label='username ', max_length=100)
	email = forms.EmailField(label='email ', max_length=100)
	telephone = forms.CharField(label='number ')
	password = forms.CharField(label='password ',max_length=100, widget=forms.PasswordInput)
	pub_date = forms.DateTimeField(label='create date', widget=forms.HiddenInput(), initial=datetime.datetime.now())

	class Meta:
		model = User
		fields = ("username", "email", "telephone", "password",	"pub_date")

	def clean_username(self):
		username = self.cleaned_data.get('username')
		username_qs = User.objects.filter(username=username)
		if username_qs.exists():
			raise forms.ValidationError("Username already exists")
		return username



class loginForm(forms.Form):
	username = forms.CharField(label='username ', max_length=100)
	password = forms.CharField(label='password ',max_length=100, widget=forms.PasswordInput)

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class GameForm(forms.ModelForm):
	name = forms.CharField(max_length=50)
	description = forms.CharField(max_length=500)
	pub_date = forms.DateField(initial=datetime.date.today)
	genre = forms.CharField(max_length=50)
	developer = forms.CharField(max_length=50)
	publisher = forms.CharField(max_length=50)
	pic = forms.ImageField()

	class Meta:
		model = Game
		fields = ("name", "description", "genre", "developer", "publisher", "pub_date", "pic")


		def __init__(self, *args, **kwargs):
			super(GameForm, self).__init__(*args, **kwargs)
			self.fields['pic'].required = False

