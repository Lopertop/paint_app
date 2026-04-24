import pygame
from tools import ShapeDrawer

pygame.init()
    
def main():
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()
    
    canva = pygame.Surface((400, 400))
    canva.fill((255, 255, 255))
    
    screen.fill((255, 255, 255))
    
    color = (0, 0, 255)
    mode = 'pencil'
    
    current_width = 5
    widths = {
        pygame.K_F1: 2,
        pygame.K_F2: 5,
        pygame.K_F3: 10
    }
    
    drawing = False
    start_pos = None
    end_pos = None
    
    while True:
        screen.fill((200, 200, 200))
        screen.blit(canva, (0, 0))
        
        current_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key in widths:
                    current_width = widths[event.key]
            
                keys = {
                    pygame.K_p: 'pencil', pygame.K_l: 'line',
                    pygame.K_e: 'erase', pygame.K_c: 'circle',
                    pygame.K_r: 'rectangle', pygame.K_s: 'square',
                    pygame.K_t: 'right_triangle', pygame.K_q: 'equilateral',
                    pygame.K_d: 'rhombus'
                }
                
                if event.key in keys: mode = keys[event.key]
            
                if event.key == pygame.K_1: color = (0, 0, 255)
                if event.key == pygame.K_2: color = (0, 255, 0)
                if event.key == pygame.K_3: color = (255, 0, 0)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing and mode == 'line':
                    ShapeDrawer.draw_line(canva, color, start_pos, event.pos, current_width)
                drawing = False
                    
        if drawing:
            if mode == 'pencil':
                ShapeDrawer.draw_line(canva, color, last_pos, current_pos, current_width)
                last_pos = current_pos
            elif mode == 'line':
                ShapeDrawer.draw_line(screen, color, start_pos, current_pos, current_width)
            elif mode == 'circle':
                ShapeDrawer.draw_circle(canva, color, current_pos, current_width)
            elif mode == 'rectangle':
                ShapeDrawer.draw_rectangle(canva, color, current_pos, current_width)
            elif mode == 'square':
                ShapeDrawer.draw_square(canva, color, current_pos, current_width)
            elif mode == 'right_triangle':
                ShapeDrawer.draw_right_triangle(canva, color, current_pos, current_width)
            elif mode == 'equilateral':
                ShapeDrawer.draw_equilateral_triangle(canva, color, current_pos, current_width)
            elif mode == 'rhombus':
                ShapeDrawer.draw_rhombus(canva, color, current_pos, current_width)
            elif mode == 'erase':
                ShapeDrawer.erase(canva, last_pos, current_pos, current_width)
                last_pos = current_pos
            
        pygame.display.flip()
        clock.tick(60)                    
                    
if __name__ == "__main__":
    main()