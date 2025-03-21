# Dog Breeds Analysis

This project analyzes the "Best in Show - Data About Dogs" dataset from Kaggle to visualize and understand characteristics of different dog breeds.

## Project Overview

This analysis examines various characteristics of dog breeds to provide insights for potential dog owners, breeders, and enthusiasts. The Jupyter notebook includes detailed code, explanations, and visualizations that reveal patterns and relationships in the dataset.

## Interactive Notebook

The `dog_breeds_analysis.ipynb` notebook contains all the code and fully rendered visualizations. You can view this notebook directly on GitHub to see all the charts and analysis without having to run any code. The notebook is designed to be easy to follow with:

- Markdown explanations before each section
- Comments throughout the code
- All visualizations rendered inline
- Color-coded charts for better interpretation

## Analyses Performed

1. **Top 10 Popular Breeds**: Visualization of the most popular dog breeds based on available data.
2. **Top 10 Most Expensive Breeds**: Visualization of the most expensive dog breeds.
3. **Top 10 Most Intelligent Breeds**: Visualization of the breeds with the highest intelligence rankings.
4. **Lifespan vs. Weight Relationship**: Analysis of how a dog's weight affects its lifespan, including regression line and statistical correlation measures.
5. **Breed Characteristics Comparison**: Radar charts comparing various characteristics of the top 5 most popular breeds, with robust handling of missing data.
6. **Price vs. Popularity Analysis**: Examination of whether a breed's price correlates with its popularity, featuring enhanced annotation and regression analysis.

## Key Visualizations

All visualizations are rendered directly in the notebook and feature:

- **Enhanced color schemes**: Carefully selected colors for better contrast and readability
- **Advanced annotations**: Regression lines, correlations, and statistical measures where applicable
- **Consistent styling**: Professional appearance across all visualizations
- **Improved legends**: Clear and descriptive legends that explain each element
- **Robust data handling**: Graceful handling of missing values to ensure visualizations work regardless of data changes

The main visualizations include:
- `top10_popular_breeds.png`: Bar chart of the most popular dog breeds
- `top10_expensive_breeds.png`: Bar chart of the most expensive dog breeds
- `top10_intelligence_breeds.png`: Bar chart of the highest-scoring dog breeds for intelligence
- `weight_vs_lifespan.png`: Scatter plot showing the relationship between dog weight and lifespan
- `top5_characteristics.png`: Radar charts of characteristics for the top 5 most popular breeds
- `price_vs_popularity.png`: Scatter plot analyzing the relationship between price and popularity

## Data Source

The data used in this analysis is from the Kaggle dataset ["Best in Show - Data About Dogs"](https://www.kaggle.com/datasets/paultimothymooney/best-in-show-data-about-dogs).

## Requirements

- Python 3.6+
- Required packages:
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - kagglehub

You can install all requirements using:
```
pip install -r requirements.txt
```

## Usage

You can either:

1. **View the notebook on GitHub**: The notebook has all visualizations pre-rendered for easy viewing
2. **Run the notebook locally**: To reproduce or modify the analysis
   - Clone this repository
   - Install requirements
   - Run `jupyter notebook dog_breeds_analysis.ipynb`

## Key Findings

- Labrador Retrievers, German Shepherds, and Golden Retrievers are consistently the most popular breeds
- French Bulldogs and Cavalier King Charles Spaniels tend to be among the most expensive breeds
- There is a clear negative correlation between dog weight and lifespan, with statistical significance
- Each breed has a unique profile of characteristics that makes it suitable for different lifestyles
- The radar chart visualization reveals how breeds differ across dimensions like trainability, shedding, and energy levels
- There doesn't appear to be a strong correlation between a breed's price and its popularity

## Author

This analysis was created as part of a data science project exploring popular datasets from Kaggle. 