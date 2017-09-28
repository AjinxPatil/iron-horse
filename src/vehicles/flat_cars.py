import global_constants
from train import FlatConsist, FreightCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = FlatConsist(roster = 'pony',
                           base_numeric_id = 1140,
                           vehicle_generation = 1)

    consist.add_unit(type = FreightCar,
                           capacity = 20,
                           vehicle_length = 4)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(roster = 'pony',
                           base_numeric_id = 1150,
                           vehicle_generation = 2)

    consist.add_unit(type = FreightCar,
                           capacity = 40,
                           vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(roster = 'pony',
                           base_numeric_id = 1160,
                           vehicle_generation = 3)

    consist.add_unit(type = FreightCar,
                           capacity = 50,
                           vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(roster = 'pony',
                           base_numeric_id = 1170,
                           vehicle_generation = 1,
                                        track_type = 'NG')

    consist.add_unit(type = FreightCar,
                           capacity = 12,
                           vehicle_length = 3)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------
    consist = FlatConsist(roster = 'llama',
                           base_numeric_id = 1180,
                           vehicle_generation = 1)

    consist.add_unit(type = FreightCar,
                           capacity = 25,
                           vehicle_length = 5)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(roster = 'llama',
                           base_numeric_id = 1510,
                           vehicle_generation = 2)

    consist.add_unit(type = FreightCar,
                           capacity = 45,
                           vehicle_length = 5)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(roster = 'llama',
                           base_numeric_id = 520,
                           vehicle_generation = 1,
                                        track_type = 'NG')

    consist.add_unit(type = FreightCar,
                           capacity = 20,
                           vehicle_length = 5)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(roster = 'llama',
                           base_numeric_id = 1500,
                           vehicle_generation = 2,
                                        track_type = 'NG')

    consist.add_unit(type = FreightCar,
                           capacity = 35,
                           vehicle_length = 5)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = FlatConsist(roster = 'antelope',
                           base_numeric_id = 1640,
                           vehicle_generation = 1)

    consist.add_unit(type = FreightCar,
                           capacity = 55,
                           vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(roster = 'antelope',
                           base_numeric_id = 1650,
                           vehicle_generation = 2)

    consist.add_unit(type = FreightCar,
                           capacity = 70,
                           vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(roster = 'antelope',
                           base_numeric_id = 2110,
                           vehicle_generation = 1,
                                        track_type = 'NG')

    consist.add_unit(type = FreightCar,
                           capacity = 20,
                           vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(roster = 'antelope',
                           base_numeric_id = 1930,
                           vehicle_generation = 2,
                                        track_type = 'NG')

    consist.add_unit(type = FreightCar,
                           capacity = 30,
                           vehicle_length = 8)

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                           end_date = global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])
