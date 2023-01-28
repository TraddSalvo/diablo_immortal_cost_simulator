import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import trunc
import plotly.express as px

import werkzeug
from werkzeug.debug.tbtools import DebugTraceback

werkzeug.debug.tbtools.get_current_traceback = DebugTraceback

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import dash
from dash import dash_table as dt
from dash import dcc
from dash import html
from dash import Input
from dash import Output
from dash import State
from multiprocess import Pool
import time
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

pd.options.mode.chained_assignment = None

from di_run_gem_sim import *


# New stuff
def format(x):
    return "${:.1f}K".format(x / 1000)


def run_multiprocess(simulations,
                     num_bundles,
                     starting_frags,
                     starting_plat,
                     Gem_one,
                     Gem_one_level_current,
                     Gem_one_type_current,
                     starting_copies_one,
                     Gem_two,
                     Gem_two_level_current,
                     Gem_two_type_current,
                     starting_copies_two,
                     Gem_three,
                     Gem_three_level_current,
                     Gem_three_type_current,
                     starting_copies_three,
                     Gem_four,
                     Gem_four_level_current,
                     Gem_four_type_current,
                     starting_copies_four,
                     Gem_five,
                     Gem_five_level_current,
                     Gem_five_type_current,
                     starting_copies_five,
                     Gem_six,
                     Gem_six_level_current,
                     Gem_six_type_current,
                     starting_copies_six):
    lu = pd.DataFrame(Lookup_vendor).T.reset_index()
    lu.columns = ["gem", "frags", "sell_price"]

    from multiprocess import Pool

    price_bundle = 217.74
    chunk_price = trunc(price_bundle * num_bundles)

    money_spent1 = chunk_price * 1
    money_spent2 = chunk_price * 2
    money_spent3 = chunk_price * 3
    money_spent4 = chunk_price * 4
    money_spent5 = chunk_price * 5
    money_spent6 = chunk_price * 6
    money_spent7 = chunk_price * 7
    money_spent8 = chunk_price * 8
    money_spent9 = chunk_price * 9
    money_spent10 = chunk_price * 10

    task1 = (
    money_spent1, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)
    task2 = (
    money_spent2, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)
    task3 = (
    money_spent3, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)
    task4 = (
    money_spent4, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)
    task5 = (
    money_spent5, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)
    task6 = (
    money_spent6, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)
    task7 = (
    money_spent7, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)
    task8 = (
    money_spent8, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)
    task9 = (
    money_spent9, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)
    task10 = (
    money_spent10, simulations, starting_frags, starting_plat, Gem_one, Gem_one_level_current, Gem_one_type_current,
    starting_copies_one, Gem_two, Gem_two_level_current, Gem_two_type_current, starting_copies_two, Gem_three,
    Gem_three_level_current, Gem_three_type_current, starting_copies_three, Gem_four, Gem_four_level_current,
    Gem_four_type_current, starting_copies_four, Gem_five, Gem_five_level_current, Gem_five_type_current,
    starting_copies_five, Gem_six, Gem_six_level_current, Gem_six_type_current, starting_copies_six)

    mult_col = [money_spent1, money_spent2, money_spent3, money_spent4, money_spent5, money_spent6, money_spent7,
                money_spent8, money_spent9, money_spent10]

    parm_list = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]

    if __name__ == '__main__':
        with Pool() as p:
            results = p.starmap(run_gem_sim_multi, parm_list)

            p.close()
            p.join()

    multi_res = pd.DataFrame(results).T
    multi_res.columns = mult_col
    return multi_res


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])


# Create server variable with Flask server object
server = app.server

