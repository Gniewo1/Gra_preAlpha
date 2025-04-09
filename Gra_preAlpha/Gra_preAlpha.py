import pygame
from sys import exit
import character





pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Pre_alpha')
clock = pygame.time.Clock()


choice = 0

#frames
main_menu = True
creation = False
map = False
pause = False
stats = False
fight = False

# goblins surface on map
map_goblin1 = True
map_goblin2 = True

#font
# text_font = pygame.font.Font('font/Pixeltype.ttf',50)
text_font = pygame.font.Font('font/Pixeltype.ttf',50)

actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False}

def movement(actions):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                actions['down'] = True
            if event.key == pygame.K_UP:
                actions['up'] = True
            if event.key == pygame.K_LEFT:
                actions['left'] = True
            if event.key == pygame.K_RIGHT:
                actions['right'] = True
            if event.key == pygame.K_z:
                actions['action1'] = True
            if event.key == pygame.K_x:
                actions['action2'] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                actions['left'] = False
            if event.key == pygame.K_RIGHT:
                actions['right'] = False
            if event.key == pygame.K_UP:
                actions['up'] = False
            if event.key == pygame.K_DOWN:
                actions['down'] = False
            if event.key == pygame.K_z:
                actions['action1'] = False
            if event.key == pygame.K_x:
                actions['action2'] = False

def movement_stop(actions):
    actions['down'], actions['up'], actions['left'], actions['right'], actions['action1'], actions['action2'] = False, False, False, False, False, False



################################################################################## LOAD ASSETS ###############################################################################

########################################   MAIN MENU ##################################################
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


############################################### CHARACTER CREATION ##############################################
    


creation_surf = pygame.Surface((1280,720))
creation_surf.fill('grey')

#player image
player_stand = pygame.image.load('player/player_front1.png').convert_alpha()
player_stand = pygame.transform.scale_by(player_stand, 10)
player_stand_rect = player_stand.get_rect(center = (200,360))

#buttons
button = pygame.Surface((40,40))
button.fill('white')
button_big = pygame.Surface((100,40))
button_big.fill('white')

    #minus buttons
button_min_str = button.get_rect(center = (800,60))
button_min_dex = button.get_rect(center = (800,210))
button_min_con = button.get_rect(center = (800,360))
button_min_int = button.get_rect(center = (800,510))
    #plus buttons
button_plus_str = button.get_rect(center = (960,60))
button_plus_dex = button.get_rect(center = (960,210))
button_plus_con = button.get_rect(center = (960,360))
button_plus_int = button.get_rect(center = (960,510))
    #options buttons
button_reset = button_big.get_rect(center = (800,660))
button_next = button_big.get_rect(center = (960,660))
    #options signs
sign_reset = text_font.render("RESET",False,"Black")
sign_next = text_font.render("NEXT",False,"Black")
sign_reset_rect = sign_reset.get_rect(center = (800,660))
sign_next_rect = sign_next.get_rect(center = (960,660))


#plus/minus signs
sign_min = text_font.render("-", False, "Black")
sign_plus = text_font.render("+", False, "Black")

sign_min_str = sign_min.get_rect(center = (800,60))
sign_min_dex = sign_min.get_rect(center = (800,210))
sign_min_con = sign_min.get_rect(center = (800,360))
sign_min_int = sign_min.get_rect(center = (800,510))
sign_plus_str = sign_plus.get_rect(center = (960,60))
sign_plus_dex = sign_plus.get_rect(center = (960,210))
sign_plus_con = sign_plus.get_rect(center = (960,360))
sign_plus_int = sign_plus.get_rect(center = (960,510))

#ability numbers
str_score = 0
dex_score = 0
int_score = 0
con_score = 0
pkt_score = 6

