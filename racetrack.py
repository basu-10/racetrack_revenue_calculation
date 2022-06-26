#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 21:27:51 2022

@author: linuxlite
"""

import csv

class Racetrack:
    
    additional_cost=50
    min_booking=3

    
    def __init__(self, type_of_vehicle, vehicle_num):       
        
        assert type_of_vehicle.lower() in ['car','bike','suv'], f"Invalid {type_of_vehicle=}"
        assert len(vehicle_num)>=3, f"Invalid length of {vehicle_num=}"
    
        self.vehicle_type=type_of_vehicle
        self.vehicle_num=vehicle_num
        
    
    #ideally, do this for the useer inputs kept in txt files
    @classmethod
    def instantiate_from_csv(cls):
        with open('rates_racetrack.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
            print(f"{items=}")
            for item in items:
                print(item.get('race_track_type'))
                print(item.get('vehicle_type'))
                print()
                
            
    
    
    
if __name__=='__main__':
    rc=Racetrack('SUV','m04',"14:00")
    print(rc.__dict__)
    #Racetrack.instantiate_from_csv()
