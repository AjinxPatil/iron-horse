import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'collett',
              base_numeric_id = 1880,
              title = '2-8-2 Collett [Steam]',
              power = 1400,
              speed = 60,
              type_base_buy_cost_points = 12, # dibble buy cost for game balance
              vehicle_generation = 3)

consist.add_unit(type = SteamLoco,
                 weight = 80,
                 vehicle_length = 8,
                 spriterow_num = 0)

consist.add_model_variant(start_date = 0,
                          end_date = global_constants.max_game_date)
