import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint

headers = {"Accept-Language": "en-US, en;q=0.5"}

# main url for programming jobs https://weworkremotely.com/categories/remote-programming-jobs#job-listings