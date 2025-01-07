from dash import dcc, html, Input, Output, callback, ALL, MATCH, callback_context, register_page, State
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from dash.exceptions import PreventUpdate
import dash

# Register this page
register_page(__name__, 
             path='/body-part-trend',
             name='Body Part Trends',
             order=2)

# GitHub raw URL for the master CSV
MASTER_CSV_URL = "https://github.com/rigg-alex/DEXA_Dashboard/blob/main/Data/master_dexa_data.csv"

# Load the data from GitHub
def load_data():
    try:
        df = pd.read_csv(MASTER_CSV_URL)
        df["Scan Date"] = pd.to_datetime(df["Scan Date"], format="%d-%m-%Y", errors="coerce")
        df.dropna(subset=["Scan Date"], inplace=True)
        return df
    except Exception as e:
        print(f"Error loading data from GitHub: {e}")
        return pd.DataFrame()

df = load_data()

# Group body parts logically
BODY_PART_GROUPS = {
    'Arms': ['Left Arm', 'Right Arm'],
    'Legs': ['Left Leg', 'Right Leg'],
    'Torso': ['Left Ribs', 'Right Ribs', 'T Spine', 'L Spine', 'Pelvis'],
    'Total': ['Total'],
    'Regions': ['Android', 'Gynoid']
}

def create_button(part):
    """Create a consistent button style"""
    return html.Button(
        part,
        id={'type': 'body-part-button', 'index': part},
        n_clicks=0,
        className='body-part-btn',
        style={
            'margin': '5px',
            'padding': '8px 15px',
            'border': '1px solid #ddd',
            'borderRadius': '4px',
            'backgroundColor': 'white',
            'cursor': 'pointer',
            'minWidth': '120px',
            'textAlign': 'center'
        }
    )

def format_ratio(fat, lean):
    """Format the fat:lean ratio in standard form"""
    ratio = fat / lean
    denominator = int(round(1 / ratio)) if ratio < 1 else 1
    numerator = round(ratio * denominator, 1)
    return f"{numerator:.1f}:{denominator}"

def create_button_group(group, parts):
    """Create a grouped set of buttons with label"""
    return html.Div([
        html.Label(group, style={
            'fontWeight': 'bold', 
            'marginBottom': '5px', 
            'display': 'block'
        }),
        html.Div([
            create_button(part) for part in parts
        ], style={
            'display': 'flex',
            'flexWrap
