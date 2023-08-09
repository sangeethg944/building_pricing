from io import BytesIO
from PIL import Image
from urllib import request
import datetime
import re
import os

API_KEY = os.getenv('API_KEY')
scale = 2
zoom = 18
save_folder = r"area_estimation/satellite_images/"


def get_satellite_image(address):
    address = re.sub('[/&]', "", address)
    address = address.replace(" ", "+")

    # Terrain maptypes = terrain, roadmap, hybrid, satellite
    URL = "http://maps.googleapis.com/maps/api/staticmap?center=" + str(address) + "&visible=" + str(
        address) + "&scale" + str(scale) + "&size=800x800&maptype=satellite" + "&zoom=" + str(
        zoom) + "&markers=%7Ccolor:blue%7C" + str(
        address) + "&sensor=true&key=AIzaSyAc-OW5YRq7WlQuiG2s3bkGCo_hQEiSL8A"

    buffer = BytesIO(request.urlopen(URL).read())
    image = Image.open(buffer)

    basename = "satellite"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix])
    image.save(save_folder + filename + ".PNG")
    return buffer



