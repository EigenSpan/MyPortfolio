# 						NOT VERY GOOD GAME
#					       --------------------

#   Developed By 
# ------------------
# Garrett Leigh Moon
# Kirsten Anne Moon


# Note the game is Absolutely incomplete. It is fully playable but some functionality isnt there. It shouldn't ever really crash
# I am continuing to fix the bugs in this game and polish it off as well I am completly remaking the game fully in object oriented programming


# 				  BUGS TO FIX / THINGS TO IMPLEMENT
# -------------------------------------------------------------------


# 8) DEFINE load_game
# 7) DEFINE save_game
# 12) ADD DIFFERENT COLOURS AND FONTS IN PRINT FOR DIFFERENT THINGS
# 5) ADD BONUS RANDOM CHANCE DROP ITEMS FROM MONSTERS
# 9) EDIT DIE FUNCTION TO EITHER LOAD OR PLACE YOU IN AN INFERMARY LOSING SOME THINGS
# 4) PUT AND EMPTY STRING VARIABLE INSIDE OF EACH ROOM AND IF PLAYER IS IN THAT ROOM THEN THE STRING IS NONEMPTY TO SHOW WHERE YOU ARE
# 11) ALSO ADD A LEGEND TO THE MAP AND maybe some other stuff
# 10) EDIT STATS FUNCTION TO SHOW ALL AVAILABLE SPELLS
# 2) ADD EXAMINE OPTIONS TO EVERY INGAME ITEM
# 13) COMMENT ALL CODE WHEN I HAVE A CHANCE
# LAST) ENEMY BALANCING COMES VERY LAST WHEN REST OF GAME IS MADE AND WORKS FINE
# 14) EDIT SHOP TO LOOK NICER
# SECOND) LINE 224 MAKE IT SO IF YOU HAVE MORE THAN 1 OF SAME ITEM IN INVENT IT PUTS THE NUMBER YOU HAVE IN FRONT OF THE ITEM
# FIRST) THE CODE IS SLIGHTLY BUGGED BETWEEN LINE 2164 AND LINE 2175 IT WORKS BUT NOT EXACTLY THE WAY I WANT IT
# FROM ABOVE) IF THE QUEST ITEMS HANDED IN ARENT IN SPECIFIC ORDER IT STOPS TAKING THEM AND YOU HAVE TO TALK TO HIM AGAIN TO GIVE REST IN
# FROM ABOVE) IT NEEDS TO ACCEPT ALL ITEMS IN YOUR INVENT IN ANY ORDER
# SECOND LAST) POPULATE OBJECTS IN ROOMS AND THEIR EXAMINE AND CHECK OPTIONS
# AFTER QUESTS) MAKE LIST ATTRIBUTE FOR ORES REQUIRED TO REFORGE EACH ITEM
# IF YOU ARE SMART LATER I THINK CELL 1 SHOULD UNLOCK A BONUS MAP THAT GOES DEEP DOWN OR SOMETHING
# MAYBE ADD DESCRIPTIONS OF EACH ROOM WITH THE EXAMINE FUNCTION
# ALSO CHANGE HIS GENERAL DIALOGUE AFTER HE SAYS CONGRATS YOU DID IT KID
# WEAPONS APPEAR WITH UNDERSCORE IN PLAYER EQUIP SLOTS CHANGE THAT TO A SPACE
# RESOURCES PART OF INVENTORY SEEMS TO BE LEAKING OVER THE BOX LINES
# REFORGE DOESNT WORK ON ITEMS THAT ARE MORE THAN 2 WORDS LONG CLEARLY JUST READING ISSUE
# SWAP ANY UNDERSCORES IN TEXT PRINTED TO SPACES ONCE DONE FIRST MAP
# DEFINE USE FUNCTION AND MAKE IT SO DOORS UNLOCK ONLY WHEN YOU USE THE APPROPRIATE KEY IN THE CORRECT ROOM
# TEST ARMORY CODE FOR ANY PROBLEMS
# WRITE FIRE EMBLEM INTO GAME SOMEWHERE
# REBALANCE ARMORS TO NOT GO OVER 100% DAMAGE REDUCTION

#							  Imports
# ---------------------------------------------------------------------

import os
import sys
import platform
import random
import math




# 							  GLOBALS
# ---------------------------------------------------------------------

player_name_choice = 'unknown'
level_up_xp = (10, 25, 40, 70, 100, 160, 250, 400, 700, 1300, 2500, 3200, 4800, 5600, 7200, 8900, 10000)
list_of_all_enemies = ["rat", "goblin", "troll", "slime", "giant", "guard"]
robbery = False
robbery_quest_complete = False
guard_post_quest_started = False
guard_post_quest_completed = False
quest_started_unlocking_the_forge = False
quest_completed_unlocking_the_forge = False
quest_unlocking_the_forge_pt2 = False
quest_started_a_colossal_task = False

# 							GAME UTILITY
# ---------------------------------------------------------------------

# CHECKS WHICH SYSTEM IS USED AND CLEARS SCREEN ACCORDINGLY
def system_checker():
	if platform.system() == "Linux" or platform.system() == "Darwin":
		os.system("clear")
	
	elif platform.system() == "Windows":
		os.system("cls")
	
	else:
		pass


# Allows the player to load a previously saved game.
def load_game():
	pass

# Allows the player to save their current progress.
def save_game():
	pass



# Adds a slight pasue that prompts player to hit enter to continue.
def continue_function():
	skip = False
	while not skip:
		answer = input("\nHit Enter To Continue: ")
		if answer == '':
			break
		else:
			pass
	system_checker()


# swaps underscores for spaces.
def underscore_swapper(some_str = ""):
	new_str = ""
	for i in some_str:
		if i != "_":
			new_str += i
		else:
			new_str += " "
	return new_str


def reverse_underscore_swapper(some_str = ""):
	new_str = ""
	for i in some_str:
		if i != " ":
			new_str += i
		else:
			new_str += "_"
	return new_str

# 						player CLASSES
# --------------------------------------------------------------------


# player damage will be set equal to the weapon of choices damage
# Used to generate the inital player player as an instance


# INHERIT ITEMS
class Charactors():


	def __init__(self, name, weapon, armor, attack_style, gold, current_hp, max_hp, hp_lvl, hp_xp, current_mana, max_mana, total_lvl, melee_lvl, melee_xp, ranged_lvl, ranged_xp, magic_lvl, magic_xp, defence_lvl, defence_xp, enemy, current_room, up_room, down_room, left_room, right_room, dungeon_map, inventory, item1, item2, item3):
		self.name = name
		self.weapon = weapon
		self.armor = armor
		self.attack_style = attack_style
		self.gold = gold
		self.current_hp = current_hp
		self.max_hp = max_hp
		self.hp_lvl = hp_lvl
		self.hp_xp = hp_xp
		self.current_mana = current_mana
		self.max_mana = max_mana
		self.total_lvl = total_lvl
		self.melee_lvl = melee_lvl
		self.melee_xp = melee_xp
		self.ranged_lvl = ranged_lvl
		self.ranged_xp = ranged_xp
		self.magic_lvl = magic_lvl
		self.magic_xp = magic_xp
		self.defence_lvl = defence_lvl
		self.defence_xp = defence_xp
		self.enemy = enemy
		self.current_room = current_room
		self.up_room = up_room
		self.down_room = down_room
		self.left_room = left_room
		self.right_room = right_room
		self.dungeon_map = dungeon_map
		self.inventory = inventory
		self.item1 = item1
		self.item2 = item2
		self.item3 = item3


	def equip(self, player_equip_choice):
		valid_choice = False
		for i in self.inventory:
			if (player_equip_choice) in self.inventory[i]:
				valid_choice = True
				if (eval(player_equip_choice)).item_type == "melee_weapon":
					player.weapon = eval(player_equip_choice)
					print("You have Equipped {}.".format(self.weapon.name))
					break
				
				elif (eval(player_equip_choice)).item_type == "armor":
					player.armor = eval(player_equip_choice)
					print("You Have Equipped {}.".format(self.armor.name))
					break
				
				elif (eval(player_equip_choice)).item_type == "item":
					if player.item1 == "no item":
						player.item1 = player_equip_choice
						(player.inventory["items"]).remove(player.item1)
						print("You Have Equipped {}.".format(underscore_swapper(self.item1)))

					elif player.item2 == "no item":
						player.item2 = player_equip_choice
						(player.inventory["items"]).remove(player.item2)
						print("You Have Equipped {}.".format(underscore_swapper(self.item2)))

					elif player.item3 == "no item":
						player.item3 = player_equip_choice
						(player.inventory["items"]).remove(player.item3)
						print("You Have Equipped {}.".format(underscore_swapper(self.item3)))

					else:
						print("You Don't Have any Open Item Slots.")

				
				else:
					pass
			
			else:
				pass
		
		if valid_choice:
			pass
		
		else:
			print("You don't have a {} to equip".format(underscore_swapper(player_equip_choice)))


	def inventory_check(self):
		system_checker()
		stats()
		print(" "*5 + "Inventory")
		print("+" + "-"*(max(len(", ".join(self.inventory["weapons"])) + 9, len(", ".join(self.inventory["armors"])) + 8, len(", ".join(self.inventory["items"])) + 7, len(", ".join(self.inventory["resources"])) + 11, len(", ".join(self.inventory["miscellaneous"])) + 15)) + "+")
		print("|Weapons: " + ", ".join(self.inventory["weapons"]) + " "*((max(len(", ".join(self.inventory["weapons"])), len(", ".join(self.inventory["armors"])) + 8, len(", ".join(self.inventory["items"])) + 7, len(", ".join(self.inventory["resources"])) + 11, len(", ".join(self.inventory["miscellaneous"])) + 15)) - len(", ".join(self.inventory["weapons"])) - 9) + "|")
		print("|Armors: " + ", ".join(self.inventory["armors"]) + " "*((max(len(", ".join(self.inventory["weapons"])) + 9, len(", ".join(self.inventory["armors"])), len(", ".join(self.inventory["items"])) + 7, len(", ".join(self.inventory["resources"])) + 11, len(", ".join(self.inventory["miscellaneous"])) + 15)) - len(", ".join(self.inventory["armors"])) - 8) + "|")
		print("|Items: " + ", ".join(self.inventory["items"]) + " "*((max(len(", ".join(self.inventory["weapons"])) + 9, len(", ".join(self.inventory["armors"])) + 8, len(", ".join(self.inventory["items"])), len(", ".join(self.inventory["resources"])) + 11, len(", ".join(self.inventory["miscellaneous"])) + 15)) - len(", ".join(self.inventory["items"])) - 7) + "|")
		print("|Rescources: " + ", ".join(self.inventory["resources"]) + " "*((max(len(", ".join(self.inventory["weapons"])) + 9, len(", ".join(self.inventory["armors"])) + 8, len(", ".join(self.inventory["items"])) + 7, len(", ".join(self.inventory["resources"])), len(", ".join(self.inventory["miscellaneous"])) + 15)) - len(", ".join(self.inventory["resources"])) - 12) + "|")
		print("|Misc: " + ", ".join(self.inventory["miscellaneous"]) + " "*((max(len(", ".join(self.inventory["weapons"])) + 9, len(", ".join(self.inventory["armors"])) + 8, len(", ".join(self.inventory["items"])) + 7, len(", ".join(self.inventory["resources"])) + 11, len(", ".join(self.inventory["miscellaneous"])) + 15)) - len(", ".join(self.inventory["miscellaneous"])) - 6) + "|")
		# WORKS
		print("+" + "-"*(max(len(", ".join(self.inventory["weapons"])) + 9, len(", ".join(self.inventory["armors"])) + 8, len(", ".join(self.inventory["items"])) + 7, len(", ".join(self.inventory["resources"])) + 11, len(", ".join(self.inventory["miscellaneous"])) + 15)) + "+")
		continue_function()

	# ensures the players inventory only contains unique items and numbers how many nonuniques there are
	def inventory_sort(self):
		for i,j in self.inventory["resources"]:
			if i == j:
				pass

			else:
				pass


	# Allows the player to cast a spell
	def spell_cast():
		pass


