from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="estados",
        base_numeric_id=9230,
        name="Estados Boxcab",
        power=1450,
        intro_date=1925,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=90, vehicle_length=6, spriterow_num=0
    )

    return consist
