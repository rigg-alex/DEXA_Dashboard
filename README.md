# DEXA Analysis Dashboard

## Overview

The DEXA Analysis Dashboard transforms raw DEXA scan PDFs into an interactive analytics platform. Starting with PDF extraction and data transformation, through to visualization and analysis, this project provides a complete solution for tracking and analyzing body composition data. The DEXA Analysis Dashboard is a web application designed to provide in-depth analysis of DEXA (Dual-energy X-ray Absorptiometry) scan data. This project was born out of the limitations of standard DEXA scan reports, particularly in their ability to track and analyze longitudinal changes in body composition.

![image](https://github.com/user-attachments/assets/2ebc9e14-92fb-424d-a4d2-92a13ca2f0a2)

## Features

### 1. Overview Dashboard
- Quick snapshot of current body composition metrics
- Comparative analysis with previous scans
- Trend visualization for key metrics
- Personal records tracking

![image](https://github.com/user-attachments/assets/9dbea6b0-78db-4d05-9339-5ec2b33f7875)


### 2. Body Part Analysis
- Detailed tracking of individual body parts
- Fat and lean mass comparisons
- Interactive selection of body regions
- Fat-to-lean mass ratio analysis

![image](https://github.com/user-attachments/assets/43718c81-a948-4775-b08b-84041c6def1f)


### 3. Composition Indices
- Comprehensive tracking of body composition metrics
- BMI and other health indicators
- Visceral fat analysis
- Android/Gynoid ratio tracking

![image](https://github.com/user-attachments/assets/f4fdb971-36f5-4777-8f3d-779b3cba82eb)


### 4. Symmetry Analysis
- Left/right body part comparisons
- Symmetry scoring system
- Trend analysis of body symmetry
- Visual representation of imbalances

![image](https://github.com/user-attachments/assets/35e14886-1bd5-4e13-a39c-3c42a5ffe8bb)


## Technology Stack

- **Frontend Framework**: Dash (Python-based)
- **Data Processing**: Python, Pandas
- **Visualization**: Plotly
- **Deployment**: Render
- **Version Control**: Git/GitHub

## Dependencies

```text
# Core dependencies
dash==2.11.1
plotly==5.10.0
gunicorn==20.1.0
pandas==2.0.3
numpy==1.23.5

# PDF transformation dependencies
pdfplumber==0.7.4
regex==2023.5.5
dash==2.11.1
plotly==5.10.0
gunicorn==20.1.0
pandas==2.0.3
numpy==1.23.5
```

## Data Source

The dashboard pulls data from two CSV files hosted on GitHub:

1. `master_dexa_data.csv`: Contains detailed body composition measurements for each body part
2. `composition_indices.csv`: Contains overall body composition metrics and indices

These CSV files are accessed via raw GitHub URLs and automatically loaded when the dashboard starts. The data includes:

### Body Part Measurements
- Detailed measurements for individual body parts
- Fat and lean mass distributions
- Bone mineral content
- Tissue areas and masses

### Composition Indices
- BMI and other health indicators
- Body fat percentages
- Visceral fat measurements
- Android/Gynoid ratios
- Lean mass indices

## Project Structure

```
DEXA_Dashboard/
├── app.py              # Main application file
├── Body_Part_Data.py      # PDF to master CSV transformation script
├── composition_indices.py  # PDF to composition indices transformation script
├── pages/             
│   ├── overview.py     # Home page with main metrics
│   ├── body_part_trend.py  # Body part analysis
│   ├── symmetry.py     # Symmetry analysis
│   └── dexa_dashboard.py   # Composition indices
├── Data/
│   ├── master_dexa_data.csv    # Processed DEXA data
│   └── composition_indices.csv  # Calculated indices
├── requirements.txt    # Project dependencies
└── Procfile           # Deployment configuration
```

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/DEXA_Dashboard.git
cd DEXA_Dashboard
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:8080`

## Deployment

This application is configured for deployment on Render. The `Procfile` and `requirements.txt` are set up for seamless deployment.

## Future Improvements

### PDF Transformation Integration
The project includes standalone scripts (`Body_Part_Data.py` and `composition_indices.py`) that transform DEXA scan PDFs into the required CSV format. A key planned improvement is integrating these directly into the web application. This will include:
- Direct PDF upload through the web interface
- Automatic data extraction and processing
- Real-time data updates
- Error handling and validation
- Progress tracking for bulk uploads

### Additional Planned Improvements
- Enhanced analysis metrics and visualizations
- Enhanced data validation and error handling
- User authentication and multi-user support
- Export functionality for reports and analyses

