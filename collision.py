''' Brownian motion calculation link below '''
''' https://scipy-cookbook.readthedocs.io/items/BrownianMotion.html '''

import pygame
import random
import math
import numpy as np
from scipy.stats import norm

MATTER = 10
ANTIMATTER = 10

WIDTH = 400
HEIGHT = 300
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Particle collision model')
clock = pygame.time.Clock()

class Element:
    def __init__(self, color, x_boundary, y_boundary, size_range = (1, 2)):
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
    
    def move(self, delta = 0.25, dt = 0.1, magnify = 300):
        self.move_x = int(norm.rvs(scale = delta**2 * dt) * magnify)
        self.move_y = int(norm.rvs(scale = delta**2 * dt) * magnify)
        
        ''' Magnifier to blow up the number so that once it's turned into an integer, it can be read correctly '''
        
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 0:
            self.x = 0

        elif self.x > self.x_boundary:
            self.x = self.x_boundary

        if self.y < 0:
            self.y = 0

        elif self.y > self.y_boundary:
            self.y = self.y_boundary


class MatterElement(Element):
    def __init__(self, x_boundary, y_boundary):
        Element.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    def __add__(self, other_element):
        if other_element.color == (255, 0, 0):
            self.size = 0
            other_element.size = 0

        elif other_element.color == (0, 0, 255):
            pass
        else:
            ''' Here to make sure the colours used are actually correct '''
            raise Exception('Tried to combine one or multiple elements of unsupported colors.')

            
class AntimatterElement(Element):
    def __init__(self, x_boundary, y_boundary):
        Element.__init__(self, (255, 0, 0), x_boundary, y_boundary)
        

def is_touching(b1, b2):
    return np.linalg.norm(np.array([b1.x, b1.y]) - np.array([b2.x, b2.y])) < (b1.size + b2.size)

def handle_collisions(element_list):
    matters, antimatters = element_list
    for matter_id, matter_element, in matters.copy().items():
        for other_elements in matters, antimatters:
            for other_element_id, other_element in other_elements.copy().items():
                if matter_element == other_element:
                    pass
                else:
                    if is_touching(matter_element, other_element):
                        matter_element + other_element
                        if other_element.size <= 0:
                            other_elements[other_element_id] = AntimatterElement(WIDTH, HEIGHT)
                        if matter_element.size <= 0:
                            matters[matter_id] = MatterElement(WIDTH, HEIGHT)
    return matters, antimatters

def draw_environment(element_list):
    matters, antimatters = handle_collisions(element_list)
    
    game_display.fill(BLACK)
    for element_dict in element_list:
        for element_id in element_dict:
            element = element_dict[element_id]
            pygame.draw.circle(game_display, element.color, [element.x, element.y], element.size)
            for speed in range(15):
                element.move()
                element.check_bounds()
            
    pygame.display.update()
    return matters, antimatters

def main():
    matter_elements = dict(enumerate([MatterElement(WIDTH, HEIGHT) for i in range(MATTER)]))
    antimatter_elements = dict(enumerate([AntimatterElement(WIDTH, HEIGHT) for i in range(ANTIMATTER)]))

    matter_elements[0] + antimatter_elements[0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                quit()
                
        matter_elements, antimatter_elements = draw_environment([matter_elements, antimatter_elements])
        clock.tick(60)

if __name__ == '__main__':
    main()
   
