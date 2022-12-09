#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:12:14 2022

@author: raghav
"""
import sys
import time
import requests
from bs4 import BeautifulSoup

print("Welcome to RPi Availability Checker India")

models=["Pi 3a","Pi 3b","Pi 3a+","Pi 3b+","Pi 4b 2GB","Pi 4b 4GB","Pi 4b 8GB",
        "Pi Zero 2W"]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

pagesRobocraze={"Pi 3b":"https://robocraze.com/products/raspberry-pi-3b",
       "Pi 3b+":"https://robocraze.com/products/raspberry-pi-3b-1",
       "Pi 3a+":"https://robocraze.com/products/raspberry-pi-3-model-a",
       "Pi 4b 2GB":"https://robocraze.com/products/raspberry-pi-4-model-b-2gb-ram",
       "Pi 4b 4GB":"https://robocraze.com/products/raspberry-pi-4-model-b-4gb-ram",
       "Pi 4b 8GB":"https://robocraze.com/products/raspberry-pi-4-model-b-8-gb-ram"}
#Robu.in requires js to load, was not able to implement it.
"""
pagesRobu={"Pi 3b":"https://robu.in/product/latest-raspberry-pi-3-model-b-original/",
           "Pi 3a+":"https://robu.in/product/raspberry-pi-3-model-a/",
           "Pi 3b+":"https://robu.in/product/raspberry-pi-3-model-b-bcm2837b0-soc-iot-poe-enabled/",
           "Pi 4b 2GB":"https://robu.in/product/raspberry-pi-4-model-b-with-2-gb-ram/",
           "Pi 4b 4GB":"https://robu.in/product/raspberry-pi-4-model-b-with-4-gb-ram/",
           "Pi 4b 8GB":"https://robu.in/product/raspberry-pi-4-model-b-with-8-gb-ram/"}
