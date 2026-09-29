# Railway Ticket Booking System

## Project overview

This is a menu-based Python program for viewing trains, searching routes, booking tickets, checking bookings with a PNR, and cancelling tickets. Booking records are saved in `booking.txt`.

## Features

- View the available trains and their details
- Search for a train by starting point and destination
- Book tickets and calculate fares by travel class
- View bookings and check a booking using its PNR
- Cancel a booking and calculate the refund

## Technologies used

- Python
- `random` module for generating PNR numbers
- `os` module for checking whether the booking file exists
- Text file storage

## How to run

1. Install Python 3.
2. Download this repository to your computer.
3. Open a terminal in the downloaded project folder.
4. Run:

   `python HarshitUpadhyay_CSEProject_26BCE10839.py`

5. Follow the options shown in the program menu.

The program creates or updates `booking.txt` in the folder from which it is run.

## Testing instructions

Run the program and try each menu option: view trains, search for a route, book a ticket, cancel a ticket, view bookings, check a PNR, and view train details. Also try an invalid menu choice, train number, and PNR, and observe the messages.

## Current limitation

Booking records are saved between runs, but train seat availability resets to the original values when the program restarts.
