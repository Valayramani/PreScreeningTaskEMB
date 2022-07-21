# -*- coding: utf-8 -*-
# Function to test a Get_Day function for various types of input. function only accepts a date in particular formate (DD.MM.YYYY).
# Function will continuously ask user to input a date until it gets valid date in valid formate.


import project
from project import Get_Data, Get_Day, Get_Time
from unittest.mock import Mock, patch


def test_Get_Day():
    with patch('builtins.input', new=Mock(side_effect=['10.16.2022', '61.10.2022', '!a:200', '10.06.201136', '10:10:2020', '10.05.2022', '201.01.2030'])):
        assert Get_Day() == '10.05.2022'
        



def main():
    test_Get_Day()
    
    
if __name__== "__main__":
    main()
