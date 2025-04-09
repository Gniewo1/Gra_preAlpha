import pygame



def render(screen,player,goblin,player_right4):
    text_font = pygame.font.Font('font/Pixeltype.ttf',50)
    cursor = pygame.image.load('surface/cursor.png')

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
            
    screen.blit(attack_label,attack_label_rect)
    screen.blit(magic_label,magic_label_rect)
    screen.blit(item_label,item_label_rect)
    screen.blit(stats_label_fight,stats_label_fight_rect)

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
