import unittest
from unittest.mock import Mock, patch
from assertpy import *
from src.sample.random_user import RandomUser
mock_result = {'results': [{'gender': 'female', 'name': {'title': 'Ms', 'first': 'Alvina', 'last': 'Castro'}, 'location': {'street': {'number': 6220, 'name': 'Avenida Brasil '}, 'city': 'Caxias do Sul', 'state': 'Ceará', 'country': 'Brazil', 'postcode': 26689, 'coordinates': {'latitude': '-77.2505', 'longitude': '160.3173'}, 'timezone': {'offset': '-8:00', 'description': 'Pacific Time (US & Canada)'}}, 'email': 'alvina.castro@example.com', 'login': {'uuid': '02d29033-226c-4a27-9c66-294a7fcc8ffd', 'username': 'happydog621', 'password': 'haggis', 'salt': 'kzXPkBJX', 'md5': 'f884acb12673af5447d03b3877743397', 'sha1': 'b75e54f7472ed8b23fd339d350a0a653a8a7f3cc', 'sha256': '11216b9cafc6e39fd132149d8a0d60a67e7874781423dc1ff7292f4ba6822502'}, 'dob': {'date': '1958-11-07T09:39:56.096Z', 'age': 62}, 'registered': {'date': '2013-05-17T03:48:27.306Z', 'age': 7}, 'phone': '(97) 7599-8530', 'cell': '(93) 5138-5397', 'id': {'name': '', 'value': None}, 'picture': {'large': 'https://randomuser.me/api/portraits/women/48.jpg', 'medium': 'https://randomuser.me/api/portraits/med/women/48.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/48.jpg'}, 'nat': 'BR'}], 'info': {'seed': '077aa1d7cbb8b953', 'results': 1, 'page': 1, 'version': '1.3'}}
mock_results = {'results': [{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Jerry', 'last': 'Bryant'}, 'location': {'street': {'number': 8144, 'name': 'School Lane'}, 'city': 'Bandon', 'state': 'Monaghan', 'country': 'Ireland', 'postcode': 82236, 'coordinates': {'latitude': '20.8279', 'longitude': '-62.4963'}, 'timezone': {'offset': '-9:00', 'description': 'Alaska'}}, 'email': 'jerry.bryant@example.com', 'login': {'uuid': '711db1ac-f285-44c5-babe-a125fb1c1822', 'username': 'sadtiger680', 'password': 'packers', 'salt': '8hFtrWt8', 'md5': '6f7c8938892be37f6b3c590255c114c4', 'sha1': '6ac99b881f473acb86f67bf8b027ed65a252ed7f', 'sha256': '7306ab00ec3b672024902630694cda6ee163f5e7e8f8be82b526203ff830e092'}, 'dob': {'date': '1948-07-03T01:50:46.380Z', 'age': 72}, 'registered': {'date': '2004-12-07T04:12:07.221Z', 'age': 16}, 'phone': '071-717-1511', 'cell': '081-133-4050', 'id': {'name': 'PPS', 'value': '9759218T'}, 'picture': {'large': 'https://randomuser.me/api/portraits/men/34.jpg', 'medium': 'https://randomuser.me/api/portraits/med/men/34.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/34.jpg'}, 'nat': 'IE'}, {'gender': 'female', 'name': {'title': 'Mrs', 'first': 'Neea', 'last': 'Peltonen'}, 'location': {'street': {'number': 8594, 'name': 'Hämeentie'}, 'city': 'Kouvola', 'state': 'Uusimaa', 'country': 'Finland', 'postcode': 20766, 'coordinates': {'latitude': '-67.6136', 'longitude': '-69.3525'}, 'timezone': {'offset': '-8:00', 'description': 'Pacific Time (US & Canada)'}}, 'email': 'neea.peltonen@example.com', 'login': {'uuid': '56081eb8-e32d-47ba-b72d-45e1b52ffeaa', 'username': 'yellowbutterfly337', 'password': 'dildo', 'salt': 'Rvi804PM', 'md5': 'd09c7d4d6c0e73e2ba4a43e92261c50e', 'sha1': 'd8c4d350094e32db68f60c27b7398aea59980b48', 'sha256': '59a4a8060b5239a70a769d431afbe902e9ffbb5cac491113d1ac1155a7d58718'}, 'dob': {'date': '1969-02-14T20:24:28.852Z', 'age': 51}, 'registered': {'date': '2004-06-29T20:59:00.746Z', 'age': 16}, 'phone': '06-190-470', 'cell': '041-325-15-64', 'id': {'name': 'HETU', 'value': 'NaNNA208undefined'}, 'picture': {'large': 'https://randomuser.me/api/portraits/women/75.jpg', 'medium': 'https://randomuser.me/api/portraits/med/women/75.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/75.jpg'}, 'nat': 'FI'}, {'gender': 'male', 'name': {'title': 'Mr', 'first': 'Emil', 'last': 'Christiansen'}, 'location': {'street': {'number': 8607, 'name': 'Granvænget'}, 'city': 'Billum', 'state': 'Danmark', 'country': 'Denmark', 'postcode': 52791, 'coordinates': {'latitude': '-37.0307', 'longitude': '167.4697'}, 'timezone': {'offset': '-3:00', 'description': 'Brazil, Buenos Aires, Georgetown'}}, 'email': 'emil.christiansen@example.com', 'login': {'uuid': '1472c82f-07c0-4154-828a-731e53425d42', 'username': 'sadbird926', 'password': 'sheepdog', 'salt': 'L9J81JJH', 'md5': '24ce603dfb8ef848f16c8c878ae9c35b', 'sha1': 'e57a82bdff7516f299d0e1df99ee491c961a7a22', 'sha256': 'a077ced5b5ca8d667ae3881c8000dde49d7d47b335e425696dfd5d41aa371cf7'}, 'dob': {'date': '1985-10-30T22:06:24.626Z', 'age': 35}, 'registered': {'date': '2014-09-12T02:48:30.535Z', 'age': 6}, 'phone': '07981799', 'cell': '69365668', 'id': {'name': 'CPR', 'value': '301085-8669'}, 'picture': {'large': 'https://randomuser.me/api/portraits/men/44.jpg', 'medium': 'https://randomuser.me/api/portraits/med/men/44.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/44.jpg'}, 'nat': 'DK'}], 'info': {'seed': 'ab996133e4f23540', 'results': 3, 'page': 1, 'version': '1.3'}}


class TestRandomUserMocks(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_get_random_user(self):
        with patch('src.sample.random_user.requests.get') as mock_get:
            mock_get.return_value.json.return_value = mock_result
            result = self.temp.get_random_user()
            assert_that(result).is_equal_to(mock_result["results"][0])

    def test_get_multiple_users(self):
        with patch('src.sample.random_user.requests.get') as mock_get:
            mock_get.return_value.json.return_value = mock_results
            result = self.temp.get_multiple_users(3)
            assert_that(result).is_length(3)

    def test_get_user_gender(self):
        with patch('src.sample.random_user.requests.get') as mock_get:
            mock_get.return_value.json.return_value = mock_result
            result = self.temp.get_random_user_gender("female")
            assert_that(result["gender"]).is_equal_to("female")

    def tearDown(self) -> None:
        self.temp = None


if __name__ == "__main__":
    unittest.main()
