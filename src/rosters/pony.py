from roster import Roster

from vehicles import aberdare
from vehicles import badger
from vehicles import bertha
#from vehicles import cargo_sprinter
from vehicles import chaplin
from vehicles import chinook
from vehicles import collett
from vehicles import donegal
from vehicles import electra
from vehicles import express_tank
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
from vehicles import slug
from vehicles import sparkycat
from vehicles import standard
from vehicles import stewart
from vehicles import suburban
from vehicles import super_shoebox
from vehicles import tideway
from vehicles import tin_rocket
from vehicles import toaster
from vehicles import tug
from vehicles import tyburn
from vehicles import walker
from vehicles import westbourne
from vehicles import wizzo

roster = Roster(id = 'pony',
                numeric_id = 1,
                # default intro dates per generation, can be over-ridden if needed by setting intro_date kw on consist
                intro_dates = [1860, 1900, 1930, 1960, 1990, 2020],
                # default speeds per generation, can be over-ridden if needed by setting speed kw arg on consist
                # speeds are roughly matched to RH trucks of same era + 5mph or so (back and forth on this many times eh?)
                speeds = {'RAIL': {'freight': [45, 45, 60, 75, 90, 110],
                                 'express': [65, 80, 95, 110, 125, 140]},
                          'NG': {'freight': [75, 110],
                                   'express': [55, 55]}},
                engines = [chaplin,
                           ramsbottom,
                           standard,
                           suburban,
                           aberdare,
                           bertha,
                           high_flyer,
                           raven,
                           express_tank,
                           collett,
                           lemon,
                           northcock,
                           electra,
                           shoebox,
                           growler,
                           chinook,
                           wizzo,
                           roarer,
                           slug,
                           tug,
                           screamer,
                           badger,
                           super_shoebox,
                           sparkycat,
                           toaster,
                           slammer,
                           tin_rocket,
                           #cargo_sprinter,
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
