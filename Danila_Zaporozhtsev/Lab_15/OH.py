import urllib.request
from bs4 import BeautifulSoup
import requests
import time
import threading


def temperature_from_meteofor():
    url = "https://meteofor.com.ua/weather-lviv-4949/"
    start_time = time.time()
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    temperature = soup.find('span', class_='unit unit_temperature_c').text.strip()
    print("Поточна температура за даними Meteofor.com.ua:", temperature)
    end_time = time.time()
    return end_time - start_time


def temperature_from_meta():
    url = "https://pogoda.meta.ua/ua/Lvivska/Lvivskiy/Lviv/"
    start_time = time.time()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    temperature = soup.find('div', class_='temp').text.strip()
    print("Поточна температура за даними Meta.ua:", temperature)
    end_time = time.time()
    return end_time - start_time


def temperature_from_sinoptik():
    url = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D1%96%D0%B2"
    start_time = time.time()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    temperature = soup.find('p', class_='today-temp').text.strip()
    print("Поточна температура за даними Sinoptik.ua:", temperature)
    end_time = time.time()
    return end_time - start_time



total_time_meteofor = 0
total_time_meta = 0
total_time_sinoptik = 0

for _ in range(5):
    total_time_meteofor += temperature_from_meteofor()
    total_time_meta += temperature_from_meta()
    total_time_sinoptik += temperature_from_sinoptik()


average_time_meteofor = total_time_meteofor / 5
average_time_meta = total_time_meta / 5
average_time_sinoptik = total_time_sinoptik / 5

print(f"Середній час виконання запиту для Meteofor.com.ua: {average_time_meteofor:.2f} секунд")
print(f"Середній час виконання запиту для Meta.ua: {average_time_meta:.2f} секунд")
print(f"Середній час виконання запиту для Sinoptik.ua: {average_time_sinoptik:.2f} секунд")


def get_all_temperatures_multithreaded():
    threads = []
    funcs = [temperature_from_meteofor, temperature_from_meta, temperature_from_sinoptik]
    for func in funcs:
        thread = threading.Thread(target=func)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


total_time_multithreaded = 0
for _ in range(5):
    start_time = time.time()
    get_all_temperatures_multithreaded()
    end_time = time.time()
    total_time_multithreaded += end_time - start_time

average_time_multithreaded = total_time_multithreaded / 5
print(f"Середній час виконання запитів в багатопотоці: {average_time_multithreaded:.2f} секунд")
