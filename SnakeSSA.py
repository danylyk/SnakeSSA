import pygame
import math
from snake import Snake
from level import Level
from Control import Control
from Items import *
from pygame.locals import *
import os

class App:
    def __preproccessing (self):
        i = 1
        while i+1 <= len(self.snake_h):
            self.snake_h.insert(i, ((self.snake_h[i-1][0]+self.snake_h[i][0])/2,(self.snake_h[i-1][1]+self.snake_h[i][1])/2))
            i += 2

        if (self.snake_h[0][0] == 0):
            self.snake_h.insert(0, (self.snake_h[0][0]-0.5, self.snake_h[0][1]))
        elif (self.snake_h[0][0] == 9):
            self.snake_h.insert(0, (self.snake_h[0][0]+0.5, self.snake_h[0][1]))
        elif (self.snake_h[0][1] == 0):
            self.snake_h.insert(0, (self.snake_h[0][0], self.snake_h[0][1]-0.5))
        elif (self.snake_h[0][1] == 9):
            self.snake_h.insert(0, (self.snake_h[0][0], self.snake_h[0][1]+0.5))

        if (self.snake_h[len(self.snake_h)-1][0] == 0 and self.snake.view[0] == -1):
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0]-0.5, self.snake_h[len(self.snake_h)-1][1]))
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0]-0.5, self.snake_h[len(self.snake_h)-1][1]))
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0]-0.5, self.snake_h[len(self.snake_h)-1][1]))
        elif (self.snake_h[len(self.snake_h)-1][0] == 9 and self.snake.view[0] == 1):
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0]+0.5, self.snake_h[len(self.snake_h)-1][1]))
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0]+0.5, self.snake_h[len(self.snake_h)-1][1]))
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0]+0.5, self.snake_h[len(self.snake_h)-1][1]))
        elif (self.snake_h[len(self.snake_h)-1][1] == 0 and self.snake.view[1] == 1):
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0], self.snake_h[len(self.snake_h)-1][1]-0.5))
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0], self.snake_h[len(self.snake_h)-1][1]-0.5))
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0], self.snake_h[len(self.snake_h)-1][1]-0.5))
        elif (self.snake_h[len(self.snake_h)-1][1] == 9 and self.snake.view[1] == -1):
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0], self.snake_h[len(self.snake_h)-1][1]+0.5))
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0], self.snake_h[len(self.snake_h)-1][1]+0.5))
            self.snake_h.append((self.snake_h[len(self.snake_h)-1][0], self.snake_h[len(self.snake_h)-1][1]+0.5))
        
        i = 1
        self.snake_h_i = []
        while i < len(self.snake_h):
            self.snake_h_i.append(self.snake_h[i])
            del self.snake_h[i]
            i += 1

    def get_pos (self, t):
        if (t > 1): 
            t = 1
            self.simulate = False
        if (t < 0): t = 0
        if t<0.5: x = 2*t*t
        else: x = -1+(4-2*t)*t
        try: p = x/(1/(len(self.snake_h)-1))
        except: 
            p = 1
            self.simulate = False
        from_p = int(p)
        if (from_p > len(self.snake_h)-2): from_p = len(self.snake_h)-2
        p_transition = p-from_p
        try: item = self.level.get_item(self.snake_h_i[from_p+1])
        except: 
            item = 0
            self.simulate = False
        end = False
        if self.level.get_item(self.snake_h_i[from_p]) == 4 and (self.snake_h_i[from_p+1][0] >= 10 or self.snake_h_i[from_p+1][1] >= 10 or self.snake_h_i[from_p+1][0] < 0 or self.snake_h_i[from_p+1][1] < 0):
            end = True
        if item == 2 or item == 1:
            self.was_end = True
        if ((item != 2 and item != 1) and self.was_end) or ((item == 1 or item == 2) and t == 1) or ((self.level.get_item(self.snake_h_i[from_p]) == 1 or self.level.get_item(self.snake_h_i[from_p]) == 2) and self.was_end):
            self.was_end = False
            self.simulate = False
            if (end):
                self.trail = pygame.image.load(os.path.join("assets", "steo_ok.png")).convert_alpha()
                self.snake_pic = pygame.image.load(os.path.join("assets", "snake_ok.png")).convert_alpha()
            else:
                self.trail = pygame.image.load(os.path.join("assets", "steo_err.png")).convert_alpha()
                self.snake_pic = pygame.image.load(os.path.join("assets", "snake_err.png")).convert_alpha()
            self.updates[5] = 1
        p_1 = ( (self.snake_h[from_p][0] + (self.snake_h_i[from_p][0]-self.snake_h[from_p][0])*p_transition ), (self.snake_h[from_p][1] + (self.snake_h_i[from_p][1]-self.snake_h[from_p][1])*p_transition ) )
        p_2 = ( (self.snake_h_i[from_p][0] + (self.snake_h[from_p+1][0]-self.snake_h_i[from_p][0])*p_transition), (self.snake_h_i[from_p][1] + (self.snake_h[from_p+1][1]-self.snake_h_i[from_p][1])*p_transition) )
        self.snake.set_view((p_2[0]-p_1[0], p_2[1]-p_1[1]))
        res_pos = (p_1[0]+(p_2[0]-p_1[0])*p_transition, p_1[1]+(p_2[1]-p_1[1])*p_transition)
        if item == 5:
            self.was_point = True
        if (item != 5 and self.was_point) or (item == 5 and t == 1):
            self.was_point = False
            add = True
            m=0
            if item != 5: m=-1
            for po in self.snake.points:
                if self.snake_h_i[from_p+1+m][0] == po[0] and self.snake_h_i[from_p+1+m][1] == po[1]:
                    add = False
                    break
            if add:
                self.snake.points.append(self.snake_h_i[from_p+1+m])
                self.updates[5] = 1
        if p > self.snake.trail_shift:
            self.snake.trail.append([res_pos, self.snake.get_angle()])
            self.snake.trail_shift += 0.4
        return res_pos

    def __init__(self):
        pygame.init()
        self.grid_coef = 534/10
        self.snake_pos = [0,0]
        self.snake_way = 0
        self.in_level = False
        self.was_end = False
        self.was_point = False

        window_info = pygame.display.Info()
        w, h = window_info.current_w, window_info.current_h
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (((w/2)-423),((h/2)-292))
        pygame.display.set_caption("Snake SSA")
        self.window = pygame.display.set_mode((846, 584))
        self.font = pygame.font.SysFont('Open Sans', 30)
        self.bg = pygame.image.load(os.path.join("assets", "main.png")).convert()
        self.run = True
        
        self.levels = []
        ls = os.listdir(os.path.join("levels"))
        for i in range(len(ls)):
            a = pygame.Surface((76,76))
            a.fill((255,255,255))
            level_name = str(ls[i].split(".")[0])
            a.blit(self.font.render(level_name, False, (0, 0, 0)), (15,28))
            ar = a.get_rect()
            ar.x, ar.y = (440-len(ls)*50)+i*100, 310
            self.levels.append([a,ar,level_name])

        self.awake()

        self.__run()

    def awake (self):
        self.bg = pygame.image.load(os.path.join("assets", "main.png")).convert()
        self.updates = [1,1,1,1,0,1]

    def start_game (self, level):
        self.bg = pygame.image.load(os.path.join("assets", "bg.png")).convert()

        self.in_level = True;

        self.level = Level(level)
        self.control = Control()

        self.simulate = False;

        self.obstracles = self.level.get_obstracles()
        self.points = self.level.get_points()
        self.start = self.level.get_start()
        self.finish = self.level.get_finish()
        self.snake = Snake([self.start[1]/10, self.start[0]/10])
        self.snake_h = [(self.start[1], self.start[0])]
        self.__preproccessing()

        for i in range(len(self.control.history)):
            self.control.history[i][1].image = pygame.image.load(os.path.join("assets", self.control.history[i][1].image)).convert_alpha()

        self.add_button_default = pygame.image.load(os.path.join("assets", "add.png")).convert_alpha()
        self.add_button_hover = pygame.image.load(os.path.join("assets", "add_hover.png")).convert_alpha()
        self.add_button = self.add_button_default
        self.add_button_rect = self.add_button.get_rect()
        self.add_button_rect.x, self.add_button_rect.y = 98,12

        self.add_event_surf = pygame.Surface((284,92), pygame.SRCALPHA, 32).convert_alpha()

        self.chl = len(self.control.history)
        if self.chl == 0:
            self.chl = 1

        self.control_height = 450/(68*self.chl)

        self.control_line = pygame.Surface((232, 10+68*self.chl))
        self.control_scroll = pygame.Surface((20, self.control_height*450))
        self.control_scroll_des = pygame.Surface((6, self.control_height*450-12))
        self.control_line.fill((230,230,230))
        self.control_scroll.fill((255,255,255))
        self.control_scroll_des.fill((65,122,153))

        self.control_line_pos = 0
        self.control_pos = 0

        self.play_button_default = pygame.image.load(os.path.join("assets", "play.png")).convert_alpha()
        self.play_button_hover = pygame.image.load(os.path.join("assets", "play_hover.png")).convert_alpha()
        self.play_button = self.play_button_default
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x, self.play_button_rect.y = 202,16

        self.snake_surf = pygame.Surface((534,534)).convert_alpha()
        self.snake_surf_bg = pygame.image.load(os.path.join("assets", "snake_surf.png")).convert_alpha()
        self.control_side = pygame.Surface((252,450)).convert_alpha()
        self.control_side_bg = pygame.image.load(os.path.join("assets", "control_side.png")).convert_alpha()
        self.snake_pic = pygame.image.load(os.path.join("assets", "snake.png")).convert_alpha()
        self.point_pic = pygame.image.load(os.path.join("assets", "point.png")).convert_alpha()
        self.point_added = pygame.image.load(os.path.join("assets", "point_added.png")).convert_alpha()

        self.control_top = pygame.image.load(os.path.join("assets", "control_top.png")).convert_alpha()
        self.control_bottom = pygame.image.load(os.path.join("assets", "control_bottom.png")).convert_alpha()
        self.add_event_bg = pygame.image.load(os.path.join("assets", "event_surf.png")).convert_alpha()

        self.start1 = pygame.image.load(os.path.join("assets", "start.png")).convert_alpha()
        self.start2 = pygame.image.load(os.path.join("assets", "start2.png")).convert_alpha()
        self.start3 = pygame.image.load(os.path.join("assets", "start3.png")).convert_alpha()
        self.start4 = pygame.image.load(os.path.join("assets", "start4.png")).convert_alpha()

        self.e_move = pygame.image.load(os.path.join("assets", "i1m.png")).convert_alpha()
        self.e_move_rect = self.e_move.get_rect()
        self.e_move_rect.x, self.e_move_rect.y = 98+6,88
        self.e_left = pygame.image.load(os.path.join("assets", "i2m.png")).convert_alpha()
        self.e_left_rect = self.e_left.get_rect()
        self.e_left_rect.x, self.e_left_rect.y = 98+85,88
        self.e_right = pygame.image.load(os.path.join("assets", "i3m.png")).convert_alpha()
        self.e_right_rect = self.e_right.get_rect()
        self.e_right_rect.x, self.e_right_rect.y = 98+176,88

        self.finish1 = pygame.image.load(os.path.join("assets", "finish.png")).convert_alpha()
        self.finish2 = pygame.image.load(os.path.join("assets", "finish2.png")).convert_alpha()
        self.finish3 = pygame.image.load(os.path.join("assets", "finish3.png")).convert_alpha()
        self.finish4 = pygame.image.load(os.path.join("assets", "finish4.png")).convert_alpha()

        self.trail = pygame.image.load(os.path.join("assets", "steo.png")).convert_alpha()
        self.dot = pygame.image.load(os.path.join("assets", "dot.png")).convert_alpha()
        self.dot_view = False

        self.window.blit(self.bg, (0,0))

        self.in_level = True
        self.updates = [1,1,1,1,0,1]

    def new_history (self):
        self.simulate = False
        self.snake_way = 0
        self.chl = len(self.control.history)
        self.control_height = 450/(68*self.chl)
        self.control_line = pygame.Surface((232, 10+68*self.chl))
        self.control_scroll = pygame.Surface((20, self.control_height*450))
        self.control_scroll_des = pygame.Surface((6, self.control_height*450-12))
        self.control_line.fill((230,230,230))
        self.control_scroll.fill((255,255,255))
        self.control_scroll_des.fill((65,122,153))
        self.control_pos = self.control_line_pos/(10+self.chl*68-450)
        self.snake_h = self.control.get_road((self.start[1],self.start[0]))
        self.__preproccessing()
        self.snake.trail.clear()
        self.snake.points.clear()
        self.snake.trail_shift = 0
        self.trail = pygame.image.load(os.path.join("assets", "steo.png")).convert_alpha()
        self.snake_pic = pygame.image.load(os.path.join("assets", "snake.png")).convert_alpha()

    def __run(self):
        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    if self.in_level:
                        self.in_level = False
                        self.awake()
                        pass
                    else:
                        self.run = False
                if self.in_level:
                    snake_new_pos = [self.snake.x, self.snake.y]
                    if e.type == pygame.KEYDOWN:
                        if e.key == 8:
                            self.control.delete_item(len(self.control.history)-1)
                            self.updates[0] = 1
                            self.new_history()
                        elif e.key == 49:
                            self.dot_view = True
                    if e.type == pygame.KEYUP:
                        if self.dot_view:
                            self.dot_view = False
                            self.updates[5] = 1
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                                if self.updates[4]:
                                    self.updates[4] = 0
                                    self.updates[5] = 1
                                self.simulate = True
                                self.snake_way = 0
                                self.snake.trail.clear()
                                self.snake.points.clear()
                                self.snake.trail_shift = 0
                                self.trail = pygame.image.load(os.path.join("assets", "steo.png")).convert_alpha()
                                self.snake_pic = pygame.image.load(os.path.join("assets", "snake.png")).convert_alpha()
                            elif self.add_button_rect.collidepoint(pygame.mouse.get_pos()):
                                if self.updates[4]: self.updates[4] = 0
                                else: self.updates[4] = 1
                                self.updates[5] = 1
                            elif self.e_move_rect.collidepoint(pygame.mouse.get_pos()):
                                self.control.add_item(CMove())
                                self.control.history[len(self.control.history)-1][1].image = pygame.image.load(os.path.join("assets", self.control.history[len(self.control.history)-1][1].image)).convert_alpha()
                                self.updates[0] = 1
                                self.new_history()
                            elif self.e_left_rect.collidepoint(pygame.mouse.get_pos()):
                                self.control.add_item(CTurnLeft())
                                self.control.history[len(self.control.history)-1][1].image = pygame.image.load(os.path.join("assets", self.control.history[len(self.control.history)-1][1].image)).convert_alpha()
                                self.updates[0] = 1
                                self.new_history()
                            elif self.e_right_rect.collidepoint(pygame.mouse.get_pos()):
                                self.control.add_item(CTurnRight())
                                self.control.history[len(self.control.history)-1][1].image = pygame.image.load(os.path.join("assets", self.control.history[len(self.control.history)-1][1].image)).convert_alpha()
                                self.updates[0] = 1
                                self.new_history()
                        elif e.button == 4:
                            if (10+self.chl*68-450 > 0):
                                self.control_line_pos += 6
                            self.control_pos = self.control_line_pos/(10+self.chl*68-450)
                            if (self.control_pos > 0):
                                self.control_pos = 0
                                self.control_line_pos = 0
                            self.updates[0] = 1
                        elif e.button == 5:
                            if (10+self.chl*68-450 > 0):
                                self.control_line_pos -= 6
                            self.control_pos = self.control_line_pos/(10+self.chl*68-450)
                            if (self.control_pos < -1):
                                self.control_pos = -1
                                self.control_line_pos = -(10+self.chl*68-450)
                            self.updates[0] = 1
                else:
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            for l in self.levels:
                                if l[1].collidepoint(pygame.mouse.get_pos()):
                                    self.start_game(l[2])
            if self.in_level:
                if self.add_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.updates[2] = 2
                    self.add_button = self.add_button_hover
                else:
                    self.add_button = self.add_button_default

                if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.updates[3] = 2
                    self.play_button = self.play_button_hover
                else:
                    self.play_button = self.play_button_default

            self.__draw()
            pygame.display.update()
        
        pygame.quit()

    def __draw (self):
        if self.updates[5]: self.window.blit(self.bg, (0,0))
        
        if self.in_level:
            if self.updates[2] or self.updates[5]: self.window.blit(self.add_button, (98,12))
            if self.updates[3] or self.updates[5]: self.window.blit(self.play_button, (202,16))

            snake_pos = self.get_pos(self.snake_way)

            if self.simulate:
                self.updates[1] = 1
                self.snake_way += 0.01/(len(self.snake_h)**0.5)
        
            if self.updates[1] or self.updates[5] or self.dot_view: 
                self.snake_surf.blit(self.snake_surf_bg, (0,0))

                if self.dot_view:
                    for d in self.snake_h_i:
                        self.snake_surf.blit(self.dot, ((d[0])*self.grid_coef+self.grid_coef/2-5, (d[1])*self.grid_coef+self.grid_coef/2-5))
        
                for obstracle_type in self.obstracles:
                    for obstracle in obstracle_type:
                        pos = [[obstracle[0][1]*self.grid_coef+self.grid_coef/2-self.grid_coef/5,obstracle[0][0]*self.grid_coef+self.grid_coef/2-self.grid_coef/5],
                               [obstracle[1][1]*self.grid_coef+self.grid_coef/2+self.grid_coef/5,obstracle[1][0]*self.grid_coef+self.grid_coef/2+self.grid_coef/5]]
                        self.__draw_border(self.snake_surf, pos)

                for steo in self.snake.trail:
                    t = pygame.transform.rotate(self.trail, steo[1])
                    sh = t.get_size()[0]/2
                    self.snake_surf.blit(t, (steo[0][0]*self.grid_coef+self.grid_coef/2-sh, steo[0][1]*self.grid_coef+self.grid_coef/2-sh))

                for po in self.snake.points:
                    self.snake_surf.blit(self.point_added, ((po[0])*self.grid_coef+self.grid_coef/2-19, (po[1])*self.grid_coef+self.grid_coef/2-19)) 

                for point in self.points:
                    self.snake_surf.blit(self.point_pic, (point[1]*self.grid_coef+self.grid_coef/2-14, point[0]*self.grid_coef+self.grid_coef/2-14))    
                angle = self.snake.get_angle()
                res_snake = pygame.transform.rotate(self.snake_pic, angle)
                sh = res_snake.get_size()[0]/2        
                self.snake_surf.blit(pygame.transform.rotate(self.snake_pic, angle), (snake_pos[0]*self.grid_coef+self.grid_coef/2-sh, snake_pos[1]*self.grid_coef+self.grid_coef/2-sh))
                self.window.blit(self.snake_surf, (287, 25))

                if (self.start[1] == 0):
                    self.window.blit(self.start1, (269,self.start[0]*self.grid_coef+self.grid_coef/2+2))
                elif (self.start[1] == 9):
                    self.window.blit(self.start2, (811,self.start[0]*self.grid_coef+self.grid_coef/2+2))
                elif (self.start[0] == 0):
                    self.window.blit(self.start3, (265+self.start[1]*self.grid_coef+self.grid_coef/2-2, 6))
                elif (self.start[0] == 9):
                    self.window.blit(self.start4, (265+self.start[1]*self.grid_coef+self.grid_coef/2-2, 548))

                if (self.finish[1] == 0):
                    self.window.blit(self.finish1, (267,self.finish[0]*self.grid_coef+self.grid_coef/2+2))
                elif (self.finish[1] == 9):
                    self.window.blit(self.finish2, (806,self.finish[0]*self.grid_coef+self.grid_coef/2+2))
                elif (self.finish[0] == 0):
                    self.window.blit(self.finish3, (265+self.finish[1]*self.grid_coef+self.grid_coef/2-2, 3))
                elif (self.finish[0] == 9):
                    self.window.blit(self.finish4, (265+self.finish[1]*self.grid_coef+self.grid_coef/2-2, 543))

            if self.updates[0] or self.updates[5]:
                for i in range(len(self.control.history)):
                    self.control_line.blit(self.control.history[i][1].image, (25, 5+68*i))
                self.control_side.blit(self.control_side_bg, (0,0))
                self.control_side.blit(self.control_line, (0, self.control_line_pos))
                self.control_side.blit(self.control_top, (0, 0))
                self.control_side.blit(self.control_bottom, (0, 434))

                self.control_scroll.blit(self.control_scroll_des, (7,7))
                if (10+self.chl*68-450 > 0):
                    self.control_side.blit(self.control_scroll, (232, -self.control_pos*(1-self.control_height)*450))

                self.window.blit(self.control_side, (7, 100))

            if (self.updates[4] and self.updates[1]) or (self.updates[4] and self.updates[0]) or (self.updates[4] and self.updates[5]) or (self.updates[4] and self.dot_view):
                self.add_event_surf.blit(self.add_event_bg, (0,0))
                self.add_event_surf.blit(self.e_move, (6,13))
                self.add_event_surf.blit(self.e_right, (85,13))
                self.add_event_surf.blit(self.e_left, (176,13))
                self.window.blit(self.add_event_surf, (92,76))
        else:
            for i in range(len(self.levels)):
                self.window.blit(self.levels[i][0], ((440-len(self.levels)*50)+i*100, 310))

        for i in range(len(self.updates)):
            if i == 4: continue
            if self.updates[i] == 2: self.updates[i] = 1
            else: self.updates[i] = 0

    def __draw_border (self, surf, pos):
        pygame.draw.line(surf, (65, 122, 153), [pos[0][0]+3, pos[0][1]], [pos[0][0]+3, pos[1][1]], 7)
        pygame.draw.line(surf, (65, 122, 153), [pos[0][0], pos[1][1]-3], [pos[1][0], pos[1][1]-3], 7)
        pygame.draw.line(surf, (65, 122, 153), [pos[0][0], pos[0][1]+3], [pos[1][0], pos[0][1]+3], 7)
        pygame.draw.line(surf, (65, 122, 153), [pos[1][0]-3, pos[0][1]], [pos[1][0]-3, pos[1][1]], 7)


app = App()