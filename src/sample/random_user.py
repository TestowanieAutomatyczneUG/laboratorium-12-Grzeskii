import requests


class RandomUser:

    def __init__(self):
        self.url = "https://randomuser.me/api/"

    def get_random_user(self):
        result = requests.get(self.url)
        data = result.json()["results"][0]
        return data

    def get_multiple_users(self, number):
        if type(number) is not int:
            raise TypeError("Wrong type")
        result = requests.get(self.url + f"?results={number}")
        data = result.json()["results"]
        return data

    def get_random_user_gender(self, gender):
        if gender != "male" and gender != "female":
            raise ValueError("Wrong gender")
        result = requests.get(self.url + f"?gender={gender}")
        data = result.json()["results"][0]
        return data
