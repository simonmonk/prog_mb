from microbit import *

class Menu:

    def __init__(self, choices):
        self.choices = choices
        self.selection = 0
        self.num_choices = len(choices)

    def __watch_for_selection(self):
        if button_a.was_pressed():
            self.selection += 1
            if self.selection >= self.num_choices:
                self.selection = 0
            key = list(self.choices)[self.selection]
            display.scroll(key, loop=True, wait=False)
        
    def ask(self):
        key = list(self.choices)[self.selection]
        display.scroll(key, loop=True, wait=False)
        while button_b.was_pressed() == False:
            self.__watch_for_selection()
        key = list(self.choices)[self.selection]
        return self.choices[key]
            
yes_no_menu = Menu({"Yes" : True, "No" : False})