#ability labels
label_str = text_font.render("STR", False, "Black")
label_dex = text_font.render("DEX", False, "Black")
label_con = text_font.render("CON", False, "Black")
label_int = text_font.render("INT", False, "Black")
label_pkt = text_font.render("PKT", False, "Black")
label_str_rect = label_str.get_rect(center = (640,60))
label_dex_rect = label_dex.get_rect(center = (640,210))
label_con_rect = label_con.get_rect(center = (640,360))
label_int_rect = label_int.get_rect(center = (640,510))
label_pkt_rect = label_pkt.get_rect(center = (1060,660))


#choose button
choice_surf = pygame.Surface((50,50))
choice_surf.fill("red")
choice_surf_big = pygame.Surface((110,50))
choice_surf_big.fill("red")

choice_min_str = choice_surf.get_rect(center = (800,60))
choice_min_dex = choice_surf.get_rect(center = (800,210))
choice_min_con = choice_surf.get_rect(center = (800,360))
choice_min_int = choice_surf.get_rect(center = (800,510))
choice_plus_str = choice_surf.get_rect(center = (960,60))
choice_plus_dex = choice_surf.get_rect(center = (960,210))
choice_plus_con = choice_surf.get_rect(center = (960,360))
choice_plus_int = choice_surf.get_rect(center = (960,510))
choice_reset = choice_surf_big.get_rect(center =(800,660))
choice_next = choice_surf_big.get_rect(center = (960,660))

choice_tab = [choice_min_str,choice_plus_str,choice_min_dex,choice_plus_dex,choice_min_con,choice_plus_con,choice_min_int,choice_plus_int,choice_reset,choice_next]
choice_button = 0

########################################   MAP  ##################################################
map_surf = pygame.image.load('surface/Map.png').convert_alpha()

#player images
    #front
player_front = pygame.image.load('player/player_front1.png').convert_alpha()
player_front = pygame.transform.scale_by(player_front, 4)
player_front2 = pygame.image.load('player/player_front2.png').convert_alpha()
player_front2 = pygame.transform.scale_by(player_front2, 4)
player_front3 = pygame.image.load('player/player_front3.png').convert_alpha()
player_front3 = pygame.transform.scale_by(player_front3, 4)
player_front4 = pygame.image.load('player/player_front4.png').convert_alpha()
player_front4 = pygame.transform.scale_by(player_front4, 4)

player_front_tab = [player_front,player_front2,player_front3,player_front4]

    #back
player_back = pygame.image.load('player/player_back1.png').convert_alpha()
player_back = pygame.transform.scale_by(player_back, 4)
player_back2 = pygame.image.load('player/player_back2.png').convert_alpha()
player_back2 = pygame.transform.scale_by(player_back2, 4)
player_back3 = pygame.image.load('player/player_back3.png').convert_alpha()
player_back3 = pygame.transform.scale_by(player_back3, 4)
player_back4 = pygame.image.load('player/player_back4.png').convert_alpha()
player_back4 = pygame.transform.scale_by(player_back4, 4)

player_back_tab = [player_back,player_back2,player_back3,player_back4]

    #left
player_left = pygame.image.load('player/player_left1.png').convert_alpha()
player_left = pygame.transform.scale_by(player_left, 4)
player_left2 = pygame.image.load('player/player_left2.png').convert_alpha()
player_left2 = pygame.transform.scale_by(player_left2, 4)
player_left3 = pygame.image.load('player/player_left3.png').convert_alpha()
player_left3 = pygame.transform.scale_by(player_left3, 4)
player_left4 = pygame.image.load('player/player_left4.png').convert_alpha()
player_left4 = pygame.transform.scale_by(player_left4, 4)

player_left_tab = [player_left,player_left2,player_left3,player_left4]

    #right
player_right = pygame.image.load('player/player_right1.png').convert_alpha()
player_right = pygame.transform.scale_by(player_right, 4)
player_right2 = pygame.image.load('player/player_right2.png').convert_alpha()
player_right2 = pygame.transform.scale_by(player_right2, 4)
player_right3 = pygame.image.load('player/player_right3.png').convert_alpha()
player_right3 = pygame.transform.scale_by(player_right3, 4)
player_right4 = pygame.image.load('player/player_right4.png').convert_alpha()
player_right4 = pygame.transform.scale_by(player_right4, 4)

