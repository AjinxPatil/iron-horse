from train import OpenCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=850,
                             gen=1,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=3)


    #--------------- pony ----------------------------------------------------------------------

    # only type A for gen 1

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=820,
                             gen=1,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')


    # no new type A for gen 2, gen 1 type A continues

    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=830,
                             gen=2,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')


    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=840,
                             gen=3,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')


    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=2440,
                             gen=3,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6,
                     chassis='4_axle_gapped_24px')


    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=1450,
                             gen=4,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=4,
                     chassis='2_axle_filled_16px')


    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=2450,
                             gen=4,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=6,
                     vehicle_length=6,
                     chassis='2_axle_filled_24px')


    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=2460,
                             gen=5,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=6)


    consist = OpenCarConsist(roster='pony',
                             base_numeric_id=2470,
                             gen=5,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=8)


    # no gen 6 open cars, cap to gen 5 in Pony
