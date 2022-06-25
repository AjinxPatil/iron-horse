from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="hippo",
        base_numeric_id=10910,
        name="Hippo",
        power=3600,
        base_track_type="NG",
        intro_date=1975,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=130, vehicle_length=8, spriterow_num=0
    )

    return consist
