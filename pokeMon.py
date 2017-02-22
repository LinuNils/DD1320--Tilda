class Pokemon(object):

    def __init__(self, name='', hp=1, attack=1, defense=1, special_attack=1, speed=1):
        '''
        :param name:
        :param hp:
        :param attack:
        :param defense:
        :param special_attack:
        :param speed:
        '''
        self.name = name
        self.hP = hp
        self.atK = attack
        self.deF = defense
        self.spA = special_attack
        self.spD = speed

    def __str__(self):
        '''
        Returns a string representation of the object when called by print(object)
        :return:
        '''
        pokemon_repr = "\n"
        pokemon_repr += "Name: "+self.name+"\n"+"HP: "+self.hP+"\n"+"Attack: "+self.atK+\
                        "\n"+"Defense: "+self.deF+"\n"+"Special Attack: "+self.spA+"\n"+"Speed :"+self.spD+"\n"
        return pokemon_repr

    def set_hp(self, hp):
        '''
        Method that sets pokemon hp
        :param hp:
        :return:
        '''
        self.hP = hp

    def set_name(self, name):
        '''
        Method that sets name
        :param name:
        :return:
        '''
        self.name = name

    def set_attack(self, attack):
        '''
        Method that sets attac
        :param attack:
        :return:
        '''
        self.atK = attack

    def set_defense(self, defense):
        '''
        Method that sets defense
        :param defense:
        :return:
        '''
        self.deF = defense

    def set_special_attack(self, spa):
        '''
        Sets special attack
        :param spa:
        :return:
        '''
        self.spA = spa

    def set_speed(self, speed):
        '''
        Sets speed
        :param speed:
        :return:
        '''
        self.spD = speed



