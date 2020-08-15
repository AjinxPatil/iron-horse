from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='garratt',
                            base_numeric_id=4050,
                            name='2-6-0+0-6-2 Garratt',
                            role='heavy_freight',
                            role_child_branch_num=-2,
                            replacement_consist_id='chinook', # this Joker ends with Chinook
                            power=2400,
                            tractive_effort_coefficient=0.4,
                            gen=3,
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=60,
                     vehicle_length=3,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=60,
                     vehicle_length=6,
                     effect_offsets=[(-3, 0), (-2, 0)], # double the smoke eh?
                     spriterow_num=1)

    consist.add_unit(type=SteamEngineUnit,
                     weight=60,
                     vehicle_length=3,
                     spriterow_num=2)

    consist.description = """ """
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """ """

    return consist