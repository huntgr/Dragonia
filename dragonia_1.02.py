import random
import sys
import time

print "Welcome to Dragonia."
chosen = False
_exit = False
running = True
count = 0
no_enemy = True
enemies = ['ogre','giant snake','ogre','giant snake','ogre','giant snake','gargoyle','dragon']
error_messages = ["Robin...no.","You think I'm going to listen to you?","um...what?","Yeah no clue what you're telling me to do.","Stop touching me there.","Will you attack already?","Glares at you.","Siiiiigh.", "You want me to do WHAT?","Sorry I don't roll that way","I would if I could.","NO..NO NO NO NO..NONONONONONONON!"]






class warlock:
    def __init__(self,name):
        self.cls = 'warlock'
        self.name = name
        self.stamina = 14
        self.wisdom = 15
        self.intellect = 16
        self.dexterity = 9
        self.strength = 7
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.miss = 150/self.intellect
        self.crit = self.intellect
        self.dict = ['drains','depletes','consumes','leeches','hits','CRITS','misses']
        self.target = 'unknown'
        self.abilities = ['Power Siphon','Entropic Assault']
        self.xp = 0
        self.lvl = 1
    def _displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def _abilities(self):
        print "Power Siphon(1).  This ability does {0} to {1} damage".format((self.intellect+self.stamina*3/2),((self.intellect+self.stamina)*7/3))
        print "Heals you for a portion of damage dealt"
        print "Entropic Assault(2). This ability does {0} to {1} damage".format((self.intellect+self.wisdom+self.stamina)/2,(self.intellect+self.wisdom+self.stamina)*7/2)
        print "Consumes a portion of you current health. Even if you miss!"
    def _ability0(self):
        damage = random.randrange(((self.intellect+self.stamina)*3/2),((self.intellect+self.stamina)*7/3))
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            heal_control = round(((self.wisdom/2)+((self.stamina*11)/self.health))/3, 0)
            self.health += (self.damage/5)+heal_control
            print 'Your Power Siphon {0} for {1} damage.'.format(self.dict[5],self.damage)
            print 'and heals you for {0}.'.format((self.damage/5)+heal_control)
            #print '{0},{1}'.format(heal_control,self.health)
        else:
            self.damage = damage
            heal_control = round(((self.wisdom/2)+((self.stamina*11)/self.health))/3, 0)
            self.health += (damage/6)+heal_control
            print 'Your Power Siphon {0} for {1} damage.'.format(self.dict[random.randrange(0,4)],self.damage)
            print 'and heals you for {0}.'.format((damage/6)+heal_control)
            #print '{0},{1}'.format(heal_control,self.health)
    def _ability1(self):
        damage = random.randrange((self.intellect+self.wisdom+self.stamina)/2,(self.intellect+self.wisdom+self.stamina)*7/2)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        sac_hp = round(self.health * (0.17),0)
        if miss <= self.miss:
            self.damage = 0
            #sac_hp = self.health * (0.1)
            self.health -= sac_hp
            print "You MISS completely!"
            print "{0} health consumed.".format(sac_hp)
        elif crit <= self.crit:
            self.damage = damage*2
            #sac_hp = self.health * (0.1)
            self.health -= sac_hp
            print "Your Entropic Assault crits for {0} damage.".format(self.damage)
            print "{0} health consumed.".format(sac_hp)
        else:
            self.damage = damage
            #sac_hp = self.health * (0.1)
            self.health -= sac_hp
            print "Your Entropic Assault deals {0} damage.".format(self.damage)
            print "{0} health consumed.".format(sac_hp)
    def _health(self):
        print "You have {0} health remaining".format(self.health)
    def _level(self):
        self.stamina += 6
        self.wisdom += 3
        self.intellect += 4
        self.dexterity += 1
        self.strength += 1
        self.health = self.stamina*10
        self.miss = 100/self.intellect
        self.crit = self.intellect
        self.lvl += 1
        print "\nYou've reached level {0}".format(self.lvl)
    def _sword(self):
        self.intellect += 30
    def _offhand(self):
        self.stamina += 10
    def _belt(self):
        self.stamina += 2
    def _cloak(self):
        self.stamina += 20
    def _trinket(self):
        self.intellect += 45
    def _legendary_weapon(self):
        self.intellect += 100



