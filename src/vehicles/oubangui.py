from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="oubangui",
        base_numeric_id=11050,
        name="2-6-6-2 Oubangui",
        power=1500,
        base_track_type="NG",
        intro_year=1920,
    )

    consist.add_unit(type=SteamEngineUnit, weight=90, vehicle_length=8, spriterow_num=0)

    return consist
