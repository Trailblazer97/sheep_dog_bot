import numpy as np
import random
import math


class SheepDog:
    def __init__(self):
        
        
        self.d1 = 1
        self.d2 = 2
        self.s = 3
        self.playground = np.zeros((8, 8))
        # self.sheep_pos = (random.randint(0, 7), random.randint(0, 7))
        self.sheep_pos = (4, 0)
        self.playground[self.sheep_pos] = 3
        # self.dog1_pos = (random.randint(0, 7), random.randint(0, 7))
        self.dog1_pos = (6, 3)
        # self.dog2_pos = (random.randint(0, 7), random.randint(0, 7))
        self.dog2_pos = (0, 7)
        
        self.occupied = np.zeros((8, 8))
        self.occupied[self.sheep_pos] = 1
        while self.sheep_pos == self.dog1_pos:
            self.dog1_pos = (random.randint(0, 7), random.randint(0, 7))
        while self.dog2_pos == self.dog1_pos and self.dog2_pos == self.sheep_pos:
            self.dog2_pos = (random.randint(0, 7), random.randint(0, 7))
        self.occupied[self.dog1_pos] = 1
        self.occupied[self.dog2_pos] = 1
        self.playground[self.dog1_pos] = 1
        self.playground[self.dog2_pos] = 2
        print(self.playground)
        # self.orderMovement = [""]

        
    def move_sheep(self): 

        change = self.select_dir()
        while self.occupied[self.sheep_pos[0] + change[0], self.sheep_pos[1] + change[1]] != 0 or not self.possible_move(self.sheep_pos, change):
            change = self.select_dir()
        
        self.occupied[self.sheep_pos] = 0
        self.playground[self.sheep_pos] = 0
        self.sheep_pos = self.sheep_pos[0] + change[0], self.sheep_pos[1] + change[1]
        self.occupied[self.sheep_pos] = 1
        self.playground[self.sheep_pos] = 3
        print(self.playground)
        input()
        

    def select_dir(self):
        movements = ["left", "right", "up", "down", "hold"]
        direction = movements[random.randint(0, 3)]
        if direction == "left":
            change = (0, -1)
        elif direction == "right":
            change = (0, 1)
        elif direction == "up":
            change = (-1, 0)
        # elif direction == "down":    
        else:
            change = (1, 0)  
        # elif direction == "hold":    
        #     change = (0, 0) 
        return change   

    def move_dog1(self):
        cross_cell = (self.sheep_pos[0] + 1, self.sheep_pos[1])
        x, y = self.manhattan_dist(cross_cell, self.dog1_pos) 
        if abs(x) < abs(y) and self.possible_move(self.dog1_pos, (0, int(y/abs(y)))) and not self.occupied[self.dog1_pos[0], self.dog1_pos[1] + int(y/abs(y))]:
            self.occupied[self.dog1_pos[0], self.dog1_pos[1]] = 0
            self.playground[self.dog1_pos[0], self.dog1_pos[1]] = 0
            self.dog1_pos = self.dog1_pos[0], self.dog1_pos[1] + int(y/abs(y))
            self.occupied[self.dog1_pos[0], self.dog1_pos[1]] = 1
            self.playground[self.dog1_pos[0], self.dog1_pos[1]] = 1
        else:
            self.occupied[self.dog1_pos[0], self.dog1_pos[1]] = 0
            self.playground[self.dog1_pos[0], self.dog1_pos[1]] = 0
            if abs(x)>0 and not self.occupied[self.dog1_pos[0] + int(x/abs(x)), self.dog1_pos[1]]:
                self.dog1_pos = self.dog1_pos[0] + int(x/abs(x)), self.dog1_pos[1] 
            self.occupied[self.dog1_pos[0], self.dog1_pos[1]] = 1
            self.playground[self.dog1_pos[0], self.dog1_pos[1]] = 1

        print(self.playground)
        input()


    def move_dog2(self):
        cross_cell = (self.sheep_pos[0], self.sheep_pos[1] + 1)
        x, y = self.manhattan_dist(cross_cell, self.dog2_pos)
        if abs(x) < abs(y) and self.possible_move(self.dog2_pos, (0, int(y/abs(y)))) and not self.occupied[self.dog2_pos[0], self.dog2_pos[1] + int(y/abs(y))]:
            self.occupied[self.dog2_pos[0], self.dog2_pos[1]] = 0
            self.playground[self.dog2_pos[0], self.dog2_pos[1]] = 0
            self.dog2_pos = self.dog2_pos[0], self.dog2_pos[1] + int(y/abs(y))
            self.occupied[self.dog2_pos[0], self.dog2_pos[1]] = 1
            self.playground[self.dog2_pos[0], self.dog2_pos[1]] = 2
        else:
            self.occupied[self.dog2_pos[0], self.dog2_pos[1]] = 0
            self.playground[self.dog2_pos[0], self.dog2_pos[1]] = 0
            if abs(x)>0 and not self.occupied[self.dog2_pos[0] + int(x/abs(x)), self.dog2_pos[1]]:
                self.dog2_pos = self.dog2_pos[0] + int(x/abs(x)), self.dog2_pos[1] 
            self.occupied[self.dog2_pos[0], self.dog2_pos[1]] = 1
            self.playground[self.dog2_pos[0], self.dog2_pos[1]] = 2
        print(self.playground)
        input()


    def possible_move(self, current_pos, change):
        a, b = current_pos
        x, y = change
        # print(x, y)
        if a+x > 7 or b+y > 7 or a+x < 0 or b+y < 0:
            return False
        else:
            return True

    def manhattan_dist(self, p1, p2):
        return (p1[0]-p2[0], p1[1]-p2[1])



    def chase(self):
        count = 0
        while self.sheep_pos != (0, 0) or self.dog1_pos != (1, 0) or self.dog2_pos != (0, 1):
            self.move_sheep()
            self.move_dog1()
            self.move_dog2()
            count+=1
            print(count)
        print("It took a total of", count, "rounds to corner the sheep!" )


maps = SheepDog()
maps.chase()