class mage:
    def __init__(self,name):
        self.cls = 'mage'
        self.name = name
        self.stamina = 8
        self.wisdom = 19
        self.intellect = 20
        self.dexterity = 7
        self.strength = 6
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.miss = 150/self.intellect
        self.crit = self.intellect
        self.dict = ['burns','incinertes','scourches','glances','hits','CRITS','misses']
        self.target = 'unknown'
        self.abilities = ['Fireball']
        self.xp = 0
        self.lvl = 1
    def _displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def _abilities(self):
        print "Fireball(1).  This ability does {0} to {1} damage".format(self.intellect*2,self.intellect*7)
        print "Barrier(2). This ability creates a magical shield that absorbs {0} to {1} damage.".format(self.intellect+(self.wisdom/2),(self.intellect+(self.wisdom/2))*2)
    def _ability0(self):
        damage = random.randrange(self.intellect*2,self.intellect*7)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            print 'Your Fireball {0} for {1} damage.'.format(self.dict[5],self.damage)
        else:
            self.damage = damage
            print 'Your Fireball {0} for {1} damage.'.format(self.dict[random.randrange(0,4)],self.damage)
    def _ability1(self):
    	player.damage = 0
        shield = random.randrange(self.intellect+(self.wisdom/2),(self.intellect+(self.wisdom/2))*2)
        self.shield = shield
        print "You create a {0} point shield".format(shield)
        
    def _health(self):
        print "You have {0} health and {1} shield remaining".format(self.health, self.shield)
        
    def _level(self):
        self.stamina += 2
        self.wisdom += 4
        self.intellect += 9
        self.dexterity += 1
        self.strength += 1
        self.health = self.stamina*10
        self.miss = 100/self.intellect
        self.crit = self.intellect
        self.lvl += 1
        print "\nYou've reached level {0}".format(self.lvl)
    def _sword(self):
        self.intellect += 30
    def _offhand(self):
        self.stamina += 10
    def _belt(self):
        self.stamina += 2
    def _cloak(self):
        self.stamina += 20
    def _trinket(self):
        self.intellect += 45
    def _legendary_weapon(self):
        self.intellect += 100
               
class warrior:
    def __init__(self,name):
        self.cls = 'warrior'
        self.name = name
        self.stamina = 17
        self.wisdom = 7
        self.intellect = 4
        self.dexterity = 12
        self.strength = 21
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.miss = 100/self.strength
        self.crit = self.strength/1.5
        self.dict = ['SLICES','WOUNDS','HITS','GLANCES','DEMOLISHES','CRITS','MISSES']
        self.target = 'unknown'
        self.abilities = ['Heroic Slash']
        self.xp = 0
        self.lvl = 1
    def _displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def _abilities(self):
        print "Heroic Slash(1).  This ability does {0} to {1} damage".format(self.strength,self.strength*4)
    def _ability0(self):
        damage = random.randrange(self.strength*2,self.strength*4)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            print 'Your Heroic Slash {0} for {1} damage.'.format(self.dict[5],self.damage)
        else:
            self.damage = damage
            print 'Your Heroic Slash {0} for {1} damage.'.format(self.dict[random.randrange(0,5)],self.damage)
    
    #def _ability1(self):
    	
    
    def _health(self):
        print "You have {0} health remaining".format(self.health)
    def _level(self):
        self.stamina += 6
        self.wisdom += 1
        self.intellect += 1
        self.dexterity += 3
        self.strength += 7
        self.health = self.stamina*10
        self.miss = 100/self.strength
        self.crit = self.strength/1.5
        self.lvl += 1
        print "\nYou've reached level {0}".format(self.lvl)
    def _sword(self):
        self.strength += 30
    def _offhand(self):
        self.strength += 15
    def _belt(self):
        self.stamina += 2
    def _cloak(self):
        self.stamina += 20
    def _trinket(self):
        self.strength += 95
    def _legendary_weapon(self):
        self.strength += 200

