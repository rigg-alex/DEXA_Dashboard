from dash import dcc, html, Input, Output, callback, register_page
import plotly.graph_objects as go
import pandas as pd

register_page(__name__, path="/dexa-dashboard", order=3)

COMPOSITION_CSV_URL = "https://raw.githubusercontent.com/rigg-alex/DEXA_Dashboard/main/Data/composition_indices.csv"

# Load the data
df = pd.read_csv(COMPOSITION_CSV_URL)
df.columns = df.columns.str.replace("Â²", "²", regex=False).str.strip()
df["Scan Date"] = pd.to_datetime(df["Scan Date"], format="%d/%m/%Y", errors="coerce")
df.dropna(subset=["Scan Date"], inplace=True)

METRICS = [
    "Total Body Weight (kg)",
    "BMI (kg/m²)",
    "Basal Metabolic Rate (kcal/day)",
    "Total Body Fat (%)",
    "Fat Mass Index (FMI)",
    "Android/Gynoid Fat Ratio",
    "Trunk/Legs Fat Ratio",
    "Trunk/Limb Fat Mass Ratio",
    "Visceral Fat Area (cm²)",
    "Visceral Fat Mass (g)",
    "Visceral Fat Volume (cm³)",
    "Subcutaneous Fat Area (cm²)",
    "Total Lean Body (%)",
    "Lean Mass Index (kg/m²)",
    "Appendicular Lean Mass Index (kg/m²)",
    "Total Bone Mass (%)"
]

def create_time_series(df, metric):
    df = df.copy()
    missing_mask = df[metric].isna()
    mean_value = df[metric].mean()
    df[metric].fillna(mean_value, inplace=True)

    fig = go.Figure()

    # Main time series line
    fig.add_trace(go.Scatter(
        x=df["Scan Date"],
        y=df[metric],
        mode='lines+markers',
        line=dict(width=2),
        marker=dict(size=8),
        name='Actual Data'
    ))

    # Highlight filled values
    if missing_mask.any():
        fig.add_trace(go.Scatter(
            x=df.loc[missing_mask, "Scan Date"],
            y=df.loc[missing_mask, metric],
            mode='markers',
            marker=dict(color='red', symbol='x', size=10),
            name='Filled Data (Mean)'
        ))

    fig.update_layout(
        title={
            'text': metric,
            'x': 0.5,
            'xanchor': 'center',
            'y': 0.95
        },
        xaxis_title="Date",
        yaxis_title=metric,
        showlegend=True,
        height=250,
        margin=dict(l=50, r=50, t=50, b=50),
        xaxis=dict(
            showgrid=False,
            zeroline=True,
            linecolor='black',
            linewidth=1,
            mirror=False,
            showline=True,
            showspikes=False
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            linecolor='black',
            linewidth=1,
            mirror=False,
            showline=True,
            showspikes=False
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.85,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255,255,255,0)',
            font=dict(size=8)
        ),
        # Remove borders
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return fig

# Layout
layout = html.Div([
    html.H2("Composition Indices Analysis", 
            style={'textAlign': 'center', 'marginBottom': '20px'}),

    # Patient selector in a card
    html.Div([
        html.Div([
            html.Label("Select Patient:", 
                      style={'marginBottom': '10px', 'display': 'block', 'fontWeight': 'bold'}),
            dcc.RadioItems(
                id='patient-selector',
                options=[{'label': name, 'value': name} 
                        for name in sorted(df["Patient Name"].unique())],
                value=sorted(df["Patient Name"].unique())[0] if not df.empty else None,
                style={'display': 'flex', 'flexDirection': 'column', 'gap': '10px'}
            )
        ], style={
            'backgroundColor': 'white',
            'padding': '20px',
            'borderRadius': '8px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
            'marginBottom': '20px'
        })
    ], style={'width': '300px', 'margin': '0 auto'}),

    # Graphs container with fixed height and scrolling
    html.Div(
        id='graphs-container',
        style={
            'display': 'grid',
            'gridTemplateColumns': 'repeat(auto-fit, minmax(350px, 1fr))',
            'gap': '20px',
            'padding': '20px',
            'maxHeight': 'calc(100vh - 250px)',
            'overflowY': 'auto',
            'overflowX': 'hidden'
        }
    )
])


@callback(
    Output('graphs-container', 'children'),
    Input('patient-selector', 'value')
)
def update_graphs(selected_patient):
    if not selected_patient:
        return html.Div("Please select a patient")

    patient_df = df[df["Patient Name"] == selected_patient].sort_values("Scan Date")
    
    if patient_df.empty:
        return html.Div("No data available for selected patient")

    # Return an empty list first to clear the container
    return [
        [], # Clear the container before adding new graphs
        *[
            html.Div([
                dcc.Graph(
                    figure=create_time_series(patient_df, metric),
                    config={'displayModeBar': False},
                    style={'background': 'white'}
                )
            ], style={
                'borderRadius': '8px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                'padding': '15px',
                'background': 'white'
            })
            for metric in METRICS
        ]
    ]