app.layout = html.Div([
    html.H5("The Lord of Greed Presents:", style={"color": "red"}),
    html.H1("DIABLO IMMORTAL COST SIMULATOR"),
    html.Div(children=[
        html.Div(children=[
            html.H4("Gem One"),
            # gem one dropdown
            html.Label('Select Gem'),
            html.Div(
                dcc.Dropdown(['Blood_Soaked_Jade',
                              'Bottled_Hope',
                              'Howlers_Call',
                              'Blessing_of_the_Worthy',
                              'Frozen_Heart',
                              'Zwensons_Haunting',
                              'Seeping_Bile',
                              'Phoenix_Ashes',
                              'Chip_of_Stoned_Flesh',
                              'Hellfire_Fragment',
                              'Echoing_Shade',
                              'Concentrated_Will'],
                             'Blood_Soaked_Jade',
                             id='gem1_select'),
                className="dash-bootstrap"),

            # Gem one rank dropdown
            html.Br(),
            html.Label('Select Rank'),
            dcc.Dropdown(['one',
                          'two',
                          'three',
                          'four',
                          'five',
                          'six',
                          'seven',
                          'eight',
                          'nine',
                          'ten'],
                         'one',
                         id='gem1_rank'),

            # Gem star count dropdown
            html.Br(),
            html.Label('Select Stars'),
            dcc.Dropdown(['two_out_of_five',
                          'three_out_of_five',
                          'four_out_of_five',
                          'five_out_of_five'],
                         'two_out_of_five',
                         id='gem1_stars'),

            # Gem starting copies
            html.Br(),
            html.Label('Starting copies'),
            dbc.Input(id="start_copies_input_one",
                      value=0,
                      type='number'),

        ], style={"border": "2px red solid", "border-radius": "5px", 'margin': '5px', 'padding': 10, 'flex': 1}),

        html.Div(children=[
            html.H4("Gem Two"),
            # gem two dropdown
            html.Label('Select Gem'),
            html.Div(
                dcc.Dropdown(['Blood_Soaked_Jade',
                              'Bottled_Hope',
                              'Howlers_Call',
                              'Blessing_of_the_Worthy',
                              'Frozen_Heart',
                              'Zwensons_Haunting',
                              'Seeping_Bile',
                              'Phoenix_Ashes',
                              'Chip_of_Stoned_Flesh',
                              'Hellfire_Fragment',
                              'Echoing_Shade',
                              'Concentrated_Will'],
                             'Seeping_Bile',
                             id='gem2_select'),
                className="dash-bootstrap"),

            # Gem two rank dropdown
            html.Br(),
            html.Label('Select Rank'),
            dcc.Dropdown(['one',
                          'two',
                          'three',
                          'four',
                          'five',
                          'six',
                          'seven',
                          'eight',
                          'nine',
                          'ten'],
                         'one',
                         id='gem2_rank'),

            # Gem star count dropdown
            html.Br(),
            html.Label('Select Stars'),
            dcc.Dropdown(['two_out_of_five',
                          'three_out_of_five',
                          'four_out_of_five',
                          'five_out_of_five'],
                         'two_out_of_five',
                         id='gem2_stars'),

            # Gem starting copies
            html.Br(),
            html.Label('Starting copies'),
            dbc.Input(id="start_copies_input_two",
                      value=0,
                      type='number'),

        ], style={"border": "2px red solid", "border-radius": "5px", 'margin': '5px', 'padding': 10, 'flex': 1}),

        html.Div(children=[
            html.H4("Gem Three"),
            # gem three dropdown
            html.Label('Select Gem'),
            html.Div(
                dcc.Dropdown(['Blood_Soaked_Jade',
                              'Bottled_Hope',
                              'Howlers_Call',
                              'Blessing_of_the_Worthy',
                              'Frozen_Heart',
                              'Zwensons_Haunting',
                              'Seeping_Bile',
                              'Phoenix_Ashes',
                              'Chip_of_Stoned_Flesh',
                              'Hellfire_Fragment',
                              'Echoing_Shade',
                              'Concentrated_Will'],
                             'Howlers_Call',
                             id='gem3_select'),
                className="dash-bootstrap"),

            # Gem one rank dropdown
            html.Br(),
            html.Label('Select Rank'),
            dcc.Dropdown(['one',
                          'two',
                          'three',
                          'four',
                          'five',
                          'six',
                          'seven',
                          'eight',
                          'nine',
                          'ten'],
                         'one',
                         id='gem3_rank'),

            # Gem star count dropdown
            html.Br(),
            html.Label('Select Stars'),
            dcc.Dropdown(['two_out_of_five',
                          'three_out_of_five',
                          'four_out_of_five',
                          'five_out_of_five'],
                         'two_out_of_five',
                         id='gem3_stars'),

            # Gem starting copies
            html.Br(),
            html.Label('Starting copies'),
            dbc.Input(id="start_copies_input_three",
                      value=0,
                      type='number'),

        ], style={"border": "2px red solid", "border-radius": "5px", 'margin': '5px', 'padding': 10, 'flex': 1}),

        html.Div(children=[
            html.H4("Gem Four"),
            # gem four dropdown
            html.Label('Select Gem'),
            html.Div(
                dcc.Dropdown(['Blood_Soaked_Jade',
                              'Bottled_Hope',
                              'Howlers_Call',
                              'Blessing_of_the_Worthy',
                              'Frozen_Heart',
                              'Zwensons_Haunting',
                              'Seeping_Bile',
                              'Phoenix_Ashes',
                              'Chip_of_Stoned_Flesh',
                              'Hellfire_Fragment',
                              'Echoing_Shade',
                              'Concentrated_Will'],
                             'Zwensons_Haunting',
                             id='gem4_select'),
                className="dash-bootstrap"),

            # Gem four rank dropdown
            html.Br(),
            html.Label('Select Rank'),
            dcc.Dropdown(['one',
                          'two',
                          'three',
                          'four',
                          'five',
                          'six',
                          'seven',
                          'eight',
                          'nine',
                          'ten'],
                         'one',
                         id='gem4_rank'),

            # Gem four count dropdown
            html.Br(),
            html.Label('Select Stars'),
            dcc.Dropdown(['two_out_of_five',
                          'three_out_of_five',
                          'four_out_of_five',
                          'five_out_of_five'],
                         'two_out_of_five',
                         id='gem4_stars'),

            # Gem starting copies
            html.Br(),
            html.Label('Starting copies'),
            dbc.Input(id="start_copies_input_four",
                      value=0,
                      type='number'),

        ], style={"border": "2px red solid", "border-radius": "5px", 'margin': '5px', 'padding': 10, 'flex': 1}),

        html.Div(children=[
            html.H4("Gem Five"),
            # gem five dropdown
            html.Label('Select Gem'),
            html.Div(
                dcc.Dropdown(['Blood_Soaked_Jade',
                              'Bottled_Hope',
                              'Howlers_Call',
                              'Blessing_of_the_Worthy',
                              'Frozen_Heart',
                              'Zwensons_Haunting',
                              'Seeping_Bile',
                              'Phoenix_Ashes',
                              'Chip_of_Stoned_Flesh',
                              'Hellfire_Fragment',
                              'Echoing_Shade',
                              'Concentrated_Will'],
                             'Chip_of_Stoned_Flesh',
                             id='gem5_select'),
                className="dash-bootstrap"),

            # Gem five rank dropdown
            html.Br(),
            html.Label('Select Rank'),
            dcc.Dropdown(['one',
                          'two',
                          'three',
                          'four',
                          'five',
                          'six',
                          'seven',
                          'eight',
                          'nine',
                          'ten'],
                         'one',
                         id='gem5_rank'),

            # Gem star count dropdown
            html.Br(),
            html.Label('Select Stars'),
            dcc.Dropdown(['two_out_of_five',
                          'three_out_of_five',
                          'four_out_of_five',
                          'five_out_of_five'],
                         'two_out_of_five',
                         id='gem5_stars'),

            # Gem starting copies
            html.Br(),
            html.Label('Starting copies'),
            dbc.Input(id="start_copies_input_five",
                      value=0,
                      type='number'),

        ], style={"border": "2px red solid", "border-radius": "5px", 'margin': '5px', 'padding': 10, 'flex': 1}),

        html.Div(children=[
            html.H4("Gem Six"),
            # gem five dropdown
            html.Label('Select Gem'),
            html.Div(
                dcc.Dropdown(['Blood_Soaked_Jade',
                              'Bottled_Hope',
                              'Howlers_Call',
                              'Blessing_of_the_Worthy',
                              'Frozen_Heart',
                              'Zwensons_Haunting',
                              'Seeping_Bile',
                              'Phoenix_Ashes',
                              'Chip_of_Stoned_Flesh',
                              'Hellfire_Fragment',
                              'Echoing_Shade',
                              'Concentrated_Will'],
                             'Echoing_Shade',
                             id='gem6_select'),
                className="dash-bootstrap"),

            # Gem five rank dropdown
            html.Br(),
            html.Label('Select Rank'),
            dcc.Dropdown(['one',
                          'two',
                          'three',
                          'four',
                          'five',
                          'six',
                          'seven',
                          'eight',
                          'nine',
                          'ten'],
                         'one',
                         id='gem6_rank'),

            # Gem star count dropdown
            html.Br(),
            html.Label('Select Stars'),
            dcc.Dropdown(['two_out_of_five',
                          'three_out_of_five',
                          'four_out_of_five',
                          'five_out_of_five'],
                         'two_out_of_five',
                         id='gem6_stars'),

            # Gem starting copies
            html.Br(),
            html.Label('Starting copies'),
            dbc.Input(id="start_copies_input_six",
                      value=0,
                      type='number'),

        ], style={"border": "2px red solid", "border-radius": "5px", 'margin': '5px', 'padding': 10, 'flex': 1}),

    ], style={'display': 'flex', 'flex-direction': 'row'}),

    html.Div(children=[
        html.Br(),
        html.Label('Select the simulation scenario you would like to run'),
        dbc.RadioItems(
            options=[
                {'label': 'Quick simulation - low confidence - (~1 minute)', 'value': 50},
                {'label': 'Normal simulation (RECOMMENDED) - medium confidence - (~3 minutes)', 'value': 250},
                {'label': 'Extensive simulation - high confidence - (>5 minutes)', 'value': 1000},
                {"label": 'Extreme simulation - comming soon', "value": 10000, "disabled": True},
            ],
            value=0,
            id="sim_input"
        ),
        # dbc.Input(id="sim_input",  value=0, type='number'),

        html.Br(),
        html.Label('Select how many bundles to display at a time (recommended 5)'),
        dbc.Input(id="bundle_input", value=5, type='number'),

        html.Br(),
        html.Label('Input the total gem food in your inventory'),
        dbc.Input(id="frag_input", value=0, type='number'),

        html.Br(),
        html.Label('Input your current platinum'),
        dbc.Input(id="plat_input", value=0, type='number'),

    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        dbc.Button("RUN GEM SIMULATION", id="loading-button", n_clicks=0, color="danger"),
        html.Br(),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        dbc.Spinner(children=[dcc.Graph(figure={}, id='chart_id', style={'height': '40vh'})], size="lg", color="danger",
                    type="grow", fullscreen=True),

    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Br(),
        dbc.Table(id="table"),

    ], style={'margin-left': '85px', 'margin-right': '85px', 'flex': 1}),

], style={'display': 'flex', 'padding': 30, 'flex-direction': 'column'})


