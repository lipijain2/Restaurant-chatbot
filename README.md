# Restaurant-chatbot

## Introduction 
  This repository contains the code used to build a simple chatbot which is used for making reservations for a restaurant. The framework used for this project is [Rasa Open Source](https://rasa.com/docs/rasa/).
## Description
The chatbot is designed using an open source machine learning framework `RASA`. The chatbot uses `Rasa forms` to extract essential imformation required for making reservation. Chatbot asks questions to the user about number of seats required, section(AC/Non-AC) in which reservation is to be made and timings dor the reservation. The restaurant opens at 7pm and closes at 10pm, so if user enter time other than this then that time will get rejected and bot will ask the user to enter a valid time. `Duckling Entity Extractor` is used to extract time from the user input and action module is used to handle the logic of time validation. In additon to this, the bot is also capable of handing some frequently asked questions(FAQs) which when asked by the user, is appropriately answered by the bot .

## Installation 
   
   In order to use chatbot, the user must have `LINUX` environment with python installed in it.

1. `Rasa Installation`

    Run `setup.py` using the following command in your terminal. This will create a fresh virtual environment `venv` in which rasa will get installed.
    ```
    $ python3 setup.py
    ```
    You can also use https://rasa.com/docs/rasa/user-guide/installation/ for rasa installation if you face any problem in installation using above process.

2. `Duckling Installation`

    Run the following commands in your terminal to install duckling entity extractor which is used to handle time validation:
    ```
    $ wget -qO- https://get.haskellstack.org/ | sh
    $ sudo apt-get install libpcre3 libpcre3-dev
    $ git clone https://github.com/facebook/duckling.git
    $ cd duckling
    $ stack build
    ```
## To run rasa 

1. `Run Duckling`

    To run duckling on your system run the following commands in the terminal:
    ```  
    $ cd Duckling                 
    $ stack exec duckling-example-exe
    ```
2. `Run Actions Server`

    To run actions server on your system run the following commands in new terminal:
    ```
    $ . ./venv/bin/activate
    $ python -m rasa_sdk.endpoint —actions actions
    ```
3. ` Run rasa`

     After running duckling and acions server the final step is to run rasa on your system. Now, to run rasa chatbot run the following commands in new terminal.
     ```
     $ . ./venv/bin/activate
     $ rasa shell —endpoints endpoints.yml
    ```
## Supported FAQs
1. Timings of the restaurant
2. Workings days of the restaurant
3. Specials of the restaurant
4. Booking cancellation procedure






