#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pokeMon import *
class Poke_List(object):
    def __init__(self, filename):
        '''
        Constructor for the list-class
        :param filename:
        '''
        self.file_name = filename
        self.poke_list = []
        self.read_from_file()

    def read_from_file(self):
        '''
        Method that reads from file, creating new objects of the class Pokemon for each line.
        Appending these objects to the attribute list.
        :return:
        '''
        try:
            file = open(self.file_name, "r")
            info = file.readlines()[1:]
            for line in info:
                temp_list = line.split(",")
                temp_pokemon = Pokemon()
                temp_pokemon.set_name(temp_list[2])
                temp_pokemon.set_attack(temp_list[4])
                temp_pokemon.set_defense(temp_list[5])
                temp_pokemon.set_hp(temp_list[3])
                temp_pokemon.set_special_attack(temp_list[6])
                temp_pokemon.set_speed(temp_list[7])
                self.poke_list.append(temp_pokemon)
            file.close()
        except:
            error = "It seems that the file you are trying to read from is invalid or corrupted, please try again."
            return error

    def search_name(self, name):
        '''
        Function for searching based on pokemon name, returns that pokemon.
        :param name:
        :return:
        '''
        not_found = 0
        for pokemon in self.poke_list:
            if pokemon.name.lower().find(name.lower()) > -1:
                print(pokemon)
            else:
                not_found = 1
        if not_found == 1:
            print("There are unfortunately no Pokémons by that name, please try with another name.\n")

    def list(self):
        '''
        Method that prints a list of all the pokemons in the pokedex
        :return:
        '''
        for pokemon in self.poke_list:
            print(pokemon)
