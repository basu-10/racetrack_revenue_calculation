#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 12:35:53 2022

race_track_type,vehicle_type,max_vehicles_allowed,cost_per_hour

@author: linuxlite
"""

from racetrack import Racetrack

class UserInput(Racetrack):
    #take ip
    
    def __init__(self, vehicle_type, vehicle_num, entry_time):  
        
        assert self.check_time_range(entry_time),f"Invalid {entry_time=}"        
        self.entry_time=entry_time
        
        super().__init__(vehicle_type, vehicle_num)
        
        
    
    
    
        
    @staticmethod
    def check_time_range(time):
        global time_start, time_end
        
        hh=int(time.split(":")[0])
        if hh in range(13,19):
            return True
        else:
            return False
        
        
        
if __name__=='__main__':
    uip=UserInput('SUV','m04',"14:00")
    print(uip.__dict__)
