import global_constants
from train import EngineConsist, MetroPaxUnit

consist = EngineConsist(id = 'medrano',
              base_numeric_id = 1490,
              title = 'Medrano [Metro Train]',
              track_type = 'METRO',
              power = 1100,
              speed = 65,
              type_base_buy_cost_points = 80, # dibble buy cost for game balance
              intro_date = 2000)

# should be 4 units, not 2
consist.add_unit(type = MetroPaxUnit,
                        weight = 30,
                        vehicle_length = 8,
                        capacity_pax = 200,
                        spriterow_num = 0)

consist.add_unit(type = MetroPaxUnit,
                        weight = 30,
                        vehicle_length = 8,
                        capacity_pax = 200,
                        spriterow_num = 1)

consist.add_model_variant(start_date = 0,
                       end_date = global_constants.max_game_date)
