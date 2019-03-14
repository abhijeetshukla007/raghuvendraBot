
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pandas as pd
from custom_rasa_utills import getTierOneTierTwo
from SendEmail import emailconfig
import requests
import logging
import item

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_restaurant'

    def getcitytype(self, loc):
        output = pandas.read_csv("./data/citytype.csv")
        return True;

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot('product')
        brand = tracker.get_slot('brand') 
        response = item.item.getLocationFromProductName(brand,product)
        if response  is None:
           response = "looks like we dont have this product avialble in the store 1375" 
        dispatcher.utter_message("-----" + str(response))
        return [SlotSet('product', None), SlotSet('brand',None)]
       

  


class ActionSearchDescription(Action):
    def name(self):
        return 'action_description'

    def getcitytype(self, loc):
        output = pandas.read_csv("./data/citytype.csv")
        return True;

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot('product')
        brand = tracker.get_slot('brand')
        response = str("DEF") +  str(item.item.productDetailsFromBarcode(product))
        dispatcher.utter_message(response)
        return [SlotSet('product', None), SlotSet('brand',None)]