class cleric:
    def __init__(self,name):
        self.cls = 'cleric'
        self.name = name
        self.stamina = 15
        self.wisdom = 10
        self.intellect = 10
        self.dexterity = 9
        self.strength = 18
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.empowered = 0
        self.miss = 100/(self.intellect + self.strength)
        self.crit = (self.wisdom + self.intellect)/1.5
        self.dict = ['cleanses','pierces','glances','devastates','hits','CRITS','misses']
        self.target = 'unknown'
        self.abilities = ['Holy Blow']
        self.xp = 0
        self.lvl = 1
    def _displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def _abilities(self):
        print "Holy Blow(1).  This ability does {0} to {1} damage.".format(self.strength+self.intellect,(self.strength + self.intellect)*3)
        print "Devine Judgment(2). This ability does {0} to {1} damage.".format(self.wisdom*2, self.wisdom*5)
        print "You enter a state of devine empowerment" 
        print "adding addition effects to your next attack."
        print "Holy Blow will deal additional damage and Devine Judgment will heal you."
        print "   "
    def _ability0(self):
        damage = random.randrange((self.strength + self.intellect)*2,(self.strength + self.intellect)*3)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if (self.empowered):
        	damage = round(damage*1.25,0)
        	self.empowered = 0
        if miss <= self.miss:
            self.damage = 0
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            print 'Your Holy Blow {0} for {1} damage.'.format(self.dict[5],self.damage)
        else:
            self.damage = damage
            print 'Your Holy Blow {0} for {1} damage.'.format(self.dict[random.randrange(0,5)],self.damage)
        
    def _ability1(self):
    	damage = random.randrange(self.wisdom*2, self.wisdom*5)
    	crit = random.randrange(1,100)
    	miss = random.randrange(1,100)
    	if (self.empowered):
    		self.health += round(damage*0.8, 0)
    		self.empowered = 0
    		print "You are healed for {0}".format(damage*0.8)
    	else:
    		self.empowered = 1
    		print "You feel empowered by a devine force!"
    	if miss <= self.miss:
    		self.damage = 0
    		print "You Missed!"
    	elif crit <= self.crit:
    		self.damage = damage * 2
    		print "Your Devine Judgment CRITS for {0} damage.".format(self.damage)
    	else:
    		self.damage = damage
    		print "Your Devine Judgment deals {0} damage.".format(self.damage)
    	
    def _health(self):
        print "You have {0} health remaining".format(self.health)
    def _level(self):
        self.stamina += 4
        self.wisdom += 3
        self.intellect += 3
        self.dexterity += 1
        self.strength += 5
        self.health = self.stamina*10
        self.miss = 100/(self.intellect + self.strength)
        self.crit = (self.wisdom + self.intellect)/1.5
        self.lvl += 1
        print "\nYou've reached level {0}".format(self.lvl)
    def _sword(self):
        self.intellect += 30
    def _offhand(self):
        self.strength += 15
    def _belt(self):
        self.stamina += 2
    def _cloak(self):
        self.stamina += 20
    def _trinket(self):
        self.strength += 45
        self.intellect += 45
    def _legendary_weapon(self):
        self.strength += 100
        self.intellect += 75

class ogre:
    def __init__(self):
        self.name = 'ogre'
        self.health = 300
        self.stamina = 30
        self.damage = 0
        self.miss = 20
        self.dict = ['SMASHES','HITS','CRUSHES','OBLITERATES','SCRAPES','BARELY HITS','CRITS','misses']
        self.target = 'unknown'
        self.xp = 75
    def _ability0(self):
        damage = random.randrange(17,30)
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "The ogre MISSES you completely!"
        elif crit ==10:
            crit = damage*2
            self.damage = crit
            print "The ogre CRITS you for {0} damage".format(self.damage)
        else:
            self.damage = damage
            print "The ogre {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def _health(self):
        print "The ogre has {0} health remaining".format(self.health)
    def _display(self):
        print "An ogre is sleeping in the next room.  He appears to be surrounded by bones from those who have attempted to kill him before."
        print '''
                      |\  ,,,,,  /|
                      | \/_   _\/ |
               /\     (_    "    _)
               \ \      (  ,--, )
               / /    ,,,\__-__/,,,
               \ \   ,,,,""""""",,,,  ,,,,
               /_/   |  |"""""""(  ) ,(  )
              [!!!]-'  / """"""" \  \ / /
               |!|----' """"""""" `,___/
                        ;;;;;;;;;
                        """""""""
                        """" """"
                        """   """
                       _"",   ,""_
                      (___)   (___)

                '''
        
