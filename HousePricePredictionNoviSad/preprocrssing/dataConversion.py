import json
import math
import pandas as pd

if __name__ == '__main__':


    city_regions = [
        "Bulevar Oslobođenja",
        "Bulevar Evrope",
        "Bulevar Patrijarha Pavla",
        "Cara Dušana",
        "Grbavica",
        "Adamovićevo Naselje",
        "Tatarsko Brdo",
        "Futoški put",
        "Liman 2",
        "Liman 3",
        "Liman 4",
        "Telep",
        "Lipov Gaj",
        "Adice",
        "Centar,"
        "Grbavica",
        "Novo Naselje",
        "Podbara",
        "Salajka",
        "Petrovaradin",
        "Socijalno",
        "Nova Detelinara",
        "Stara Detelinara",
        "Detelinara",
        "Sajmište",
        "Železnička stanica",
        "Veternik",
        "Liman",
        "Veternička Rampa",
        "Sremska Kamenica",
        "Kej",
        "Spens",
        "Klisa",
        "Satelit",
        "Šarengrad",
        "Rotkvarija",
        "Avijatičarsko Naselje",
        "Stari Grad",
        "Popovica"
    ]


    dictionary = {}
    with open("../scraping/scraped-flats.json", "r", encoding='utf-8') as infile:
        dictionary = json.load(infile)


    def transform_and_append_price(price, price_list):
        splits = price.split()
        number = splits[0].split(".")
        # print(spl)
        if len(number) > 1:
            new_str = number[0] + number[1]
            new_int = math.floor((int(new_str) / 25000))
            sttr = int(new_str)
        else:
            new_str = number[0]
            new_int = math.floor((int(new_str) / 25000))
            sttr = int(new_str)
        price_list.append(sttr)


    def transform_and_append_surface(surface, surface_list):
        splits = surface.split()
        surface_num = splits[0]
        surface_list.append(int(surface_num))

    def transform_and_append_garage(garage,garage_list):
        if garage is None:
            garage_list.append(0)
        elif '1' in garage:
            garage_list.append(1)
        elif '2' in garage:
            garage_list.append(2)
        elif '3' in garage:
            garage_list.append(3)
        else:
            garage_list.append(0)


    def transform_and_append_rooms(rooms, rooms_list):
        rooms_dec = rooms.split()[0]
        rooms_num = rooms_dec.split('.')
        if len(rooms_num) > 1:
            if rooms_num[1] == '5':
                rooms_list.append(float(rooms_num[0])+1)
                return
        rooms_list.append(float(rooms_num[0]))

    def transform_and_append_year_of_build(yearOfBuild,yearOfByuild_list):
        if yearOfBuild is None:
            yearOfByuild_list.append(None)
            return
        yearOfBuild_num = yearOfBuild.split('-')[0]
        yearOfByuild_list.append(int(yearOfBuild_num))


    def transform_and_append_furniture(furniture, furniture_list):
        furniture_list.append(map_furniture(furniture))


    def map_furniture(namestenost):
        if namestenost == 'namešteno':
            return 2
        elif namestenost == 'polunamešteno':
            return 1
        elif namestenost == 'prazno':
            return 0
        else:
            return None

    def transform_and_append_floor(floor,floor_list):
        if floor is None:
            floor_list.append(None)
            return
        if 'prizemlje' in floor:
            floor_list.append(1)
        elif 'suteren' in floor:
            floor_list.append(0)
        elif '.' in floor:
            floor_num = floor.split('.')[0]
            floor_list.append(int(floor_num)+1)
        elif 'potkrovlje' in floor:
            splits = floor.split()
            floor_num = splits[0].split('/')[1]
            floor_list.append(int(floor_num)+1)
        elif '/' in floor:
            floor_num = floor.split('/')[0]
            floor_list.append(int(floor_num))
        else:
            floor_list.append(None)

    def transform_and_append_location(address,location,city_regions,location_list):
        for region in city_regions:
            if region.lower() in address.lower() or region.lower() in location.lower():
                location_list.append(region)
                return
        location_list.append("retka_lokacija")


    price = []
    address = []
    location = []
    surface = []
    rooms = []

    heating = []
    infrastructure = []
    furniture = []
    equipment = []
    elevator= []

    floor = []
    flatType = []
    parking  = []
    garage =[]
    yearOfBuild = []

    state = []

    for i in range(len(dictionary)):
        transform_and_append_price(dictionary[i].get('Cena:', None), price)
        address.append(dictionary[i].get('Adresa:', None))
        # location.append(dictionary[i].get('Lokacija:', None))
        transform_and_append_location(dictionary[i].get('Adresa:', None),dictionary[i].get('Lokacija:', None),city_regions,location)
        transform_and_append_surface(dictionary[i].get('Površina:', None), surface)
        transform_and_append_rooms(dictionary[i].get('Broj soba:', None), rooms)
        heating.append(dictionary[i].get('Grejanje:', None))
        infrastructure.append(dictionary[i].get('Infrastruktura:', None))
        transform_and_append_furniture(dictionary[i].get('Nameštenost:', None), furniture)
        equipment.append(dictionary[i].get('Opremljenost:', None))
        transform_and_append_garage(dictionary[i].get('Garaža:', None),garage)
        elevator.append(dictionary[i].get('Lift:',None))

        # floor.append(dictionary[i].get('Spratnost:', None))
        transform_and_append_floor(dictionary[i].get('Spratnost:', None),floor)
        flatType.append(dictionary[i].get('Tip:', None))
        parking.append(dictionary[i].get('Parking:', None))
        transform_and_append_year_of_build(dictionary[i].get('Godina izgradnje:', None),yearOfBuild)
        state.append(dictionary[i].get('Stanje:',None))
        print(i)
    data_tuples = list(zip(price[:], location[:], surface[:], rooms[:], heating[:],
                            furniture[:],  flatType[:], elevator[:] ,garage[:], infrastructure[:], floor[:], yearOfBuild[:],state[:]))
    temp_df = pd.DataFrame(data_tuples, columns=['cena','lokacija', 'površina', 'broj soba',
                                                 'grejanje', 'nameštenost',
                                                 'tip','lift','garaža','infrastruktura','sprat','godina izgradnje','stanje'])
    temp_df.to_csv('../data/kategoričneVrednostiNumerisane.csv', encoding='utf-8')
    print(temp_df)
