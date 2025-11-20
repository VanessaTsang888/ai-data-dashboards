# AI-Powered Data Dashboard Website Application

The objective of this personal AI software development project is to learn to use AI-powered coding assistant in Streamlit that helps generate, refine, and maintain interactive data dashboards using Python and OpenAI’s API.

The objective of my interactive data dashboard website application visualise a range of different types of data in the form of filtering tables and scatter plot garph. My application is built with basic widgets, data panels, a live chatbot, AI-driven code-generation execution, and robust error feedback. All of this with python programming.

Digital Accessibility: The 'tooltip' feature on each plot within the scatter plot visulisation graph is for both accessibility and makes this graph more interactive. To use this feature, the user with reduced vision problem simply hover their cursor over a plot and a pop-up panel will appear for them to read the details of the plot in plain text.

OpenAI Platform: The model I am using is the "gpt-3.5-turbo" because this model is fast, efficient, robust and afforable.

## Data, Tables, and Graphs

Sample Data: I am using the Iris Dataset as it contains different data values, statistics, scatter plot and multiple filtering tables.

Scatter plot: this visualisation graph is very interactive. Click and drag the graph to pan in and out. To zoom in and to, use the scroll ball on your mouse. Hoever your cursor over a plot to activate the tooltip feature. Each species is colour coded - see the Key on the right side of the graph.

Filtering tables: when you hover over a row, it will be highlighted in ligh grey colour for accessibility. Click on a heading to filter/sort the column of data.

## Requirements

Install Python 3.12
Streamlit 1.35.0
The small embedding model (text-embedding-3-small) from the [OpenAI Platform](https://platform.openai.com/docs/models/text-embedding-3-small)

## Getting Started

- `git clone` the repository
- Navigate to the directory
- Run `pip install -r requirements.txt` to install dependencies
- Run
  - `streamlit run gui.py` # to run the file. Browser will launch in the URL: http://localhost:8501/

## Dependencies

Including development dependencies.

| Package                                               | Description |
| ----------------------------------------------------- | ----------- |
| [Python 3.12](https://www.)                           | xxxx        |
| [streamlit>=1.35.0](https://www.)                     | xxxx        |
| [pandas>=2.2.0](https://www.)                         | xxxx        |
| [numpy>=1.26.0](https://www.)                         | xxx         |
| [altair>=5.3.0](https://www.npmjs.com/package/dotenv) | xxx         |
| [vegafusion>=1.6.6](https://www.)                     | xxx         |
| [openai>=1.30.0](https://www.)                        | xxx         |
| [pytest>=8.2.1](https://www.)                         | xxx         |
