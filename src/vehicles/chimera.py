from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="chimera",
        base_numeric_id=10030,
        name="Chimera",
        role="heavy_freight_4",
        power=5200,
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=6,
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=128,  # weight reduced from 140 to nerf run cost down :P
        vehicle_length=8,
        spriterow_num=0,
    )

    return consist
