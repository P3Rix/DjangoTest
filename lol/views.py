from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

from django.shortcuts import render

from .models import User

from .models import Game

from .forms import UserForm

from .forms import loginForm

from .forms import ImageUploadForm

from .forms import GameForm

from .models import HypeRatio

from .models import Votes

from django.core.paginator import Paginator


def index(request):
	latest_games_list = Game.objects.order_by('pub_date')
	paginator = Paginator(latest_games_list, 8)
	page = request.GET.get('page')
	latest_games_list = paginator.get_page(page)
	List = [1, 2, 3] 
	admin = False
	if 'member_id' in request.session:
		session = User.objects.get(id=request.session['member_id'])
		user = session
		session = session.username
		session = "Hi "+ session +"!"
		if user.userlevel == 'admin':
			admin = True
	else:
		session = None

	context = {'latest_games_list': latest_games_list, 'session': session, 'list': List, 'admin': admin}
	return render(request, 'lol/index.html', context)

def registerview(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request
		form = UserForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
			user = form.save(commit=False)
			user.password = make_password(form.cleaned_data['password'])
			user.status = 1
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
			#return HttpResponseRedirect('/thanks/')
			user.save()
			return HttpResponseRedirect('/lol/')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = UserForm()

	return render(request, 'lol/register.html', {'form': form})

def detail(request, game_id):
	game = Game.objects.get(id=game_id)
	if 'member_id' in request.session:
		session = User.objects.get(id=request.session['member_id'])
		user = session
		session = session.username
		session = "Hi "+ session +"!"
		if user.userlevel == 'admin':
			admin = True
	else:
		session = None
	try:
		nohasvoted = Votes.objects.get(id_user=user.id, id_game=game.id)
	except Votes.DoesNotExist:
		nohasvoted = True

	context = {'game': game, 'session': session, 'novoted': nohasvoted}
	return render(request, 'lol/game.html', context)


def login(request):
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			user = User.objects.get(username=form.cleaned_data['username'])
			if check_password(form.cleaned_data['password'], user.password):
				request.session['member_id'] = user.id
				return HttpResponseRedirect('/lol/')

	else:
		form = loginForm()

	return render(request, 'lol/login.html',{'form': form})

#Por ahora esta de aqui no sirve para nada
def register(request):
	user = User()
	try:
		user = User.objects.exclude(username=username)
	except User.DoesNotExist:
		return HttpResponse("You're voting on user %s." % user.password)
	raise ValidationError(u'Username "%s" is already in use.' % username)

	return render(request, 'lol/register.html')

def uploadImage(request):
	print("hola")
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		user = User.objects.get(id=request.session['member_id'])
		if form.is_valid():
			user.model_pic = form.cleaned_data['image']
			user.save()
			return render(request, 'lol/profile.html', {'user': user, 'session': request.session['member_id'], 'photo': True})
	return HttpResponseForbidden('allowed only via POST')

def voteLike(request):
	if request.method == 'POST':
		game_id 
	return HttpResponseForbidden('allowed only via POST')

def voteDislike(request):
	
	return HttpResponseForbidden('allowed only via POST')

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponseRedirect('/lol/')


def profile(request):
	if 'member_id' in request.session:
		user = User.objects.get(id=request.session['member_id'])
		if user.model_pic == "pic_folder/None/no-img.jpg":
			return render(request, 'lol/profile.html', {'user': user, 'session': request.session['member_id'], 'photo': False})
		else:
			return render(request, 'lol/profile.html', {'user': user, 'session': request.session['member_id'], 'photo': True})
	else:
		return HttpResponseRedirect('/lol/')


def registergame(request):
	user = User.objects.get(id=request.session['member_id'])
	if user.userlevel == "admin":
		if request.method == 'POST':
	        # create a form instance and populate it with data from the request
			form = GameForm(request.POST, request.FILES)
	        # check whether it's valid:
			if form.is_valid():
				game = form.save()
				hyperatio = HypeRatio()
				hyperatio.id_game = game.id
				hyperatio.save()
				return HttpResponseRedirect('/lol/')

	    # if a GET (or any other method) we'll create a blank form
		else:
			form = GameForm()

		return render(request, 'lol/registergame.html', {'form': form})
	else:
		return HttpResponseRedirect('/lol/')

# Create your views here.
