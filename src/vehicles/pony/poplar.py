from train import PassengerEngineMetroConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineMetroConsist(
        roster_id=roster_id,
        id="poplar",
        base_numeric_id=1930,
        name="Poplar",
        role="pax_metro",
        role_child_branch_num=-1,
        power_by_power_source={
            "METRO": 600,
        },
        gen=1,
        sprites_complete=False,
    )

    # should be 4 units not 2, would look nicer short, but eh, painting
    consist.add_unit(
        type=MetroUnit,
        weight=36,
        capacity=120,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist.description = """."""
    consist.foamer_facts = """ """

    return consist