# player has starting stats
# -------------------------
# name = unknown until chosen by the player
# weapon = none unil taught to fight then given fists
# armor = none until given rags
# atack_style = melee can be changed to ranged or magic
# gold = 0
# current hp = 10
# max hp = 10
# hp_lvl = 1
# hp xp = 0
# current mana = 5
# total mana = 5
# total xp = 0
# melee lvl = 1
# melee xp = 0
# ranged lvl = 1
# ranged xp = 0
# magic lvl = 1
# magic xp = 0
# defence lvl = 1
# defence xp = 0
# enemy = None
# current_room = None
# up_room = None
# down_room = None
# left_room = None
# right_room = None
# map = False
player = Charactors(player_name_choice, 'None', 'None', 'melee', 0, 10, 10, 1, 0, 5, 5, 0, 1, 0, 1, 0, 1, 0, 1, 0, "None", "None", "None", "None", "None", "None", False, {"weapons": ["fists"], "armors": ["rags"], "items": ["health_potion","mana_potion",'bomb', "health_potion"], "resources": [], "miscellaneous" : []}, "no item", "no item", "no item")


# NAME 3 ITEMS SLOTS AS ATTRIBUTES IN CHARACTORS CLASS AND FINISH UP THE STATS FUNCTION
# ADD A SPOT FOR CASTABLE SPELLS

def stats():
	print("+" + "-"*20 +         										       												         		       "+")
	print("|" + "{}'s Stats".format(player.name) + " "*(12 - len(player.name)) + 													     		   "|" + "-"*22 +                                                             											 			     "+")
	print("|" + "Level {}".format(player.total_lvl) + " "*(14 - len(str(player.total_lvl))) + 													   "|" + " "*4 + "Equipped Gear" + " "*5 + 																								 "|")
	print("|" + "-"*20 +                                                       													     		       "|" + "-"*22 +                               											   											 "|")
	print("|" + "{}/{} Hitpoints".format(player.current_hp, player.max_hp) + " "*(9 - len(str(player.current_hp)) - len(str(player.max_hp))) +     "|" + "Weapon: " + underscore_swapper(str(player.weapon.name)) + " "*(14 - len(str(player.weapon.name))) +       					 "|")
	print("|" + "{}/{} Mana".format(player.current_mana, player.max_mana) + " "*(14 - len(str(player.current_mana)) - len(str(player.max_mana))) + "|" + "Damage: " + str(player.weapon.damage + player.melee_lvl) + " "*(14 - len(str(player.weapon.damage + player.melee_lvl))) +      "|") 
	print("|" + "{} Melee".format(player.melee_lvl) + " "*(14 - len(str(player.melee_lvl))) +       											   "|"  + "Armor: " + underscore_swapper(str(player.armor.name)) + " "*(15 - len(str(player.armor.name))) +         					 "|")
	print("|" + "{} Ranged".format(player.ranged_lvl) + " "*(13 - len(str(player.ranged_lvl))) +    											   "|"  + "Defence: " + str(player.armor.defence) + " "*(13 - len(str(player.armor.defence))) + 										 "|")
	print("|" + "{} Magic".format(player.magic_lvl) + " "*(14 - len(str(player.magic_lvl))) + 												       "|" + "Item 1: " + underscore_swapper(player.item1) + " "*(14 - len(player.item1)) +        											 "|")
	print("|" + "{} Defence".format(player.defence_lvl) + " "*(12 - len(str(player.defence_lvl))) +                                                "|" + "Item 2: " + underscore_swapper(player.item2) + " "*(14 - len(player.item2)) +        											 "|")
	print("|" + "{} Gold".format(player.gold) + " "*(15 - len(str(player.gold))) +        														   "|" + "Item 3: " + underscore_swapper(player.item3) + " "*(14 - len(player.item3)) +       											 "|")
	print("+" + "-"*20 +																													       "+" + "-"*22 + "+")


class pets():
	pass







# Generates monsters as instances to fight

class monster():
	
	def __init__(self, name, lvl, current_hp, max_hp, current_mana, max_mana, damage, gold_drop, xp_gain, quest_drop = "None"):
		self.name = name
		self.lvl = lvl
		self.current_hp = current_hp
		self.max_hp = max_hp
		self.current_mana = current_mana
		self.max_mana = max_mana
		self.damage = damage
		self.gold_drop = gold_drop
		self.xp_gain = xp_gain
		self.quest_drop = quest_drop

# Rat has stats
# -------------
# name = rat
# current_hp = 6
# max_hp = 6
# current_mana = 0
# max_mana = 0
# damage = 0.5
# attack_speed = 8
# gold_drop = 3
# xp_gain = 5


rat = monster('rat', 1, 6, 6, 0, 0, 1, 3, 5)

goblin = monster('goblin', 3, 10, 10, 0, 0, 2, 7, 10)

troll = monster('troll', 5, 15, 15, 0, 0, 3, 11, 25)

slime = monster("slime", 7, 25, 25, 0, 0, 6, 16, 45 )

giant = monster('giant', 10, 80, 80, 0, 0, 7, 140, 100)

crazy_joe = monster("crazy_joe", 1, 12, 12, 0, 0, 1, 15, 10)

guard = monster("guard", 12, 40, 40, 10, 10, 5, 80, 60)


hooded_figure_monster = monster("Hooded Figure", 3, 18, 18, 0, 0, 2, 25, 50 )
mercenary = monster("mercenary", 3, 18, 18, 0, 0, 2, 25, 50)

warden = monster("warden", 20, 200, 200, 100, 100, 11, 1600, 2000)

overseer = monster("overseer", 25, 500, 500, 200, 200, 17, 2500, 3000)

# CHECK IF I CAN GET RID OF THIS
# List of enemy instances

list_of_enemies = [rat, goblin, troll, giant]

# This allows the monsters names to be called

list_of_enemies_names = [rat.name + ",", goblin.name + ",", troll.name + ", or", giant.name]

# Generates NPC's as instances

# WILL MAKE THE MONSTER GOLD DROPS DISTRIBUTED
def gold_calc():
	pass



def enemy_stats():
	print("|" + "-"*20 +                                                                                                                                                   "|")
	print("|" + "{}'s Stats".format(player.enemy.name) + " "*(12 - len(player.enemy.name)) + 													     		               "|")
	print("|" + "-"*20 + 																																			       "|")
	print("|" + "{}/{} Hitpoints".format(player.enemy.current_hp, player.enemy.max_hp) + " "*(9 - len(str(player.enemy.current_hp)) - len(str(player.enemy.max_hp))) +     "|")
	print("|" + "{}/{} Mana".format(player.enemy.current_mana, player.enemy.max_mana) + " "*(14 - len(str(player.enemy.current_mana)) - len(str(player.enemy.max_mana))) + "|")
	print("|" "{} Gold".format(player.enemy.gold_drop) + " "*(15 - len(str(player.enemy.gold_drop))) + 																	   "|")
	print("|" + "-"*20 + 																																				   "|")


# 							GEAR CLASSES
# --------------------------------------------------------------------



# Generates Melee Weapons as instances

class MeleeWeapon():

	item_type = "melee_weapon"

	def __init__(self, name, damage, lifesteal, melee_lvl_required, cost, reforge_number = 0):
		self.damage = damage
		self.lifesteal = lifesteal
		self.melee_lvl_required = melee_lvl_required
		self.cost = cost		
		self.name = name
		self.reforge_number = reforge_number

	# used to modify melee effects
	
	def melee_modifiers(self):
		return 0


	# returns total damage that a player attack will do
	# will change to a random number between some value and max value after beta

	def total_melee_damage(self):
		return (player.weapon.damage + player.melee_lvl + player.weapon.melee_modifiers())

	def total_lifesteal(self):
		return (player.weapon.total_melee_damage() * player.weapon.lifesteal / 100)


# Attack speed (1-10) 10 being fastest

# shortsword stats
# -----------------
# damage = 5
# accuracy = 95 
# cleave_range = 3 
# attack_speed = 9 
# lifesteal = 0
# melee_lvl_required = 2
# cost = 50

fists = MeleeWeapon("fists", 1, 0, 1, 0)

wood_sword = MeleeWeapon("wood_sword", 2, 0, 1, 5)

shortsword = MeleeWeapon("shortsword", 5, 0, 2, 50)

longsword = MeleeWeapon("longsword", 9, 0, 3, 125)

greatsword = MeleeWeapon("greatsword", 12, 0, 7, 400)

supreme_sword = MeleeWeapon("supreme_sword", 18, 0, 13, 1200)

vampire_sword = MeleeWeapon("vampire_sowrd", 14, 15, 17, 2200)

ultimate_sword = MeleeWeapon("ultimate_sowrd", 23, 7, 24, 5000)

death_scythe = MeleeWeapon("death_scythe", 35, 20, 25, 9999)




#IGNORE RANGED AND MAGIC FOR THE BETA
#-------------------------------------

# Generates ranged weapons

class RangedWeapon():

	def __init__(self, name, damage, ranged_lvl_required, cost):
		self.name = name
		self.damage = damage
		self.ranged_lvl_required = ranged_lvl_required
		self.cost = cost

	# used to modify ranged effects

	def total_ranged_damage():
		pass

# slingshot stats
# ---------------
# damage = 3
# arrow_range = 25
# reload_speed = 6
# arrow_velocity = 3
# ranged_lvl_required = 1
# cost = 25

slingshot = RangedWeapon("slingshot", 3, 1, 25)

short_bow = RangedWeapon("short_bow", 6, 2, 120)

long_bow = RangedWeapon("long_bow", 11, 5, 500)

crossbow = RangedWeapon("crossbow", 16, 11, 1400)

god_bow = RangedWeapon("god_bow", 22, 18, 2600)

artemis_bow = RangedWeapon("artemis_bow", 33, 25, 6300)


# Generates magic spells

class spells():
	pass




# Generates armors as instances

class Armors():
	
	item_type = "armor"

	def __init__(self, name, shineyness, defence_lvl_required, defence, cost, reforge_number = 0):
		self.name = name
		self.shineyness = shineyness
		self.defence_lvl_required = defence_lvl_required
		self.defence = defence
		self.cost = cost
		self.reforge_number = reforge_number

	def defence_modifiers(self):
		return 0

	def total_defence(self):
		return (player.armor.defence + player.defence_lvl + player.armor.defence_modifiers())


# TEST

class Items(Charactors):

	item_type = "item"

	def __init__(self, owner, name, damage, health_restore, mana_restore, cost):
		self.owner = owner
		self.name = name
		self.damage = damage
		self.health_restore = health_restore
		self.mana_restore = mana_restore
		self.cost = cost

	# NO ERRORS BUT NOT USING ITEM PROBABLY THE IF IN ITEMLIST IS FAILING
	def use_item(item_choice):
		item_list = [player.item1, player.item2, player.item3]
		enemy_hp_lost = 0
		used_item = False

		if item_choice in item_list:
		
			
			if item_choice == "bomb":
				if player.enemy != "None":
					player.enemy.current_hp -= (eval(item_choice)).damage
					used_item = True
					print("You Have Dealt {} Damage To The {}".format((eval(item_choice)).damage, player.enemy.name))
				else:
					print("You Don't Have An Enemy To Throw A Bomb At")

			elif item_choice == "health_potion":
				if player.current_hp < player.max_hp:
					player.current_hp += round(player.max_hp * (eval(item_choice)).health_restore)
					if player.current_hp > player.max_hp:
						player.current_hp = player.max_hp
						used_item = True
						print("You Drink A Health Potion And Restore Your Health To Full")
					else:
						used_item = True
						print("You Drink A Health Potion And Restore {} Health".format(round((eval(item_choice)).health_restore * player.max_hp)))	
				else:
					print("Your Health Is Already Full")

			elif item_choice == "mana_potion":
				if player.current_mana < player.max_mana:
					player.current_mana += round(player.max_mana * (eval(item_choice)).mana_restore)
					if player.current_mana > player.max_mana:
						player.current_mana = player.max_mana
						used_item = True
						print("You Drink A Mana Potion And Restore Your Mana To Full")
					else:
						used_item = True
						print("You Drink A Mana Potion And Restore {} Mana".format(round((eval(item_choice)).mana_restore * player.max_mana)))
				else:
					print("Your Mana Is Already Full")

			if used_item:
				for i in range(len(item_list)):

					if item_list[i] == item_choice:
						item_list[i] = "None"

						if item_list[0] == "None":
							player.item1 = "no item"

						elif item_list[1] == "None":
							player.item2 = "no item"

						elif item_list[2] == "None":
							player.item3 = "no item"
			else:
				pass
					
		else:
			print("You Do Not Have A {} Equipped To Use".format(underscore_swapper(item_choice)))


health_potion = Items(player, "health potion", 0, 0.33, 0 , 50)

mana_potion = Items(player, "mana potion", 0, 0, 0.33, 100)