class gargoyle:
    def __init__(self):
        self.name = 'gargoyle'
        self.health = 450
        self.stamina = 45
        self.damage = 0
        self.miss = 5
        self.dict = ['DECIMATES','HITS','CRUSHES','OBLITERATES','SCRAPES','BARELY HITS','CRITS','misses']
        self.target = 'unknown'
        self.xp = 150
    def _ability0(self):
        damage = random.randrange(30,45)
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "The Gargoyle MISSES you completely!"
        elif crit ==10:
            crit = damage*1.5
            self.damage = crit
            print "The Gargoyle CRITS you for {0} damage".format(self.damage)
        else:
            self.damage = damage
            print "The Gargoyle {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def _health(self):
        print "The Gargoyle has {0} health remaining".format(self.health)
    def _display(self):
        print "You enter the next room and a Gargoyle guards a tomb.  I wonder whats inside?"
        print """
               /|    /(_)\    |\                
             /' `\   \`,'/   /' `\              
           /' / | `\_/\~/\_/' | \ `\          
          O  |   \/'   V   `\/   |  O        
         O   |,-,|   ,_;_,   |,-,|   O       
        oO    \  \\ '\ I /` //  /    Oo     
        oO     \ \`\  \ /  /'/ /     Oo     
         O    /~\ \,\  |  /,/ /~\    O       
    ______O  /__/ /__| I |__\ \__\  O____    
    |      \|  '''  ''' ```  ```  |/     
        """

class dragon:
    def __init__(self):
        self.name = 'dragon'
        self.health = 1000
        self.stamina = 100
        self.damage = 0
        self.miss = 7
        self.dict = ['HITS','BITES','BURNS','DEVOURES','BREATHES FIRE','CRITS','MISSES']
        self.target = 'unknown'
        self.xp = 1000
    def _ability0(self):
        damage = random.randrange(1,80)
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "The Dragon MISSES you completely!"
        elif crit ==10:
            crit = damage*2.5
            self.damage = crit
            print "The Dragon CRITS you for {0}".format(self.damage)
        else:
            self.damage = damage
            print "The Dragon {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def _health(self):
        print "The Dragon has {0} health remaining".format(self.health)
    def _display(self):
        print "You happen upon a dragon's lair.  The gold and spoils he is guarding are beyond your wildest dreams.  If you can manage to defeat him..."
        print """
                                             ..
                                     ,o""'o
                                  ,o$"     o
                               ,o$$$                                 
                             ,o$$$'
                           ,o$"o$'
                         ,o$$"$"'   
                      ,o$"$o"$"'    
                   ,oo$"$"$"$"$$`                      ,oooo$$$$$$$$oooooo.  
                ,o$$$"$"$"$"$"$"o$`..             ,$o$"$$"$"'            `oo.o
             ,oo$$$o"$"$"$"$  $"$$$"$`o        ,o$$"o$$$o$'                 `o
          ,o$"$"$o$"$"$"$  $"$$o$$o $$o`o   ,$$$$$o$"$$o'                    $
        ,o"$$"'  `$"$o$" o$o$o"  $$$o$o$oo"$$$o$"$$"$o"'                     $
     ,o$"'        `"$ "$$o$$" $"$o$o$$"$o$$o$o$o"$"$"`""o                   ' 
   ,o$'          o$ `"$"$o "$o$$o$$$"$$$o"$o$$o"$$$    `$$  
  ,o'           (     `" o$"$o"$o$$$"$o$"$"$o$"$$"$ooo|  `` 
 $"$             `    (   `"o$$"$o$o$$ "o$o"   $o$o"$"$    )
(  `                   `    `o$"$$o$" "o$$     "o /|"$o"
 `                           `$o$$$$"" o$      "o$\|"$o'
                              `$o"$"$ $ "       `"$"$o$
                               "$$"$$ "oo         ,$""$ 
                               $"$o$$""o"          ,o$"$
                               $$"$$"$ "o           `,",
                     ,oo$oo$$$$$$"$o$$$ ""o           
                  ,o$$"o"o$o$$o$$$"$o$$oo"oo
                ,$"oo"$$$$o$$$$"$$$o"o$o"o"$o o
               ,$$$""$$o$,      `$$$$"$$$o""$o $o               
               $o$o$"$,          `$o$"$o$o"$$o$ $$o             
              $$$o"o$$           ,$$$$o$$o"$"$$ $o$$oo      ,   
              "$o$$$ $`.        ,"$$o$"o$""$$$$ `"$o$$oo    `o
              `$o$o$"$o$o`.  ,.$$"$o$$"$$"o$$$$   `$o$$ooo    $$ooooooo
                `$o$"$o"$"$$"$$"$"$$o$$o"$$o"        `"$o$o            `"o
                   `$$"$"$o$$o$"$$"$ $$$  $ "           `$"$o            `o
                      `$$"o$o"$o"$o$ "  o $$$o            `$$"o          ,$
                         (" ""$""'     o"" "o$o             `$$ooo     ,o$$
                              $$'""o   (   "$o$$$"o            `$o$$$o$"$'
                                ) ) )           )  ) )            ` "'
        """
