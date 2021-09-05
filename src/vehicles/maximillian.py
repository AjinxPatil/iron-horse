from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="maximillian",
        base_numeric_id=5910,
        name="Maximillian",
        role="universal",
        role_child_branch_num=2,
        power=900,
        random_reverse=True,
        base_track_type="NG",
        gen=4,
        intro_date_offset=10,
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=30,
        vehicle_length=6,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """ """
    consist.foamer_facts = """ """

    return consist