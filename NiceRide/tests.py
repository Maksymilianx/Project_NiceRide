from django.contrib.auth.models import User
from django.test import Client, TestCase
import pytest
from django.urls import reverse


from NiceRide.models import Car, Opinions


@pytest.mark.django_db
def test_offers_GET(user):
    c = Client()
    c.force_login(user)
    url = reverse('offers')
    response = (c.get(url))
    assert response.status_code == 200


@pytest.mark.django_db
def test_offer_details_GET(user):
    Car.objects.create(id=1)
    c = Client()
    url = reverse('details', args=(1,))
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_offer_GET(user):
    c = Client()
    c.force_login(user)
    url = reverse('add_offer')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_offer_POST(user):
    c = Client()
    c.force_login(user)
    url = reverse('add_offer')
    response = c.post(url, {'brand_of_car': 'samochod', 'car_model': 'jakistam'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_adv_search_GET(user):
    c = Client()
    url = reverse('adv_search')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_adv_search_POST(user):
    c = Client()
    url = reverse('adv_search')
    response = c.post(url, {'brand_of_car': 'fura', 'price_min': '1'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_comment_GET(user):
    c = Client()
    c.force_login(user)
    url = reverse('add_comment')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_comment_POST(user):
    c = Client()
    c.force_login(user)
    url = reverse('add_comment')
    response = c.post(url, {'content': 'ala ma kota'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_comment_GET(user):
    User.objects.create(id=2)
    Opinions.objects.create(author_id=2)
    c = Client()
    c.force_login(user)
    url = reverse('edit_comment', args=(2,))
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_offer_GET(user):
    Car.objects.create(id=1)
    c = Client()
    c.force_login(user)
    url = reverse('edit_offer', args=(1,))
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_offer_GET(user):
    Car.objects.create(id=1)
    c = Client()
    c.force_login(user)
    url = reverse('delete_offer', args=(1,))
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_send_message_GET(user):
    c = Client()
    c.force_login(user)
    url = reverse('send_message')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_send_message_GET(user):
    c = Client()
    c.force_login(user)
    url = reverse('send_message')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_send_message_POST(user):
    c = Client()
    c.force_login(user)
    url = reverse('send_message')
    response = c.post(url, {'to_user': 1, 'content': 'Hottentottenstottertrottelmutterbeutelrattenlattengitterkofferattentäter'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_message_list_GET(user):
    c = Client()
    c.force_login(user)
    url = reverse('message_list')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_about_GET(user):
    c = Client()
    c.force_login(user)
    url = reverse('about')
    response = c.get(url)
    assert response.status_code == 200
