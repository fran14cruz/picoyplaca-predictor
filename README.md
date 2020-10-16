# picoyplaca-predictor
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