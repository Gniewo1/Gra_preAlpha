import pygame
import random

def randomize(x):
    a = random.randint(1, x)
    return a




class Player:
    def __init__(self):
        self.str_score = 0
        self.dex_score = 0
        self.con_score = 0
        self.int_score = 0
        self.pkt_score = 6
        self.max_hp = (self.con_score + 8)*3
        self.current_hp = 0
        self.attack = 0
        self.attack_magic = 0
        self.AC = 0
        self.AC_flat = 0
        self.attack_penalty = 0
        self.damage_dice = 8
        self.bonus_damage = 0
        self.actions = 3
        self.flat = False


        
    def add_point(self, a):
        match a:
            case 'str':
                if self.pkt_score > 0:
                    self.str_score += 1
                    self.pkt_score -= 1
            case 'dex':
                if self.pkt_score > 0:
                    self.dex_score += 1
                    self.pkt_score -= 1
            case 'con':
                if self.pkt_score > 0:
                    self.con_score += 1
                    self.pkt_score -= 1
            case 'int':
                if self.pkt_score > 0:
                    self.int_score += 1
                    self.pkt_score -= 1

    def remove_point(self, a):
        match a:
            case 'str':
                if self.str_score > 0:
                    self.pkt_score += 1
                    self.str_score -= 1
            case 'dex':
                if self.dex_score > 0:
                    self.pkt_score += 1
                    self.dex_score -= 1
            case 'con':
                if self.con_score > 0:
                    self.pkt_score += 1
                    self.con_score -= 1
            case 'int':
                if self.int_score > 0:
                    self.pkt_score += 1
                    self.int_score -= 1

    def calculate_stats(self):
        self.max_hp = (self.con_score + 8)*3
        self.attack = self.str_score + 5
        self.AC = self.dex_score + 13
        self.AC_flat = self.dex_score + 11
        self.attack_magic = self.int_score + 5

    def reset_actions(self):
        self.actions = 3
        self.attack_penalty = 0



class Monster:
     def __init__(self):
        self.current_hp = 0
        self.max_hp = 0
        self.attack = 0
        self.damage_dice = 0
        self.damage_bonus = 0
        self.AC = 0
        self.AC_flat = 0
        self.reflex = 0
        self.will = 0
        self.fortitude = 0
        self.attack_penalty = 0
        self.flat = False

class Goblin(Monster):
    def __init__(self):
        self.current_hp = 17
        self.max_hp = 17
        self.attack = 8
        self.damage_dice = 8
        self.damage_bonus = 3
        self.AC = 17
        self.AC_flat = 15
        self.reflex = 18
        self.will = 15
        self.fortitude = 17
        self.attack_penalty = 0
        self.flat = False

class Fight(Player,Monster):
    def __init__(self, Player,Monster):
        self.player = Player
        self.monster = Monster

    def player_attack(self,Player,Monster):
        attack_roll = randomize(20)
        attack_total = attack_roll + Player.attack - Player.attack_penalty
        if Monster.flat: result_number = attack_total - Monster.AC_flat
        else: result_number = result_number = attack_total - Monster.AC
       

        Player.attack_penalty += 5
        Player.actions -= 1

        if result_number < 0:
            result = 0
        elif 0 <= result_number < 10:
            result = 1
        else: result = 2
        return attack_roll, attack_total, result

    def player_damage(self,Player):
        damage_roll = randomize(Player.damage_dice)
        damage = (damage_roll + Player.bonus_damage)
        return damage
        

    def monster_attack(self,Player,Monster):
        attack_roll = randomize(20)
        attack_total = attack_roll + Monster.attack - Monster.attack_penalty
        if Player.flat: result_number = attack_total - Player.AC_flat
        else: result_number = result_number = attack_total - Player.AC

        Monster.attack_penalty += 5
        Monster.actions -= 1

        if result_number < 0:
            result = 0
        elif 0 <= result_number < 10:
            result = 1
        else: result = 2
        return result

    def monster_damage(self,Monster,Player):
        damage_roll = randomize(Monster.damage_dice)
        damage = damage_roll + Monster.bonus_damage
        Player.current_hp -= damage
        return damage

    








    








