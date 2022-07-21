# -*- coding: utf-8 -*-

# Function to test a Get_Data function for various types of input. function only accepts a input as positive integer greater than 0
# Function will continue calling it in a loop and shows the error until it reaches to valid input.

import project
from project import Get_Data, Get_Day, Get_Time
from unittest.mock import Mock, patch



def test_Get_Data():
    with patch('builtins.input', new=Mock(side_effect=['!%', 'abc', -3, 0, 2, '"§b3', '*/'])):
        assert Get_Data() == 2                                                                    
        



def main():
    test_Get_Data()
    
    
if __name__== "__main__":
    main()
