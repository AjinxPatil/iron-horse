from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="unicorn",
        base_numeric_id=12290,
        name="Unicorn",
        role="heavy_express",
        role_child_branch_num=1,
        power=3200,
        random_reverse=True,
        gen=5,
        intro_date_offset=5,  # introduce later than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=90, vehicle_length=8, spriterow_num=0
    )

    return consist
