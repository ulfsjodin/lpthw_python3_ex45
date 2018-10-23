from sys import exit
from textwrap import dedent
import random_nums
#import slumptalen2

try:

    class Hall(object):
    
        def enter(self):
            print('Welcome to the Hall') 
            global svar 
            answer = input('choose a room to enter. ')
            return answer 
    
            exit(1)
    
    class Engine(object):
    
        def __init__(self, scene_map):
            self.scene_map = scene_map
    
        def play(self):
            current_scene = self.scene_map.opening_scene()
            last_scene = self.scene_map.next_scene('divide')
            
            scener = ['','',]
    
            while current_scene != last_scene:
                next_scene_name = current_scene.enter()
                if next_scene_name in Map.rum:
                    current_scene = self.scene_map.next_scene(next_scene_name)   
                    scener.append(next_scene_name)
    #                print(next_scene_name, 'next_scene_name')
    
                if next_scene_name == 'prev':
                    next_scene_name = scener[-2]
                    current_scene = self.scene_map.next_scene(next_scene_name)
    
                    print(next_scene_name, 'next_scene_name')
    
            current_scene.enter()
    
    points = 0
    class Plus(Hall):
    
    
        def enter(self):
            print('Plus'.center(20, '='))
            random_nums.random_math('plus')
            return 'hall'
    
    class Minus(Hall):
    
        def enter(self):
            print('Minus'.center(20, '='))
            random_nums.random_math('minus')
            return 'hall'
    
    class Multiply(Hall):
    
        def enter(self):
            print('Multiply'.center(20, '='))
            random_nums.random_math('multiply')
            return 'hall'
    
    class Divide(Hall):
    
        def enter(self):
            print('Divide'.center(20, '='))
            print('This is the end, Good job')
    
    
    
    class Map(object):
    
        rum = {
                'hall' : Hall(),
                'plus' : Plus(),
                'minus' : Minus(),
                'multiply' : Multiply(),
                'divide' : Divide(),
                }
    
        def __init__(self, start_scene):
            pass
            self.start_scene = start_scene
    
        def next_scene(self, scene_name):
            hej = Map.rum.get(scene_name)
            return hej
    
        def opening_scene(self):
            pass
            return self.next_scene(self.start_scene)
    
    
    a_map = Map('hall')
    a_game = Engine(a_map)
    a_game.play()
    
    if __name__ == "__main__":
        a_game.play()

except:
    print(' Good Bye!')
