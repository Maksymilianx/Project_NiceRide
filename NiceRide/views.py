import random
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, ListView
from rest_framework.response import Response

from NiceRide.forms import OfferCreationForm, OpinionCreationForm, MessageCreationForm
from NiceRide.models import Car, Opinions, Messages, ObserveCar


class IndexView(View):
    def get(self, request):
        lst = list(Car.objects.all())
        return render(request, 'index.html', {"lst": lst})


class SellCarView(LoginRequiredMixin, View):
    def get(self, request):
        color = Car.COLORS
        return render(request, 'add_offer.html', {'color': color})

    def post(self, request):
        car_brand = request.POST.get('brand_of_car')
        car_model = request.POST.get('car_model')
        description = request.POST.get('description')
        date = request.POST.get('created')
        price = request.POST.get('price')
        year = request.POST.get('production_year')
        mileage = request.POST.get('mileage')
        engine = request.POST.get('engine_capacity')
        hp = request.POST.get('horse_power')
        country = request.POST.get('country')
        fuel_type = request.POST.get('fuel_type')
        # images = request.FILES.getlist('images')
        type = request.POST.get('type')
        color = request.POST.get('color')
        car_offer = Car(brand_of_car=car_brand, car_model=car_model, description=description, created=date, price=price,
                        production_year=year, mileage=mileage, engine_capacity=engine, horse_power=hp, country=country,
                        car_color=color, fuel_type=fuel_type, type=type)
        car_offer.save()
        return redirect("index")


class OffersView(View):
    def get(self, request):
        car_name = request.GET.get('brand_of_car', '')
        offers_list = Car.objects.filter(brand_of_car__icontains=car_name).order_by('-created')
        paginator = Paginator(offers_list, 10)
        page = request.GET.get('page')
        offers = paginator.get_page(page)

        page_number = []
        for page in range(offers.paginator.num_pages):
            page += 1
            page_number.append(page)
        return render(request, "offers.html", {'offers': offers, 'page_number': page_number})


class OfferDetailsView(View):
    def get(self, request, id):
        offer = Car.objects.get(pk=id)
        comments = Opinions.objects.all()
        return render(request, "offer_details.html", {'offer': offer, 'comments': comments})


class OfferAddBookmarksView(View):
    def get(self, request, id):
        offer = Car.objects.get(pk=id)
        oc = ObserveCar()
        oc.save()
        oc.followed_by.add(request.user)
        oc.followed.add(offer)
        return redirect('details', id)


class ShowBookmarksView(LoginRequiredMixin, ListView):
    model = ObserveCar
    template_name = 'bookmarks_list.html'

    def get_queryset(self):
        return ObserveCar.objects.filter(followed_by=self.request.user)


class CommentView(LoginRequiredMixin, View):
    def get(self, request):
        form = OpinionCreationForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = OpinionCreationForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.author = request.user
            opinion.save()
            return redirect('offers')
        return render(request, "form.html", {'form': form})


class EditCommentView(LoginRequiredMixin, UpdateView):
    model = Opinions
    fields = ['content']
    success_url = reverse_lazy('offers')
    template_name = 'form.html'


class DeleteOfferView(LoginRequiredMixin, DeleteView):
    model = Car
    fields = ['brand_of_car', 'car_model', 'description', 'price', 'production_year', 'mileage', 'engine_capacity',
              'horse_power', 'country', 'car_color', 'fuel_type', 'type']
    success_url = reverse_lazy('offers')
    template_name = 'add_offer.html'


class EditOfferView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['brand_of_car', 'car_model', 'description', 'price', 'production_year', 'mileage', 'engine_capacity',
              'horse_power', 'country', 'car_color', 'fuel_type', 'type']
    success_url = reverse_lazy('offers')
    template_name = 'add_offer.html'


def is_valid_queryparam(param):
    return param != '' and param is not None


class AdvancedSearchView(View):
    def get(self, request):
        queryset = Car.objects.all()
        ft = Car.TYPE_OF_FUEL
        return render(request, "advanced_search.html", {'queryset': queryset, 'fuel_types': ft})

    def post(self, request):

        queryset = Car.objects.all()
        car_brand = request.POST.get('car_brand')
        car_model = request.POST.get('car_model')
        price_min = request.POST.get('price_min')
        price_max = request.POST.get('price_max')
        mileage_min = request.POST.get('mileage_min')
        mileage_max = request.POST.get('mileage_max')
        fuel_type = request.POST.get('fuel_type')

        if is_valid_queryparam(car_brand):
            queryset = queryset.filter(brand_of_car__icontains=car_brand)
        if is_valid_queryparam(car_model):
            queryset = queryset.filter(car_model__icontains=car_model)
        if is_valid_queryparam(price_min):
            queryset = queryset.filter(price__gte=price_min)
        if is_valid_queryparam(price_max):
            queryset = queryset.filter(price__lt=price_max)
        if is_valid_queryparam(mileage_min):
            queryset = queryset.filter(price__gte=mileage_min)
        if is_valid_queryparam(mileage_max):
            queryset = queryset.filter(price__lt=mileage_max)
        if fuel_type != 'Wybierz...':
            queryset = queryset.filter(fuel_type=fuel_type)

        return render(request, "advanced_search.html", {'queryset': queryset})


class FindOffersView(View):
    def get(self, request):
        offers_list = Car.objects.filter('name')
        return render(request, 'index.html', {'offers_list': offers_list})


class MessagesView(LoginRequiredMixin, View):
    def get(self, request):
        form = MessageCreationForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = MessageCreationForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.from_user = request.user
            message.save()
            return redirect('index')
        return render(request, 'form.html', {'form': form})


class ShowMessagesView(LoginRequiredMixin, ListView):
    model = Messages
    template_name = 'message_list.html'

    def get_queryset(self):
        return Messages.objects.filter(to_user=self.request.user)


class AboutView(View):
    def get(self, request):
        return render(request, "about.html")