@app.callback(
    [Output(component_id='chart_id', component_property='figure'),
     Output(component_id='table', component_property='children')],
    [Input(component_id='loading-button', component_property='n_clicks'),

     State(component_id='sim_input', component_property='value'),
     State(component_id='bundle_input', component_property='value'),
     State(component_id='frag_input', component_property='value'),
     State(component_id='plat_input', component_property='value'),
     State(component_id='gem1_select', component_property='value'),
     State(component_id='gem1_rank', component_property='value'),
     State(component_id='gem1_stars', component_property='value'),
     State(component_id='start_copies_input_one', component_property='value'),
     State(component_id='gem2_select', component_property='value'),
     State(component_id='gem2_rank', component_property='value'),
     State(component_id='gem2_stars', component_property='value'),
     State(component_id='start_copies_input_two', component_property='value'),
     State(component_id='gem3_select', component_property='value'),
     State(component_id='gem3_rank', component_property='value'),
     State(component_id='gem3_stars', component_property='value'),
     State(component_id='start_copies_input_three', component_property='value'),
     State(component_id='gem4_select', component_property='value'),
     State(component_id='gem4_rank', component_property='value'),
     State(component_id='gem4_stars', component_property='value'),
     State(component_id='start_copies_input_four', component_property='value'),
     State(component_id='gem5_select', component_property='value'),
     State(component_id='gem5_rank', component_property='value'),
     State(component_id='gem5_stars', component_property='value'),
     State(component_id='start_copies_input_five', component_property='value'),
     State(component_id='gem6_select', component_property='value'),
     State(component_id='gem6_rank', component_property='value'),
     State(component_id='gem6_stars', component_property='value'),
     State(component_id='start_copies_input_six', component_property='value')],

)
def update_graph(n_clicks, sim_input, bundle_input, frag_input, plat_input, gem1_select, gem1_rank, gem1_stars,
                 start_copies_input_one, gem2_select, gem2_rank, gem2_stars, start_copies_input_two, gem3_select,
                 gem3_rank, gem3_stars, start_copies_input_three, gem4_select, gem4_rank, gem4_stars,
                 start_copies_input_four, gem5_select, gem5_rank, gem5_stars, start_copies_input_five, gem6_select,
                 gem6_rank, gem6_stars, start_copies_input_six):
    if n_clicks is None:
        return dash.no_update
    else:

        foo_ = run_multiprocess(sim_input,
                                bundle_input,
                                frag_input,
                                plat_input,
                                # gem one
                                gem1_select,
                                gem1_rank,
                                gem1_stars,
                                start_copies_input_one,
                                # gem two
                                gem2_select,
                                gem2_rank,
                                gem2_stars,
                                start_copies_input_two,
                                # gem three
                                gem3_select,
                                gem3_rank,
                                gem3_stars,
                                start_copies_input_three,
                                # gem four
                                gem4_select,
                                gem4_rank,
                                gem4_stars,
                                start_copies_input_four,
                                # gem five
                                gem5_select,
                                gem5_rank,
                                gem5_stars,
                                start_copies_input_five,
                                # gem six
                                gem6_select,
                                gem6_rank,
                                gem6_stars,
                                start_copies_input_six)

        base_resonance = find_resonance(gem1_rank, gem1_stars) + find_resonance(gem2_rank, gem2_stars) + find_resonance(
            gem3_rank, gem3_stars) + find_resonance(gem4_rank, gem4_stars) + find_resonance(gem5_rank,
                                                                                            gem5_stars) + find_resonance(
            gem6_rank, gem6_stars)

        foo_2 = foo_.melt()

        fig = px.box(data_frame=foo_2, x='variable', y='value', color_discrete_sequence=["red"])
        fig.update_layout(transition_duration=500, title="Simulated Resonance Distributions by Spend",
                          xaxis_title="Spend in usd (plus tax)",
                          yaxis_title="Total Resonance", font=dict(size=18))
        fig.add_hline(y=base_resonance,
                      line_dash="dot",
                      line_color="blue",
                      line_width=1,
                      opacity=0.7,
                      annotation_text=f"Starting Resonance: {int(base_resonance)}.")
        fig.add_hline(y=3000,
                      line_dash="dot",
                      line_color="black",
                      line_width=1,
                      opacity=0.7,
                      annotation_text=f"3K")
        fig.add_hline(y=5000,
                      line_dash="dot",
                      line_color="black",
                      line_width=1,
                      opacity=0.7,
                      annotation_text=f"5K")
        test_2 = foo_.describe().iloc[3:, :]

        col = pd.Series(foo_.columns).apply(format).to_list()
        test_2.columns = col
        summary_df = test_2.reset_index()
        summary_df = summary_df.rename(columns={"index": "RNG"})
        summary_df['RNG'] = summary_df['RNG'].replace(['min', '25%', '50%', '75%', 'max'],
                                                      ['Very Unlucky', 'Unlucky', 'Expected', 'Lucky', 'Very Lucky'])

        table = dbc.Table.from_dataframe(summary_df, striped=True, bordered=True, hover=True, index=False)

        return [fig, table]


if __name__ == '__main__':
    app.run_server(debug=True)