bomb = Items(player, "bomb", 5, 0, 0, 100)

no_item = Items(player, "no item", 0, 0, 0, 0)


# demon plate stats
# -----------------
# shineyness = Matte Black
# defence_lvl_required = 25
# defence = 40
# cost = 8000
# potion_slots = 5

guard_armor = Armors("guard_armor", "pretty shiney", 1, 1, 0)

rags = Armors("rags", 'The least shiney anything can be', 1, 1, 0)

not_rags = Armors("not_rags", 'Shineyer than rags but still not very shiney',2 , 3, 22)
	
leather_gear = Armors("leather_gear", 'slightly shiney when you polish it', 3, 5, 88)

prime_leather = Armors("prime_leather", "slightly shiney even when not polished", 5, 8, 165)

rusty_metal = Armors("rusty_metal", "less shiney than you'd like", 8, 11, 385)

chain_mail = Armors("chain_mail", "starting to see the shine", 11, 16, 900)

plate_mail = Armors("plate_mail", "ooh shiney", 15, 21, 1400)

elegant_mail = Armors("elegant_mail", "Thats some shine", 19, 24, 2200)

flawless_plate = Armors("flawless_plate", "Shineyer than the sun", 22, 29, 3700)

god_plate = Armors("god_plate", "BLINDINGLY SHINEY", 24, 33, 5600)

demon_plate = Armors("demon_plate", "Matte Black", 25, 40, 8000)


class NPC():
	
	def __init__(self, name, room, stock, dialogue, store_type = "None", quest_items = []):
		self.name = name
		self.room = room
		self.stock = stock
		self.dialogue = dialogue
		self.store_type = store_type
		self.quest_items = quest_items
		# Find a better way to interchange the title of damage and defence.
	def trade(self):

		while True:
			system_checker()
			stats()
			print(" ")
			print("What would you like to buy?")
			print("---------------------------")
			if self.store_type == "weapon_store":
				print("  Name           DMG       Level  Cost")
				print("  ----           ---       -----  ----")
			elif self.store_type == "armor_store":
				print("  Name           DEF       Level  Cost")
				print("  ----           ---       -----  ----")
			elif self.store_type == "item_store":
				print("  Name             Cost")
				print("  ----             ----")
			else:
				pass

			for i in self.stock:
				if (eval(i)).item_type == "melee_weapon":
					print("- " + str(underscore_swapper(i)) + ":" + " "*(16 - len(i)) + str((eval(i)).damage) + " "*(9 - len(str((eval(i)).damage))) + str((eval(i).melee_lvl_required)) + " "*(6 - len(str((eval(i).melee_lvl_required)))) + str((eval(i)).cost) + " Gold")
				elif (eval(i)).item_type == "armor":
					print("- " + str(underscore_swapper(i)) + ":" + " "*(16 - len(i)) + str((eval(i)).defence) + " "*(9 - len(str((eval(i)).defence))) + str((eval(i).defence_lvl_required)) + " "*(6 - len(str((eval(i).defence_lvl_required)))) + str((eval(i)).cost) + " Gold")
				elif (eval(i)).item_type == "item":
					print("- " + str(underscore_swapper(i)) + ":" + " "*(16 - len(i)) + str((eval(i)).cost) + " Gold")

			print("- Leave")
			player_response = input(": ").lower().strip()
			if reverse_underscore_swapper(player_response) in self.stock:
				if player.gold >= (eval(reverse_underscore_swapper(player_response))).cost:
					if eval(reverse_underscore_swapper(player_response)).item_type == "melee_weapon":
						if player.melee_lvl >= (eval(reverse_underscore_swapper(player_response)).melee_lvl_required):
							player.gold -= (eval(reverse_underscore_swapper(player_response))).cost
						# USE THIS LATER TO CHECK ITEM TYPE
							system_checker()
							stats()
							player.inventory["weapons"].append(reverse_underscore_swapper(player_response))
							print("You have bought a {}".format(player_response))
							self.stock.remove(reverse_underscore_swapper(player_response))
							continue_function()
							break

						else:
							system_checker()
							stats()
							print("Your melee level isnt high enough to use this item")
							continue_function()
							pass

					elif eval(reverse_underscore_swapper(player_response)).item_type == "armor":
						if player.defence_lvl >= (eval(reverse_underscore_swapper(player_response)).defence_lvl_required):	
							player.gold -= (eval(reverse_underscore_swapper(player_response))).cost
							system_checker()
							stats()
							player.inventory["armors"].append(reverse_underscore_swapper(player_response))
							print("You have bought a {}".format(player_response))
							self.stock.remove(reverse_underscore_swapper(player_response))
							continue_function()
							break

						else:
							system_checker()
							stats()
							print("Your defence level isnt high enough to use this item")
							continue_function()
							pass
					else:
						pass	

				else:
					system_checker()
					stats()
					print("You do not have enough gold to buy this item")
					continue_function()
					pass

			elif player_response == "leave":
				system_checker()
				stats()
				print("You leave.")
				continue_function()
				break

			else:
				pass

	# dialogue_selec will pick which sequence of words will be said by npc
	def talk(self, dialogue_select):
		if self.dialogue[dialogue_select] == "None":
			pass
		else:
			system_checker()
			stats()
			print(self.name + ": " + self.dialogue[dialogue_select])

kiffy = NPC("Kiffy", "corridor", ["death_scythe", "artemis_bow", "demon_plate"], {"corridor_dialogue" : "If you want to escape this prison you are going to need a map.\nJoe in cell 3 should be able to help you with that.\nJust be careful he can be a bit nutty", "general_dialogue": " "})

billy = NPC("Billy", "weapon_smith", ["wood_sword", "shortsword", "longsword", "greatsword", "supreme_sword", "vampire_sword", "ultimate_sword"], {"billy_dialogue1": "Wow! You killed that big rat all on your own?\n Well aren't you just a big hero\n Maybe one day you can actually kill a monster bigger than my foot...\n In the meantime if you got the gold I got the guns... I mean swords.", "billy_dialogue2": "Hey uh sorry... It's been a rough day.\nMy brother was killed last night protecting my shop.\nWell If you need any weapons you can buy em here.", "general_dialogue": "Those damn goblins! You gotta watch your gold around them."}, "weapon_store")

mell = NPC("Mell", "armor_smith", ["not_rags", "leather_gear", "prime_leather", "rusty_metal", "chain_mail", "plate_mail", "elegant_mail", "flawless_plate", "god_plate"], {"mell_dialogue1": "Hey! I heard you killed crazy joe.\nThanks, that guy would always come around and try and bite me.\nHeres 300 gold for getting him off my back.\nI can also sell your armors to keep you alive longer in here.", "general_dialogue": "If you want to survive here, you're going to need to become an experienced fighter."}, "armor_store")

clara = NPC("Clara", "alchemist", ["health_potion", "mana_potion", "bomb"], {"general_dialogue": "Sometimes the guards take people... Once they pass the guard post, they are never seen again."}, "item_store")

hooded_figure = NPC("Hooded Figure", "cell_5", [], {"robbery1": "Hey you wanna get some weapons fast?", "robbery2.y": "All we gotta do is rob billy the weapon smith, are you in?", "robbery2.n": "Whatever man see you later.", "robbery3.y": "He has a mercenary guard his wares at night. Kill the merc and steal some gear.", "robbery3.n": "You know too much... time to die!", "general_dialogue": "None"})

marco = NPC("marco", "cell_10", [], {"general_dialogue": "None", "guard_post_quest": "Hey we need to get out of here. I'm planning an attack on the guard tower, are you in?", "guard_post_quest.yes": "Talk to me in cell 4 when you are ready. We will escape!", "guard_post_quest.no": "Come talk to me again when you change your mind", "guard_post_quest_not_strong_enough": "Come talk to me again when you are stronger", "guard_post_quest_ready": "The only way out is through that guard post, Are you ready to fight some guards?", "guard_post_quest_ready.no": "Gear up and come talk to me when you are ready", "guard_post_quest_ready.yes": "Lets go for our freedom", "colossal_task_start": "We're gunna get out of this \nFirst we have to get through the marble hall and break into the armory \nThe marble hall will be filled with guards so be ready for lots of fighting \nUnless you can find a way in without killing all the guards \nIn the armory The warden resides, he will put up a big fight \nAfter killing him we will need to fight our way through the colosseum \nOnce the overseer is dead we will be free to escape \nI will follow your lead", "marco_lives": "Now we only face two more great tasks ahead \nFirst we have to kill the Warden in the armory \nThen we have to kill the Overseer \nRest up if you need to the road ahead will be challanging. \nThe armory door is locked so in the meantime search around for a key \nOnce you are ready we will head to the armory"})

drunkard = NPC("drunkard", "cell_7",[], {"general_dialogue": "I've been past the guard post... I Even saw a dragon and fire", "unlocking_the_forge_pt1": "The only way out of this place is to fight in the colosseum.\n You will be paired up against well trained warriors fortified with heavily enhanced weapons...\n Basically you will die.\n The only way you will stand a chance is to upgrade your gear using the forge.\n I was enslaved here to work the forge, if you can get past the guard post I can reforge your gear at the forge\n Once the guards are dealt with come talk to me at the forge.\nBy the way my names Thorag, and I'm counting on you to get us all out of here.", "unlocking_the_forge_pt2": "Ahh it's no good the forge is dead, but maybe...\nAha, it can be kickstarted but I need you to bring me some things...\nI need:\n------\nA rat's tail\nA troll's tooth\nA Ball of slime\nA goblin's skull\nAnd finally a Giant's hammer\nFind theese items by killing monsters found here\nJust keep in mind you might need to take a few down until you get what you're looking for.\nWill you go on this quest to revive the forge?", "unlocking_the_forge_pt2.yes": "Good come back when you have gathered all the resources", "unlocking_the_forge_pt2.no": "Well just come back if you change your mind"}, "None", ["rats_tail", "trolls_tooth", "goblin_skull", "ball_of_slime", "giants_hammer"])

miner_frank = NPC("miner frank", "mines", [], {"general_dialogue": "Hehe ya find any precious metals yet?", "mine_intro_dialogue": "Beware... The mines can be very dangerous\nIf you are willing to take the risk you can make it away with some valuble ores."})


# PRETTY SURE I CAN GET RID OF THIS BUT WILL CHECK
list_of_npcs = [kiffy, billy, mell, clara]



# 								ROOMS
#------------------------------------------------------------------------


# EITHER LINKED LIST OR HAVE variables up, down, left, right to show what rooms are in each direction and allow access

# Generates rooms as instances 

class RoomGenerator():
	def __init__(self, name = "None", up_room = "None", down_room = "None", left_room = "None", right_room = "None", enemies_in_room = "None", shop_in_room = "None", npcs_in_room = "None", room_fight = False, items_in_room = {}):
		self.name = name
		self.up_room = up_room
		self.down_room = down_room
		self.left_room = left_room
		self.right_room = right_room
		self.enemies_in_room = enemies_in_room
		self.shop_in_room = shop_in_room
		self.npcs_in_room = npcs_in_room
		self.room_fight = room_fight
		self.items_in_room = items_in_room




# items_in_room[0] = examine text
# items_in_room[1] = hidden objects


# 												PRISON MAP ROOMS
# ----------------------------------------------------------------------------------------------------------------------

cell_6 = RoomGenerator("cell_6", "None", "None", "None", "None", "None", "None", "None", False, {"bed": ["Probably not the most comfortable, but you can still rest in it", "None"], "bucket": ["When you gotta go...","None"], "cell_door": ["A locked cell door", "None"]})

corridor = RoomGenerator("corridor", "cell_3", "cell_6", "None", "None", "None", "None", "kiffy", False, {})

cell_3 = RoomGenerator("cell_3", "None", "corridor", "None", "None", crazy_joe, "None", "None", False, {})

rat_pits = RoomGenerator("rat_pits", "None", "cell_5", "None", "corridor", rat, "None", "None", True, {})

cell_5 = RoomGenerator("cell_5", "rat_pits", "weapon_smith", "None", "None", "None", "None", "hooded_figure", False, {})

weapon_smith = RoomGenerator("weapon_smith", "cell_5", "None", "None", "None", "None", "billy", "billy", False, {})

armor_smith = RoomGenerator("armor_smith", "None", "cell_7", "corridor", "troll_hut", "None", "mell", "mell", False, {})

cell_7 = RoomGenerator("cell_7", "armor_smith", "None", "None", "goblin_cave", "None", "None", "drunkard", False, {})

