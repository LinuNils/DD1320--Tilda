#!/usr/bin/env python
# -*- coding: utf-8 -*-
from poke_list import *


hig_menu = 4
low_menu = 1
#file_name = "Excel Pkdx V5.14 - Pokedex.csv"
file_name = "pokedex.txt"

def main(file_name):
    '''

    :param file_name:
    :return:
    '''
    poke_list = Poke_List(file_name)
    menu(poke_list)

def menu(poke_list):
    '''
    Function that generates a simple menu consisting of some choices, then asks you for differend options
    :param poke_list:
    :return:
    '''
    print("Hi and welcome to the Pokédex!")
    choice = 1
    while choice != 4:
        try:
            print("\nPlease choose one of the following alternatives:"
                  "\n1 - Search for Pokémons."
                  "\n2 - Print list of Pokémons."
                  "\n3 - Exit\n")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                sub_menu(poke_list)
            elif choice == 2:
                poke_list.list()
            elif choice == 3:
                print("Exiting the Pokédex, goodbye.")
                break
        except:
            print("You need to enter a valid number between %d" %low_menu + "and %d \n" %(hig_menu-1))

def sub_menu(listobject):
    '''
    Function that generates a submenu based on what input that has been passed from previous menu
    :param choice:
    :return:
    '''
    poke_list = listobject
    breaker = True
    while breaker:
        sub_choice = 0
        try:

            while sub_choice != 2:
                print( "\n1 - Search by name:"
                       "\n2 - Return to main menu.")
                sub_choice = int(input("\nPlease enter your choice: "))
                if sub_choice == 1:
                    name = input("\nPlease enter a name: ")
                    poke_list.search_name(name)
                elif sub_choice == 2:
                    breaker = False
        except:
            print("Not a valid choice, please try again.")


main(file_name)