player_right_tab = [player_right,player_right2,player_right3,player_right4]

#goblin images
goblin_surf = pygame.image.load('enemy/goblin.png').convert_alpha()
goblin_surf = pygame.transform.scale_by(goblin_surf, 1/12)
goblin_surf_1 = goblin_surf.get_rect(center = (1100,200))
goblin_surf_2 = goblin_surf.get_rect(center = (900,400))

    ############################pause in map##########################3
pause_menu = pygame.Surface((200,700))
pause_menu.fill('white')
pause_menu_background = pygame.Surface((210,710))
pause_menu_background.fill('black')
pause_menu_rect = pause_menu.get_rect(center = (1170,360))
pause_menu_background_rect = pause_menu_background.get_rect(center = (1170,360))
    
    #label
stats_label = text_font.render("STATS", False, "Black")
save_label = text_font.render("SAVE", False, "Black")
exit_label = text_font.render("EXIT", False, "Black")
stats_label_rect = stats_label.get_rect(center = (1170,60))
save_label_rect = save_label.get_rect(center = (1170,360))
exit_label_rect = exit_label.get_rect(center = (1170,660))
    #cursor
cursor_number = 0

cursor = pygame.image.load('surface/cursor.png')
cursor_stats = cursor.get_rect(center = (1100,60))
cursor_save = cursor.get_rect(center = (1100,360))
cursor_exit = cursor.get_rect(center = (1100,660))

cursor_tab = [cursor_stats,cursor_save,cursor_exit]

    ############# fight in map ###################
fight_choice = 0

move_number = 0
move_direction = 0


player_x = 640
player_y = 360

############################################################################################### KEY DOWNS #############################################################################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
   
 ######################### MAIN MENU #########################################
        if main_menu:
            if event.type == pygame.KEYDOWN and main_menu == True:
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
            

######################## CHARACTER CREATION ####################################
        if event.type == pygame.KEYDOWN and creation == True:
            if event.key == pygame.K_x:
                main_menu = True
                creation = False

            if event.key == pygame.K_DOWN:
                choice_button = (choice_button + 2) % 10
            if event.key == pygame.K_UP:
                choice_button = (choice_button - 2) % 10
            if event.key == pygame.K_LEFT:
                choice_button = (choice_button - 1) % 10
            if event.key == pygame.K_RIGHT:
                choice_button = (choice_button + 1) % 10

            if event.key == pygame.K_z:
                if choice_button == 0:
                    player.remove_point('str')
                if choice_button == 1:
                    player.add_point('str')
                if choice_button == 2:
                    player.remove_point('dex')
                if choice_button == 3:
                    player.add_point('dex')
                if choice_button == 4:
                    player.remove_point('con')
                if choice_button == 5:
                    player.add_point('con')
                if choice_button == 6:
                    player.remove_point('int')
                if choice_button == 7:
                    player.add_point('int')
                if choice_button == 8:
                    player.str_score = 0
                    player.dex_score = 0
                    player.int_score = 0
                    player.con_score = 0
                    player.pkt_score = 6
                if choice_button == 9 and player.pkt_score == 0:
                    player.max_hp = (player.con_score + 8)*3
                    player.current_hp = player.max_hp
                    creation = False
                    map = True
                    goblin = character.Goblin()
                    character.Player.calculate_stats(player)
                    

                    

