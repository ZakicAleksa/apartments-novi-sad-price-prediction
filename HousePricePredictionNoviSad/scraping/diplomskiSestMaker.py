import math

import pandas as pd
import json


def calculate_rooms(rooms, lists):
    room_num_decimal = rooms.split()[0]
    lists.append()

def calculate_floor(floor, lists):
    splits = floor.split()
    spl = splits[0].split("/")
    s = spl[0].split(".")[0]
    lists.append(s)


def map_furniture(namestenost):
    if namestenost == 'namešteno':
        return 1
    elif namestenost == 'polunamešteno':
        return 2
    elif namestenost == 'prazno':
        return 3
    else:
        return None

def calculate_equipment(equipments,equipement_list,kuhinjski_list):
    splits = equipments.split(",")
    equipmentGrade = len(splits)
    kuhinja = 0
    for equipment in splits:
        if "kuhinjski elementi" in equipment:
            # equipmentGrade = equipmentGrade + 1
            kuhinja = 1
        if "ležaj" in equipment:
            equipmentGrade = equipmentGrade + 1
    equipement_list.append(equipmentGrade)
    kuhinjski_list.append(kuhinja)


def calculate_price(price, lists):
    splits = price.split()
    spl = splits[0].split(".")
    # print(spl)
    if len(spl) > 1:
        new_str = spl[0] + spl[1]
        new_int = math.floor((int(new_str)/25000))
        sttr = float(new_str)
    else:
        new_str = spl[0]
        new_int = math.floor((int(new_str) / 25000))
        sttr = float(new_str)
    lists.append(sttr)


def calculate_area(elem, areas):
    my = ''
    for s in elem:
        if s == 'm':
            break
        my += s
    areas.append(my)


def calculate_year(elem, years):
    if elem is not None:
        years.append(elem.split("-")[0])
    else:
        years.append('0')


def parse_location(location, current_locations):
    splited = location.split(",")
    if "Gradske" in splited[1]:
        if splited[0][0] == ' ':
            locations.append(splited[0][1:])
        else:
            locations.append(splited[0])
    else:
        if splited[1][0] == ' ':
            locations.append(splited[1][1:])
        else:
            locations.append(splited[1])

def parseAdress(adress,addresses):
    if "centar" in adress.lower():
        addresses.append("Centar")
    elif "nova detelinara" in adress.lower():
            addresses.append("Nova Detelinara")
    else:
        if adress[0] == ' ':
            addresses.append(adress[1:])
        else:
            addresses.append(adress)


if __name__ == '__main__':
    # list_dictionary = {}
    list_dictionar1 = {}
    with open("../diplomski/data/diplomskiApartmani.json", "r", encoding='utf-8') as infile:
        list_dictionary = json.load(infile)
    # with open("../resources/finalApartments2.json", "r", encoding='utf-8') as infile:
    #     list_dictionary1 = json.load(infile)
    # list_dictionary.extend(list_dictionary1)

    cene = []
    adrese = []
    sobe = []
    grejanje = []
    infrastructure = []
    namestenost = []
    opremljenost = []
    povrsina = []
    spratnost = []
    tip=[]
    kuhinja = []


    average_price = []
    lifts = []

    evidents = []
    states = []
    availables = []
    yearOfBuild = []
    locations = []

    print(list_dictionary[:10])
    print("Length of map:" + str(len(list_dictionary)))
    for i in range(len(list_dictionary)):
        calculate_price(list_dictionary[i]['Cena:'], cene)
        calculate_rooms(list_dictionary[i]['Broj soba:'], sobe)
        parseAdress(list_dictionary[i]['Adresa:'], adrese)
        grejanje.append(list_dictionary[i]['Grejanje:'])
        infrastructure.append(list_dictionary[i]['Infrastruktura:'])
        namestenost.append(map_furniture(list_dictionary[i]['Nameštenost:']))
        calculate_equipment(list_dictionary[i]['Opremljenost:'], opremljenost,kuhinja)

        # opremljenost.append(list_dictionary[i].get('Opremljenost:'))

        calculate_area(list_dictionary[i]['Površina:'], povrsina)
        calculate_floor(list_dictionary[i]['Spratnost:'], spratnost)
        tip.append(list_dictionary[i]["Tip:"])

        data_tuples = list(zip(cene[:], adrese[:], sobe[:], grejanje[:],infrastructure[:],
                               namestenost[:], opremljenost[:],kuhinja[:], povrsina[:], spratnost[:], tip[:],
                               ))  # list of each players name and salary paired together
        temp_df = pd.DataFrame(data_tuples, columns=['cene', 'adrese', 'sobe', 'grejanje',
                                                     'infrastructure', 'namestenost', 'opremljenost','kuhinja', 'povrsina', 'spratnost', 'tip'])  # creates dataframe of each tuple in list
        temp_df.to_csv('kuhinja.csv', encoding='utf-8')
        print(temp_df)





        # lifts.append(list_dictionary[i].get('Lift:'))
        # evidents.append(list_dictionary[i]['Uknjiženost:'])
        # states.append(list_dictionary[i].get('Stanje:'))
        # availables.append(list_dictionary[i].get('Useljivo:'))
        # calculate_year(list_dictionary[i].get('Godina izgradnje:'), yearOfBuild)
        # parse_location(list_dictionary[i]['Lokacija'], locations)


    # print("Length of prices:" + str(len(prices)))
    # print("Length of addresses:" + str(len(addresses)))
    # print("Length of rooms:" + str(len(rooms)))
    # print("Length of gr:" + str(len(grs)))
    # print("Length of nams:" + str(len(nams)))
    # print("Length of lifts:" + str(len(lifts)))
    # print("Length of stores:" + str(len(stores)))
    # print("Length of areas:" + str(len(areas)))
    # print(prices)
    # print(addresses)
    # print(rooms)
    # print(grs)
    # print(nams)
    # print(lifts)
    # print(stores)
    # print(areas)
    # print(evidents)
    # print(states)
    # print(availables)
    # print(yearOfBuild)
    # print(floors)

