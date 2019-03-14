## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_product
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_brand
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_product
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_brand
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_restaurant
    - utter_goodbye

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_product
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_brand
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_product
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_brand
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - export


## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_brand
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* affirm
    - utter_goodbye
    - export

## Generated Story -1081030314473945414
* greet
    - utter_greet
* restaurant_search
    - utter_ask_brand
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_product
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": "300"}
    - action_restaurant
    - slot{"location": "jabalpur"}
    - action_restaurant
    - slot{"location": "jabalpur"}
    - utter_goodbye
    - export