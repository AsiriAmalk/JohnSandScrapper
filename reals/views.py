from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import numpy as np
from .models import Search

BASE_URL = "https://www.johnsand.co/for-sale/properties-available-in-london/{:d}/?sort_by=newest"


def get_page_count():
    site = "https://www.johnsand.co/for-sale/properties-available-in-london/?sort_by=newest"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, features="html.parser")
    return int(soup.find("span", {"class": "pagination__total-pages"}).text.split(" ")[1])


def get_card_list_for_site(site):
    #     site= "https://www.johnsand.co/for-sale/properties-available-in-london/?sort_by=newest"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, features="html.parser")

    cards = soup.find_all("article", {"class": "grid-item"})

    card_list = []

    for i in range(len(cards)):

        card = cards[i].text.strip().splitlines()
        url = cards[i].find_all(href=True)[0]['href']

        while ("" in card):
            card.remove("")
        for j in range(len(card)):
            card[j] = card[j].rstrip(" ")

        inter = card[3].split("(s)")
        while ("" in inter):
            inter.remove("")

        numbers = []

        #     a_string = inter[0]
        for a_string in inter:
            numbers.append([int(word) for word in a_string.split() if word.isdigit()])
        numbers = np.array(numbers).flatten()

        try:
            #         print(i)
            card.insert(3, numbers[0])
            card.insert(4, numbers[1])
        except:
            card.insert(3, "NA")
            card.insert(4, "NA")
        card.insert(5, url)
        card_list.append(card)
    return card_list

# def delete(request):


def home(request):
    if request.GET.get("delete_db") == "delete_db":
        Search.objects.all().delete()
        Search.objects.get()

    if request.GET.get("start") == "start":
        # print("hello")

        page_count = get_page_count()
        all_cards = []
        # get all_cards(page_count):
        for page_id in range(page_count):
            site_url = BASE_URL.format(page_id)
            all_cards.extend(get_card_list_for_site(site=site_url))

        for card in all_cards:
            card_ = Search(title=card[0],
                           address=card[1],
                           price=card[2],
                           beds=card[3],
                           bath=card[4],
                           link=card[5]
                           )

            card_.save()
        print("Scrapped")

    return render(request, 'base.html')
