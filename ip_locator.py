from geolite2 import geolite2
import requests
import pygeoip

def my_ip_location(my_ip):
    reader = geolite2.reader()
    location = reader.get(my_ip)

    #geolite database dict values and fine tunning
    a=(location['city']['names']['en'])
    d=(location['location'])

    string = ("City: %s  |  Location: %s" % (a,d))
    return string

def find_ip():
    return requests.get('https://api.ipify.org').text



# pip install maxminddb-geolite2