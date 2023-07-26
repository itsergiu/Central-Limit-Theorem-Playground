# Central Limit Theorem - from Theory to Code to App
# Created by: Sergiu Iatco, date 27.07.2023
# https://www.linkedin.com/in/sergiuiatco/
import streamlit as st
import numpy as np
import scipy.stats as stats
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image


# Function to display an image
def display_image():
    image = Image.open('Central Limit Theorem.jpeg')
    st.image(image, caption='', use_column_width=True)


# Function to display Python code
def display_code_from_file(filename):
    with open(filename, "r") as file:
        code = file.read()
    st.code(code, language="python")


def generate_random_sample(_sample_size):
    return np.random.uniform(0, 1, _sample_size)


def calculate_sample_mean(sample):
    return np.mean(sample)


def simulate_sample_means(_num_simulations, _sample_size):
    _sample_means = []
    for _ in range(_num_simulations):
        sample = generate_random_sample(_sample_size)
        sample_mean = calculate_sample_mean(sample)
        _sample_means.append(sample_mean)
    return _sample_means


def plot_sample_distribution(_sample_means):
    fig = make_subplots(rows=1, cols=2, subplot_titles=('Sample Distribution', 'Standard Normal Distribution'))

    # Plot the sample distribution
    fig.add_trace(
        go.Histogram(x=_sample_means, nbinsx=30, opacity=0.6, marker=dict(color='blue'), name='Sample Means'),
        row=1, col=1
    )

    # Calculate the mean and standard deviation of the sample means
    sample_mean = np.mean(_sample_means)
    sample_std = np.std(_sample_means)

    # Create a range of values for the x-axis
    x = np.linspace(sample_mean - 3*sample_std, sample_mean + 3*sample_std, 1000)

    # Plot the standard normal distribution
    fig.add_trace(
        go.Scatter(x=x, y=stats.norm.pdf(x, loc=sample_mean, scale=sample_std),
                   line=dict(color='red'), name='Standard Normal'),
        row=1, col=2
    )

    fig.update_layout(title='Central Limit Theorem ',
                      xaxis=dict(title='Sample Means'),
                      yaxis=dict(title='Density'),
                      showlegend=False)

# https://blog.streamlit.io/a-new-streamlit-theme-for-altair-and-plotly/

    st.plotly_chart(
        fig,
        theme="streamlit",  # ✨ Optional, this is already set by default!
    )


with st.sidebar:
    rb = ['Playground', 'Python code', 'Central Limit Theorem']
    selected_rb = st.radio('Select:', rb)
    # Sidebar controls
    sl_num_simulations = st.slider('Number of simulations:',  min_value=1000, max_value=10000, value=100, step=100,
                                   key='k_sl_num_simulations')
    sl_sample_size = st.slider('Sample size:', min_value=5, max_value=100, value=5, step=5,
                               key='k_sl_sample_size')

    st.markdown('📖 Read the [post](https://www.linkedin.com/feed/update/urn:li:activity:7089091830310477824/)')

if selected_rb == 'Playground':
    st.header('Playground')
    sample_size = sl_sample_size
    num_simulations = sl_num_simulations
    sample_means = simulate_sample_means(num_simulations, sample_size)
    plot_sample_distribution(sample_means)

elif selected_rb == 'Python code':
    st.header('Python Code')
    display_code_from_file('app.py')
elif selected_rb == 'Central Limit Theorem':
    display_image()
    st.markdown('📖 Source: [LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7089091830310477824/)')
