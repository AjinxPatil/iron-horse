from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='triton',
                            base_numeric_id=3910,
                            name='Triton',
                            role='heavy_freight_2',
                            power=6850, # relatively tiny jump from gen 5, compared to gen 4->5, very high-powered single unit engines are unbalanced for Pony
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            gen=6,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=7,  # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=128,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist