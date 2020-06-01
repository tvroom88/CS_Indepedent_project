from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from restaurants.forms import MenuForm, RegisterRestaurantForm, MenuUpdateForm
from restaurants.models import Menu, Restaurant
from account.models import Account

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def restaurant_view(request):
	context = {}
	# context['restaurant'] = Restaurant.objects.all()
	# context['menus'] = Menu.objects.all()
	user = request.user
	if not user.is_authenticated:
		return render(request, 'restaurant.html', context)


	owner = Account.objects.get(email=request.user.email)
	context['restaurant'] = Restaurant.objects.filter(owner = owner)
	return render(request, 'restaurant.html', context)


def register_restaurant_view(request):
	context = {}

	if request.POST:
		form = RegisterRestaurantForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			owner = Account.objects.get(email=request.user.email)
			obj.owner = owner
			obj.save()
			return redirect('restaurant_home_view')

		else:
			context['restaurant_register_form'] = form
	else:  # GET request
		form = RegisterRestaurantForm()
		context['restaurant_register_form'] = form
	return render(request, 'register_restaurant.html', context)



def register_new_menu_view(request):
	context = {}

	owner = Account.objects.get(email=request.user.email)
	context['restaurant'] = Restaurant.objects.filter(owner=owner)

	if request.POST:
		form = MenuForm(request.POST)

		restaurant_name = request.POST.get('restaurant_name')
		restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)

		if form.is_valid():




			obj = form.save(commit=False)

			obj.restaurant = restaurant
			obj.save()
			return redirect('menu_board')
			# form.save()
			# return redirect('restaurant_home_view')

		else:
			context['menu_form'] = form
	else:  # GET request
		form = MenuForm()
		context['menu_form'] = form
	return render(request, 'register_menu.html', context)


def menu_board_view(request):
	context = {}

	owner = Account.objects.get(email=request.user.email)

	restaurant = Restaurant.objects.filter(owner = owner)
	context['restaurant'] = restaurant

	foods_list = Menu.objects.filter(restaurant__in=restaurant).order_by(('-id'))
	# context['foods'] = foods_list

	#------------ paginator things ------------------------
	page = request.GET.get('page', 1)
	paginator = Paginator(foods_list, 3)

	try:
		foods = paginator.page(page)
	except PageNotAnInteger:
		foods = paginator.page(1)
	except EmptyPage:
		foods = paginator.page(paginator.num_pages)

	context['foods'] = foods

	# ------------------------

	return render(request, 'menu_board.html', context)


# ------------------------------------

# def menu_delete(request, pk):
def menu_delete(request):
	menu = get_object_or_404(Menu, id=request.POST['food_id'])
	menu.delete()
	return redirect('menu_board')


def menu_update(request, pk):
	context={}
	user = request.user
	if not user.is_authenticated:
		return redirect('login')


	menu = get_object_or_404(Menu, pk = pk)


	if menu.restaurant.owner != user:
		return HttpResponseRedirect("You are not the author of the post")


	# 레스토랑 내용을 가져옴

	owner = Account.objects.get(email=request.user.email)
	context['restaurant'] = Restaurant.objects.filter(owner=owner)

	if request.POST:
		form = MenuUpdateForm(request.POST)

		if form.is_valid():
			obj = form.save(commit=False)

			restaurant_name = request.POST.get('restaurant_name')
			restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)

			obj.restaurant = restaurant
			obj.save()

			# menu = obj
			return redirect('menu_board')

		else:
			form = MenuUpdateForm(request.POST)


	form = MenuUpdateForm(
		initial={
			"menu": menu.Menu,
			"price": menu.price,
			"info": menu.Info,
		}
	)

	context['form'] = form
	return render(request, 'menu_update.html', context)


