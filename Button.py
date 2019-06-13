import pygame 
class buttons(): #create class to use for button
    def __init__(self, width, height, color,text,x,y,fontcol=(0,0,0), font="Arial",size=44): #setting up class by initializing
        '''

        :param width:
        width of button
        :param height:
        height of button
        :param color:
        color of button
        :param font:
        font in "" of buttons
        :param size:
        size of font
        '''

        self.font = pygame.font.SysFont(font, size, bold=False, italic=False)  # setting up button looks
        self.surface = pygame.Surface([width, height]) #surfacing button to display
        self.rect = self.surface.get_rect()
        self.surface.fill(color) #colour fill
        self.text=text
        self.surface.blit((self.font.render(text, True, fontcol, color)),(0,0)) #button surface 
        self.rect.x=x
        self.rect.y=y #creating rectangle figure
        self.x=x
        self.y=y
