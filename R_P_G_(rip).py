import random
import time
class Hero:
    def __init__(self, name, hp, damage):
        self.name= name
        self.hp=hp
        self.damage=damage
        self.level=1
        self.xp=0
        self.skills=None

    def hero_creater(name,rass,prof):
        hp=0
        damage=0
        if rass == rass_list[0]:
            hp +=1000
            damage +=10
        elif rass==rass_list[1]:
            hp +=90
            damage +=90
        elif rass == rass_list[2]:
            hp +=100
            damage +=10
        elif rass == rass_list[3]:
            hp +=200
            damage +=80
        elif rass == rass_list[4]:
            hp+=10
            damage +=666
        else:
            print('такого нельзя')

        if prof == prof_list[0]:
            hp += 300
            damage -= 9
        elif prof == prof_list[1]:
            hp += 80
            damage -= 8
        elif prof == prof_list[2]:
            hp += 100
            damage += 15
        elif prof == prof_list[3]:
            hp += 50
            damage += 35
        elif prof == prof_list[4]:
            hp -= 0
            damage += 65
        else:
            time.sleep(2)
            print('такого нельзя')
        return Hero(name,hp,damage)
    def attack(self,victim):
        max_xp=self.level*100
        victim.hp-=self.damage
        if self.skills==skills_list[0]:
            g=random.randint(1,20)
            if g>=15:
                time.sleep(2)
                print(f'{h_name} победил/a {victim.name}/a  ты получил 10 очков опыта')
                self.xp += 10
                # self.weapon()
                self.skills = random.choice(skills_list)
                time.sleep(2)
                print(f'вы теперь можете использовать {self.skills}')
                if self.xp >= max_xp:
                    self.level_up(max_xp)
                loot = random.randint(0, 3)
                if loot == 0:
                    gift = self.weapon()
                    time.sleep(2)
                    print(f'ты получил {gift}')
                elif loot == 1:
                    gift = self.armor()
                    time.sleep(2)
                    print(f'ты получил {gift}')
                elif loot == 2:
                    gift = self.food()
                    time.sleep(2)
                    print(f'ты получил {gift}')
                else:
                    time.sleep(2)
                    print('диллер - нехороший человек!!!!!')
        else:

            if victim.hp<=0:
                time.sleep(2)
                print(f'{h_name} победил/a {victim.name}/a  ты получил 10 очков опыта')
                self.xp+=10
                #self.weapon()
                self.skills=random.choice(skills_list)
                time.sleep(2)
                print(f'вы теперь можете использовать {self.skills}')
                if self.xp>=max_xp:
                    self.level_up(max_xp)
                loot=random.randint(0,3)
                if loot==0:
                    gift=self.weapon()
                    time.sleep(2)
                    print(f'ты получил {gift}')
                elif loot==1:
                    gift = self.armor()
                    time.sleep(2)
                    print(f'ты получил {gift}')
                elif loot==2:
                    gift = self.food()
                    time.sleep(2)
                    print(f'ты получил {gift}')
                else:
                    time.sleep(2)
                    print('диллер - нехороший человек!!!!!')

                return False
            else:
                if self.skills!=None:
                    skills_use()
                    time.sleep(2)
                print(f'у {victim.name}/a осталось {victim.hp} жизней')
                return True
    def level_up(self,max_xp):
        self.xp-=max_xp
        self.level+=1
        self.damage+=self.level*10
        self.hp += self.level * 10
        time.sleep(2)
        print('leve up')
        print(f'твой уровень теперь {self.level}')
    def weapon(self):
        weapon_type=weapon_list[random.randint(0,2)]
        weapon_cost=random.choice(list(weapon_rarety.keys()))
        if weapon_type==weapon_list[0]:
            self.damage+=random.randint(1,5)*weapon_cost
        elif weapon_type==weapon_list[1]:
            self.damage+=random.randint(1,5)*weapon_cost
        elif weapon_type==weapon_list[2]:
            self.damage+=random.randint(1,5)*weapon_cost
        return weapon_type,weapon_rarety[weapon_cost]
    def armor(self):
        armor_type=armor_list[random.randint(0,2)]
        armor_cost=random.choice(list(weapon_rarety.keys()))
        if armor_type==armor_list[0]:
            self.hp+=random.randint(1,5)*armor_cost
        elif armor_type==armor_list[1]:
            self.hp+=random.randint(1,5)*armor_cost
        elif armor_type==armor_list[2]:
            self.hp+=random.randint(1,5)*armor_cost
        return armor_type,weapon_rarety[armor_cost]
    def food(self):
        food_random=list(food_dict.keys())
        food_type=random.choice(food_random)
        if food_type==food_random[2]:
            time.sleep(2)
            print('У ВАС ОСТАНОВИЛОСЬ СЕРДЦЕ')
            time.sleep(2)
            quit()
        self.xp+=food_type
        return food_dict[food_type]





