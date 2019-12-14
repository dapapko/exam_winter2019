import requests
import geopy.distance
import json
import datetime

with open("settings.json", encoding='utf-8', errors='ignore') as settings_file:
    settings = json.load(settings_file)


class Trip:
    def __init__(self, points: list, car_type: str, baby: bool, animal: bool):
        self.points = points
        self.type: str = car_type
        self.baby: bool = baby
        self.animal: bool = animal
        self.length = 0
        self.price = 0

    @staticmethod
    def get_coordinates(address: str):
        try:
            url = f"https://geocode-maps.yandex.ru/1.x?geocode={address}&apikey={settings['apiKey']}&format=json"
            r = requests.get(url)
        except requests.exceptions.RequestException:
            return -1
        try:
            coordinates: list = r.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
        except KeyError:
            return -1
        return tuple(coordinates)

    @staticmethod
    def get_distance(src: str, dest: str):
        src_coords: int = Trip.get_coordinates(src)
        dest_coords: int = Trip.get_coordinates(dest)
        if src_coords == -1 or dest_coords == -1:
            return -1
        distance = geopy.distance.vincenty(src_coords, dest_coords).km
        return distance

    def get_overall_length_of_route(self):
        length: int = 0
        for i in range(0, len(self.points) - 1):
            print(f"From: {self.points[i]}")
            print(f"To: {self.points[i+1]}")
            dist = Trip.get_distance(self.points[i], self.points[i + 1])
            print(f"Distance: {dist}")
            length += dist
        self.length = length

    @staticmethod
    def is_between(number: int, lowerbound: int, upperbound: int):
        return lowerbound <= number <= upperbound

    def calculate_price(self):
        if self.length <= 0:
            self.price = 0
        minimal_price: int = settings["minimalPrice"]
        additional_services_cost = 0
        if self.baby:
            additional_services_cost += settings["babyChair"]
        if self.animal:
            additional_services_cost += settings["pet"]
        price: int = self.length * settings["perKilometerPrice"][self.type]
        current_date = datetime.datetime.now()
        landing_price = settings["landingPrice"][self.type]
        if Trip.is_between(current_date.hour, 22, 23) or Trip.is_between(current_date.hour, 0, 6):
            price = price * (settings["nightLandingPrice"] + 1)
            landing_price = landing_price * (settings["nightPerKilometerPrice"] + 1)
        if self.length > 10:
            price = price * settings["tenKilometeresCoefficient"]
        elif self.length > 15:
            price = price * settings["fifteenKilometeresCoefficient"]
        if price < minimal_price:
            price = minimal_price
        print(f"Distance: {self.length}")
        self.price =  price + landing_price + additional_services_cost