class giant_snake:
    def __init__(self):
        self.name = 'snake'
        self.health = 250
        self.stamina = 25
        self.damage = 0
        self.miss = 15
        self.dict = ['HITS','BITES','KNICKS','DEVOURES','POISONS','CRITS','MISSES']
        self.target = 'unknown'
        self.xp = 65
    def _ability0(self):
        damage = random.randrange(20,30)
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "The giant snake MISSES you completely!"
        elif crit ==10:
            crit = damage*2.5
            self.damage = crit
            print "The giant snake CRITS you for {0}".format(self.damage)
        else:
            self.damage = damage
            print "The giant snake {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def _health(self):
        print "The giant snake has {0} health remaining".format(self.health)
    def _display(self):
        print "You enter the next room and startle a Giant Snake.  He attacks!"
        print '''
           ---_ ...... _/_ -    
          /  .      ./ .'*\ \    
          : '         /__-'   \. 
         /                      )
       _/                  >   .' 
     /   .   .       _.-" /  .'   
     \           __/"     /.'/|   
       \ '--  .-" /     //' |\|  
        \|  \ | /     //_ _ |/|
         `.  \:     //|_ _ _|\|
         | \/.    //  | _ _ |/| 
          \_ | \/ /    \ _ _ \\\ 
              \__/      \ _ _ \|\
        '''

def _ogre_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player._sword()
        print "\nAfter defeating the Ogre you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player._belt()
        print "\nAfter defeating the Ogre you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player._offhand()
        print "\nAfter defeating the Ogre you find an Offhand.\n"
    else:
        print "\nAfter defeating the Ogre you find nothing but junk\n"
    player._displayStats()

def _snake_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player._sword()
        print "\nAfter defeating the Giant Snake you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player._belt()
        print "\nAfter defeating the Giant Snake you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player._offhand()
        print "\nAfter defeating the Giant Snake you find an Offhand.\n"
    else:
        print "\nAfter defeating the Giant Snake you find nothing but junk\n"
    player._displayStats()

def _gargoyle_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player._sword()
        print "\nAfter defeating the Gargoyle you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player._belt()
        print "\nAfter defeating the Gargoyle you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player._offhand()
        print "\nAfter defeating the Gargoyle you find an Offhand.\n"
    elif rand >= 90 and rand <= 95:
        player._trinket()
        print "\nAfter defeating the Gargoyle you find an extremely rare Trinket.\n"
    elif rand == 100:
        player._legendary_weapon()
        print "\nAfter defeating the Gargoyle you find a Weapon that hasn't been seen for thousands of years.\n"
    else:
        print "\nAfter defeating the Gargoyle you find nothing but junk\n"
    player._displayStats()

def _dragon_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player._sword()
        print "\nAfter defeating the Dragon you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player._belt()
        print "\nAfter defeating the Dragon you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player._offhand()
        print "\nAfter defeating the Dragon you find an Offhand.\n"
    elif rand > 70 and rand <= 95:
        player._trinket()
        print "\nAfter defeating the Dragon you find an extremely rare Trinket.\n"
    elif rand > 95 and rand <= 100:
        player._legendary_weapon()
        print "\nAfter defeating the Dragon you find a Weapon that hasn't been seen for thousands of years.\n"
    else:
        print "\nAfter defeating the Dragon you find nothing but junk\n"
    player._displayStats()
    
def _abilities():
    print "Your abilities are: "
    player._abilities()
    sys.stdout.flush()