goblin_cave = RoomGenerator("goblin_cave", "None", "mines", "cell_7", "None", goblin, "None", "None", True, {})

mines = RoomGenerator("mines", "goblin_cave", "None", "cell_10", "None", "None", "None", "miner_frank", False, {})

cell_10 = RoomGenerator("cell_10", "None", "None", "slime_den", "mines", "None", "None", "marco", False, {})

slime_den = RoomGenerator("slime_den", "None", "None", "None", "cell_10", slime, "None", "None", True, {})

troll_hut = RoomGenerator("troll_hut", "alchemist", "None", "armor_smith", "None", troll, "None", "None", True, {})

alchemist = RoomGenerator("alchemist", "None", "troll_hut", "cell_4", "None", "None", "clara", "clara", False, {})

cell_4 = RoomGenerator("cell_4", "None", "None", "None", "alchemist", "None", "None", "None", False, {})

guard_post = RoomGenerator("guard_post", "None", "cell_4", "cell_1", "None", guard, "None", "None", False, {"armor_chest": ["A locked chest probably filled with guards armor", "None"], "table": ["A table with a note on it the note reads: \nIt is very unfortunate that darren was killed by a slime \nMoreso it was unfortunate he had the only chest key on him and it dissolved in the slime \nWe will get a new one to you once it can be made \nIt may take a while, the key mould should still be somewhere in the forge \nUnfortunatly our forge smith has escaped somewhere into the depths of the prison \nNo doubt he's passed out in a ditch somewhere \nDamn drunk \nRegardless if you can find some copper ore you can probably smelt a new key yourself \nRegards, The warden", "None"]})

cell_1 = RoomGenerator("cell_1", "None", "None", "giants_keep", "guard_post", "None", "None", "None", False, {})

giants_keep = RoomGenerator("giants_keep", "None", "None", "None", "cell_1", giant, "None", "None", True, {})

forge = RoomGenerator("forge", "giants_keep", "None", "None", "None", "None", "None", "None", False, {"shelves": ["Storage for the forge", "key_mould"]})

marble_hall = RoomGenerator("marble_hall", "None", "None", "guard_post", "None", "None", "None", "None", False, {"dead_guards": ["The guards you and marco fought","armory_key"]})

armory = RoomGenerator("armory", "None", "marble_hall", "None", "None", warden, "None", "None", False, {})

colosseum = RoomGenerator("colosseum", "None", "None", "None", "armory", overseer, "None", "None", False, {})

# -----------------------------------------------------------------------------------------------------------------------


# MAP 2 ROOMS
# -----------------------------------------------------------------------------------------------------------------------










# -----------------------------------------------------------------------------------------------------------------------


# Map 3 ROOMS
# -----------------------------------------------------------------------------------------------------------------------










# -----------------------------------------------------------------------------------------------------------------------


# 								MAPS
# ---------------------------------------------------------------------
colosseum_name = "???"
armory_name = "???"
giants_keep_name = "???"
cell_1_name = "???"
guard_post_name = "???"
marble_hall_name = "???"
forge_name = "???"
cell_4_name = "???"
alchemist_name = "???"
rat_pits_name = "???"
armor_smith_name = "???"
troll_hut_name = "???"
cell_5_name = "???"
cell_7_name = "???"
goblin_cave_name = "???"
weapon_smith_name = "???"
slime_den_name = "???"
cell_10_name = "???"
mines_name = "???"

#TURN THIS INTO A FUNCTION CALLED MAP_UPDATE WHICH WILL UPDATE THE MAP EACH TIME MAP() IS CALLED.

#              colosseum             armory

