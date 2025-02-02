from typing import List

from .Locations import *
from .Locations import LocationData


class PlanetData(NamedTuple):
    name: str
    number: int
    locations: List[LocationData] = []


ARANOS_TUTORIAL = PlanetData("Aranos Tutorial", 0)
OOZLA = PlanetData("Oozla", 1, [
    OOZLA_OUTSIDE_MEGACORP_STORE,
    OOZLA_END_STORE_CUTSCENE,
    OOZLA_MEGACORP_SCIENTIST,
    OOZLA_TRACTOR_PUZZLE_PB,
    OOZLA_SWAMP_RUINS_PB,
    OOZLA_SWAMP_MONSTER_II,
])
MAKTAR_NEBULA = PlanetData("Maktar Nebula", 2, [
    MAKTAR_ARENA_CHALLENGE,
    MAKTAR_PHOTO_BOOTH,
    MAKTAR_DEACTIVATE_JAMMING_ARRAY,
    MAKTAR_JAMMING_ARRAY_PB,
    MAKTAR_CRANE_PB,
])
ENDAKO = PlanetData("Endako", 3, [
    ENDAKO_CLANK_APARTMENT_SS,
    ENDAKO_CLANK_APARTMENT_GB,
    ENDAKO_RESCUE_CLANK_HELI,
    ENDAKO_RESCUE_CLANK_THRUSTER,
    ENDAKO_LEDGE_PB,
    ENDAKO_CRANE_PB,
    ENDAKO_CRANE_NT,
])
BARLOW = PlanetData("Barlow", 4, [
    BARLOW_INVENTOR,
    BARLOW_HOVERBIKE_RACE_TRANSMISSION,
    BARLOW_HOVERBIKE_RACE_PB,
    BARLOW_HOUND_CAVE_PB,
])
FELTZIN_SYSTEM = PlanetData("Feltzin System", 5, [
    FELTZIN_DEFEAT_THUG_SHIPS,
    FELTZIN_RACE_PB,
    FELTZIN_CARGO_BAY_NT,
])
NOTAK = PlanetData("Notak", 6, [
    NOTAK_TOP_PIER_TELESCREEN,
    NOTAK_WORKER_BOTS,
    NOTAK_BEHIND_BUILDING_PB,
    NOTAK_PROMENADE_SIGN_PB,
    NOTAK_TIMED_DYNAMO_PB,
    NOTAK_PROMENADE_END_NT,
])
SIBERIUS = PlanetData("Siberius", 7, [
    SIBERIUS_DEFEAT_THIEF,
    SIBERIUS_FLAMEBOT_LEDGE_PB,
    SIBERIUS_FENCED_AREA_PB,
])
TABORA = PlanetData("Tabora", 8, [
    TABORA_MEET_ANGELA,
    TABORA_UNDERGROUND_MINES_END,
    TABORA_UNDERGROUND_MINES_PB,
    TABORA_CANYON_GLIDE_PB,
    TABORA_NORTHEAST_DESERT_PB,
    TABORA_CANYON_GLIDE_PILLAR_NT,
])
DOBBO = PlanetData("Dobbo", 9, [
    DOBBO_DEFEAT_THUG_LEADER,
    DOBBO_FACILITY_TERMINAL,
    DOBBO_SPIDERBOT_ROOM_PB,
    DOBBO_FACILITY_GLIDE_PB,
    DOBBO_FACILITY_GLIDE_NT,
])
HRUGIS_CLOUD = PlanetData("Hrugis Cloud", 10, [
    HRUGIS_DESTROY_DEFENSES,
    HRUGIS_RACE_PB,
])
JOBA = PlanetData("Joba", 11, [
    JOBA_FIRST_HOVERBIKE_RACE,
    JOBA_SHADY_SALESMAN,
    JOBA_ARENA_BATTLE,
    JOBA_ARENA_CAGE_MATCH,
    JOBA_HIDDEN_CLIFF_PB,
    JOBA_LEVITATOR_TOWER_PB,
    JOBA_HOVERBIKE_RACE_SHORTCUT_NT,
    JOBA_TIMED_DYNAMO_NT,
])
TODANO = PlanetData("Todano", 12, [
    TODANO_SEARCH_ROCKET_SILO,
    TODANO_STUART_ZURGO_TRADE,
    TODANO_FACILITY_INTERIOR,
    TODANO_NEAR_STUART_ZURGO_PB,
    TODANO_END_TOUR_PB,
    TODANO_SPIDERBOT_CONVEYOR_PB,
    TODANO_ROCKET_SILO_NT,
])
BOLDAN = PlanetData("Boldan", 13, [
    BOLDAN_FIND_FIZZWIDGET,
    BOLDAN_SPIDERBOT_ALLEY_PB,
    BOLDAN_FLOATING_PLATFORM_PB,
    BOLDAN_UPPER_DOME_PB,
    BOLDAN_FOUNTAIN_NT,
])
ARANOS_PRISON = PlanetData("Aranos Prison", 14, [
    ARANOS_CONTROL_ROOM,
    ARANOS_PLUMBER,
    ARANOS_UNDER_SHIP_PB,
])
GORN = PlanetData("Gorn", 15, [
    GORN_DEFEAT_THUG_FLEET,
    GORN_RACE_PB,
])
SNIVELAK = PlanetData("Snivelak", 16, [
    SNIVELAK_RESCUE_ANGELA,
    SNIVELAK_DYNAMO_PLATFORMS_PB,
    SNIVELAK_SWINGSHOT_TOWER_NT,
])
SMOLG = PlanetData("Smolg", 17, [
    SMOLG_BALLOON_TRANSMISSION,
    SMOLG_DISTRIBUTION_FACILITY_END,
    SMOLG_MUTANT_CRAB,
    SMOLG_FLOATING_PLATFORM_PB,
    SMOLG_WAREHOUSE_PB,
])
DAMOSEL = PlanetData("Damosel", 18, [
    DAMOSEL_HYPNOTIST,
    DAMOSEL_TRAIN_RAILS,
    DAMOSEL_DEFEAT_MOTHERSHIP,
    DAMOSEL_FROZEN_FOUNTAIN_PB,
    DAMOSEL_PYRAMID_PB,
])
GRELBIN = PlanetData("Grelbin", 19, [
    GRELBIN_FIND_ANGELA,
    GRELBIN_MYSTIC_MORE_MOONSTONES,
    GRELBIN_ICE_PLAINS_PB,
    GRELBIN_UNDERWATER_TUNNEL_PB,
    GRELBIN_YETI_CAVE_PB,
])
YEEDIL = PlanetData("Yeedil", 20, [
    YEEDIL_DEFEAT_MUTATED_PROTOPET,
    YEEDIL_BRIDGE_GRINDRAIL_PB,
    YEEDIL_TRACTOR_PILLAR_PB,
])
DOBBO_ORBIT = PlanetData("Dobbo Orbit", 22)
DAMOSEL_ORBIT = PlanetData("Damosel Orbit", 23)
SHIP_SHACK = PlanetData("Ship Shack", 24)
WUPASH_NEBULA = PlanetData("Wupash Nebula", 25)
JAMMING_ARRAY = PlanetData("Jamming Array", 26)
INSOMNIAC_MUSEUM = PlanetData("Insomniac Museum", 30)

LOGIC_PLANETS = [
    OOZLA,
    MAKTAR_NEBULA,
    ENDAKO,
    BARLOW,
    FELTZIN_SYSTEM,
    NOTAK,
    SIBERIUS,
    TABORA,
    DOBBO,
    HRUGIS_CLOUD,
    JOBA,
    TODANO,
    BOLDAN,
    ARANOS_PRISON,
    GORN,
    SNIVELAK,
    SMOLG,
    DAMOSEL,
    GRELBIN,
    YEEDIL,
]

ALL_LOCATIONS: list[LocationData] = [
    location
    for locations in [planet.locations for planet in LOGIC_PLANETS]
    for location in locations
]