################################## MAP #####################################
        if map:
            if pause:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        cursor_number = (cursor_number + 1) % 3
                    if event.key == pygame.K_UP:
                        cursor_number = (cursor_number - 1) % 3
                    if event.key == pygame.K_x:
                        pause = False
                    if event.key == pygame.K_z:
                        match cursor_number:
                            case 0:
                                stats = True
                                pause = False
                            case 1:
                                pass
                            case 2:
                                pause = False
                                map = False
                                main_menu = True

            ############# STATS IN MAP ######################
            elif stats:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        stats = False
                        pause = True

            ############# FIGHT IN MAP ######################
            elif fight:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        fight_choice = (fight_choice + 2) % 4
                    if event.key == pygame.K_UP:
                        fight_choice = (fight_choice - 2) % 4
                    if event.key == pygame.K_LEFT:
                        fight_choice = (fight_choice - 1) % 4
                    if event.key == pygame.K_RIGHT:
                        fight_choice = (fight_choice + 1) % 4
                    if event.key == pygame.K_z:
                        if fight_choice == 0:
                            if player.actions > 0:
                                attack_roll, attack_total, result = fight_goblin.player_attack(player,goblin)
                                damage = fight_goblin.player_damage(player) * result
                                goblin.current_hp -= damage
                if goblin.current_hp <= 0:
                    player.reset_actions()
                    fight = False

                if player.actions <= 0:
                    player.reset_actions()
                            
                            

            else:
                movement(actions)

###################################################################################### DISPLAYS #################################################################################

############################# MAIN MENU #################################
    if main_menu:
        #main surface display
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

############################# CHARACTER CREATION #################################
    if creation:
        #ability score
        score_str = text_font.render(str(player.str_score), False, "Black")
        score_dex = text_font.render(str(player.dex_score), False, "Black")
        score_con = text_font.render(str(player.con_score), False, "Black")
        score_int = text_font.render(str(player.int_score), False, "Black")
        score_pkt = text_font.render(str(player.pkt_score), False, "Black")

        score_str_rect = score_str.get_rect(center = (1120,60))
        score_dex_rect = score_dex.get_rect(center = (1120,210))
        score_con_rect = score_con.get_rect(center = (1120,360))
        score_int_rect = score_int.get_rect(center = (1120,510))
        score_pkt_rect = score_pkt.get_rect(center = (1120,660))

        
       
        #displays

        
        screen.blit(creation_surf,(0,0))
        screen.blit(player_stand,player_stand_rect)

        if choice_button < 8:
            screen.blit(choice_surf,choice_tab[choice_button])
        else:
            screen.blit(choice_surf_big,choice_tab[choice_button])



        screen.blit(button,button_min_str)
        screen.blit(button,button_min_dex)
        screen.blit(button,button_min_con)
        screen.blit(button,button_min_int)

        screen.blit(button,button_plus_str)
        screen.blit(button,button_plus_dex)
        screen.blit(button,button_plus_con)
        screen.blit(button,button_plus_int)

        screen.blit(button_big,button_reset)
        screen.blit(button_big,button_next)
        screen.blit(sign_reset,sign_reset_rect)
        screen.blit(sign_next,sign_next_rect)

        screen.blit(sign_min,sign_min_str)
        screen.blit(sign_min,sign_min_dex)
        screen.blit(sign_min,sign_min_con)
        screen.blit(sign_min,sign_min_int)
        screen.blit(sign_plus,sign_plus_str)
        screen.blit(sign_plus,sign_plus_dex)
        screen.blit(sign_plus,sign_plus_con)
        screen.blit(sign_plus,sign_plus_int)

        screen.blit(label_str,label_str_rect)
        screen.blit(label_dex,label_dex_rect)
        screen.blit(label_con,label_con_rect)
        screen.blit(label_int,label_int_rect)
        screen.blit(label_pkt,label_pkt_rect)

        screen.blit(score_str,score_str_rect)
        screen.blit(score_dex,score_dex_rect)
        screen.blit(score_con,score_con_rect)
        screen.blit(score_int,score_int_rect)
        screen.blit(score_pkt,score_pkt_rect)

        