def prison_map_check():

	
	prison_map = ("||" + "-"*64 + "||" + "-"*20 + "||\n" 
			    + "||" + " "*64 + "||" + " "*20 + "||\n" 
			    + "||" + " "*((64 - len(colosseum_name))//2) + colosseum_name + " "*((64 - len(colosseum_name))//2 + len(colosseum_name) % 2) + "||" + " "*((20 - len(armory_name))//2) + armory_name + " "*((20 - len(armory_name))//2 + len(armory_name) % 2) + "||\n"
			    + "||" + " "*64 + "  " + " "*20 + "||\n"
			    + "||" + " "*64 + "||" + " "*20 + "||\n"
			    + "||" + " "*64 + "||" + " "*20 + "||\n"
			    + "||" + "-"*64 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
			    
			    #    giants_keep	    cell_1 		  guard_post     		   marble_hall
			    + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*((20 - len(giants_keep_name))//2) + giants_keep_name + " "*((20 - len(giants_keep_name))//2 + len(giants_keep_name) % 2) + "||" + " "*((20 - len(cell_1_name))//2) + cell_1_name + " "*((20 - len(cell_1_name))//2 + len(cell_1_name) % 2) +  "||" + " "*((20 - len(guard_post_name))//2) + guard_post_name + " "*((20 - len(guard_post_name))//2 + len(guard_post_name) % 2) +  "||" + " "*((20 - len(marble_hall_name))//2) + marble_hall_name + " "*((20 - len(marble_hall_name))//2 + len(marble_hall_name) % 2) + "||\n"
			    + "||" + " "*20 + "  " + " "*20 + "  " + " "*20 + "  " + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
			    
			    #    			forge		     		cell_3 	        		 cell_4 		      alchemist
			    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*((20 - len(forge_name))//2) + forge_name + " "*((20 - len(forge_name))//2 + len(forge_name) % 2) + "||" + " "*7 + "Cell 3" + " "*7  + "||" + " "*((20 - len(cell_4_name))//2) + cell_4_name + " "*((20 - len(cell_4_name))//2 + len(cell_4_name) % 2) + "||" + " "*((20 - len(alchemist_name))//2) + alchemist_name + " "*((20 - len(alchemist_name))//2 + len(alchemist_name) % 2) +"||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "  " + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
			    
			    #     rat_pits					corridor	  		  armor_smith	   			troll_hut
			    + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*((20 - len(rat_pits_name))//2) + rat_pits_name + " "*((20 - len(rat_pits_name))//2 + len(rat_pits_name) % 2) + "||" + " "*6 + "Corridor" + " "*6 + "||" + " "*((20 - len(armor_smith_name))//2) + armor_smith_name + " "*((20 - len(armor_smith_name))//2 + len(armor_smith_name) % 2) + "||" + " "*((20 - len(troll_hut_name))//2) + troll_hut_name + " "*((20 - len(troll_hut_name))//2 + len(troll_hut_name) % 2) + "||\n"
			    + "||" + " "*20 + "  " + " "*20 + "  " + " "*20 + "  " + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
			    
			    #       		  cell_5			    		 cell_6			 				cell_7		       goblin_cave
			    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*((20 - len(cell_5_name))//2) + cell_5_name + " "*((20 - len(cell_5_name))//2 + len(cell_5_name) % 2) + "||" + " "*7 + "Cell 6" + " "*7 + "||" + " "*((20 - len(cell_7_name))//2) + cell_7_name + " "*((20 - len(cell_7_name))//2 + len(cell_7_name) % 2) + "||" + " "*((20 - len(goblin_cave_name))//2) + goblin_cave_name + " "*((20 - len(goblin_cave_name))//2 + len(goblin_cave_name) % 2) + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "  " + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"

			    #     		   weapon_smith	   		  slime_den	        cell_10					mines
			    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*((20 - len(weapon_smith_name))//2) + weapon_smith_name + " "*((20 - len(weapon_smith_name))//2 + len(weapon_smith_name) % 2) + "||" + " "*((20 - len(slime_den_name))//2) + slime_den_name + " "*((20 - len(slime_den_name))//2 + len(slime_den_name) % 2) + "||" + " "*((20 - len(cell_10_name))//2) + cell_10_name + " "*((20 - len(cell_10_name))//2 + len(cell_10_name) % 2) + "||" + " "*((20 - len(mines_name))//2) + mines_name + " "*((20 - len(mines_name))//2 + len(mines_name) % 2) + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "  " + " "*20 + "  " + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
			    + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*20 + "||\n")  
	
	if player.dungeon_map:
		print("You are currently in: {}".format(player.current_room.name))
		print(prison_map)
		continue_function()
	else:
		print("You do not have a map")
		continue_function()
		pass
	

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 																				Map 2
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CHANGE ALL TITLES OF ROOMS

#              colosseum             armory
overworld_map = ("||" + "-"*64 + "||" + "-"*20 + "||\n" 
		    + "||" + " "*64 + "||" + " "*20 + "||\n" 
		    + "||" + " "*27 + "Colosseum" + " "*28 + "||" + " "*7 + "Armory" + " "*7 + "||\n"
		    + "||" + " "*64 + "  " + " "*20 + "||\n"
		    + "||" + " "*64 + "||" + " "*20 + "||\n"
		    + "||" + " "*64 + "||" + " "*20 + "||\n"
		    + "||" + "-"*64 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    
		    #    giants_keep	    cell_1 		  guard_post     		   marble_hall
		    + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*4 + "Giants Keep" + " "*5 + "||" + " "*7 + "Cell 1" + " "*7 + "||" + " "*5 + "Guard post" + " "*5 + "||" + " "*5 + "Marble hall" +" "*4 + "||\n"
		    + "||" + " "*20 + "  " + " "*20 + "  " + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
		    
		    #    			forge		     		cell_3 	        		 cell_4 		      alchemist
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*8 + "Forge" + " "*7 + "||" + " "*7 + "Cell 3" + " "*7  + "||" + " "*7 + "Cell 4" + " "*7 + "||" + " "*6 + "Alchemist" + " "*5 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    
		    #     rat_pits					corridor	  		  armor_smith	   			troll_hut
		    + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*6 + "Rat Pits" + " "*6 + "||" + " "*6 + "Corridor" + " "*6 + "||" + " "*5 + "Armor Smith" + " "*4 + "||" + " "*6 + "Troll Hut" + " "*5 + "||\n"
		    + "||" + " "*20 + "  " + " "*20 + "  " + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
		    
		    #       		  cell_5			    		 cell_6			 				cell_7		       goblin_cave
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*7 + "Cell 5" + " "*7 + "||" + " "*7 + "Cell 6" + " "*7 + "||" + " "*7 + "Cell 7" + " "*7 + "||" + " "*5 +"Goblin Cave" + " "*4 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"

		    #     		   weapon_smith	   		  slime_den	        cell_10					mines
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*4 + "Weapon Smith" + " "*4 + "||" + " "*6 + "Slime Den" + " "*5 + "||" + " "*7 + "Cell 10" + " "*6 + "||" + " "*7 + "mines" + " "*6 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "  " + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*20 + "||\n")  


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------


#																				 Map 3
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CHANGE ALL TITLES OF ROOMS

#              colosseum             armory
underworld_map = ("||" + "-"*64 + "||" + "-"*20 + "||\n" 
		    + "||" + " "*64 + "||" + " "*20 + "||\n" 
		    + "||" + " "*27 + "Colosseum" + " "*28 + "||" + " "*7 + "Armory" + " "*7 + "||\n"
		    + "||" + " "*64 + "  " + " "*20 + "||\n"
		    + "||" + " "*64 + "||" + " "*20 + "||\n"
		    + "||" + " "*64 + "||" + " "*20 + "||\n"
		    + "||" + "-"*64 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    
		    #    giants_keep	    cell_1 		  guard_post     		   marble_hall
		    + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*4 + "Giants Keep" + " "*5 + "||" + " "*7 + "Cell 1" + " "*7 + "||" + " "*5 + "Guard post" + " "*5 + "||" + " "*5 + "Marble hall" +" "*4 + "||\n"
		    + "||" + " "*20 + "  " + " "*20 + "  " + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
		    
		    #    			forge		     		cell_3 	        		 cell_4 		      alchemist
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*8 + "Forge" + " "*7 + "||" + " "*7 + "Cell 3" + " "*7  + "||" + " "*7 + "Cell 4" + " "*7 + "||" + " "*6 + "Alchemist" + " "*5 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    
		    #     rat_pits					corridor	  		  armor_smith	   			troll_hut
		    + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*6 + "Rat Pits" + " "*6 + "||" + " "*6 + "Corridor" + " "*6 + "||" + " "*5 + "Armor Smith" + " "*4 + "||" + " "*6 + "Troll Hut" + " "*5 + "||\n"
		    + "||" + " "*20 + "  " + " "*20 + "  " + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
		    
		    #       		  cell_5			    		 cell_6			 				cell_7		       goblin_cave
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*7 + "Cell 5" + " "*7 + "||" + " "*7 + "Cell 6" + " "*7 + "||" + " "*7 + "Cell 7" + " "*7 + "||" + " "*5 +"Goblin Cave" + " "*4 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"

		    #     		   weapon_smith	   		  slime_den	        cell_10					mines
		    + "||" + "-"*8 + " "*4 + "-"*8 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*8 + " "*4 + "-"*8 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*4 + "Weapon Smith" + " "*4 + "||" + " "*6 + "Slime Den" + " "*5 + "||" + " "*7 + "Cell 10" + " "*6 + "||" + " "*7 + "mines" + " "*6 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "  " + " "*20 + "  " + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||" + " "*20 + "||\n"
		    + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*20 + "||" + "-"*20 + "||\n")  


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------




# Allows the player to move rooms
def move_rooms():
	# Shows which rooms are around the players current room
	list_of_possible_moves = [underscore_swapper(player.current_room.up_room), underscore_swapper(player.current_room.down_room), underscore_swapper(player.current_room.left_room), underscore_swapper(player.current_room.right_room), "cancel"]
	# Creates a loop that only breaks when a valid room is chosen
	while True:
		stats()
		print("You can move to any of the following rooms")
		print("------------------------------------------")
		for i in list_of_possible_moves:
			# Removes all of the None rooms
			if i != "None":
				# Prints only the movable rooms
				print("- " + underscore_swapper(i) + "\n")
			else:
				pass

		where_to_move = input("Which room would you like to move to?: ").lower()
		system_checker()
		stats()
		# Makes sure you pick a valid room
		if where_to_move == "cancel":
			print("You stay put")
			continue_function()
			break

		elif where_to_move in list_of_possible_moves:
			# Moves the player to the new room
			player.current_room = eval(reverse_underscore_swapper(where_to_move))
			print("You have moved to {}".format(underscore_swapper(player.current_room.name)))
			continue_function()
			break
		# If invalid selection makes them choose again
		else:
			system_checker()
			pass


# 						PLAYER MECHANICS
#---------------------------------------------------------------------


# Levels up melee if needed
def melee_level_up(player):
	# Ensures max lvl is 25
	if player.melee_lvl < 25:
		for i in range(len(level_up_xp) - 1):
			# Makes sure you need right xp for the right level
			if player.melee_xp >= level_up_xp[i] and player.melee_lvl == i + 1:
				# Levels up the players melee lvl
				player.melee_lvl += 1
				# Sets current melee xp to 0
				player.melee_xp = 0
				print("Congratulations you have leveld up to {} melee".format(player.melee_lvl))
			else:
				pass
	else:
		pass

# Levels up ranged if needed
def ranged_level_up(player):
	if player.ranged_lvl < 25:
		for i in range(len(level_up_xp) - 1):
			if player.ranged_xp >= level_up_xp[i] and player.ranged_lvl == i + 1:
				player.ranged_lvl += 1
				player.ranged_xp = 0
				print("Congratulations you have leveld up to {} ranged".format(player.ranged_lvl))
			else:
				pass
	else:
		pass

# Levels up magic if needed
def magic_level_up(player):
	if player.magic_lvl < 25:
		for i in range(len(level_up_xp) - 1):
			if player.magic_xp >= level_up_xp[i] and player.magic_lvl == i + 1:
				player.magic_lvl += 1
				player.magic_xp = 0
				print("Congratulations you have leveld up to {} magic".format(player.magic_lvl))
			else:
				pass
	else:
		pass

# Levels up defence if needed
def defence_level_up(player):
	if player.defence_lvl < 25:
		for i in range(len(level_up_xp) - 1):
			if player.defence_xp >= level_up_xp[i] and player.defence_lvl == i + 1:
				player.defence_lvl += 1
				player.defence_xp = 0
				print("Congratulations you have leveld up to {} defence".format(player.defence_lvl))
			else:
				pass
	else:
		pass

# Levels up Hp if needed
def hp_level_up(player):
	# Ensures max lvl is 25
	if player.hp_lvl < 25:
		for i in range(len(level_up_xp) - 1):
			# Makes sure you need the right xp for the right level
			if player.hp_xp >= level_up_xp[i] and player.hp_lvl == i + 1:
				# Levels up the players hp
				player.hp_lvl += 1
				# Sets current hp_xp = o
				player.hp_xp = 0
				# Changes the players max hp to 7 + 3 * hp_lvl , 3 extra max hp per level up
				player.max_hp = 7 + (3 * player.hp_lvl)
				# When player levels up thei current hp is set to the new max
				player.current_hp = player.max_hp
				print("Congratulations you have leveld up to {} hitpoints".format(player.hp_lvl))
			else:
				pass
	else:
		pass

# Runs all level up functions to check for any possible level ups. To be called after each fight after give_xp().
def level_up():

	melee_level_up(player)

	ranged_level_up(player)

	magic_level_up(player)

	defence_level_up(player)

	hp_level_up(player)


# Gives the player xp. To be called at the end of each fight along with level_up().

def give_xp():
	# Checks the players attack style and gives xp in the according style
	if player.attack_style == "melee":
		player.melee_xp += player.enemy.xp_gain
		player.hp_xp += (player.enemy.xp_gain / 2)
		print("You have gained {} melee xp and {} hitpoints xp".format(player.enemy.xp_gain, player.enemy.xp_gain / 2))
	
	elif player.attack_style == "ranged":
		player.ranged_xp += player.enemy.xp_gain
		player.hp_xp += (player.enemy.xp_gain / 2)
		print("You have gained {} ranged xp and {} hitpoints xp".format(player.enemy.xp_gain, player.enemy.xp_gain / 2))
	
	elif player.attack_style == "magic":
		player.magic_xp += player.enemy.xp_gain
		player.hp_xp += (player.enemy.xp_gain / 2)
		print("You have gained {} magic xp and {} hitpoints xp".format(player.enemy.xp_gain, player.enemy.xp_gain / 2))
	
	else:
		pass

	player.defence_xp += player.enemy.xp_gain / 3


# ONCE LOAD IS DEFINED WHEN YOU DIE LOAD LAST SAVE OR WE CAN MAKE AN INFIRMERY AND SOME PENALTY
# Kills player if hp falls to 0
def die():
	dead = False
	if player.current_hp == 0:
		dead = True
		print("You Have Died!")
		return dead
	else:
		return dead


# Allows the player to attack and deals damage to the current enemy and gives player health if they have lifesteal.
def melee_attack():
	# If the players weapon has no lifesteal gives no health
	if player.weapon.lifesteal == 0:
		pass
	else:
		# Ensures the players hp will never go above their max hp from lifesteal.
		if player.current_hp + player.weapon.total_lifesteal() > player.max_hp:
			player.current_hp = player.max_hp
		else:
			# Allows the player to lifesteal and prints how much life you have stolen and prints your current hp .
			player.current_hp += round(player.weapon.total_lifesteal())
			print("You steal {} hitpoints from the {}".format(round(player.weapon.total_lifesteal()), player.enemy.name))
	# Deals damage to the enemy and prints how much damage the enemy has taken.
	player.enemy.current_hp -= player.weapon.total_melee_damage()
	print("You have dealt {} damage to the {}".format(player.weapon.total_melee_damage(), player.enemy.name))
	continue_function()

# Allows the enemy to attack and deal damage to you, accounts for your total defence then displays the damage you took and how much health you currently have.
def enemy_attack():
	print("It's the {}'s turn".format(player.enemy.name))
	player.current_hp -= (round(player.enemy.damage *(1 - (player.armor.total_defence()) / 100)))
	print("The {} has hit you for {}".format(player.enemy.name, (round(player.enemy.damage *(1 - (player.armor.total_defence() / 100))))))
	continue_function()



# CAN USE EVAL FUNCTION TO MAKE THE SELECTION PROCESS EASIER
# WILL DEFINITLY NEED EDITING AFTER BETA TO ACCOUNT FOR IF MONSTER IS IN CURRENT_ROOM.
def enemy_select(fight_overide):
	if fight_overide == True:
		player.enemy = player.current_room.enemies_in_room
		fight_choice = "yes"

	else:

		while True:
			stats()
			# prints list of enemies and allows user input to choose enemy wanted to fight
			print("would you like to fight a {}".format(player.current_room.enemies_in_room.name))
			fight_choice = input("Type yes or no: ").lower().strip()
			system_checker()
			# Checks if the enemy chosen is in list_of_enemies and then sets it to your current enemy
			if fight_choice == "yes":
				player.enemy = player.current_room.enemies_in_room
				system_checker()
				stats()
				print("You have chosen to fight a {}".format(player.enemy.name))
				continue_function()
				break
				
			elif fight_choice == "no":
				system_checker()
				stats()
				print("You have chosen not to fight a {}".format(player.current_room.enemies_in_room.name))
				continue_function()
				break
			#Loop wont be broken if invalid choice an prints it to the user
			else:
				system_checker()
				stats()
				print("Invalid selection, Please type yes or no")
				continue_function()
	return fight_choice




# fight_overide and one_time_fight are either True or False
# fight_overide is used to force a player into a fight when they enter a specific room and they cant run
# one_time_fight removes the enemy from the room after the fight essentially killing them forever after the fight
def fight(fight_overide = False, one_time_fight = False):
	# Allows player to choose to fight or not.
	if enemy_select(fight_overide) == "yes":
		# For running away from a fight.
		run = False
		# ecides whose turn it currently is.
		player_turn = False
		enemy_turn = False
		# Used to keep track of defence xp each fight.
		hp_lost = 0
		# Decides who goes first both are equally likely.
		turn_count = random.randint(1,2)
		if turn_count == 1:
			player_turn = True
		else:
			enemy_turn = True
		# Defines the actual loop where the fight and post fight rewards take place.
		while not run:
			# Kills the player if their hp falls to 0 and ends fight.
			if player.current_hp <= 0:
				die()
				break
			# If monsters hp falls to 0 rewards the player with gold and xp. Checks for level_up(). Ends fight.
			elif player.enemy.current_hp <= 0:
				system_checker()
				stats()
				print("congratulations you have defeated a {}".format(player.enemy.name))
				if player.enemy.quest_drop == "None":
					pass
				else:
					# 1/3 chance of getting quest item from killing a monster
					quest_drop_chance = random.randint(1,3)
					if quest_drop_chance == 2:
						print("You have found a {}".format(player.enemy.quest_drop))
						player.inventory["miscellaneous"].append(player.enemy.quest_drop)
						player.enemy.quest_drop = "None"
					else:
						pass
				print("You have found {} gold".format(player.enemy.gold_drop))
				player.gold += player.enemy.gold_drop
				give_xp()
				player.defence_xp += hp_lost
				print("You have gained {} defence xp".format(hp_lost))
				level_up()
				continue_function()
				break
			# IF both the player and momnster have hp the fight plays on.
			else:
				# Defines the actual loop where the fight mechanics take place.
				while player.current_hp > 0 and player.enemy.current_hp > 0 and run == False:
					system_checker()
					stats()
					print(" ")
					enemy_stats()
					# Allows the player to make a move on their turn
					if player_turn:
						print("It's {}'s turn to move".format(player.name))
						result = input("Would you like to attack or run?: ").lower().strip()
						system_checker()
						stats()
						print(" ")
						enemy_stats()
						# Allows for a melee attack.
						if result == "attack" and player.attack_style == "melee":
							melee_attack()
							player_turn = False
							enemy_turn = True
							pass
						# Allows for a ranged attack.
						elif result == "attack" and player.attack_style == "ranged":
							player_turn = False
							enemy_turn = True
							pass
						# Allows the player to use a magic attack / spell.
						elif result == "attack" and player.attack_style == "magic":
							player_turn = False
							enemy_turn = True
							pass
						# Allows the player to choose to run with 1/3 chance of sucseeding.
						elif result == "run":
							if not fight_overide:
								run_chance = random.randint(1,3)
								if run_chance == 2:
									run = True
									system_checker()
									stats()
									print("You have escaped")
									continue_function()
									break
								# If player fails to run Makes it enemies turn.
								else:
									system_checker()
									stats()
									print("You failed to escape")
									player_turn = False
									enemy_turn = True
									continue_function()
							else:
								system_checker()
								stats()
								print("You can not run from your destiny!")
								continue_function()

						# TEST
						# Allows the player to use items
						elif len(result) > 0 and result.split()[0] == "use":
							system_checker()
							stats()

							if player.item1 == reverse_underscore_swapper(result)[5:]:
								item.use_item(reverse_underscore_swapper(result)[5:])
								print("You Have Used" + result[5:])
								player_turn = False
								enemy_turn = True
								continue_function()

							elif player.item2 == reverse_underscore_swapper(result)[5:]:
								item.use_item(reverse_underscore_swapper(result)[5:])
								print("You Have Used" + result[5:])
								player_turn = False
								enemy_turn = True
								continue_function()

							elif player.item3 == reverse_underscore_swapper(result)[5:]:
								item.use_item(reverse_underscore_swapper(result)[5:])
								print("You Have Used" + result[5:])
								player_turn = False
								enemy_turn = True
								continue_function()

							else:
								print("You Don't Have A {} To Use".format((result)[5:]))
								continue_function()


						else:
							pass
					# Allows the enemy to attack when it is their turn.
					else:
						enemy_attack()
						enemy_turn = False
						player_turn = True
						hp_lost += player.enemy.damage
		
		# Resets enemies hp and mana to max so they can be fought again later.
		# Also makes the players current enemy none so they can select again later.
		if not one_time_fight:
			player.enemy.current_hp = player.enemy.max_hp
			player.enemy.current_mana = player.enemy.max_mana
		else:
			player.current_room.enemies_in_room = "None"

		player.enemy = "None"

	else:
		pass	


# THIS FUNCTION IS VERY OUTDATED BUT I DONT WANT TO RE WRITE ALL THE JOE FIGHT
# CHANGE THIS TO INSTANCE_FIGHT AND ACCOUNT FOR ALL POSSIBLE INSTANCED FIGHTS
def fight_joe():
	system_checker()
	stats()
	player.enemy = crazy_joe
	print("crazy joe says: Hello there, I'm gunna eat yar insides wauhahah")
	continue_function()
	print("This game undegoes a turnbased fight system in which each turn you make a choice")
	print("Weather you or your enemy goes first is up to the toss of the coin")
	print("You can choose to try and attack with melee or ranged, use a spell, sip a potion or run")
	print("Attacking with melee or ranged just depends what weapon you have currently equiped and to attack just type attack")
	print("If you want to cast a spell you can just type spell and select from a list of your known spells")
	print("To sip a potion you just have to type potion and finally to run you just type run")
	print("But there is no runnin from crazy joe... He will find ya if you do")
	continue_function()
	# ecides whose turn it currently is.
	player_turn = False
	enemy_turn = False
	# Used to keep track of defence xp each fight.
	hp_lost = 0
	# Decides who goes first both are equally likely.
	turn_count = random.randint(1,2)
	if turn_count == 1:
		player_turn = True
	else:
		enemy_turn = True
	# Defines the actual loop where the fight and post fight rewards take place.
	while True:
		# Kills the player if their hp falls to 0 and ends fight.
		if player.current_hp <= 0:
			die()
			break
		# If monsters hp falls to 0 rewards the player with gold and xp. Checks for level_up(). Ends fight.
		elif player.enemy.current_hp <= 0:
			system_checker()
			stats()
			print("congratulations you have defeated a {}".format(player.enemy.name))
			print("You have found {} gold".format(player.enemy.gold_drop))
			player.gold += player.enemy.gold_drop
			give_xp()
			player.defence_xp += hp_lost
			print("You have gained {} defence xp".format(hp_lost))
			level_up()
			continue_function()
			break
		# IF both the player and momnster have hp the fight plays on.
		else:
			# Defines the actual loop where the fight mechanics take place.
			while player.current_hp > 0 and player.enemy.current_hp > 0:
				stats()
				print(" ")
				enemy_stats()
			# Allows the player to make a move on their turn
				if player_turn:
					print("It's {}'s turn to move".format(player.name))
					result = input("Would you like to attack or run?: ").lower().strip()
					system_checker()
					stats()
					print(" ")
					enemy_stats()
					# Allows for a melee attack.
					if result == "attack" and player.attack_style == "melee":
						melee_attack()
						player_turn = False
						enemy_turn = True
						pass
					# YOU CANT RUN FROM CRAZY JOE
					elif result == "run":
						system_checker()
						stats()
						print(" ")
						enemy_stats()
						print("You try to run but crazy joe finds you")
						print("crazy joe says: ya can't run from me")
						continue_function()
						pass
					else:
						system_checker()
						pass
				# Allows the enemy to attack when it is their turn.
				else:
					enemy_attack()
					enemy_turn = False
					player_turn = True
					hp_lost += player.enemy.damage
	
	while True:
		system_checker()
		stats()
		print("As crazy joe falls to the ground bleeding out he signals for you to come close")
		print("crazy joe: come close there is something you need to know")
		player_response = input("Would you like to move closer?: ").lower()
		if player_response == "yes":
			system_checker()
			stats()
			print("You get close to listen to what joe has to say")
			continue_function()
			stats()
			print("He tries to bite off a piece of your ear")
			print("Crazy joe finally closes his eyes and dies")
			# ACHIEVEMENT UNLUCKED: VANGOGH
			continue_function()
			break
		elif player_response == "no":
			system_checker()
			stats()
			print("You hesitate knowing all too well why they call him crazy joe")
			print("You feel lucky to still have all of your appendages")
			# ACHIEVEMENT UNLOCKED: ALL APPENDAGES 
			continue_function()
			break
		else:
			pass

	player.enemy = "None"
	corridor.left_room = "rat_pits"
	corridor.right_room = "armor_smith"
	player.dungeon_map = True
	stats()
	print("It looks like that old cook crazy joe had a map of this place")
	print("To check your map at any time just type map and hit enter")
	continue_function()

# NEED TO FIX NPC.room DOESN"T WORK.
# Write when I get back
# Gives a list of things the player can do 
def help_function():
	system_checker()
	print("To use any commands type them out and hit enter.")
	print("Include spaces if there are any")
	print("Nothing will be required to be typed in caps")
	print("--------------------------------------------")	
	print("- move : Allows you to move rooms")
	print("- invent : opens up your inventory")
	print("- equip 'item' : Allows you to equip an 'item' so long as you have it" )
	print("- use 'item' : Allows you to use an equipped 'item'")
	print("- check 'object' : Allows you to check an 'object' in a room to see if there are any hidden treasures")
	print("- craft : opens up a list of items you can craft and their components")
	print("- examine 'object' : Describes the object")

	if player.dungeon_map:
		print("- map : Allows you to see the map")
	if player.current_room == cell_6:
		print("- rest: restores all of your health and mana")
	if (player.current_room).shop_in_room != "None":
		print("- trade : Allows you to trade with an NPC Vendor ")
	if (player.current_room).npcs_in_room != "None":
		print("- talk : Allows you to talk with an NPC")
	if player.current_room == "forge":
		print("- reforge : Allows you to upgrade your gear in the forge")

# ADD ON STUFF FOR AFTER FULL WORKING GAME
# ----------------------------------------

# Generates a random enemy for the player to fight
def random_enemy():
	global list_of_all_enemies
	random_enemy_list = []
	for enemy in list_of_all_enemies:
		if player.total_lvl >= (eval(enemy)).lvl:
			random_enemy_list.append(enemy)
		else:
			pass
	selected_enemy = random.randint(0,abs(len(random_enemy_list) - 1))
	player.current_room.enemies_in_room = eval(random_enemy_list[selected_enemy])

# Use mined ores / gems to reforge gear
# KEEP GETTING EOF AND IF YOU TYPE SOMETHING THAT ACTUALLY SHOULD WORK NOTHING HAPPENS
def reforge():
	while True:
		system_checker()
		stats()
		print("What would you like to reforge?")
		player_reforge_choice = reverse_underscore_swapper(input(": ").strip().lower())
		if player_reforge_choice in player.inventory["weapons"]:  	
			if eval(player_reforge_choice).reforge_number < 5:
				eval(player_reforge_choice).damage =  round((eval(player_reforge_choice).damage * (random.randint(12,15) / 10)), 1)
				eval(player_reforge_choice).reforge_number += 1
				print("You have upgraded your {}. It now deals {} damage".format(player_reforge_choice, eval(player_reforge_choice).damage))
				continue_function()
				break
			else:
				print("{} Has been upgraded to its maximum".format(player_reforge_choice))
				continue_function()
				break

		elif player_reforge_choice in player.inventory["armors"]: 	
			if eval(player_reforge_choice).reforge_number < 5:
				eval(player_reforge_choice).defence = round((eval(player_reforge_choice).defence * (random.randint(12,15) / 10)), 1)
				eval(player_reforge_choice).reforge_number += 1
				print("You have upgraded your {}. It now has {} Defence".format(player_reforge_choice, eval(player_reforge_choice).defence))
				continue_function()
				break
			else:
				print("{} Has been upgraded to its maximum".format(player_reforge_choice))
				continue_function()
				break

		else:
			print("You do not have an item {}, or it is not reforgable.".format(player_reforge_choice))
			continue_function()
			break

# Used to mine ores in certain rooms. Make it a litle minigame type thing.
def mine():
	system_checker()
	stats()
	list_of_ores = ["Bronze ore", "Steel ore", "Titanium ore"]
	ore_multiplier = 1
	
	mine_chance = random.randint(1,3)
	# Have to fight an enemy
	if mine_chance == 2:
		print("You have been attacked")
		continue_function()
		random_enemy()
		fight(True, False)
	# gives player a random spread of resources
	else:
		ore_select = random.randint(1,10)
		amount_of_ore = random.randint(1,10)

		if ore_select <= 5:
			chosen_ore = list_of_ores[0]
		elif 6 <= ore_select <= 8:
			chosen_ore = list_of_ores[1]
		else:
			chosen_ore = list_of_ores[2]

		if amount_of_ore <= 5:
			ore_multiplier = 1
		elif 6 <= amount_of_ore <= 9:
			ore_multiplier = 2
		else:
			ore_multiplier = 3

		print("You have found {} {}".format(ore_multiplier, chosen_ore))
		while ore_multiplier > 0:
			(player.inventory["resources"]).append(chosen_ore)
			ore_multiplier -= 1
		
		continue_function()


# used to craft items and potions.
def craft():
	pass


def examine(player_item_examine):
	system_checker()
	stats()
	if reverse_underscore_swapper((player_item_examine).lower()) in player.current_room.items_in_room:
		print(underscore_swapper(player.current_room.items_in_room[reverse_underscore_swapper(player_item_examine)][0]))

	elif reverse_underscore_swapper((player_item_examine).lower()) == "room":
		print("This room contains")
		print("------------------")
		for room_items in player.current_room.items_in_room:
			print("-" + " " + "{}".format(underscore_swapper(room_items)))
	else:
		print("There is no {} in this room".format(player_item_examine))
		print("To see a list of the objects in this room")
		print("Type: examine room ")


def check(player_item_check):
	system_checker()
	stats()
	any_hidden_items = []
	if (player_item_check).lower() in player.current_room.items_in_room:
		for hidden_items in player.current_room.items_in_room[player_item_check][1:]:
			if hidden_items != "None":
				any_hidden_items.append(hidden_items)
				(player.inventory["miscellaneous"]).append(hidden_items)
				(player.current_room.items_in_room[player_item_check]).remove(hidden_items)
				print("You have found A {}".format(hidden_items))
				continue_function()
			else:
				pass
		
		if len(any_hidden_items) == 0:
			print("There are no hidden items here")
			continue_function()
		else:
			pass

	else:
		print("There is no {} in this room".format(player_item_check))
		continue_function()



# 						PLAYABLE GAME CODE
#---------------------------------------------------------------------

system_checker()

# Prints the title of the game

print('Not Very Good Game')
print('------------------')

continue_function()

# Defines the main loop of the game

def main():
	print("Type (Load) To Continue")
	print("Type (New) For A New Game ")
	print("Type (Exit) To Exit The Game")
	choice = input("").lower().strip()
	# Allows the player to load a saved game.
	if choice == "load":
		system_checker()
		load_game()
	# Allows the player to start a new game.
	# ADD A BUTTON THAT ASKS THEM IF THEY ARE SURE AND INFORMS THEM IT WILL ERASE ANY OTHER SAVED DATA.
	elif choice == "new":
		system_checker()
		new_game()
	# Allows the player to exit the game.
	elif choice == "exit":
		sys.exit()
	# If they choose an invalid option it returns them to the options.	
	else:
		system_checker()
		main()


# Starts a new game when called.

def new_game():

	# States the Rules of the game and gives slight beginning tips.
	print("Rules of the game")
	print("To execute any command simply just type it and hit enter")
	print("To see a full list of commands type help")
	print("The game map is essentially a grid")
	print("To move, type: move")
	print("Some actions may only work in specific rooms however")
	print("For example you can rest by typing: rest")
	print("But this only works if you are in cell 6")
	print("Nothing is case sensitive so don't worry at all about caps")
	print("If there is a space Like in health potion make sure to type the space")
	print("I really hope you enjoy my first ever game envygg")

	continue_function()

	# Sets the players starting weapon and armor to fists and rags respectively.
	player.current_room = cell_6
	player.weapon = fists
	player.armor = rags

	# First official text that the player reads in game.

	print("You Awake in a dark stone cell with no memeory of how you got there")
	print("All you have are the rags you are wearing and your fists")
	print("The only things in your room are a bed, a bucket in the corner and the door out")
	print("What will you do?")
	continue_function()

	

	# TESTING CODE ZONE
	#--------------------------------------------------------------------------
	"""
	player.inventory["miscellaneous"] = ["rats_tail", "trolls_tooth", "goblin_skull", "ball_of_slime", "giants_hammer"]
	player.current_room = alchemist
	player.gold = 30000
	player.melee_lvl = 25
	player.defence_lvl = 25
	player.magic_lvl = 20
	player.hp_lvl = 15
	player.weapon = ultimate_sword
	player.armor = god_plate
	"""
	#--------------------------------------------------------------------------


	kiffy_talk1 = False
	robber_choice = False
	billy_sad = False
	start_sequence = False

	global guard_post_quest_completed
	global quest_started_unlocking_the_forge
	global guard_post_quest_started
	global quest_unlocking_the_forge_pt2
	global quest_completed_unlocking_the_forge
	global quest_started_a_colossal_task
	

	while True:
		global colosseum_name
		global rat_pits_name
		global armory_name
		global giants_keep_name
		global cell_1_name
		global guard_post_name
		global marble_hall_name
		global forge_name
		global cell_4_name
		global alchemist_name
		global rat_pits_name
		global armor_smith_name
		global troll_hut_name
		global cell_5_name
		global cell_7_name
		global goblin_cave_name
		global weapon_smith_name
		global slime_den_name
		global cell_10_name
		global mines_name


		player.total_lvl = math.floor((player.melee_lvl / 3) + (player.ranged_lvl / 3) + (player.magic_lvl / 3) + (player.hp_lvl / 3))


		die()
		stats()

		player_action = input("What would you like to do?: ").lower().strip()
		system_checker()
		

		if player_action == "move":
			move_rooms()

			if player.current_room == corridor and kiffy_talk1 == False:
				system_checker()
				stats()
				print("As you leave your cell you see a woman in pure ebony armor weilding an onyx scythe stained with blood. She has one white wing and strawberry hair.")
				print("Your whole body termbles as you can hear your heart beating out of your chest.")
				print("It appears death has come for you")
				print("She apporaches you, as she speaks her voice instantly calms you")
				continue_function()
				kiffy.talk("corridor_dialogue")
				kiffy_talk1 = True
				continue_function()
				stats()
				print("Before you can make out any words she is gone")
				corridor.npcs_in_room = "None"
				continue_function()

			elif player.current_room == cell_3 and crazy_joe.current_hp > 0:
				fight_joe()
				
			else:
				pass

		elif player_action == "rest":
			if player.current_room == cell_6:
				player.current_hp = player.max_hp
				player.current_mana = player.max_mana
				system_checker()
				stats()
				print("You feel well rested, Your hitpoints and mana have been restored.")
				continue_function()
			else:
				system_checker()
				stats()
				print("There is nowhere to rest here")
				continue_function()
		# Checks map if player chooses
		elif player_action == "map":
			system_checker()
			stats()
			prison_map_check()


		elif player_action == "fight" and player.current_room.room_fight:
			fight(False, False)

		elif player_action == "fight":
			system_checker()
			stats()
			print("There is nothing to fight here")
			continue_function()

		elif player_action == "trade":
			if player.current_room == weapon_smith:	
				NPC.trade(billy)

			elif player.current_room == armor_smith:
				NPC.trade(mell)

			elif player.current_room == alchemist:
				NPC.trade(clara)
			else:
				system_checker()
				stats()
				print("There is nobody to trade here.")
				continue_function()

		elif len(player_action) > 0 and player_action.split()[0] == "equip":
			system_checker()
			stats()
			player.equip(reverse_underscore_swapper(player_action)[6:])
			continue_function()

		elif len(player_action) > 0 and player_action.split()[0] == "use":
			system_checker()
			stats()
			Items.use_item(reverse_underscore_swapper(player_action)[4:])
			continue_function()


		elif player_action == "help":
			help_function()
			continue_function()

		elif len(player_action) > 0 and player_action.split()[0] == "check":
			system_checker()
			stats()
			check(reverse_underscore_swapper(player_action)[6:])

		elif len(player_action) > 0 and player_action.split()[0] == "examine":
			examine(player_action[8:])
			continue_function()

		elif player_action == "invent":
			system_checker()
			stats()
			player.inventory_check()

		elif player_action == "talk":
			system_checker()
			stats()
			if player.current_room.npcs_in_room != "None":
				if ((eval(player.current_room.npcs_in_room)).dialogue)["general_dialogue"] == "None":
					system_checker()
					pass
				else:
					(eval(player.current_room.npcs_in_room)).talk("general_dialogue")
					continue_function()

			else:
				print("There is nobody here to talk to")
				continue_function()

		elif player_action == "reforge":
			if quest_completed_unlocking_the_forge:
				if player.current_room == forge:
					if "key_mould" in player.inventory["miscellaneous"] and "Bronze ore" in player.inventory["resources"]:
						system_checker()
						stats()
						player.inventory["resources"].remove("Bronze ore")
						player.inventory["miscellaneous"].remove("key_mould")
						player.inventory["miscellaneous"].append("guard_chest_key")
						print("You have made a guard chest key")
						continue_function()

					else:
						reforge()
				
				else:
					print("You need to be in the forge to reforge gear")
			else:
				pass



		elif player_action == "teleport":
			print("Where would you like to teleport to?")
			player_teleport = input(": ").lower().strip()
			player.current_room = eval(player_teleport)



		# MAKES THE MAP SHOW ROOM NAMES AFTER YOUR FIRST TIME IN ROOM
# -------------------------------------------------------------------
		
		

		if player.current_room == colosseum:
			if colosseum_name == "???":
				print("You Enter a grand colosseum")
				print("It's empty too empty")
				print("You hear a loud horn")
				print("The gates circling the colosseum open")
				print("You see hordes of trolls racing out")
				print("You rush in cutting down troll after troll")
				print("They seem endless in numbers")
				print("A blazing fire surrounds the colosseum")
				print("The flames engulf everything turning all of the trolls to ashes")
				if "fire_emblem" in player.inventory["miscellaneous"]:
					# PLAYER ACHIEVEMENT: UNDERCOOKED
					print("your fire emblem protects you from the flames")
				else:
					# PLAYER ACHIEVEMENT: DO YOU SMELL BURNT TOAST?
					print("The flames burn into your armor damaging you greatly")
					player.current_hp -= 0.75 * player.max_hp
				continue_function()
				print("Decening down the stairs, A black suit of armor with glowing green eyes")
				print("The Overseer stands between you and freedom")
				print("You prepare yourself for your final fight")
				continue_function()
				fight(True, True)
				# WRITE AN END SCNE FOR WHEN YOU KILL OVERSEER AFTER THIS
				print("congrats you beat he game")
				continue_function()
			colosseum_name = "colosseum"
		
		elif player.current_room == cell_6:
			if start_sequence == False and (player_action == "examine cell door" or player_action == "check cell door"):
				name_chosen = False
				while not name_chosen:
					system_checker()
					stats()
					print("A young man runs by the door.")
					print("He notices you and walks back to your cell")
					print("young man: Looks like they caught another, If you want to survive here you better be willing to fight.")
					print("The names marco by the way, whats your name?")
					player_decision = input(": ")
					if str(player_decision) == player_decision:
						if 0 < len(player_decision) < 13:
							while True:
								system_checker()
								stats()
								print("Are you sure you want your name to be {}?".format(player_decision))
								player_confirm = input(": ").lower().strip()
								if player_confirm == "yes":
									player.name = player_decision
									name_chosen = True
									system_checker()
									break
								elif player_confirm == "no":
									break

								else:
									print("Please type yes or no")

						elif len(player_decision) >= 13:
							print("Player name must be less than 13 charactors in length")
							continue_function()
					else:
						print("Player name must not contain any special charactors. Stick to letters, numbers and spaces.")

				start_sequence = True
				system_checker()
				stats()
				print("marco: {} eh? Not what I would name my kid but hey, whatever works... Ha I'm just kidding".format(player_decision))
				print("Well for starters you're gunna need to make it out of that cell, 'check' around for a key to the cell door")
				print("After that you're probably gunna want some gear to keep yourself safe.")
				print("Theres lots of weapons and armors here. You can buy em from shops or if you're lucky get some of killing monsters")
				print("There are specific rooms monsters like to hang out in. If you are looking for a fight, they are where to go.")
				print("... I gotta get going. Maybe we will meet again, good luck {}".format(player_decision))
				continue_function()
				stats()
				print("marco runs off")
				cell_6.items_in_room["bed"][1] = "key"
				continue_function()
			
			if "key" in player.inventory["miscellaneous"]:
				cell_6.up_room = "corridor"
				cell_6.items_in_room["cell_door"][0] = "An unlocked cell door"



		elif player.current_room == rat_pits:
			if rat_pits_name == "???":
				system_checker()
				stats()
				print("A Giant Rat scurries at you")
				print("It attacks")
				continue_function()
				fight(True, False)
			rat_pits_name = "rat pits"

		elif player.current_room == armory:
			if armory_name == "???":
				print("You and marco open the armory door")
				print("Hulking in front of you is the Jail Warden")
				print("His plate mail red from the blood of inmates")
				print("He charges marco with his great spiked mace")
				print("He smashes marco into the wall")
				print("marco lays clinging to his life")
				print("The warden turns to you")
				Print("You look into his crazed eyes and see only a wild animal looking back at you")
				print("As his gaze locks in on you he thirsts for your blood")
				print("The warden charges you")
				continue_function()
				fight(True, True)
				armory.items_in_room = {"wardens_body": ["The lifeless body of a crazed animal who has lost all sense of humanity", "colosseum_key"], "weapon_racks": ["Rows of weapons, none of them to your taste however", "None"], "armor_chests": ["You already have all the guards armor you want", "None"], "guards_corpses": ["The guards killed by some angel of death", "None"]}
				system_checker()
				stats()
				print("The wardens colossal body falls to the ground")
				print("You have put the crazed animal to rest")
				print("You race over to marco whose barly alive")
				if "health_potion" in player.inventory["miscellaneous"]:
					print("You open your health potion and help Marco drink some. Marco opens his eyes slightly but he's still in rough shape.")
				elif player.armor != "rags":
					print("You use rip up your old rags to make bandages for Marco. He's not doing so well though")
				else:
					print("Marco is bleeding heavily and you can't help")
					print("You look around and after some time find rags and bandage him up as best you can. It's not good.")
				print("Elite guards pile in from the next room")
				print("They stutter for a moment as they see the wardens lifeless body")
				print("They quickly regain their composure and surround you")
				print("The end has come")
				print("You take your weapon in hand and stand up shakily, ready to fight")
				print("The elite guards charge you. You feel death is near.")
				print("In the time it takes to blink a shadow as black as night appears directly in front of you")
				print("In an instant you feel a swift gust of wind strong enough to make you kneel back")
				print("You open your eyes, look down and see an onyx scythe dripping blood")
				print("You look up and see long strawberry hair flowing with the wind")
				print("You look forward and see eighteen elite guards reduced to corpses")
				print("Blood staining every wall in the armory")
				print("The angle of death looks back at you")
				print("She says: I can't stay in this realm for long, Go now!")
				print("not missing a beat you pickup marco and sprint away")
				print("Eventually you help marco back to Clara")
				print("She bandages his wounds and heals him to the best of her abilities")
				print("You and marco head back to cell 7 to finalize the escape plans")
				print("You should talk to marco when you are ready")
				continue_function()
				marco.dialogue["general_dialogue"] = "I don't think I am going to be much help in combat anymore... \nWell there should only be one more task at hand before we can all leave this hell. \nThe colosseum. You need to enter it and kill all the mightiest who might defend the exits \nThis is no easy task, the overseer has rarely ever been seen \nOnly once have I seen him. It was in a fight \nOur most skilled warrior attempted to break us all free. \nUnfortunatly in a matter of seconds he was cut in three and dragged away. \nThis fight will be the greatest challange yet but if you can succed where all others have failed, then we will all be truley set free."
				continue_function()
				player.current_room = "cell_7"

			armory_name = "armory"

			if colosseum_key in player.inventory["miscellaneous"]:
				armory.left_room = "colosseum"


		elif player.current_room == giants_keep:
			if giants_keep_name == "???":
				system_checker()
				stats()
				print("There is a Giant blocking your way forward")
				print("It attacks")
				continue_function()
				fight(True, False)

			giants_keep_name = "giants keep"

		elif player.current_room == cell_1:
			cell_1_name = "cell 1"

		elif player.current_room == guard_post:
			guard_post_name = "guard post"
			if guard_post_quest_completed:
				if player_action == "talk":
					system_checker()
					stats()
					if player.total_lvl >= 20:
						marco.talk("colossal_task_start")
						quest_started_a_colossal_task = True
						guard_post.right_room = "marble_hall"
						continue_function()
					else:
						print("marco: You are not yet strong enough for this quest.\nCome back when you are at least level 20")
						continue_function()

				else:
					pass
			
			if "guard_chest_key" in player.inventory["miscellaneous"]:
				player.inventory["miscellaneous"].remove("guard_chest_key")
				guard_post.items_in_room["armor_chest"][0] = "An unlocked chest full of guards armor"
				guard_post.items_in_room["armor_chest"][1] = "guard_armor"
			
			if "guard_armor" in player.inventory["miscellaneous"]:
				player.inventory["miscellaneous"].remove("guard_armor")
				player.inventory["armors"].append("guard_armor")

		elif player.current_room == marble_hall:
			if marble_hall_name == "???":
				marble_hall.enemies_in_room = guard
				if player.armor.name == "guard_armor":
					# Player Achievement: 200 IQ
					system_checker()
					stats()
					print("You and marco cleverly sneak into the marble hall")
					print("There are seven guards")
					print("You two get the jump on the guards")
					print("You and marco are able to take out four of the guards before they bear arms")
					print("There are three guards left, Prepare to fight")
					continue_function()
					fight(True, False)
					fight(True, False)
					marble_hall.enemies_in_room = "None"
					system_checker()
					stats()
					print("You and marco make quick work of the guards")
					continue_function()
					stats()
					guard_post.npcs_in_room = "None"
					marco.room = "marble_hall"
					marble_hall.npcs_in_room = "marco"
					marco.talk("marco_lives")
					continue_function()
				else:
					system_checker()
					stats()
					print("You and marco storm the marble hall")
					print("There are seven guards")
					print("Three guards surround you")
					print("Prepare to fight")
					continue_function()
					stats()
					player.current_room.enemies_in_room = guard
					fight(True, False)
					fight(True, False)
					fight(True, False)
					print("As The third guard falls you run to help marco")
					print("He finishes killing the first two guards")
					print("But there are just too many guards")
					print("One guard manages to stab marco in the chest")
					print("He falls to the ground")
					print("You run over to defend him, Its all up to you now")
					continue_function()
					stats()
					fight(True, False)
					fight(True, False)
					marble_hall.enemies_in_room = "None"
					system_checker()
					stats()
					print("As the last guard falls you are finally done fighting")
					print("Marco is in rough shape but he will be okay")
					print("He drinks a healing potion and starts to feel better")
					guard_post.npcs_in_room = "None"
					marco.room = "marble_hall"
					marble_hall.npcs_in_room = "marco"
					marco.talk("marco_lives")
					continue_function()
			marble_hall_name = "marble hall"

			if "armory_key" in player.inventory["miscellaneous"]:
				player.inventory["miscellaneous"].remove("armory_key")
				marble_hall.up_room = "armory"


		elif player.current_room == forge:
			forge_name = "forge"
			if guard_post_quest_completed and quest_started_unlocking_the_forge and not quest_unlocking_the_forge_pt2:
				forge.npcs_in_room = "drunkard"
				drunkard.room = "forge"
				drunkard.dialogue["general_dialogue"] = "None" 
				if player_action == "talk" and not quest_unlocking_the_forge_pt2:
					while True:
						system_checker()
						drunkard.talk("unlocking_the_forge_pt2")
						player_choice = input(": ").strip().lower()
						if player_choice == "yes":
							drunkard.talk("unlocking_the_forge_pt2.yes")
							continue_function()
							quest_unlocking_the_forge_pt2 = True
							rat.quest_drop = "rats_tail"
							troll.quest_drop = "trolls_tooth"
							goblin.quest_drop = "goblin_skull"
							slime.quest_drop = "ball_of_slime"
							giant.quest_drop = "giants_hammer"
							drunkard.dialogue["general_dialogue"] = "None"
							break
						elif player_choice == "no":
							drunkard.talk("unlocking_the_forge_pt2.no")
							continue_function()
							break
						else:
							pass
			
			elif quest_unlocking_the_forge_pt2:
				if player_action == "talk":
					for player_item in player.inventory["miscellaneous"]:
						if player_item in drunkard.quest_items:
							system_checker()
							stats()
							(player.inventory["miscellaneous"]).remove(player_item)
							drunkard.quest_items.remove(player_item)
							print("You have handed over a {}".format(underscore_swapper(player_item)))
						else:
							pass
						continue_function()


					if len(drunkard.quest_items) > 0:
						system_checker()
						stats()
						print("Drunkard: You still need")
						for quest_item in drunkard.quest_items:
							print("-" + underscore_swapper(quest_item))
						
					# COMPLETE QUEST UNLOCKING THE  FORGE
					# PLAYER ACHIEVEMENT: SOMETHING FUNNY
					else:
						quest_completed_unlocking_the_forge = True
						drunkard.dialogue["general_dialogue"] = "You did it kid, the forge is active for use\nWhen you want to upgrade your gear come back here\nI will reforge it to be stronger than before"
						drunkard.talk("general_dialogue")
						drunkard.dialogue["general_dialogue"] = "None"
					continue_function()
			else:
				pass

			
		elif player.current_room == cell_4:
			cell_4_name = "cell 4"
			guard_post_raid = False
			if guard_post_quest_started and not guard_post_raid and player_action == "talk" and not guard_post_quest_completed:
				while True:
					marco.talk("guard_post_quest_ready")
					player_choice = input(": ").lower().strip()
					if player_choice == "yes":
						marco.talk("guard_post_quest_ready.yes")
						continue_function()
						guard_post_raid = True
						cell_4.up_room = "guard_post"
						player.current_room = guard_post
						stats()
						print("You both move to the guard post")
						continue_function()
						stats()
						print("Guard: What are you doing here inmates? \nGet back to your cells")
						print("The guards attacks")
						continue_function()
						fight(True, False)
						guard_post.enemies_in_room = "None"
						# GIVE PLAYER ACHIEVEMENT: ANARCHY!
						guard_post_quest_completed = True
						cell_4.npcs_in_room = "None"
						marco.room = "guard_post"
						guard_post.npcs_in_room = "marco"
						marco.dialogue["general_dialogue"] = "None"
						break
					elif player_choice == "no":
						marco.talk("guard_post_quest_ready.no")
						continue_function()
						break
					else:
						pass
			else:
				pass

		elif player.current_room == alchemist:
			alchemist_name = "alchemist"

		elif player.current_room == armor_smith:
			if armor_smith_name == "???":
				mell.talk("mell_dialogue1")
				continue_function()
				player.gold += 300

			armor_smith_name = "armor smith"

		elif player.current_room == troll_hut:
			if troll_hut_name == "???":
				system_checker()
				stats()
				print("There is a troll blocking your way forward")
				print("It attacks")
				continue_function()
				fight(True, False)

			troll_hut_name = "troll hut"

		elif player.current_room == cell_5:
			global robbery_quest_complete
			global robbery
			if cell_5_name == "???" or (player_action == "talk" and not robbery_quest_complete) and (player_action == "talk" and not robbery):
				valid_response = False
				while not valid_response:
					hooded_figure.talk("robbery1")
					player_response1 = input(": ").lower()
					system_checker()
					stats()
					if player_response1 == "yes":
						while True:
							hooded_figure.talk("robbery2.y")
							player_response2 = input(":").lower()
							if player_response2 == "yes":
								hooded_figure.talk("robbery3.y")
								valid_response = True
								robbery = True
								continue_function()
								break


							elif player_response2 == "no":
								hooded_figure.talk("robbery3.n")
								continue_function()
								cell_5.enemies_in_room = hooded_figure_monster
								fight(True, True)
								valid_response = True
								player.current_room.npcs_in_room = "None"
								robbery_quest_complete = True
								# GIVE ACHIEVEMENT: GOOD BOY
								break



							else:
								pass
							
					elif player_response1 == "no":
						hooded_figure.talk("robbery2.n")
						continue_function()
						valid_response = True
						break

					else:
						pass

			cell_5_name = "cell 5"

		elif player.current_room == cell_7:
			cell_7_name = "cell 7"
			if player.total_lvl > 14 and not quest_started_unlocking_the_forge:
				drunkard.dialogue["general_dialogue"] = "None"
				if player_action == "talk":
					drunkard.talk("unlocking_the_forge_pt1")
					drunkard.name = "Thorag"
					giants_keep.down_room = "forge"
					continue_function()
					quest_started_unlocking_the_forge = True
					drunkard.dialogue["general_dialogue"] = "Get rid of the guards and meet me in the forge"

				else:
					pass
		

		elif player.current_room == goblin_cave:
			if goblin_cave_name == "???":
				gold_storage = player.gold
				system_checker()
				stats()
				print("A goblin stole all your gold")
				# GIVE PLAYER ACHIEVEMENT: I DECLARE BNACKRUPCY
				player.gold = 0
				continue_function()
				fight(True, False)
				system_checker()
				player.gold += gold_storage
				stats()
				print("You got your gold back")
				continue_function()

			goblin_cave_name = "goblin cave"
		# CHANGE BILLY DIALOGUE
		elif player.current_room == weapon_smith:
			
			if weapon_smith_name == "???" and not robbery:
				billy.talk("billy_dialogue1")
				continue_function()
				weapon_smith_name = "weapon smith"

			if robbery_quest_complete and robbery:
				# GIVE PLAYER ACHIEVEMENT: OH BROTHER...
				billy.talk("billy_dialogue2")
				robbery = False
				billy.dialogue["general_dialogue"] = "I miss him..."
				continue_function()
			

			elif not robbery_quest_complete and robbery:
				system_checker()
				stats()
				print("Mercenary: HEY! You can't be here shops closed")
				weapon_smith.enemies_in_room = mercenary
				continue_function()
				fight(True, True)
				player.current_room = cell_5
				player.inventory["weapons"].append("shortsword")
				(billy.stock).remove("shortsword")
				system_checker()
				stats()
				print("You have escaped to cell 5 without being noticed")
				print("You made it back to cell 5 with a shortsword")
				continue_function()
				robbery_quest_complete = True
			else:
				pass

			weapon_smith_name = "weapon smith"


		elif player.current_room == slime_den:
			if slime_den_name == "???":
				system_checker()
				stats()
				print("There is a slime blocking your way forward")
				print("It attacks")
				continue_function()
				fight(True, False)

			slime_den_name = "slime den"

		elif player.current_room == cell_10:
			if player_action == "talk" and not guard_post_quest_started:
				if player.total_lvl < 10:
					marco.talk("guard_post_quest_not_strong_enough")
					continue_function()
				else:
					while True:
						system_checker()
						stats()
						marco.talk("guard_post_quest")
						player_choice = input(": ").lower().strip()
						system_checker()
						stats()
						if player_choice == "yes":
							marco.talk("guard_post_quest.yes")
							guard_post_quest_started = True
							cell_10.npcs_in_room = "None"
							cell_4.npcs_in_room = "marco"
							continue_function()
							break
						elif player_choice == "no":
							marco.talk("guard_post_quest.no")
							continue_function()
							break

						else:
							pass

			cell_10_name = "cell 10"

		elif player.current_room == mines:
			if mines_name == "???":
				system_checker()
				stats()
				miner_frank.talk("mine_intro_dialogue")
				continue_function()
			else:
				pass
			
			if player_action == "mine":
				mine()

			mines_name = "mines"

#----------------------------------------------------------------------------------



	continue_function()

main()




