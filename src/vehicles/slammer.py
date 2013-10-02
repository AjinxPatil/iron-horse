import global_constants
from train import Train, DieselLoco

vehicle = DieselLoco(id = 'slammer',
            numeric_id = 1360,
            title = 'Slammer [Diesel]',
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 80,
            power = 600,
            weight = 65,
            vehicle_length = 8,
            buy_menu_width = 32,
            loading_speed = 20,
            intro_date = 1980,
            str_type_info = 'COASTER',
            vehicle_life = 40,
            graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=1986,
                       spritesheet_suffix=0)

vehicle.add_model_variant(intro_date=1985,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)
