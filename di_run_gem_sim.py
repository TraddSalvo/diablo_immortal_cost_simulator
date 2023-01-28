import pandas as pd
import random
import numpy as np
from math import trunc
import time
import warnings

warnings.filterwarnings("ignore")

# Meta data: Frags, min plat sell
Lookup_vendor = {"1_Berserkers_Eye_[*]": [1, 900],
                 "1_Caarsens_Invigoration_[*]": [1, 900],
                 "1_Chained_Death_[*]": [1, 900],
                 "1_Defiant_Soul_[*]": [1, 900],
                 "1_Everlasting_Torment_[*]": [1, 900],
                 "1_Freedom_and_Devotion_[*]": [1, 900],
                 "1_Mocking_Laughter_[*]": [1, 900],
                 "1_Nightmare_Wreath_[*]": [1, 900],
                 "1_Pain_of_Subjugation_[*]": [1, 900],
                 "1_Respite_Stone_[*]": [1, 900],
                 "1_Seleds_Weakening_[*]": [1, 900],
                 "1_Trickshot_Gem_[*]": [1, 900],
                 "1_Zod_Stone_[*]": [1, 900],
                 "1_Heartstone_[*]": [1, 900],
                 "1_Blessed_Pebble_[*]": [1, 900],
                 "2_Battleguard_[**]": [4, 3900],
                 "2_Bloody Reach_[**]": [4, 3900],
                 "2_Cutthroats_Grin_[**]": [4, 3900],
                 "2_Followers_Burden_[**]": [4, 3900],
                 "2_Lightning_Core_[**]": [4, 3900],
                 "2_Power_and_Command_[**]": [4, 3900],
                 "2_The_Hunger_[**]": [4, 3900],
                 "2_Unity_Crystal_[**]": [4, 3900],
                 "2_Kir_Sling_[**]": [4, 3900],
                 "2_Volatility_Shard_[**]": [4, 3900],
                 "2_The_Abiding_Curse_[**]": [4, 3900],
                 "502_Blessing_of_the_Worthy_[**---]": [32, 39000],
                 "502_Blood_Soaked_Jade_[**---]": [32, 64000],
                 "502_Bottled_Hope_[**---]": [32, 64000],
                 "502_Chip_of_Stoned_Flesh_[**---]": [32, 48000],
                 "502_Echoing_Shade_[**---]": [32, 60000],
                 "502_Howlers_Call_[**---]": [32, 39000],
                 "502_Phoenix_Ashes_[**---]": [32, 41000],
                 "502_Seeping_Bile_[**---]": [32, 64000],
                 "502_Zwensons_Haunting_[**---]": [32, 38000],
                 "502_Frozen_Heart_[**---]": [32, 39555],
                 "502_Hellfire_Fragment_[**---]": [32, 35000],
                 "502_Concentrated_Will_[**---]": [32, 29000],
                 "503_Blessing_of_the_Worthy_[***--]": [32, 65000],
                 "503_Blood_Soaked_Jade_[***--]": [32, 125000],
                 "503_Bottled_Hope_[***--]": [32, 75000],
                 "503_Chip_of_Stoned_Flesh_[***--]": [32, 54000],
                 "503_Echoing_Shade_[***--]": [32, 77000],
                 "503_Howlers_Call_[***--]": [32, 50000],
                 "503_Phoenix_Ashes_[***--]": [32, 58000],
                 "503_Seeping_Bile_[***--]": [32, 80000],
                 "503_Zwensons_Haunting_[***--]": [32, 40000],
                 "503_Frozen_Heart_[***--]": [32, 87000],
                 "503_Hellfire_Fragment_[***--]": [32, 35000],
                 "503_Concentrated_Will_[***--]": [32, 40000],
                 "504_Blessing_of_the_Worthy_[****-]": [32, 94000],
                 "504_Blood_Soaked_Jade_[****-]": [32, 320000],
                 "504_Bottled_Hope_[****-]": [32, 182000],
                 "504_Chip_of_Stoned_Flesh_[****-]": [32, 99000],
                 "504_Echoing_Shade_[****-]": [32, 160000],
                 "504_Howlers_Call_[****-]": [32, 120000],
                 "504_Phoenix_Ashes_[****-]": [32, 150000],
                 "504_Seeping_Bile_[****-]": [32, 320000],
                 "504_Zwensons_Haunting_[****-]": [32, 160000],
                 "504_Frozen_Heart_[****-]": [32, 150000],
                 "504_Hellfire_Fragment_[****-]": [32, 115000],
                 "504_Concentrated_Will_[****-]": [32, 90000],
                 "505_Blessing_of_the_Worthy_[*****]": [32, 450000],
                 "505_Blood_Soaked_Jade_[*****]": [32, 640000],
                 "505_Bottled_Hope_[*****]": [32, 640000],
                 "505_Chip_of_Stoned_Flesh_[*****]": [32, 340000],
                 "505_Echoing_Shade_[*****]": [32, 640000],
                 "505_Howlers_Call_[*****]": [32, 450000],
                 "505_Phoenix_Ashes_[*****]": [32, 450000],
                 "505_Seeping_Bile_[*****]": [32, 640000],
                 "505_Zwensons_Haunting_[*****]": [32, 340000],
                 "505_Frozen_Heart_[*****]": [32, 430000],
                 "505_Hellfire_Fragment_[*****]": [32, 340000],
                 "505_Concentrated_Will_[*****]": [32, 340000]}