############################# MAP #################################
    if map:
        match move_direction:
            case 0:
                player_present = player_back_tab[int(move_number)]
            case 1:
                player_present = player_front_tab[int(move_number)]
            case 2:
                player_present = player_left_tab[int(move_number)]
            case 3:
                player_present = player_right_tab[int(move_number)]
        if actions['down']:
            move_direction = 1
            if player_y <= 660:
                player_y += 8
            move_number = (move_number + 0.1) % 4
        if actions['up']:
            move_direction = 0
            if player_y >= 0:
                player_y -= 8
            move_number = (move_number + 0.1) % 4
        if actions['left']:
            move_direction = 2
            if player_x >= 0:
                player_x -= 8
            move_number = (move_number + 0.1) % 4
        if actions['right']:
            move_direction = 3
            if player_x <= 1220:
                player_x += 8
            move_number = (move_number + 0.1) % 4
        if actions['action2']:
            pause = True

        #collison
        player_rect = player_present.get_rect(center = (player_x,player_y))
        if player_rect.colliderect(goblin_surf_1) and map_goblin1:
            fight = True
            map_goblin1 = False
            if goblin.current_hp <= 0:
                goblin.current_hp = goblin.max_hp
            fight_goblin = character.Fight(player,goblin)
            character.Player.calculate_stats(player)
        if player_rect.colliderect(goblin_surf_2) and map_goblin2:
            fight = True
            map_goblin2 = False
            if goblin.current_hp <= 0:
                goblin.current_hp = goblin.max_hp
            fight_goblin = character.Fight(player,goblin)
            character.Player.calculate_stats(player)

        screen.blit(map_surf,(0,0))
        screen.blit(player_present,(player_rect))
        if map_goblin1:
            screen.blit(goblin_surf, goblin_surf_1)
        if map_goblin2:
            screen.blit(goblin_surf, goblin_surf_2)
        ########## PAUSE IN MAP #############
        if pause:
            movement_stop(actions)
            screen.blit(pause_menu_background,pause_menu_background_rect)
            screen.blit(pause_menu,pause_menu_rect)
            screen.blit(stats_label,stats_label_rect)
            screen.blit(save_label,save_label_rect)
            screen.blit(exit_label,exit_label_rect)
            screen.blit(cursor,cursor_tab[cursor_number])
        ########## STATS IN PAUSE #############
        if stats:
            movement_stop(actions)
            #HP
            score_hp = text_font.render(str(player.current_hp) + '/' + (str(player.max_hp)), False, "Black")
            score_hp_rect = score_hp.get_rect(center = (320,60))

            bar_len = player.current_hp/player.max_hp
            max_hp_bar = pygame.Surface((200,21))
            max_hp_bar.fill('black')
            current_hp_bar = pygame.Surface(((200/bar_len),20))
            current_hp_bar.fill('red')
            max_hp_bar_rect = max_hp_bar.get_rect(center = (320,80))
            current_hp_bar_rect = current_hp_bar.get_rect(center = (320,80))

           
            screen.blit(creation_surf,(0,0))
            screen.blit(player_stand,player_stand_rect)
            screen.blit(label_str,label_str_rect)
            screen.blit(label_dex,label_dex_rect)
            screen.blit(label_con,label_con_rect)
            screen.blit(label_int,label_int_rect)

            screen.blit(score_str,score_str_rect)
            screen.blit(score_dex,score_dex_rect)
            screen.blit(score_con,score_con_rect)
            screen.blit(score_int,score_int_rect)

            screen.blit(score_hp,score_hp_rect)
            screen.blit(max_hp_bar,max_hp_bar_rect)
            screen.blit( current_hp_bar, current_hp_bar_rect)
        ############# FIGHT IN MAP ##############################
        if fight:
            movement_stop(actions)
            screen.blit(creation_surf,(0,0))
            player_fight = pygame.transform.scale_by(player_right4, 5)
            player_fight_rect = player_fight.get_rect(center = (320,480))
            screen.blit(player_fight,player_fight_rect)

                #options
            fight_options_back = pygame.Surface((610,210))
            fight_options_back.fill('black')
            fight_options_back_rect = fight_options_back.get_rect(center = (960,600))
            fight_options_surf = pygame.Surface((600,200))
            fight_options_surf_rect = fight_options_surf.get_rect(center = (960,600))
            fight_options_surf.fill('white')
            screen.blit(fight_options_back,fight_options_back_rect)
            screen.blit(fight_options_surf,fight_options_surf_rect)
                #labels
            attack_label = text_font.render("ATTACK", False, "Black")
            attack_label_rect = attack_label.get_rect(center = (810,540))
            magic_label = text_font.render("MAGIC", False, "Black")
            magic_label_rect = magic_label.get_rect(center = (1110,540))
            item_label = text_font.render("ITEM", False, "Black")
            item_label_rect = item_label.get_rect(center = (810,660))
            stats_label_fight = text_font.render("STATS", False, "Black")
            stats_label_fight_rect = stats_label_fight.get_rect(center = (1110,660))
            attack_bonus_label = text_font.render("ATTACK BONUS: " + str(player.attack - player.attack_penalty), False, "Black")
            attack_bonus_label_rect = attack_bonus_label.get_rect(center = (800,480))
            actions_label = text_font.render("ACTIONS: " + str(player.actions), False, "Black")
            actions_label_rect = attack_bonus_label.get_rect(center = (1200,480))

            screen.blit(attack_label,attack_label_rect)
            screen.blit(magic_label,magic_label_rect)
            screen.blit(item_label,item_label_rect)
            screen.blit(stats_label_fight,stats_label_fight_rect)
            screen.blit(attack_bonus_label,attack_bonus_label_rect)
            screen.blit(actions_label,actions_label_rect)
                #choice
            attack_choice = cursor.get_rect(center = (670,540))
            magic_choice = cursor.get_rect(center = (960,540))
            item_choice = cursor.get_rect(center = (670,660))
            stats_choice = cursor.get_rect(center = (960,660))

            fight_choice_tab = [attack_choice,magic_choice,item_choice,stats_choice]

            screen.blit(cursor,fight_choice_tab[fight_choice])

                #goblin image
            goblin_fight_surf = pygame.transform.scale_by(goblin_surf, 5)
            goblin_fight_surf = pygame.transform.flip(goblin_fight_surf, True, False)
            goblin_fight_surf_rect = goblin_fight_surf.get_rect(center = (960,300))
            screen.blit(goblin_fight_surf,goblin_fight_surf_rect)
                #health bars
                    #player
            score_hp = text_font.render(str(player.current_hp) + '/' + (str(player.max_hp) + 'HP'), False, "Black")
            score_hp_rect = score_hp.get_rect(center = (320,260))

            bar_len = player.current_hp/player.max_hp
            max_hp_bar = pygame.Surface((200,21))
            max_hp_bar.fill('black')
            current_hp_bar = pygame.Surface(((200/bar_len),20))
            current_hp_bar.fill('red')
            max_hp_bar_rect = max_hp_bar.get_rect(center = (320,280))
            current_hp_bar_rect = current_hp_bar.get_rect(center = (320,280))

            screen.blit(score_hp,score_hp_rect)
            screen.blit(max_hp_bar,max_hp_bar_rect)
            screen.blit(current_hp_bar,current_hp_bar_rect)

                    #goblin
            goblin_score_hp = text_font.render(str(goblin.current_hp) + '/' + (str(goblin.max_hp) + 'HP'), False, "Black")
            goblin_score_hp_rect = goblin_score_hp.get_rect(center = (960,80))

            goblin_bar_len = goblin.current_hp/goblin.max_hp
            goblin_max_hp_bar = pygame.Surface((200,21))
            goblin_max_hp_bar_rect = goblin_max_hp_bar.get_rect(center = (960,100))
            goblin_max_hp_bar.fill('black')
            screen.blit(goblin_max_hp_bar,goblin_max_hp_bar_rect)
            if goblin_bar_len > 0:
                goblin_current_hp_bar = pygame.Surface(((goblin_bar_len*200),20))
                goblin_current_hp_bar.fill('red')
                goblin_current_hp_bar_rect = goblin_current_hp_bar.get_rect(center = (960,100))
                screen.blit(goblin_current_hp_bar,goblin_current_hp_bar_rect)

            screen.blit(goblin_score_hp,goblin_score_hp_rect)
            
            


                

            






    


    pygame.display.update()
    clock.tick(60)