def _damage(chosen_ability):
     global _exit
     print ""
     #player._ability0()
     eval("player."+chosen_ability)
     enemy.health -= player.damage
     enemy._ability0()
     if(player.shield):
         if(player.shield < enemy.damage):
             enemy.damage -= player.shield
             player.shield = 0
         else:
             player.shield -= enemy.damage
             enemy.damage = 0
     player.health -= enemy.damage
     player._health()
     enemy._health()
     print ""
     if enemy.health <= 0 and player.health > 0:
         print "\nThe enemy has been defeated! WELL DONE!  You rest for a bit and regain some health"
         print "..."
         print "......"
         player.health = player.health + enemy.stamina*2
         if player.health > (player.stamina*10):
             player.health = player.stamina*10
         player._health()
         player.xp += enemy.xp
         if player.xp >= player.lvl * player.lvl * 65:
             player._level()
             player._displayStats()
             player._health()
             player._abilities()
             time.sleep(2)
         if enemy.name == 'ogre':
             _ogre_loot(player)
         elif enemy.name == 'snake':
             _snake_loot(player)
         elif enemy.name == 'gargoyle':
             _gargoyle_loot(player)
         elif enemy.name == 'dragon':
             _dragon_loot(player)
         else:
             print "something bad happened"
         time.sleep(2)
     elif player.health <= 0:
         print "\nYou have been slain! Better luck next time"
         print "...GAMEOVER..."
         _reset()
         _exit = True
    
def _attack(enemy):
    print "\nWhat would you like to use?"
    player._abilities()
    inpute = raw_input(">>> ")
    if int(inpute) == 1:
        _damage("_ability0()")
    elif int(inpute) == 2:
        _damage("_ability1()")
    sys.stdout.flush()
            
def _dance():
    print "\nYour character breaks into dance. 'This is awkward'"
    sys.stdout.flush()

def _reset():
    global chosen
    global _exit
    global no_enemy
    global enemies
    chosen = False
    no_enemy = True
    enemies = ['ogre','giant snake','ogre','giant snake','ogre','giant snake','gargoyle','dragon']
    _exit = False
    
while running != False:
    print "\nPlease choose your class: Mage (1), Warrior (2), Cleric(3), Warlock(4)"
    while chosen != True:
        _exit = False
        try:
            _class = raw_input(">>> ")
            if int(_class) is 1:
                print "Enter your adventurer's name"
                my_name = raw_input(">>> ")
                player = mage(my_name)
                chosen = True
            elif int(_class) is 2:
                print "Enter your adventurer's name"
                my_name = raw_input(">>> ")
                player = warrior(my_name)
                chosen = True
            elif int(_class) is 3:
                print "Enter your adventurer's name"
                my_name = raw_input(">>> ")
                player = cleric(my_name)
                chosen = True
            elif int(_class) is 4:
                print "Enter your adventurer's name"
                my_name = raw_input(">>> ")
                player = warlock(my_name)
                chosen = True
            elif int(_class) is 5:
                running = False
                chosen = True
            else:
                print "incorrect input"
        except ValueError:
            count += 1
            
    if running == False:
        break
    print ('\nWelcome ' + player.cls + ' '+ player.name +' lets begin our journey through Dragonia.  Good luck.')
    print "\nThe following commands are allowed: attack, dance, abilities, and exit.  More to come!\n"
    player._displayStats()
    print ""
    player._abilities()
    print ""
    _reset()
    time.sleep(3)
    while _exit == False:
        try:
            if no_enemy == True:
                if enemies == []:
                    print "You efforts have been valient, victory is yours!"
                    _reset()
                    break      
                else:
                    enemies_left = len(enemies)
                    if enemies_left == 1:
                        pick_enemy = 0
                    else:
                        pick_enemy = random.randrange(0,enemies_left)
                    if enemies[pick_enemy] == 'ogre':
                        enemy = ogre()
                    elif enemies[pick_enemy] == 'giant snake':
                        enemy = giant_snake()
                    elif enemies[pick_enemy] == 'gargoyle':
                        enemy = gargoyle()
                    elif enemies[pick_enemy] == 'dragon':
                        enemy = dragon()
                    enemy._display()
                    no_enemy = False
            inpt = raw_input(">>> ")
            if inpt == 'attack':
                _attack(enemy)
                if enemy.health <= 0 and player.health > 0:
                    no_enemy = True
                    if enemies != []:
                        enemies.pop(pick_enemy)
            elif inpt == 'abilities':
                _abilities()
            elif inpt == 'dance':
                _dance()
            elif inpt == 'exit':
                _exit = True
                running = False
            else:
                val = random.randrange(0,12)
                print "{0}".format(error_messages[val])
        except:
            count += 1
