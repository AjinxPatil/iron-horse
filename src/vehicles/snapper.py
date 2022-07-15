from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="snapper",
        base_numeric_id=9630,
        name="Snapper",
        role="pax_railbus",
        role_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 350,
        },
        gen=4,
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        tail_light="railcar_24px_1",
    )

    consist.description = """A better railcar, for a new narrow-gauge century."""
    consist.foamer_facts = """CFC X2000/X5000, CFD Autorails"""

    return consist
