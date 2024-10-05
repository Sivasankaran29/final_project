# Web Scraping: Product Recommendations with Sentiment Analysis from Flipkart

## Project Overview

This project aims to develop an automated system for collecting and analyzing product reviews from Flipkart. By leveraging web scraping techniques and sentiment analysis, the project generates data-driven product recommendations based on customer sentiments.

### Skills Developed

- Web Scraping
- Data Parsing and Structuring
- Sentiment Analysis
- Data Visualization
- Python Programming
- Libraries Used: Selenium, Requests, Beautiful Soup, Pandas, TextBlob
- Implementing LangChain for Product Recommendations
- AWS Deployment

### Domain Focus

- E-commerce
- Data Science
- Machine Learning
- Deep Learning
- Natural Language Processing (NLP)

## Problem Statement

The goal of this project is to automate the collection and analysis of product reviews from Flipkart, with the following key tasks:

1. **Web Scraping**: Extract product reviews from Flipkart across various categories.
2. **Data Cleaning and Structuring**: Process and structure the scraped data.
3. **Sentiment Analysis**: Analyze the sentiments expressed in the reviews.
4. **Product Recommendation**: Recommend top products based on sentiment analysis results.
5. **Visualization and Reporting**: Create visual representations of the findings.

## Approach

1. **Data Collection**: Scraped product reviews from Flipkart using web scraping techniques.
2. **Data Cleaning and Structuring**: Organized the data into a structured format.
3. **Sentiment Analysis**: Performed sentiment analysis on the reviews.
4. **Product Recommendation**: Used LangChain to generate product recommendations.
5. **Visualization and Reporting**: Visualized results and compiled a comprehensive report.

## Results

- A dataset of scraped reviews from Flipkart.
- Sentiment analysis results categorizing sentiments (positive, negative, neutral).
- A list of recommended products based on sentiment analysis.
- Visualizations depicting sentiment distribution and product recommendations.
- A detailed report summarizing the approach, analysis, and findings.

## Business Use Cases

- Enhance product recommendation engines for e-commerce platforms.
- Analyze consumer sentiment for market research firms.
- Monitor customer feedback for retail companies.
- Integrate insights into business intelligence tools.

## Dataset Description

- **Source**: Live product pages from Flipkart.
- **Products Analyzed**: Comparison of five mobile phones in the price range of ₹20,000 to ₹40,000.
- **Format**: Structured format (CSV or JSON).
- **Variables**: Product ID, Review Text, Rating, Sentiment Score.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Required libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name

git clone https://github.com/Sivasankaran29/final_project.git
cd final_project

pip3 install streamlit
# If you have a requirements.txt, run this:
pip3 install -r requirements.txt

sudo apt install python3-venv -y

python3 -m venv venv

source venv/bin/activate

pip install streamlit

git pull origin main

ls

streamlit run final_project.py --server.port 8501 --server.address 0.0.0.0

http://<your-ec2-public-ip>:8501
