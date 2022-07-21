# -*- coding: utf-8 -*-
# Function to test a Get_Time function for various types of input. function only accepts a Time in particular formate (HH:MM).
# Function will continuously ask user to input a time until it gets valid time in valid formate.


import project
from project import Get_Data, Get_Day, Get_Time
from unittest.mock import Mock, patch


def test_Get_Time():
    with patch('builtins.input', new=Mock(side_effect=['30:30', '12:61', '06.15', '20:45', 'gh:30', '?'])):
        assert Get_Time() == '20:45'
        
        


def main():
    test_Get_Time()
    
    
if __name__== "__main__":
    main()
        
    

