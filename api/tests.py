from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from .resources import APITestResources

User = get_user_model()


# Create your tests here.
class RentAPITestCase(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create(
            username='testname',
            email='example@example.com',
            is_staff=True
        )
        user.set_password('password')
        user.save()
        self.client.login(username='testname', password='password')

        url = api_reverse('api:category')
        data = APITestResources().get_dataname()
        self.client.post(url, data, format='json')

        url = api_reverse('api:role')
        data = APITestResources().get_dataname()
        self.client.post(url, data, format='json')

        url = api_reverse('api:staff-create')
        data = APITestResources().get_datastaff()
        self.client.post(url, data, format='json')

        url = api_reverse('api:filmtype')
        data = APITestResources().get_dataname()
        self.client.post(url, data, format='json')

        url = api_reverse('api:film-create')
        data_film = APITestResources().get_datafilm()
        data_film['title'] = 'title2'
        self.client.post(url, data_film, format='json')

        url = api_reverse('api:account')
        data = APITestResources.get_datauser()
        self.client.post(url, data, format='json')

        return super().setUp()

    def test_rent_cu(self):
        # Create
        url = api_reverse('api:film')
        get_response_before = self.client.get(url, format='json')

        url = api_reverse('api:rent-create')
        data = APITestResources.get_datarent()
        create_response = self.client.post(url, data, format='json')

        self.assertEqual(
            create_response.status_code, status.HTTP_201_CREATED
        )

        url = api_reverse('api:film')
        get_response = self.client.get(url, format='json')
        self.assertEqual(
            get_response_before.data['results'][0]['availability'] - 1,
            get_response.data['results'][0]['availability']
        )

        # Update
        data_id = create_response.data['id']
        url = api_reverse('api:rent-up-del', kwargs={'id': data_id})
        data = APITestResources.get_datarent_update()
        update_response = self.client.put(url, data, format='json')
        self.assertEqual(
            update_response.status_code, status.HTTP_200_OK
        )

        data['return_day'] = APITestResources.get_datarent_update_error()
        update_response = self.client.put(url, data, format='json')
        self.assertEqual(
            update_response.status_code, status.HTTP_400_BAD_REQUEST
        )
