import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

def get_html_from_link(page_link):
    '''
        Get HTML from web page and parse it.

        :param page_link: link of the webpage we want to scrap
        :type page_link: string
        :return: BeautifulSoup object (HTML parsed)
        :rtype: bs4.BeautifulSoup
    '''
   
    response = requests.get(page_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_links_to_movies(root_html):
    '''
        Extract book links from URL_BOOK_LISTE

        :param root_html: BeautifulSoup Element that contains all books links
        :type book_html: bs4.BeautifulSoup
        :return: List of all book links in the page
        :rtype: list(str)
    '''
    movie_links = []

    for element in root_html.find_all('a'):
        try:
            ref = element['href']
        except KeyError:
            print(f"Error with tag a : \n{element} \nit might not contain any href")
        if '/film/' in ref and 'critiques' not in ref and 'seances' not in ref:
            movie_links.append(ref)

    return movie_links



def extract_movie_info(movie_html):

        movie_title = movie_html.find('h1', {"itemprop": "name"}).text.strip() #strip enlève les tabulations et les espaces
        
        movie_release_date = movie_html.find('small', {"class": "pvi-product-year"}).text.strip()
    
        
        if movie_html.find('span', {'class': 'pvi-scrating-value'}) is None:
            movie_rating = 'Non indiqué'
        else:
            movie_rating = movie_html.find('span', {'class': 'pvi-scrating-value'}).text.strip()
            
            
        movie_director = movie_html.find('span', {"itemprop": "director"}).text.strip()
        
        
        if movie_html.find('span', {"itemprop": "genre"}) is None:
            movie_gender = 'Non indiqué'
        else:
            movie_gender = movie_html.find('span', {"itemprop": "genre"}).text.strip()
        
     
        if movie_html.find('span', {'class': "d-offset ecot-contact-label", 'itemprop': "name"}) is None:
            movie_actors = 'Non indiqué'
        else:
            movie_actors = movie_html.find('span', {'class': "d-offset ecot-contact-label", 'itemprop': "name"}).text.strip()
            
        
        return movie_title, movie_release_date, movie_rating, movie_director, movie_gender, movie_actors    


URL_MOVIE_BASE = 'https://www.senscritique.com/'
URL_MOVIE_LISTE = '/films/tops/top111/?p={page_number}'

page_number = 1
page_link = f'https://www.senscritique.com/films/tops/top111/?p={page_number}'
print(get_html_from_link(page_link).prettify())