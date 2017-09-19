from roster import Roster

from vehicles import aberdare
from vehicles import bertha
from vehicles import cargo_sprinter
from vehicles import chaplin
from vehicles import chinook
from vehicles import collett
from vehicles import cyclops
from vehicles import donegal
from vehicles import double_juice
from vehicles import electra
from vehicles import fleet
from vehicles import growler
from vehicles import high_flyer
from vehicles import hudswell
from vehicles import lemon
from vehicles import longwater
from vehicles import northcock
from vehicles import ramsbottom
from vehicles import raven
from vehicles import roarer
from vehicles import screamer
from vehicles import serpentine
from vehicles import shoebox
from vehicles import slammer
from vehicles import standard
from vehicles import stewart
from vehicles import suburban
from vehicles import tideway
from vehicles import tin_rocket
from vehicles import tug
from vehicles import tyburn
from vehicles import walker
from vehicles import westbourne
from vehicles import wizzo

# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
# speeds are roughly matched to RH trucks of same era + 5mph or so (back and forth on this many times eh?)
speeds = dict(gen_1_wagon_speeds = [45, 75],
              gen_2_wagon_speeds = [60, 90],
              gen_3_wagon_speeds = [75, 110],
              gen_4_wagon_speeds = [90, None],
              ng_gen_1_wagon_speeds = [55, 55])

roster = Roster(id = 'pony',
                numeric_id = 1,
                speeds = speeds,
                engines = [chaplin,
                           ramsbottom,
                           standard,
                           suburban,
                           aberdare,
                           bertha,
                           high_flyer,
                           raven,
                           collett,
                           lemon,
                           northcock,
                           electra,
                           shoebox,
                           growler,
                           chinook,
                           wizzo,
                           roarer,
                           double_juice,
                           tug,
                           cyclops,
                           screamer,
                           slammer,
                           tin_rocket,
                           cargo_sprinter,
                           # brit extras
                           serpentine,
                           westbourne,
                           fleet,
                           longwater,
                           tyburn,
                           tideway,
                           # brit ng
                           stewart,
                           hudswell,
                           donegal,
                           walker])
