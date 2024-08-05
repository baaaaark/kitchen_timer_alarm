# Kitchen Timer App

A simple kitchen timer assistant built with Python and Tkinter.  Ultimately designed for Raspberry Pi, this is the minimally viable product of what will some day be a more fully featured  kitchen assistant.

## Description

This project is currently a GUI-based timer application that allows users to add, manage, and delete timers.  In addition, every time an alarm is created, deleted, or expires, the app sends an API call to a custom back-end program, and ultimately stored into an event-driven database.

## Project Idea

This is the start of a somewhat ambitious home automation system, which will ultimately allow for all kinds of household events to be recorded in a event-sourced database.  The main goal to this is twofold: to be able to record raw data for visualization, but also to create a household-wide alert and notification system for a variety of household events.

## Future Improvements / Priority List

1. Integrate custom timers for common household events (dishwasher, brewing tea or coffee, etc.)
2. Create an alarm-style timer that will give alerts at a specific date/time.
3. Create a parent task/event class for the above data types to inherit, and implementing interfaces where appropriate
4. Using the GPIO pins on the Pi to connect high-temp thermometers, allowing for notifications when the oven or food reaches a certain temperature.
5. A feature to store HTML files of recipes and cooking guides from websites, to have available for quick reference.