# return the resonance value of the gem
def find_resonance(rank, gem_type):
    if gem_type == 'two_out_of_five':
        if rank == 'one':
            res = 30.00
        elif rank == 'two':
            res = 110.00
        elif rank == 'three':
            res = 190.00
        elif rank == 'four':
            res = 280.00
        elif rank == 'five':
            res = 370.00
        elif rank == 'six':
            res = 460.00
        elif rank == 'seven':
            res = 550.00
        elif rank == 'eight':
            res = 640.00
        elif rank == 'nine':
            res = 730.00
        else:
            res = 820.00
    elif gem_type == 'three_out_of_five':
        if rank == 'one':
            res = 60.00
        elif rank == 'two':
            res = 140.00
        elif rank == 'three':
            res = 230.00
        elif rank == 'four':
            res = 320.00
        elif rank == 'five':
            res = 410.00
        elif rank == 'six':
            res = 500.00
        elif rank == 'seven':
            res = 590.00
        elif rank == 'eight':
            res = 680.00
        elif rank == 'nine':
            res = 770.00
        else:
            res = 860.00
    elif gem_type == 'four_out_of_five':
        if rank == 'one':
            res = 90.00
        elif rank == 'two':
            res = 180.00
        elif rank == 'three':
            res = 270.00
        elif rank == 'four':
            res = 360.00
        elif rank == 'five':
            res = 450.00
        elif rank == 'six':
            res = 540.00
        elif rank == 'seven':
            res = 630.00
        elif rank == 'eight':
            res = 720.00
        elif rank == 'nine':
            res = 810.00
        else:
            res = 900.00
    elif gem_type == 'five_out_of_five':
        if rank == 'one':
            res = 100.00
        elif rank == 'two':
            res = 200.00
        elif rank == 'three':
            res = 300.00
        elif rank == 'four':
            res = 400.00
        elif rank == 'five':
            res = 500.00
        elif rank == 'six':
            res = 600.00
        elif rank == 'seven':
            res = 700.00
        elif rank == 'eight':
            res = 800.00
        elif rank == 'nine':
            res = 900.00
        else:
            res = 1000.00
    return (res)


