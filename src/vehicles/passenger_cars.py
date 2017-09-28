import global_constants
from train import PassengerConsist, PassengerCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = PassengerConsist(roster = 'pony',
                               base_numeric_id = 740,
                               vehicle_generation = 1,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                           capacity = 25,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'pony',
                               base_numeric_id = 750,
                               vehicle_generation = 2,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                            capacity = 55,
                            vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'pony',
                               base_numeric_id = 760,
                               vehicle_generation = 3,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                           capacity = 75,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'pony',
                               base_numeric_id = 770,
                               vehicle_generation = 1,
                               track_type = 'NG')

    consist.add_unit(type = PassengerCar,
                           capacity = 25,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------
    consist = PassengerConsist(roster = 'llama',
                               base_numeric_id = 780,
                               vehicle_generation = 1,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                            capacity = 40,
                            vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'llama',
                               base_numeric_id = 790,
                               vehicle_generation = 2,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                            capacity = 50,
                            vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'llama',
                               base_numeric_id = 800,
                               vehicle_generation = 3,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                            capacity = 60,
                            vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'llama',
                               base_numeric_id = 810,
                               vehicle_generation = 1,
                               speedy = True,
                               track_type = 'NG')

    consist.add_unit(type = PassengerCar,
                            capacity = 30,
                            vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'llama',
                               base_numeric_id = 1350,
                               vehicle_generation = 2,
                               speedy = True,
                               track_type = 'NG')

    consist.add_unit(type = PassengerCar,
                            capacity = 40,
                            vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)



    consist = PassengerConsist(roster = 'llama',
                               base_numeric_id = 1370,
                               vehicle_generation = 3,
                               speedy = True,
                               track_type = 'NG')

    consist.add_unit(type = PassengerCar,
                            capacity = 50,
                            vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    #--------------- antelope ----------------------------------------------------------------------
    consist = PassengerConsist(roster = 'antelope',
                               base_numeric_id = 1580,
                               vehicle_generation = 1,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                            capacity = 55,
                            vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'antelope',
                               base_numeric_id = 1560,
                               vehicle_generation = 2,
                               speedy = True)

    consist.add_unit(type = PassengerCar,
                            capacity = 80,
                            vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'antelope',
                               base_numeric_id = 2130,
                               vehicle_generation = 1,
                               speedy = True,
                               track_type = 'NG')

    consist.add_unit(type = PassengerCar,
                            capacity = 20,
                            vehicle_length = 5)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)


    consist = PassengerConsist(roster = 'antelope',
                               base_numeric_id = 1940,
                               vehicle_generation = 2,
                               speedy = True,
                               track_type = 'NG')

    consist.add_unit(type = PassengerCar,
                            capacity = 30,
                            vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date)
