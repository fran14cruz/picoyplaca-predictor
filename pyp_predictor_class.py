'''
This script defines a class describing a predictor for "Pico y Placa".
"Pico y Placa" is a restriction for the use of ground transportation in Quito, Ecuador.
It consists of the following rules:
- Vehicles cannot circulate from 07:00 to 09:30 and in the afternoon from 16:00 to 19:30.
- The ciculation schedule responds to the last digit of the vehicle plate:
    * Monday, Wednesday, Friday: 1, 3, 5, 7, 9.
    * Tuesday, Thursday, Saturday: 2, 4, 6, 8, 0.
    * Sunday: no private vehicles can circulate.
Example:
A vehicle with plate PCQ-8981, the last digit is 1
According to the "Pico y Placa" rule, this vehicle cannot circulate on Mondays from 07:00
to 09:30 and in the afternoon from 16:00 to 19:30.
Other than these hours, the vehicle can circulate with no problems in Quito.

Francisco Cruz - GitHub: @fran14cruz
'''
from datetime import datetime   # module to work with dates as date objects
import re   # regular expressions for validation

# Object
class Pyp_predictor:
    '''This is a class for the Pico y Placa predictor'''
    __oddDays = ['Monday', 'Wednesday', 'Friday']   # Monday, Wednesday, Friday: 1, 3, 5, 7, 9.
    __evenDays = ['Tuesday', 'Thursday', 'Saturday']   # Tuesday, Thursday, Saturday: 2, 4, 6, 8, 0.

    # Constructor
    def __init__(self, license_no='', date='', time=''):
        self.__license_no = license_no   # license plate number
        self.__date = date
        self.__time = time

    # Setters
    def set_license_no(self, license_no):
        self.__license_no = license_no

    def set_date(self, date):
        self.__date = date

    def set_time(self, time):
        self.__time = time

    # Getters
    def get_license_no(self):
        return self.__license_no

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    # Method: introduction message
    def intro_msg(self):
        print("** Welcome to the Pico y Placa Predictor! **\n")

    # Method: user input
    def user_input(self):
        self.__license_no = self.validate_plate_no()
        
        date_format = "%d-%m-%Y"
        time_format = "%H:%M"

        date_entry_msg = "Enter date in DD-MM-YYYY format: "
        time_entry_msg = "Enter time in HH:MM format: "

        date_entry = self.validate_datetime(date_entry_msg, date_format)   # date entry
        time_entry = self.validate_datetime(time_entry_msg, time_format)   # time entry

        date_time_str = "{} {}".format(date_entry, time_entry)
        date_time_obj = datetime.strptime(date_time_str, "%d-%m-%Y %H:%M")   # create datetime object based on user input
        
        self.__date = date_time_obj.strftime("%A, %d.%m.%Y")   # assign date
        self.__time = date_time_obj.strftime("%H:%M")   # assign time

        return date_time_obj

    # Method: display user input
    def display_input(self):
        print("\nLicense no.: {}".format(self.__license_no), end='\n')
        print("Date: {}".format(self.__date))
        print("Time: {}".format(self.__time))

    # Method: determine result
    def det_result(self):
        date_time_obj = self.user_input()   # call user input
        self.display_input()   # display user input

        day = date_time_obj.strftime("%A")   # store day as a string
        last_digit = int(self.__license_no[-1])   # last digit plate number extraction

        time_obj = date_time_obj.time()   # get time object

        if day == 'Sunday':
            print("If this is a private vehicle, it cannot circulate.")
        elif day in self.__oddDays and last_digit % 2 != 0 and not self.in_time_range(time_obj):
            print("This vehicle cannot circulate.")
        elif day in self.__evenDays and last_digit % 2 == 0 and not self.in_time_range(time_obj):
            print("This vehicle cannot circulate.")
        else: 
            print("This vehicle can circulate. Have a nice trip!")

    # Method: check time
    def in_time_range(self, time):
        flag = True
        time_limits = ['7:00', '9:30', '16:00', '19:30']   # define time limits
        time_limits_obj = []   # time limits datetime object
        for hour in time_limits:
            time_limits_obj.append(self.convert_to_time(hour))
        
        if (time >= time_limits_obj[0] and time <= time_limits_obj[1]) or (time >= time_limits_obj[2] and time <= time_limits_obj[3]):
            flag = False
        
        return flag
    
    # Method: convert string to time
    def convert_to_time(self, time):   # time is a string
        datetime_obj = datetime.strptime(time, "%H:%M")
        time_obj = datetime_obj.time()

        return time_obj

    # Method: value plate number (Ecuador format: AAA-1111)
    def validate_plate_no(self):
        while True:
            license_no = input("Please, enter your license plate number: ")
            if not re.match("^[A-Za-z]{3}-[0-9]{4}$", license_no):
                print("Invalid plate number!")
                continue
            else:
                break

        return license_no

    # Method: validate date and time input
    def validate_datetime(self, msg, v_format):
        while True:
            try:
                user_entry = input(msg)
                valid_date = datetime.strptime(user_entry, v_format)
            except ValueError:
                print("Invalid input format!")
                continue
            else:
                break
        return user_entry


def main():
    prediction = Pyp_predictor()
    prediction.intro_msg()
    prediction.det_result()

if __name__ == '__main__':
    main()