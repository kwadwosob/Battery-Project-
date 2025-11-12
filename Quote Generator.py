"""
Author : Kwadwo Sarpong
Date : 11/12/205
Subject: Quote generator for 4Sons Cleaning
"""

#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt

class Cost:
    def __init__(self, labor_cost, supplies_cost, transportation_cost, markup):
        self.labor_cost = labor_cost
        self.supplies_cost = supplies_cost
        self.transportation_cost = transportation_cost
        self.markup = markup

    def total_cost(self):
        return self.labor_cost + self.supplies_cost + self.transportation_cost + self.markup
    
    # def markup(self):
        
        

quote = Cost(200, 10, 30, 40)
print(quote.total_cost())