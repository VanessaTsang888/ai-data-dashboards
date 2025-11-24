# AI-Powered Data Dashboard Website Application - 'Visualise Data on Species'

The objective of this personal project is to use an AI-powered coding assistant build a website application that helps generate, refine, and maintain an interactive data dashboard using Python and OpenAI’s API.

The objective of my interactive data dashboard website application is to visualise a range of different data types based on the subject of **_'species'_** (flowers), and in the form of filtering tables, and a scatter plot graph. My application is built with basic widgets, data panels, a live chatbot, AI-driven code-generation execution, and robust error feedback. All of this with python programming and with the Streamlit python tool. This data dashboard is targeted to both technical and non technical user because I have programmed the application to generated Python code as a response and a response that is non technical such as a filtering table containing the relevant data.

OpenAI Platform: The AI model I am using is the [gpt-3.5-turbo](https://platform.openai.com/docs/models/gpt-3.5-turbo) because this model is fast, efficient, robust and afforable.

Digital Accessibility: The 'tooltip' feature on each plot within the scatter plot visualisation graph is for both accessibility and makes this graph more interactive. To use this feature, user's with reduced vision problems can simply hover their cursor over a plot, and a pop-up panel will appear for them to read the details of the plot in plain text.

## Data, Tables, and Graphs

Sample Data: I am using the 'Iris Dataset' as it contains different data values, statistics, scatter plot and multiple filtering tables based on the subject of 'species'.

Scatter plot: This visualisation graph (chart) is very interactive. Click and drag the graph to pan in and out. To zoom in and to, use the scroll ball on your mouse. Hover your cursor over a plot to activate the tooltip feature. Each species is colour coded - see the 'Key' on the right side of the graph.

Filtering tables: For accessibility, when you hover over a row, it will be highlighted in light grey colour. Click on a 'heading' to filter/sort the data column.

Left sidebar Filter Options: Use these filter options to speed up in sourcing particular data on a specific specie. For example, you may wish to visualise data for the 'virginica' specie and only the sepal width and the petal length in centimetres.

## How to use the AI Chatbot

First take a look at the data within filtering table and the scatter plot graph. Then to find the data you require faster, use the AI Chatbot by asking the bot your question(s). Examples of questions are as follows:

- Q1) "Show the first 6 rows where the setosa width is below 5 cm".
  The bot will respond (the answer) with the answer in Python code (Generated Python Code), and also a respond with a filtering table containing the data the user has asked for.
- Q2) "Show the first 10 rows where the revenue column is below 4".
  We get an **_error msg_** as expected because revenue is not within the subject of 'species', and not within the Iris Dataset that is based on the subject of 'species'.

### Handle Errors and provide User Feedback

  Whilst programming the an AI Chatbot to work as expected on my data dashboard, I have written Python code to handle possible errors in order to provide users with feedback when they have requested data that do not exist in this application. This helps improve the user-centric experience on this application. Part of software development best practice is to ensure we catch any possible errors and provide user feedback.

## Skills

1. Python Programming
2. AI Software Development
3. Data Analysis
4. Artificial Intelligence (AI)
5. Data Modeling

## Requirements

1. Install Python 3.12
2. Streamlit 1.35.0
3. the ['gpt-3.5-turbo'](https://platform.openai.com/docs/models/gpt-3.5-turbo)

## Getting Started

- `git clone` the repository
- Navigate to the directory
- Run `pip install -r requirements.txt` to install dependencies
- Run
  - `streamlit run gui.py` # to run the file. Browser will launch in the URL: http://localhost:8501/

### Dependencies

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
