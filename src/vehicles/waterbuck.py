from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="waterbuck",
        base_numeric_id=11060,
        name="Waterbuck",
        power=2200,
        base_track_type="NG",
        intro_year=1990,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=120, vehicle_length=8, spriterow_num=0
    )

    return consist
