#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 12:44:06 2022

@author: linuxlite
"""

from user_input import UserInput


class RacetrackMain:
    
    
    def __init__(self):
        #__ui=UserInput('BIKE', 'M04', '14:00')
        #print(__ui.__dict__)
        '''
        while True:  
            user_ip=input(">> ")'''
            
        with open('user_input_lines.txt','r') as f:
            for line in f.readlines():                   
                self.processs_booking(line.strip(" \n"))
        
    
    def booking_validation(self, vehicle_type, vehicle_num, entry_time):  
        #print(repr((vehicle_type, vehicle_num, entry_time),))
        if vehicle_type and vehicle_type.lower() in ['car','bike','suv']:
            if vehicle_num and len(vehicle_num)>=3:
                if self.check_time_range(entry_time):
                    return True
                else:
                    print("INVALID_ENTRY_TIME")
                    return False
        else:
            print('??>>')
        
    def process_additional(self, vehicle_num, end_time):
        print(repr((vehicle_num, end_time),))
        
    
    @staticmethod
    def check_time_range(time):
        global time_start, time_end
        
        hh=int(time.split(":")[0])
        if hh in range(13,18):
            return True
        else:
            return False
    
    
    def processs_booking(self,user_ip):        
        
        user_ip=user_ip.split(" ")
        
        if user_ip[0].lower()=='book':
            vehicle_type = user_ip[1]
            vehicle_num= user_ip[2]
            entry_time= user_ip[3]   
            
            if self.booking_validation(vehicle_type, vehicle_num, entry_time):
                ui=UserInput(vehicle_type, vehicle_num, entry_time)
                print(ui.__dict__)
            else:
                print('###')
        
                

if __name__=='__main__':
    o=RacetrackMain()
    
