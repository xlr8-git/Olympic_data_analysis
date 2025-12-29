# AI-Assisted Olympic Games Analytics (1896–2016)

An interactive, data-science–driven Olympic Games analytics dashboard enhanced with LLM-powered natural language explanations for every visualization.

This project combines rigorous Exploratory Data Analysis (EDA) with modern AI (LLMs) to make insights both accurate and interpretable, even for non-technical users.

---

## Project Highlights

- End-to-end exploratory data analysis on 120 years of Olympic data
- AI-generated explanations for every chart using Groq Compound models
- Interactive filters (Year, Country, Sport)
- Global medal distribution visualization
- Trend analysis across participation, gender, age, and physical attributes
- Secure API handling using environment-based configuration

This is not just a visualization project. The focus is on correct, domain-aware data analysis presented the way a professional data scientist would.

---

## Data Science Approach

Key analytical considerations in this project include:

- Event-level medal correction to avoid duplicate medal counting
- Proper handling of missing values and duplicates
- Time-series analysis of Olympic participation
- Gender representation trends across decades
- Sport-specific physical profiling (height and weight)
- Interpretation grounded in historical and social context

The AI layer augments the analysis; it does not replace analytical reasoning.

---

## Tech Stack

### Core
- Python
- Pandas for data manipulation
- Seaborn, Matplotlib, Plotly for visualization
- Streamlit for interactive dashboards

### AI and LLM
- LangChain
- Groq Compound Models for future-proof LLM routing
- Natural language graph explanations

### Configuration
- python-dotenv
- Secure environment variable management

---

## Dashboard Features

- Year range selection (1896–2016)
- Country-wise filtering
- Sport-wise filtering
- Participation trends over time
- Gender distribution analysis
- Age distribution of gold medalists
- Height vs weight analysis of athletes
- Country-wise medal dominance
- Global medal distribution map
- Explain-this-graph functionality for every visualization

---

## Project Structure
```bash
Olympic_data_analysis/
│
├── app.py
├── llm_explainer.py
├── athlete_events.csv
├── noc_regions.csv
├── .env
├── .gitignore
└── README.md
```


---

## Setup and Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/xlr8-git/Olympic_data_analysis.git
cd Olympic_data_analysis
```
2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
   
Create a .env file:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
5. Run the application
```bash
streamlit run app.py
```

#### Example Usage
A non-technical user can apply filters, explore trends and distributions, and request clear AI-generated explanations for each visualization. The explanations remain grounded in the underlying statistical analysis.

### Key Learnings
Combining exploratory data analysis with LLMs without sacrificing analytical rigor

Designing future-proof AI integrations using compound models

Building dashboards that emphasize insights over visuals

Presenting analysis aligned with real-world data science workflows