class Enemy:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def enemy_creater():
        r_name=random.choice(evil_humans)
        r_hp=random.randint(1,500)
        r_damage = random.randint(1, 500)
        return Enemy(r_name,r_hp,r_damage)

    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            time.sleep(2)
            print('game over')
            time.sleep(2)
            quit()
        else:
            time.sleep(2)
            print(f'у {victim.name}/a осталось {victim.hp} жизней')
class Friend:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def friend_creater():
        f_name=random.choice(rass_list)
        f_hp=random.randint(1,100)
        f_damage = random.randint(1, 100)
        return Friend(f_name,f_hp,f_damage)
def war():
    time.sleep(2)
    answer=input(f'готов ли ты принять бой с {e.name}(да/нет/win+del)').lower()
    if answer=='да':
        fight_results=p.attack(e)
        if fight_results==True:
            e.attack(p)
            war()
    elif answer=='нет':
        eskeyp=random.randint(0,20)
        if eskeyp<=15:
            time.sleep(2)
            print(f'побег не удався, {e.name} тебя побьёт')
            e.attack(p)
            war()
        else:
            time.sleep(2)
            print('ты убежав')
    elif answer=='win+del':
        time.sleep(2)
        print('-_- game over')
    else:
        time.sleep(2)
        print('rotate banana,rotate faster banan a, goooooooo, G        O, can you feel the power of rotation ban an as????? ')
        war()
def skills_use():
    if p.skills==skills_list[0]:
        time.sleep(2)
        print('ты невидимый -_-, у тебя есть шанс проскользнуть мимо врага')
    elif p.skills==skills_list[1]:
        time.sleep(2)
        print('ты теперь страшный,0_о')
        p.damage+=1000
    elif p.skills==skills_list[2]:
        time.sleep(2)
        print('молодец!')
        e.damage-=100

rass_list=['чебурек','кот','эльф','человек-армен','вращающийся таракан']
prof_list=['величайший шаурмен','домашний обитатель','монстр из под кровати','воинъ Староруссии','гонщик из нижнего Тагила']
evil_humans=['Ольга Александровна','собака','ЬУЪ','Никол Болас, бог-дракон','Элиш Норн, мать машин ']
weapon_list=['поножи волшебного пенделя','пивная кега','шприц из подъезда']
armor_list=['кострюля','кожанка','три метра медного кабеля']
weapon_rarety={1:'обычная ',5:'необычная',10:'ЛЕГЕНДАРНАЯ'}
food_dict={1:'привакзальная шаурма',5:'глина',10:'вода в собственном соку',15:'абрикосове варенье',20:'энэргетик'}
skills_list=['невидимость','устрашение','моральная устойчивость']
h_name=input('вашим именем на сегодня будет - ')
print(f'доступные(и не очень) проффессии - {prof_list}')
h_prof=input('введите профессию, в адрес которой в дальнейшем вы будете неуважительно высказываться ')
print(f'доступные(и не очень) рассы - {rass_list}')
h_rass=input('введите рассу, в адрес которой в дальнейшем вы будете неуважительно высказываться ').lower()
p = Hero.hero_creater(h_name, h_rass,h_prof)
time.sleep(2)
print(f'здравствуй {p.name}, у тебя {p.hp} жизней, а твой уровен так мал, что тебе лучше и не знать '
 f'о его существовании, но зато ты силён, бьёшь ты на целых {p.damage} урона')
while True:
    room=random.randint(0,2)
    if room==1:
        f = Friend.friend_creater()
        time.sleep(2)
        print('ты встретил(а) друга')
        print(f'твой друг - {f.name} , у него {f.damage} урона и {f.hp} жизней')
        time.sleep(2)
        p.damage+=f.damage
        p.hp+=f.hp

    elif room==0:
        e=Enemy.enemy_creater()
        time.sleep(2)
        print('ты встретил(а) врага')
        print(f'твой враг - {e.name} , у него {e.damage} урона и {e.hp} жизней')
        time.sleep(2)
        war()
    else:
        time.sleep(2)
        print('тебе повезло и ты никого не встретил\n идём дальше')
        time.sleep(2)
