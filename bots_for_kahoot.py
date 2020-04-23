from selenium import webdriver
import time;


# The user type here if he want array of names or fixed names
namesOption = input('0 - array of names \n1 - to fixed name : ');




# Verify if the user type a number
while not(namesOption.isdigit()) or ((str(namesOption) != '0') and (str(namesOption) != '1')):
    namesOption = input('0 - array of names \n1 - to fixed name : ');






# How many bots the user want
bots = input('Type how many bots do you want (max recomended: 8): ');


# Verify if the user type a number 
while not(bots.isdigit()):
    bots = input('Type how many bots do you want (max recomended: 8): ');





# The user type here the kahoot pin
pin = input('Enter the game pin : ');



# If the user want array of names
if(int(namesOption) == 0):



    # String with names separated with ","
    names = input("Type here the bots names (split the names using ',' without spaces): ");
    
    # Function that transform the string at array
    names = names.split(',');



    # Openning the Goole
    driver = webdriver.Chrome("C:/Users/samta/OneDrive/Programacao/Python/chromedriver.exe");




    for i in range(int(bots)):



        # Oppenning the google aba if is not the firts time
        if(i != 0):
            driver.execute_script("window.open('https://kahoot.it/v2/', '_blank')");
            driver.switch_to_window(driver.window_handles[i]);
            




        # Oppenning the Google aba if is the first time
        else:
            driver.get('https://kahoot.it/v2/');




        # Getting the game pin input
        game_pin_input = driver.find_element_by_name('gameId');

        # Typing the pin
        game_pin_input.send_keys(pin);




        # getting the btn to enter 
        btn_enter_pin = driver.find_element_by_tag_name('button');

        # Clicking
        btn_enter_pin.click();



        # Waiting loading time
        time.sleep(1.35);

        # getting the input to type the name
        name_input = driver.find_element_by_name('nickname');

        # Typing the name
        name_input.send_keys(names[i]);




        # Getting the button to enter the game
        btn_enter_name = driver.find_element_by_tag_name('button');

        # Clicking in the button
        btn_enter_name.click();












# If the option was 1
else:



    # Name
    name = input("Type here the bot name: ");
    


    # Oppenning the Google
    driver = webdriver.Chrome("C:/Users/samta/OneDrive/Programacao/Python/chromedriver.exe");




    for i in range(int(bots)):


        # Oppenning the google aba if is not the firts time

        if(i != 0):
            driver.execute_script("window.open('https://kahoot.it/v2/', '_blank')");
            driver.switch_to_window(driver.window_handles[i]);





        # Oppenning the Google aba if is the first time
        else:
            driver.get('https://kahoot.it/v2/');




        # Getting the game pin input
        game_pin_input = driver.find_element_by_name('gameId');

        # Typing the pin
        game_pin_input.send_keys(pin);




        # getting the btn to enter 
        btn_enter_pin = driver.find_element_by_tag_name('button');

        # Clicking
        btn_enter_pin.click();



        # Waiting the loading
        time.sleep(1.35);

        # getting the input to type the name
        name_input = driver.find_element_by_name('nickname');

        # Typing the name
        name_input.send_keys(name + str(i));




        # Getting the button to enter the game
        btn_enter_name = driver.find_element_by_tag_name('button');

        # Clicking in the button
        btn_enter_name.click();
