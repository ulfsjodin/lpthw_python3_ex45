#Här kommer ett nytt spel inom kort
from sys import exit
from textwrap import dedent
from random import randint


class Hall(object):

    def enter(self):
        print('welcome') 
        svar = input('skriv vilket rum du vill in i :> ')
        return svar 

        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('trollen')
        
        scener = ['','',]

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            if next_scene_name in Map.rum:
                current_scene = self.scene_map.next_scene(next_scene_name)   
                scener.append(next_scene_name)
                print('while if')
                print(scener)

            if next_scene_name == 'prev':
                next_scene_name = scener[-2]
                print(next_scene_name, 'next_scene_name_2')
                current_scene = self.scene_map.next_scene(next_scene_name)
                current_scene.enter() 

        current_scene.enter()


class Plus(Hall, Engine):
    """Kanske det är här? Men någon extra funktion?"""

    def enter(self):
        print('Plus'.center(20, '='))
        svar = input('skriv vilket rum du vill in i :> ')
        return svar 

class Minus(Hall):

    def enter(self):
        print('Minus'.center(20, '='))
        svar = input('skriv vilket rum du vill in i :> ')
        return svar 

class Multiply(Hall):

    def enter(self):
        print('Multiply'.center(20, '='))
        svar = input('skriv vilket rum du vill in i :> ')
        return svar 

class Divide(Hall):

    def enter(self):
        print('Divide'.center(20, '='))
        svar = input('skriv vilket rum du vill in i :> ')
        return svar 

class Eqvation(Hall):

    def enter(self):
        print('Eqvation i rutan') 
        print('Plus'.center(20, '='))

class Troll(Hall):

    def enter(self):
        print('Nu tog trollen dig')
        print('Troll'.center(40, '='))
        return 'eqvation'


class Map(object):

    rum = {
            'hallen' : Hall(),
            'plus' : Plus('hall'),
            'minus' : Minus(),
            'multiply' : Multiply(),
            'divide' : Divide(),
            'eqvation' : Eqvation(),
            'trollen' : Troll()
            }

    def __init__(self, start_scene):
        pass
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        hej = Map.rum.get(scene_name)
        return hej

    # Kanske man ska börja här i Map?
    def previous_scene(self):
        pass

    def opening_scene(self):
        pass
        return self.next_scene(self.start_scene)


a_map = Map('hallen')
a_game = Engine(a_map)
a_game.play()

