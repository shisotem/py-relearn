import os

from roboter import recommendation
from roboter import restaurant_data_manager
from roboter import utils


user_name = input('< Hello, I am Roboko. What is your name?\n> ')

if utils.is_data_present('ranking.csv'):
    next_recommendation_index = 0
    while next_recommendation_index >= 0:
        recommendation.recommend_restaurant(next_recommendation_index)
        if recommendation.is_preferred():
            break
        next_recommendation_index = recommendation.update_next_recommendation_index(
            next_recommendation_index
        )

new_restaurant = input(f'< {user_name}, which restaurants do you like?\n> ')
restaurant_data_manager.add_restaurant_vote(new_restaurant)
restaurant_data_manager.sort_restaurant()
print(f'> Thank you so much, {user_name}!\n> Have a good day!')
