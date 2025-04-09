import pygame
import character

class menu(main_menu,creation,text_font,screen,choice):
    #font


    #button surface
    newgame_button = pygame.Surface((200,100))
    newgame_button.fill('white')
    loadgame_button = pygame.Surface((200,100))
    loadgame_button.fill('white')
    exit_button = pygame.Surface((200,100))
    exit_button.fill('white')

    #rect button 
    newgame_button_rect = newgame_button.get_rect(center = (640,200))
    loadgame_button_rect = loadgame_button.get_rect(center = (640,350))
    exit_button_rect = exit_button.get_rect(center = (640,500))

    #text surface
    newgame_surf = text_font.render("New Game", False, "Black")
    loadgame_surf = text_font.render("Load Game", False, "Black")
    exit_surf = text_font.render("Exit", False, "Black")

    #rect text surface
    newgame_rect = newgame_surf.get_rect(center = (640,200))
    loadgame_rect = loadgame_surf.get_rect(center = (640,350))
    exit_rect = exit_surf.get_rect(center = (640,500))

    #main menu image
    main_surf = pygame.image.load('surface/Menu.jpg')

    #choice button
    newgame_choice = pygame.Surface((210,110))
    newgame_choice.fill('red')
    loadgame_choice = pygame.Surface((210,110))
    loadgame_choice.fill('red')
    exit_choice = pygame.Surface((210,110))
    exit_choice.fill('red')

    #choice button rect
    newgame_choice_rect = newgame_choice.get_rect(center = (640,200))
    loadgame_choice_rect = loadgame_choice.get_rect(center = (640,350))
    exit_choice_rect = exit_choice.get_rect(center = (640,500))

    def keydowns(main_menu,creation):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                choice = (choice + 1) % 3
            if event.key == pygame.K_UP:
                choice = (choice - 1) % 3
            if event.key == pygame.K_z:
                if choice == 0:
                    main_menu = False
                    creation = True
                    player = character.Player()
                if choice == 2:
                    pygame.quit()
                    exit()

    def display(screen,choice):
        screen.blit(main_surf,(0,0))

        #choice display
        if choice == 0:
            screen.blit(newgame_choice,newgame_choice_rect)
        elif choice == 1:
            screen.blit(loadgame_choice,loadgame_choice_rect)
        else:
            screen.blit(exit_choice,exit_choice_rect)

        #button surface display
        screen.blit(newgame_button,newgame_button_rect)
        screen.blit(loadgame_button,loadgame_button_rect)
        screen.blit(exit_button,exit_button_rect)

        #text surface display
        screen.blit(newgame_surf,newgame_rect)
        screen.blit(loadgame_surf,loadgame_rect)
        screen.blit(exit_surf,exit_rect)


