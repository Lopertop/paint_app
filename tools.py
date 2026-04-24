import pygame
import math
from datetime import datetime

class ShapeDrawer:
    @staticmethod
    def draw_line(screen, color, start_pos, end_pos, width):
        pygame.draw.line(screen, color, start_pos, end_pos, width)
    
    @staticmethod
    def draw_circle(screen, color, pos, width):
        pygame.draw.circle(screen, color, pos, 20, width)
    
    @staticmethod
    def draw_rectangle(screen, color, pos, width):
        pygame.draw.rect(screen, color, (pos[0] - 30, pos[1] - 20, 50, 20), width)
        
    @staticmethod
    def erase(screen, start_pos, end_pos, width):
        pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos, width * 3)
    
    @staticmethod
    def draw_square(screen, color, pos, width):
        pygame.draw.rect(screen, color, (pos[0] - 20, pos[1] - 20, 40, 40), width)
    
    @staticmethod
    def draw_right_triangle(screen, color, pos, width):
        points = [
            (pos[0], pos[1]),
            (pos[0], pos[1] + 40),
            (pos[0] + 40, pos[1])
        ]
        pygame.draw.polygon(screen, color, points, width)
        
    @staticmethod
    def draw_equilateral_triangle(screen, color, pos, width):
        size = 40
        h = size * math.sqrt(3) / 2
        points = [
            (pos[0], pos[1] - h / 2),
            (pos[0] - size / 2, pos[1] + h / 2),
            (pos[0] + size / 2, pos[1] + h / 2)
        ]
        pygame.draw.polygon(screen, color, points, width)
        
    @staticmethod
    def draw_rhombus(screen, color, pos, width):
        size = 25
        points = [
            (pos[0], pos[1] - size),
            (pos[0] + size, pos[1]),
            (pos[0], pos[1] + size),
            (pos[0] - size, pos[1])
        ]
        pygame.draw.polygon(screen, color, points, width)
    
    @staticmethod
    def flood_fill(surface, start_pos, fill_color):
        width, height = surface.get_size()
        color = surface.get_at(start_pos)
        
        if color == fill_color:
            return

        pixels = pygame.PixelArray(surface)
        rgb = surface.map_rgb(color)
        fill_rgb = surface.map_rgb(fill_color)
        
        stack = [start_pos]
        
        while stack:
            x, y = stack.pop()
            
            if pixels[x, y] == rgb:
                pixels[x, y] = fill_rgb
                
                if x + 1 < width: stack.append((x + 1, y))
                if x - 1 >= 0: stack.append((x - 1, y))
                if y + 1 < height: stack.append((x, y + 1))
                if y - 1 >= 0: stack.append((x, y - 1))
        
        del pixels
    
    @staticmethod
    def draw_text(surface, text, pos, color, font_size=30):
        font = pygame.font.SysFont("Arial", font_size)
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, pos)
        
    @staticmethod
    def save_canva(surface):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"image_{timestamp}.png"
        
        try:
            pygame.image.save(surface, filename)
        except Exception as error:
            print(error)
