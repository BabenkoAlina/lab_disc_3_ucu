"""Lab 3"""

import random

class State:
    """State"""
    def __init__(self):
        # initializing states
        # not random
        self.wake_up = self._create_wake_up()
        next(self.wake_up)
        self.eat = self._create_eat()
        next(self.eat)
        self.study = self._create_study()
        next(self.study)
        # random
        self.get_grades = self._create_get_grades()
        next(self.get_grades)
        self.write_poems = self._create_write_poems()
        next(self.write_poems)
        self.talk_to_people = self._create_talk_to_people()
        next(self.talk_to_people)
        # other states
        self.tired = self._create_tired()
        next(self.tired)
        self.sleep = self._create_sleep()
        next(self.sleep)
        self.life_hard = 0

        self.current_state = self.wake_up

        self.stopped = False

    def send(self, char):
        """The function sends the curretn input to the current state
        It captures the StopIteration exception and marks the stopped flag.
        """
        try:
            self.current_state.send(char)
        except StopIteration:
            self.stopped = True
    def generate_day(self):
        """The function iterates the State object."""
        for i in range(6, 24):
            if 6 <= i <= 12:
                print(f"---Time:{i} am---")
            elif 13<= i < 23:
                print(f"---Time:{i} pm---")
            else:
                print(f"---Time:{i} pm---")
                self.current_state = self.tired
            self.current_state.send(i)
            if self.current_state is self.sleep:
                break
        
    def _create_wake_up(self):
        while True:
            # once received store the input in `char`
            char = yield
            rand = round(random.random(), 2)
            print('Only 5 minutes... \n')
            if char == 7 or char == 13 or char == 18:
                # on receiving 7 or 13 or 18 the state moves to `eat`
                self.current_state = self.eat
                print("I`m going to trapezna. -> \n")
            elif 0 < rand <= 0.2:
                # on receiving random the state moves to `study`
                self.current_state = self.study
                print("I`m going to do discrete math. -> \n")
            elif 0.4 <= rand < 0.5:
                # on receiving random the state moves to `write_poems`
                self.current_state = self.write_poems
                print("I`m going to write a poem. -> \n")
            elif 0.5 <= rand < 0.7:
                # on receiving random the state moves to `get_grades`
                self.current_state = self.get_grades
                print("Let me see my CMS... -> \n")

    def _create_eat(self):
        while True:
            char = yield
            if char != 23:
                print("Now I`m in trapezna. \n")
                if char == 8 or char == 14 or char == 19:
                    # on receiving `8 or 14 or 19` the state moves to `study`
                    self.current_state = self.study
                    print("I`m going to do discrete math. -> \n")
                else:
                    self.current_state = self.study
            else:
                self.current_state = self.tired

    def _create_study(self):
        while True:
            char = yield
            rand = round(random.random(), 2)
            if char != 23:
                self.life_hard += 10
                print("Now I`m doing my homework. ")
                if self.life_hard < 0:
                    self.life_hard = 0
                print(f"My life is {self.life_hard} % hard now. \n")
                if self.life_hard > 90:
                    # if lise_hard > 90 - the state moves to `tired`
                    self.current_state = self.tired
                    print("...Low energy... \n")
                else:
                    if char == 13 or char == 18:
                        # on receiving `13 or 18` the state moves to `eat`
                        self.current_state = self.eat
                        print("I`m going to trapezna. -> \n")
                    elif 0.4 < rand < 0.6:
                        # on receiving random the state moves to `talk_to_people`
                        self.current_state = self.talk_to_people
                        print("I`m going to talk to people. -> \n")
                    elif 0 < rand <= 0.2:
                        # on receiving random the state moves to `write)poems`
                        self.current_state = self.write_poems
                        print("I`m going to write a poem. -> \n")
            else:
                self.current_state = self.tired


    def _create_talk_to_people(self):
        while True:
            char = yield
            rand = round(random.random(), 2)
            if char != 23:
                print("Now I`m talking to people.")
                self.life_hard -= 10
                if self.life_hard < 0:
                    self.life_hard = 0
                print(f"My life is {self.life_hard} % hard now. \n")
                if 0 < rand <= 0.6:
                    # on receiving random the state moves to `study`
                    self.current_state = self.study
                    print("I`m going to do discrete math -> \n")
                elif 0.7 < rand < 1:
                    # on receiving random the state moves to `get_grades`
                    self.current_state = self.get_grades
                    print("Let me see my CMS... -> \n")
                elif char == 13 or char == 18:
                    # on receiving `13 or 18` the state moves to `eat`
                    self.current_state = self.eat
                    print("I`m going to trapezna. -> \n")
            else:
                self.current_state = self.tired

    def _create_get_grades(self):
        while True:
            char = yield
            rand = round(random.random(), 2)
            if char != 23:
                print("Oh, i got my grades! They are nice!")
                self.life_hard -= 15
                if self.life_hard < 0:
                    self.life_hard = 0
                print(f"My life is {self.life_hard} % hard now.")
                if 0 < rand < 0.8:
                    # on receiving random the state moves to `write_poems`
                    self.current_state = self.write_poems
                    print("I`m going to write a poem. -> \n")
                elif char == 13 or char == 18:
                    # on receiving `13 or 18` the state moves to `study`
                    self.current_state = self.eat
                    print("I`m going to trapezna. -> \n")
            else:
                self.current_state = self.tired

    def _create_write_poems(self):
        while True:
            char = yield
            rand = round(random.random(), 2)
            if char != 23:
                print("Now I`m writing a poem. \n")
                if self.life_hard > 90:
                    print(f"My life is {self.life_hard} % hard now.")
                    self.current_state = self.sleep
                    print("...Low energy... \n")
                elif 0 < rand < 0.9:
                    # on receiving random the state moves to `study`
                    self.current_state = self.study
                    print("I`m going to do discrete math. -> \n")
                elif char == 13 or char == 18:
                    # on receiving `13 or 18` the state moves to `eat`
                    self.current_state = self.eat
                    print("I`m going to trapezna. -> \n")
            else:
                self.current_state = self.tired

    def _create_tired(self):
        while True:
            char = yield
            if char == 23:
                print("Sorry, no plans. Day is off.")
            else:
                print(print("I was so tired... Bye"))
            # the state moves to `sleep`
            self.current_state = self.sleep

    def _create_sleep(self):
        while True:
            yield
