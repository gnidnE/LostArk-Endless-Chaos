"""
    Make sure you have configed abilities for your specific class and spell position:
    key: keybind of the spell
    abilityType: do not change for now
    hold: if the spell is a hold spell, I DONT RECOMMENDED you to utilize hold spells
    holdTime: hold for x amount of milliseconds
    cast: if the spell is a cast spell
    castTime: cast time in milliseconds
    position: DO NOT CHANGE, they are fixed by HUD Size and Resolution
    directional: if the spell needs to be pointed at a direction where mobs are at

    My recommendations:
    Go to Trixion
    Find the spells/tripod combinations which does the LARGEST AoE around your character
    Try to avoid spells that moves your character a lot
    For instant spells that have long animations, Change the spell to cast mode and give it a proper cast time in milliseconds
    Trial and Error, until it works nicely
    Ideally how fast your chaos run should be:
    Floor 2 clear time should be around 100 - 160 seconds
    Floor 3 clear time could be anywhere around 200 - 300 seconds
"""
abilities = {
    "sorceress": [
        {
            "key": "q",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 738, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "w",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 777, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "e",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 816, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "r",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 855, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "a",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 759, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "s",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 797, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "d",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 835, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "f",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 873, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "v",
            "abilityType": "awakening",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 691, "top": 894, "width": 19, "height": 11},
            "directional": False,
        },
        {
            "key": "z",
            "abilityType": "specialty1",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 895, "top": 839, "width": 13, "height": 12},
            "directional": False,
        },
    ],
    "arcana": [
        {
            "key": "q",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 738, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "w",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": True,
            "castTime": 500,
            "position": {"left": 777, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "e",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": True,
            "castTime": 300,
            "position": {"left": 816, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "r",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": True,
            "castTime": 2500,
            "position": {"left": 855, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "a",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": True,
            "castTime": 300,
            "position": {"left": 759, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "s",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": True,
            "castTime": 500,
            "position": {"left": 797, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "d",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": True,
            "castTime": 500,
            "position": {"left": 835, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "f",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 873, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "v",
            "abilityType": "awakening",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 691, "top": 894, "width": 19, "height": 11},
            "directional": False,
        },
        {
            "key": "z",
            "abilityType": "specialty1",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 895, "top": 839, "width": 13, "height": 12},
            "directional": False,
        },
    ],
    "artillerist": [
        {
            "key": "q",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 738, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "w",
            "abilityType": "normal",
            "hold": True,
            "holdTime": 2000,
            "cast": False,
            "castTime": None,
            "position": {"left": 777, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "e",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 816, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "r",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 855, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "a",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": False,
            "position": {"left": 759, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "s",
            "abilityType": "normal",
            "hold": True,
            "holdTime": 1500,
            "cast": False,
            "castTime": None,
            "position": {"left": 797, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "d",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 835, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "f",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 873, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "v",
            "abilityType": "awakening",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 691, "top": 894, "width": 19, "height": 11},
            "directional": True,
        },

    ],
    "bard": [
        {
            "key": "q",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 738, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "w",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": True,
            "castTime": 1000,
            "position": {"left": 777, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "e",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": True,
            "castTime": 1000,
            "position": {"left": 816, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "r",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 855, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "a",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 759, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "s",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 797, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "d",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": True,
            "castTime": 1800,
            "position": {"left": 835, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "f",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 873, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "v",
            "abilityType": "awakening",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 691, "top": 894, "width": 19, "height": 11},
            "directional": False,
        },
        {
            "key": "z",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 895, "top": 839, "width": 13, "height": 12},
            "directional": False,

        },
    ],
    "reaper": [
        {
            "key": "q",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 738, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "w",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 777, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "e",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 816, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "r",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 855, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "a",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": False,
            "position": {"left": 759, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "s",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 797, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "d",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 835, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "f",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 873, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "v",
            "abilityType": "awakening",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 691, "top": 894, "width": 19, "height": 11},
            "directional": True,
        },

    ],
    "machinist": [
        {
            "key": "q",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 738, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "w",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 777, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "e",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 816, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "r",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 855, "top": 869, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "a",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": False,
            "position": {"left": 759, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "s",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 797, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "d",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 835, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "f",
            "abilityType": "normal",
            "hold": True,
            "holdTime": 3000,
            "cast": False,
            "castTime": None,
            "position": {"left": 873, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "v",
            "abilityType": "awakening",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 691, "top": 894, "width": 19, "height": 11},
            "directional": False,
        },
    ],
    "glavier": [
        {
            "key": "q",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 738, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "w",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 777, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "e",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 816, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "r",
            "abilityType": "normal",
            "hold": True,
            "holdTime": 2000,
            "cast": False,
            "castTime": None,
            "position": {"left": 855, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "a",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": False,
            "position": {"left": 759, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "s",
            "abilityType": "normal",
            "hold": True,
            "holdTime": 1500,
            "cast": False,
            "castTime": None,
            "position": {"left": 797, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "d",
            "abilityType": "normal",
            "hold": True,
            "holdTime": 2500,
            "cast": False,
            "castTime": None,
            "position": {"left": 835, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "f",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 873, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "v",
            "abilityType": "awakening",
            "hold": True,
            "holdTime": 2500,
            "cast": False,
            "castTime": None,
            "position": {"left": 691, "top": 894, "width": 19, "height": 11},
            "directional": True,
        },
    ],
    "scrapper": [
        {
            "key": "q",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 738, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "w",
            "abilityType": "normal",
            "hold": True,
            "holdTime": 2000,
            "cast": False,
            "castTime": None,
            "position": {"left": 777, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "e",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 816, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "r",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 855, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "a",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": False,
            "position": {"left": 759, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "s",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 797, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "d",
            "abilityType": "normal",
            "hold": True,
            "holdTime": 2000,
            "cast": False,
            "castTime": None,
            "position": {"left": 835, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "f",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 873, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "v",
            "abilityType": "awakening",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 691, "top": 894, "width": 19, "height": 11},
            "directional": True,
        },
    ],
    "shadowhunter": [
        {
            "key": "q",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 738, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "w",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 777, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "e",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 816, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "r",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 855, "top": 869, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "a",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": False,
            "position": {"left": 759, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "s",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 797, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "d",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 835, "top": 907, "width": 15, "height": 15},
            "directional": False,
        },
        {
            "key": "f",
            "abilityType": "normal",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 873, "top": 907, "width": 15, "height": 15},
            "directional": True,
        },
        {
            "key": "v",
            "abilityType": "awakening",
            "hold": False,
            "holdTime": None,
            "cast": False,
            "castTime": None,
            "position": {"left": 691, "top": 894, "width": 19, "height": 11},
            "directional": True,
        },
    ],
}