def run_gem_sim_multi(money_spent,
                      simulations,
                      starting_frags,
                      starting_plat,
                      # gem one
                      Gem_one,
                      Gem_one_level_current,
                      Gem_one_type_current,
                      starting_copies_one,
                      # gem two
                      Gem_two,
                      Gem_two_level_current,
                      Gem_two_type_current,
                      starting_copies_two,
                      # gem three
                      Gem_three,
                      Gem_three_level_current,
                      Gem_three_type_current,
                      starting_copies_three,
                      # gem four
                      Gem_four,
                      Gem_four_level_current,
                      Gem_four_type_current,
                      starting_copies_four,
                      # gem five
                      Gem_five,
                      Gem_five_level_current,
                      Gem_five_type_current,
                      starting_copies_five,
                      # gem six
                      Gem_six,
                      Gem_six_level_current,
                      Gem_six_type_current,
                      starting_copies_six
                      ):
    import pandas as pd
    import random
    import numpy as np
    from math import trunc
    import time
    import warnings
    warnings.filterwarnings("ignore")

    ranking_lu = pd.DataFrame({'current_level': ['one', 'one', 'one', 'one', 'one', 'one', 'one', 'one', 'one', 'one',
                                                 'two', 'two', 'two', 'two', 'two', 'two', 'two', 'two', 'two', 'three',
                                                 'three', 'three', 'three', 'three', 'three', 'three', 'three', 'four',
                                                 'four', 'four', 'four', 'four', 'four', 'four', 'five', 'five', 'five',
                                                 'five', 'five', 'five', 'six', 'six', 'six', 'six', 'six', 'seven',
                                                 'seven', 'seven', 'seven', 'eight', 'eight', 'eight', 'nine', 'nine',
                                                 'ten'],
                               'rank_performed': ['1 to 1', '1 to 2', '1 to 3', '1 to 4', '1 to 5', '1 to 6', '1 to 7',
                                                  '1 to 8', '1 to 9', '1 to 10', '2 to 2', '2 to 3', '2 to 4', '2 to 5',
                                                  '2 to 6', '2 to 7', '2 to 8', '2 to 9', '2 to 10', '3 to 3', '3 to 4',
                                                  '3 to 5', '3 to 6', '3 to 7', '3 to 8', '3 to 9', '3 to 10', '4 to 4',
                                                  '4 to 5', '4 to 6', '4 to 7', '4 to 8', '4 to 9', '4 to 10', '5 to 5',
                                                  '5 to 6', '5 to 7', '5 to 8', '5 to 9', '5 to 10', '6 to 6', '6 to 7',
                                                  '6 to 8', '6 to 9', '6 to 10', '7 to 7', '7 to 8', '7 to 9',
                                                  '7 to 10', '8 to 8', '8 to 9', '8 to 10', '9 to 9', '9 to 10',
                                                  '10 to 10'],
                               'max_rank_achieved':
                                   ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                                    'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'three',
                                    'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'four', 'five', 'six',
                                    'seven', 'eight', 'nine', 'ten', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                                    'six', 'seven', 'eight', 'nine', 'ten', 'seven', 'eight', 'nine', 'ten', 'eight',
                                    'nine', 'ten', 'nine', 'ten', 'ten'],
                               'copies_needed': [0, 0, 1, 2, 7, 13, 25, 37, 55, 73, 0, 1, 2, 7, 13, 25, 37, 55, 73, 0,
                                                 1, 6, 12, 24, 36, 54, 72, 0, 5, 11, 23, 35, 53, 71, 0, 6, 18, 30, 48,
                                                 66, 0, 12, 24, 42, 60, 0, 12, 30, 48, 0, 18, 36, 0, 18, 0],
                               'frags_needed': [0, 50, 125, 225, 475, 850, 1575, 2300, 3375, 4450, 0, 75, 175, 425, 800,
                                                1525, 2250, 3325, 4400, 0, 100, 350, 725, 1450, 2175, 3250, 4325, 0,
                                                250, 625, 1350, 2075, 3150, 4225, 0, 375, 1100, 1825, 2900, 3975, 0,
                                                725, 1450, 2525, 3600, 0, 725, 1800, 2875, 0, 1075, 2150, 0, 1075, 0]})

    simulation_list = []

    price_bundle = 217.74

    number_bundles = 20
    x = 0

    for i in range(number_bundles):
        x = x + (price_bundle * 5)
        simulation_list.append(trunc(x))

    col = pd.Series(simulation_list).apply(format).to_list()
    summary_df = pd.DataFrame(columns=col, index=['min', '25%', '50%', '75%', 'max']).reset_index()

    frag_price = 900

    # RNG Params
    gems = ['one_star', 'two_star', 'five_two', 'five_three', 'five_four', 'five_five']
    gem_prob = [0.754, 0.201, 0.03375, 0.009, 0.0018, 0.00045]

    # Pity Params
    gems_pity = ['five_two', 'five_three', 'five_four', 'five_five']
    gem_prob_pity = [0.75, 0.20, 0.04, 0.01]

    one_star_gem_id = ["1_Berserkers_Eye_[*]",
                       "1_Caarsens_Invigoration_[*]",
                       "1_Chained_Death_[*]",
                       "1_Defiant_Soul_[*]",
                       "1_Everlasting_Torment_[*]",
                       "1_Freedom_and_Devotion_[*]",
                       "1_Mocking_Laughter_[*]",
                       "1_Nightmare_Wreath_[*]",
                       "1_Pain_of_Subjugation_[*]",
                       "1_Respite_Stone_[*]",
                       "1_Seleds_Weakening_[*]",
                       "1_Trickshot_Gem_[*]",
                       "1_Zod_Stone_[*]",
                       "1_Heartstone_[*]",
                       "1_Blessed_Pebble_[*]", ]

    two_star_gem_id = ["2_Battleguard_[**]",
                       "2_Bloody Reach_[**]",
                       "2_Cutthroats_Grin_[**]",
                       "2_Followers_Burden_[**]",
                       "2_Lightning_Core_[**]",
                       "2_Power_and_Command_[**]",
                       "2_The_Hunger_[**]",
                       "2_Unity_Crystal_[**]",
                       "2_Kir_Sling_[**]",
                       "2_Volatility_Shard_[**]",
                       "2_The_Abiding_Curse_[**]"]

    five_star_two_gem_id = ["502_Blessing_of_the_Worthy_[**---]",
                            "502_Blood_Soaked_Jade_[**---]",
                            "502_Bottled_Hope_[**---]",
                            "502_Chip_of_Stoned_Flesh_[**---]",
                            "502_Echoing_Shade_[**---]",
                            "502_Howlers_Call_[**---]",
                            "502_Phoenix_Ashes_[**---]",
                            "502_Seeping_Bile_[**---]",
                            "502_Zwensons_Haunting_[**---]",
                            "502_Frozen_Heart_[**---]",
                            "502_Hellfire_Fragment_[**---]",
                            "502_Concentrated_Will_[**---]"]

    five_star_three_gem_id = ["503_Blessing_of_the_Worthy_[***--]",
                              "503_Blood_Soaked_Jade_[***--]",
                              "503_Bottled_Hope_[***--]",
                              "503_Chip_of_Stoned_Flesh_[***--]",
                              "503_Echoing_Shade_[***--]",
                              "503_Howlers_Call_[***--]",
                              "503_Phoenix_Ashes_[***--]",
                              "503_Seeping_Bile_[***--]",
                              "503_Zwensons_Haunting_[***--]",
                              "503_Frozen_Heart_[***--]",
                              "503_Hellfire_Fragment_[***--]",
                              "503_Concentrated_Will_[***--]"]

    five_star_four_gem_id = ["504_Blessing_of_the_Worthy_[****-]",
                             "504_Blood_Soaked_Jade_[****-]",
                             "504_Bottled_Hope_[****-]",
                             "504_Chip_of_Stoned_Flesh_[****-]",
                             "504_Echoing_Shade_[****-]",
                             "504_Howlers_Call_[****-]",
                             "504_Phoenix_Ashes_[****-]",
                             "504_Seeping_Bile_[****-]",
                             "504_Zwensons_Haunting_[****-]",
                             "504_Frozen_Heart_[****-]",
                             "504_Hellfire_Fragment_[****-]",
                             "504_Concentrated_Will_[****-]"]

    five_star_five_gem_id = ["505_Blessing_of_the_Worthy_[*****]",
                             "505_Blood_Soaked_Jade_[*****]",
                             "505_Bottled_Hope_[*****]",
                             "505_Chip_of_Stoned_Flesh_[*****]",
                             "505_Echoing_Shade_[*****]",
                             "505_Howlers_Call_[*****]",
                             "505_Phoenix_Ashes_[*****]",
                             "505_Seeping_Bile_[*****]",
                             "505_Zwensons_Haunting_[*****]",
                             "505_Frozen_Heart_[*****]",
                             "505_Hellfire_Fragment_[*****]",
                             "505_Concentrated_Will_[*****]"]

    # Meta data: Frags, min plat sell
    Lookup_vendor = {"1_Berserkers_Eye_[*]": [1, 900],
                     "1_Caarsens_Invigoration_[*]": [1, 900],
                     "1_Chained_Death_[*]": [1, 900],
                     "1_Defiant_Soul_[*]": [1, 900],
                     "1_Everlasting_Torment_[*]": [1, 900],
                     "1_Freedom_and_Devotion_[*]": [1, 900],
                     "1_Mocking_Laughter_[*]": [1, 900],
                     "1_Nightmare_Wreath_[*]": [1, 900],
                     "1_Pain_of_Subjugation_[*]": [1, 900],
                     "1_Respite_Stone_[*]": [1, 900],
                     "1_Seleds_Weakening_[*]": [1, 900],
                     "1_Trickshot_Gem_[*]": [1, 900],
                     "1_Zod_Stone_[*]": [1, 900],
                     "1_Heartstone_[*]": [1, 900],
                     "1_Blessed_Pebble_[*]": [1, 900],
                     "2_Battleguard_[**]": [4, 3900],
                     "2_Bloody Reach_[**]": [4, 3900],
                     "2_Cutthroats_Grin_[**]": [4, 3900],
                     "2_Followers_Burden_[**]": [4, 3900],
                     "2_Lightning_Core_[**]": [4, 3900],
                     "2_Power_and_Command_[**]": [4, 3900],
                     "2_The_Hunger_[**]": [4, 3900],
                     "2_Unity_Crystal_[**]": [4, 3900],
                     "2_Kir_Sling_[**]": [4, 3900],
                     "2_Volatility_Shard_[**]": [4, 3900],
                     "2_The_Abiding_Curse_[**]": [4, 3900],
                     "502_Blessing_of_the_Worthy_[**---]": [32, 39000],
                     "502_Blood_Soaked_Jade_[**---]": [32, 64000],
                     "502_Bottled_Hope_[**---]": [32, 64000],
                     "502_Chip_of_Stoned_Flesh_[**---]": [32, 48000],
                     "502_Echoing_Shade_[**---]": [32, 60000],
                     "502_Howlers_Call_[**---]": [32, 39000],
                     "502_Phoenix_Ashes_[**---]": [32, 41000],
                     "502_Seeping_Bile_[**---]": [32, 64000],
                     "502_Zwensons_Haunting_[**---]": [32, 38000],
                     "502_Frozen_Heart_[**---]": [32, 39555],
                     "502_Hellfire_Fragment_[**---]": [32, 35000],
                     "502_Concentrated_Will_[**---]": [32, 29000],
                     "503_Blessing_of_the_Worthy_[***--]": [32, 65000],
                     "503_Blood_Soaked_Jade_[***--]": [32, 125000],
                     "503_Bottled_Hope_[***--]": [32, 75000],
                     "503_Chip_of_Stoned_Flesh_[***--]": [32, 54000],
                     "503_Echoing_Shade_[***--]": [32, 77000],
                     "503_Howlers_Call_[***--]": [32, 50000],
                     "503_Phoenix_Ashes_[***--]": [32, 58000],
                     "503_Seeping_Bile_[***--]": [32, 80000],
                     "503_Zwensons_Haunting_[***--]": [32, 40000],
                     "503_Frozen_Heart_[***--]": [32, 87000],
                     "503_Hellfire_Fragment_[***--]": [32, 35000],
                     "503_Concentrated_Will_[***--]": [32, 40000],
                     "504_Blessing_of_the_Worthy_[****-]": [32, 94000],
                     "504_Blood_Soaked_Jade_[****-]": [32, 320000],
                     "504_Bottled_Hope_[****-]": [32, 182000],
                     "504_Chip_of_Stoned_Flesh_[****-]": [32, 99000],
                     "504_Echoing_Shade_[****-]": [32, 160000],
                     "504_Howlers_Call_[****-]": [32, 120000],
                     "504_Phoenix_Ashes_[****-]": [32, 150000],
                     "504_Seeping_Bile_[****-]": [32, 320000],
                     "504_Zwensons_Haunting_[****-]": [32, 160000],
                     "504_Frozen_Heart_[****-]": [32, 150000],
                     "504_Hellfire_Fragment_[****-]": [32, 115000],
                     "504_Concentrated_Will_[****-]": [32, 90000],
                     "505_Blessing_of_the_Worthy_[*****]": [32, 450000],
                     "505_Blood_Soaked_Jade_[*****]": [32, 640000],
                     "505_Bottled_Hope_[*****]": [32, 640000],
                     "505_Chip_of_Stoned_Flesh_[*****]": [32, 340000],
                     "505_Echoing_Shade_[*****]": [32, 640000],
                     "505_Howlers_Call_[*****]": [32, 450000],
                     "505_Phoenix_Ashes_[*****]": [32, 450000],
                     "505_Seeping_Bile_[*****]": [32, 640000],
                     "505_Zwensons_Haunting_[*****]": [32, 340000],
                     "505_Frozen_Heart_[*****]": [32, 430000],
                     "505_Hellfire_Fragment_[*****]": [32, 340000],
                     "505_Concentrated_Will_[*****]": [32, 340000]}
    lu = pd.DataFrame(Lookup_vendor).T.reset_index()
    lu.columns = ["gem", "frags", "sell_price"]

    # Pity Roller
    def roll_pity():
        X = random.choices(gems_pity, weights=gem_prob_pity)[0]
        if X == 'five_two':
            return (random.choices(five_star_two_gem_id)[0])
        elif X == 'five_three':
            return (random.choices(five_star_three_gem_id)[0])
        elif X == 'five_four':
            return (random.choices(five_star_four_gem_id)[0])
        elif X == 'five_five':
            return (random.choices(five_star_five_gem_id)[0])
        else:
            return ("error")

    # Gem Roller
    def roll_gem():
        X = random.choices(gems, weights=gem_prob)[0]
        if X == 'one_star':
            return (random.choices(one_star_gem_id)[0])
        elif X == 'two_star':
            return (random.choices(two_star_gem_id)[0])
        elif X == 'five_two':
            return (random.choices(five_star_two_gem_id)[0])
        elif X == 'five_three':
            return (random.choices(five_star_three_gem_id)[0])
        elif X == 'five_four':
            return (random.choices(five_star_four_gem_id)[0])
        elif X == 'five_five':
            return (random.choices(five_star_five_gem_id)[0])
        else:
            return ("error")

    # sinulate roles based on number of crests with pity
    def spend_money(runs=25):
        counter = 0
        list_0 = []
        for _ in range(runs):
            x_ = roll_gem()
            if "five" in x_:
                counter = 1
                list_0.append(x_)
            elif counter >= 50:
                counter = 1
                Y_ = roll_pity()
                list_0.append(Y_)
            else:
                counter += 1
                list_0.append(x_)

        merge_test = pd.DataFrame(list_0)
        merge_test.columns = ["gem"]

        return (merge_test.merge(lu, left_on='gem', right_on='gem', how="left"))

    # identify highest gem level
    def identify_max_gem1_level(roll_info_df, current_gem_type_1):
        if current_gem_type_1 == 'five_out_of_five':
            return ('five_out_of_five')
        elif roll_info_df['gem'].str.contains('505').any() == True:
            return ('five_out_of_five')
        elif roll_info_df['gem'].str.contains('504').any() == True:
            return ('four_out_of_five')
        elif current_gem_type_1 == 'four_out_of_five':
            return ('four_out_of_five')
        elif roll_info_df['gem'].str.contains('503').any() == True:
            return ('three_out_of_five')
        elif current_gem_type_1 == 'three_out_of_five':
            return ('three_out_of_five')
        elif roll_info_df['gem'].str.contains('502').any() == True:
            return ('two_out_of_five')
        elif current_gem_type_1 == 'two_out_of_five':
            return ('two_out_of_five')
        else:
            return ('error')

    # return the resonance value of the gem
    def find_resonance(rank, gem_type):
        if gem_type == 'two_out_of_five':
            if rank == 'one':
                res = 30.00
            elif rank == 'two':
                res = 110.00
            elif rank == 'three':
                res = 190.00
            elif rank == 'four':
                res = 280.00
            elif rank == 'five':
                res = 370.00
            elif rank == 'six':
                res = 460.00
            elif rank == 'seven':
                res = 550.00
            elif rank == 'eight':
                res = 640.00
            elif rank == 'nine':
                res = 730.00
            else:
                res = 820.00
        elif gem_type == 'three_out_of_five':
            if rank == 'one':
                res = 60.00
            elif rank == 'two':
                res = 140.00
            elif rank == 'three':
                res = 230.00
            elif rank == 'four':
                res = 320.00
            elif rank == 'five':
                res = 410.00
            elif rank == 'six':
                res = 500.00
            elif rank == 'seven':
                res = 590.00
            elif rank == 'eight':
                res = 680.00
            elif rank == 'nine':
                res = 770.00
            else:
                res = 860.00
        elif gem_type == 'four_out_of_five':
            if rank == 'one':
                res = 90.00
            elif rank == 'two':
                res = 180.00
            elif rank == 'three':
                res = 270.00
            elif rank == 'four':
                res = 360.00
            elif rank == 'five':
                res = 450.00
            elif rank == 'six':
                res = 540.00
            elif rank == 'seven':
                res = 630.00
            elif rank == 'eight':
                res = 720.00
            elif rank == 'nine':
                res = 810.00
            else:
                res = 900.00
        elif gem_type == 'five_out_of_five':
            if rank == 'one':
                res = 100.00
            elif rank == 'two':
                res = 200.00
            elif rank == 'three':
                res = 300.00
            elif rank == 'four':
                res = 400.00
            elif rank == 'five':
                res = 500.00
            elif rank == 'six':
                res = 600.00
            elif rank == 'seven':
                res = 700.00
            elif rank == 'eight':
                res = 800.00
            elif rank == 'nine':
                res = 900.00
            else:
                res = 1000.00
        return (res)

    # Get plat and frags

    def calculate_usable_materials(data, Gem_one, Gem_two, Gem_three, Gem_four, Gem_five, Gem_six, gems_to_sell):

        calc_variables = data[
            data['gem'].str.contains('|'.join([Gem_one, Gem_two, Gem_three, Gem_four, Gem_five, Gem_six]),
                                     case=False) == False]

        # remove gems to sell
        usable_plat = calc_variables[calc_variables['gem'].isin(gems_to_sell) == True].sell_price.sum() * 0.75
        usable_frags = calc_variables[calc_variables['gem'].isin(gems_to_sell) == False].frags.sum()

        return ({'platinum': usable_plat,
                 'frags': usable_frags})

    def spend_money_for_bundles(moniez):
        return (trunc(trunc(moniez / 200) * 15000 / 160))

    def find_market_price(gem):
        plat_price = lu[lu['gem'].str.contains('502')]
        plat_price = plat_price[plat_price['gem'].str.contains(gem, case=False)].iloc[0, 2]
        return (plat_price)

    def optimize_resonance_new(data_Set, Gem_name, Gem_level_current, Gem_type_current, frag_price, extra_copies, frags,
                               platnum):

        gem_price_ = find_market_price(Gem_name)
        copies = data_Set[data_Set['gem'].str.contains(Gem_name, case=False)].count()[0] + extra_copies

        breakPoints = ranking_lu.loc[ranking_lu.current_level == Gem_level_current]
        breakPoints['plat_left'] = breakPoints.apply(
            lambda x: optimize_platinum(gem_price_, frag_price, x.copies_needed, x.frags_needed, copies, frags,
                                        platnum), axis=1)

        # calculate max rank achieveable
        max_rank = breakPoints[breakPoints.plat_left >= 0].iloc[-1, :]['max_rank_achieved']

        # calculate plat leftover
        plat_leftover = breakPoints[breakPoints.plat_left >= 0].iloc[-1, :]['plat_left']

        # calculate frags used
        frags_used_ = breakPoints[breakPoints.plat_left >= 0].iloc[-1, :]['frags_needed']

        # calculate frags leftover
        frags_leftover = frags - frags_used_

        # record meta data for QA
        meta_details = breakPoints[breakPoints.plat_left >= 0].iloc[-1, :]

        # Identify maximum gems found in dataset
        max_gem_type_found = identify_max_gem1_level(data_Set[data_Set['gem'].str.contains(Gem_name, case=False)],
                                                     Gem_type_current)

        # Calculate resonance
        base_resonance = find_resonance(Gem_level_current, Gem_type_current)
        total_resonance = find_resonance(max_rank, max_gem_type_found)

        ret = {'meta_data': meta_details,
               'total_resonance': total_resonance,
               'plat_leftover': plat_leftover,
               'frags_leftover': frags_leftover.clip(min=0)}

        return (ret)

    # Allocation breakpoint combination of frags and copies
    # first either buying or selling the optimal copies needed
    # next using resulting plat to purchase frags needed if possible
    # returns negative if cannot afford

    def optimize_platinum(gem_price, frag_price, copy_needs, frags_needs, current_copies, current_frags,
                          current_platinum):

        remaining_copy = current_copies - copy_needs
        remaining_frag = current_frags - frags_needs

        if remaining_copy < 0:
            platnum_2 = (remaining_copy * gem_price) + current_platinum
        else:
            platnum_2 = current_platinum + (remaining_copy * gem_price)

        if remaining_frag < 0:
            platnum_3 = (remaining_frag * frag_price) + platnum_2
        else:
            platnum_3 = platnum_2

        return (platnum_3)

    fstar = lu[lu['gem'].str.contains('|'.join('50'), case=False) == True]
    sell_list = fstar[fstar['gem'].str.contains('|'.join([Gem_one, Gem_two, Gem_three, Gem_four, Gem_five, Gem_six]),
                                                case=False) == False]
    Gems_to_sell = sell_list.gem.to_list()

    # Random gem optimize order
    gem_setlist_one = (Gem_one, Gem_one_level_current, Gem_one_type_current, frag_price, starting_copies_one)
    gem_setlist_two = (Gem_two, Gem_two_level_current, Gem_two_type_current, frag_price, starting_copies_two)
    gem_setlist_three = (Gem_three, Gem_three_level_current, Gem_three_type_current, frag_price, starting_copies_three)
    gem_setlist_four = (Gem_four, Gem_four_level_current, Gem_four_type_current, frag_price, starting_copies_four)
    gem_setlist_five = (Gem_five, Gem_five_level_current, Gem_five_type_current, frag_price, starting_copies_five)
    gem_setlist_six = (Gem_six, Gem_six_level_current, Gem_six_type_current, frag_price, starting_copies_six)

    # List of the list
    gem_grouplist = [gem_setlist_one, gem_setlist_two, gem_setlist_three, gem_setlist_four, gem_setlist_five,
                     gem_setlist_six]

    list_test = []

    total_resonance = []
    for i in range(simulations):
        dataset = spend_money(spend_money_for_bundles(money_spent))

        # randomize gems
        random.shuffle(gem_grouplist)

        plat_000 = \
        calculate_usable_materials(dataset, Gem_one, Gem_two, Gem_three, Gem_four, Gem_five, Gem_six, Gems_to_sell)[
            'platinum'] + starting_plat
        frags_000 = \
        calculate_usable_materials(dataset, Gem_one, Gem_two, Gem_three, Gem_four, Gem_five, Gem_six, Gems_to_sell)[
            'frags'] + starting_frags

        # gem one
        gem_one_simulation = optimize_resonance_new(dataset,
                                                    *gem_grouplist[0],
                                                    frags=frags_000,
                                                    platnum=plat_000)

        # gem two
        gem_two_simulation = optimize_resonance_new(dataset,
                                                    *gem_grouplist[1],
                                                    frags=gem_one_simulation['frags_leftover'],
                                                    platnum=gem_one_simulation['plat_leftover'])

        # gem three
        gem_three_simulation = optimize_resonance_new(dataset,
                                                      *gem_grouplist[2],
                                                      frags=gem_two_simulation['frags_leftover'],
                                                      platnum=gem_two_simulation['plat_leftover'])

        # gem four
        gem_four_simulation = optimize_resonance_new(dataset,
                                                     *gem_grouplist[3],
                                                     frags=gem_three_simulation['frags_leftover'],
                                                     platnum=gem_three_simulation['plat_leftover'])

        # gem five
        gem_five_simulation = optimize_resonance_new(dataset,
                                                     *gem_grouplist[4],
                                                     frags=gem_four_simulation['frags_leftover'],
                                                     platnum=gem_four_simulation['plat_leftover'])

        # gem six
        gem_six_simulation = optimize_resonance_new(dataset,
                                                    *gem_grouplist[5],
                                                    frags=gem_five_simulation['frags_leftover'],
                                                    platnum=gem_five_simulation['plat_leftover'])

        totalres = gem_one_simulation['total_resonance'] + gem_two_simulation['total_resonance'] + \
                   gem_three_simulation['total_resonance'] + gem_four_simulation['total_resonance'] + \
                   gem_five_simulation['total_resonance'] + gem_six_simulation['total_resonance']

        list_test.append(totalres)
    sim_res = np.array(list_test)
    return (sim_res)