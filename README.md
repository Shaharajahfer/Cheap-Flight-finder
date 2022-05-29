
# Cheap Flight finder


## Description

Build a python application which uses OOP, Sheety API, Tequila API and Twilio API to send SMS texts if flights for desired destination fall below a certain price.


## Steps

- Having a google sheet which tracks the locations we want to visit and the price cut off.
- A flight search API is searching through all locations and looking for cheapest flight for the next 6 months.
- If it finds a flight that is cheaper than the predefined price, then it sends a message to our mobile phone through Twilio sms module