"""
pagesFactoryForward={"Pi 3b":"https://www.factoryforward.com/product/raspberry-pi-3-model-b/",
                     "Pi 3a+":"https://www.factoryforward.com/product/raspberry-pi-3-model-a-plus/",
                     "Pi 3b+":"https://www.factoryforward.com/product/raspberry-pi-3-model-b-plus/",
                     "Pi 4b 2GB":"https://www.factoryforward.com/product/raspberry-pi-4-model-b-2gb/",
                     "Pi 4b 4GB":"https://www.factoryforward.com/product/raspberry-pi-4-model-b-4gb/",
                     "Pi 4b 8GB":"https://www.factoryforward.com/product/raspberry-pi-4-model-b-8gb-ram/"}

pagesSilverline={"Pi 3b":"https://www.silverlineelectronics.in/collections/raspberry-pi-3/products/raspberry-pi-3-model-b-1",
                 "Pi 3a+":"https://www.silverlineelectronics.in/collections/the-raspberry-pi/products/raspberry-pi-3-model-a-plus-silverline-india",
                 "Pi 3b+":"https://www.silverlineelectronics.in/collections/the-raspberry-pi/products/raspberry-pi-3-model-bplus-silverline-india",
                 "Pi 4b 2GB":"https://www.silverlineelectronics.in/collections/the-raspberry-pi/products/raspberry-pi-4-model-b-2gb",
                 "Pi 4b 4GB":"https://www.silverlineelectronics.in/collections/the-raspberry-pi/products/raspberry-pi-4-model-b-4gb-silverline-india",
                 "Pi 4b 8GB":"https://www.silverlineelectronics.in/collections/the-raspberry-pi/products/raspberry-pi-4-model-b-8gb-silverline-india"}

pagesThingbits={"Pi 3b":"https://www.thingbits.in/products/raspberry-pi-3-model-b",
                "Pi 3a+":"https://www.thingbits.in/products/raspberry-pi-3-model-a-plus",
                "Pi 3b+":"https://www.thingbits.in/products/raspberry-pi-3-model-b-1-4ghz-cortex-a53-with-1gb-ram",
                "Pi 4b 2GB":"https://www.thingbits.in/products/raspberry-pi-4-model-b-2-gb-ram",
                "Pi 4b 4GB":"https://www.thingbits.in/products/raspberry-pi-4-model-b-4-gb-ram",
                "Pi 4b 8GB":"https://www.thingbits.in/products/raspberry-pi-4-model-b-8-gb-ram"}

pagesCraziPi={"Pi 3b":"https://www.crazypi.com/raspberry-pi-products/raspberry-pi-latest-model-boards/raspberry-pi3-india-best-price",
              "Pi 3a+":"https://www.crazypi.com/raspberry-pi-products/raspberry-pi-latest-model-boards/raspberry-pi-3-model-a-plus-india",
              "Pi 3b+":"https://www.crazypi.com/raspberry-pi-products/raspberry-pi-latest-model-boards/raspberry-pi-3-model-b-plus-india",
              "Pi 4b 2GB":"https://www.crazypi.com/raspberry-pi-products/raspberry-pi-latest-model-boards/raspberry-pi4-with-2gb-ram",
              "Pi 4b 4GB":"https://www.crazypi.com/raspberry-pi-products/raspberry-pi-latest-model-boards/raspberry-pi4-with-4gb-ram",
              "Pi 4b 8GB":"https://www.crazypi.com/raspberry-pi-products/raspberry-pi-latest-model-boards/raspberry-pi4-with-8gb-ram"}

pagesEmbeddinator={"Pi 3b":"http://embeddinator.com/Welcome/detail/161",
                   "Pi 3b+":"http://embeddinator.com/Welcome/detail/162",
                   "Pi 4b 2GB":"http://embeddinator.com/Welcome/detail/164",
                   "Pi 4b 4GB":"http://embeddinator.com/Welcome/detail/165",
                   "Pi 4b 8GB":"http://embeddinator.com/Welcome/detail/165"}

sites=["Robocraze","Silverline Electronics","FactoryForward",
       "Thingbits","CrazyPi (Unofficial)","Embeddinator (Unofficial)"]
siteLinkList=[pagesRobocraze,pagesSilverline,pagesFactoryForward,
              pagesThingbits,pagesCraziPi,pagesEmbeddinator]
for a in range(len(sites)):
    print(f"\nChecking at {sites[a]}")
    pages=siteLinkList[a]
    for i in range(len(models)):
        try:
            page = requests.get(pages[models[i]])
        except KeyError:
            continue
        soup = BeautifulSoup(page.content, 'html.parser')
        pricing=""
        #Code for Robocraze
        if sites[a]=="Robocraze":
            for b in soup.findAll('button',
                                  attrs={'class':'btn product-form__cart-submit btn--secondary-accent'}):
                name=b.find('span')
            if name.text.strip()=="Add to cart":
                pricingData=soup.find('span',
                          attrs={'class','price-item price-item--sale'})
                pricing=pricingData.text.strip()
                availability="Available"
            else:
                availability="Sold Out"
        #Code for FactoryForward
        elif sites[a]=="FactoryForward":
            for b in soup.findAll('span',
                                  attrs={'class':'product-stock'}):
                name=b.find('span')
            if name.text.strip()=="Out of stock":
                availability="Sold Out"
            else:
                availability="Available"
        #Code for Silverline
        elif sites[a]=="Silverline Electronics":
            for b in soup.findAll('p',
                                  attrs={'class':'product-inventory'}):
                name=b.find('span')
            if name.text.strip()=="Out of stock":
                availability="Sold Out"
            else:
                availability="Available"
        #Code for Thingbits
        elif sites[a]=="Thingbits":
            for b in soup.findAll('div',
                                  attrs={'class':'text-uppercase price'}):
                name=b.find('span',
                            attrs={'class':'h5'})
            if (name.text.strip()=="In Stock" or name.text.strip()=="Backordered"):
                pricingData=soup.find('span',
                                      attrs={'class','h3 pr-1'})
                pricing=pricingData.text.strip()
                if name.text.strip()=="In Stock":
                    availability="Available"
                else:
                    availability="Backordered"
            else:
                availability="Sold Out"
        #Code for CrazyPi
        elif sites[a]=="CrazyPi (Unofficial)":
            for b in soup.findAll('div',
                                  attrs={'class':'inner-box-desc'}):
                name=b.find('div',attrs={"class":"stock"})
            if name.text.strip("Availability: ")=="In Stock":
                pricingData=soup.find('span',
                                      attrs={'class','price-new'})
                pricing=pricingData.text.strip()
                availability="Available"
            else:
                availability="Sold Out"
        #Code for Embeddinator
        elif sites[a]=="Embeddinator (Unofficial)":
            for b in soup.findAll('div',
                                  attrs={'class':'pr_switch_wrap'}):
                x=b.find('div')
                name=x.find('span')
            if name.text.strip("Availability: ")=="In Stock":
                pricingData=soup.find('span',
                                      attrs={'class','price'})
                pricing=pricingData.text.strip()
                availability="Available"
            else:
                availability="Sold Out"
        #Adding terminal colors in platforms other than windows
        if sys.platform!="win32":
            if availability=="Available":
                availability=f"{bcolors.OKGREEN}Available{bcolors.ENDC}"
            elif availability=="Backordered":
                availability=f"{bcolors.OKCYAN}Backordered{bcolors.ENDC}"
            elif availability=="Sold Out":
                availability=f"{bcolors.FAIL}Sold Out{bcolors.ENDC}"
        print(models[i]+":",availability,pricing)

print("\nThank you for using RPi Availability checker India")
print("Note: Robu.in is not checked due to some technical reasons")
print("\nClosing automatically in 60 Seconds")
time.sleep(60)
