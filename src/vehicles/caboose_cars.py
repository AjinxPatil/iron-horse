from train import CabooseCarConsist, CabooseCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=4100,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="2_axle_ng_8px")

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=1290,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=CabooseCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=1280,
        gen=1,
        subtype="A",
        docs_image_spriterow=6,
        sprites_complete=True,
    )

    consist.add_unit(type=CabooseCar, chassis="2_axle_caboose_16px")

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=2210,
        gen=1,
        subtype="B",
        docs_image_spriterow=6,
        sprites_complete=True,
    )

    consist.add_unit(type=CabooseCar, chassis="4_axle_caboose_24px")
