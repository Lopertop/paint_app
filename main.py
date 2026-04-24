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
    
    active_text = ""
    text_pos = None
    is_typing = False
    
    current_width = 5
    widths = {
        pygame.K_F1: 2,
        pygame.K_F2: 5,
        pygame.K_F3: 10
    }
    
    drawing = False
    start_pos = None
    last_pos = None
    
    while True:
        screen.fill((200, 200, 200))
        screen.blit(canva, (0, 0))
        
        current_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if is_typing:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        ShapeDrawer.draw_text(canva, active_text, text_pos, color)
                        active_text = ""
                        is_typing = False
                    elif event.key == pygame.K_ESCAPE:
                        active_text = ""
                        is_typing = False
                    elif event.key == pygame.K_BACKSPACE:
                        active_text = active_text[:-1]
                elif event.type == pygame.TEXTINPUT:
                    active_text += event.text
                continue
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_CTRL:
                        ShapeDrawer.save_canva(canva)
                    else:
                        mode = 'square'
                
                if event.key in widths:
                    current_width = widths[event.key]
            
                keys = {
                    pygame.K_p: 'pencil', pygame.K_l: 'line',
                    pygame.K_e: 'erase', pygame.K_c: 'circle',
                    pygame.K_r: 'rectangle', pygame.K_s: 'square',
                    pygame.K_t: 'right_triangle', pygame.K_q: 'equilateral',
                    pygame.K_d: 'rhombus', pygame.K_f: 'fill',
                    pygame.K_m: 'text'
                }
                
                if event.key in keys: mode = keys[event.key]
            
                if event.key == pygame.K_1: color = (0, 0, 255)
                if event.key == pygame.K_2: color = (0, 255, 0)
                if event.key == pygame.K_3: color = (255, 0, 0)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'text':
                    if active_text:
                        ShapeDrawer.draw_text(canva, active_text, text_pos, color)
                    is_typing = True
                    text_pos = event.pos
                    active_text = ""
                if mode == 'fill':
                    ShapeDrawer.flood_fill(canva, event.pos, color)
                else:
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
        
        if is_typing:
            ShapeDrawer.draw_text(screen, active_text + "|", text_pos, color)
            
        pygame.display.flip()
        clock.tick(60)                    
                    
if __name__ == "__main__":
    main()