import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

# Set style for plots
plt.style.use('fivethirtyeight')
sns.set(font_scale=1.2)

# Create a directory for saving figures
os.makedirs('dog_figures', exist_ok=True)

# Download dataset
print("Downloading dog breeds dataset...")
path = kagglehub.dataset_download("paultimothymooney/best-in-show-data-about-dogs")
print(f"Dataset downloaded to: {path}")

# Load the dataset
# Assuming the CSV file is in the downloaded directory
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
if not csv_files:
    raise FileNotFoundError("No CSV files found in the downloaded dataset")

# Print available files to identify the correct one
print(f"Available files: {os.listdir(path)}")

# Let's try to load the first CSV file
dog_data = pd.read_csv(os.path.join(path, csv_files[0]))

# Display basic info about the dataset
print("\nDataset Overview:")
print(f"Shape: {dog_data.shape}")
print("\nColumns:")
print(dog_data.columns.tolist())
print("\nSample data:")
print(dog_data.head())

# Check for missing values
print("\nMissing values:")
print(dog_data.isnull().sum())

# Function to save figures
def save_figure(fig, filename):
    fig.savefig(os.path.join('dog_figures', filename), bbox_inches='tight', dpi=300)
    plt.close(fig)

# Analysis 1: Top 10 popular breeds
# Assuming there's a column related to popularity
popularity_columns = [col for col in dog_data.columns if 'popular' in col.lower()]
if popularity_columns:
    pop_column = popularity_columns[0]
    print(f"\nAnalyzing popularity using column: {pop_column}")
    
    # Sort by popularity and get top 10
    top_popular = dog_data.sort_values(by=pop_column, ascending=False).head(10)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=pop_column, y='Breed', data=top_popular, ax=ax)
    ax.set_title('Top 10 Most Popular Dog Breeds')
    ax.set_xlabel('Popularity Score')
    
    # Save figure
    save_figure(fig, 'top10_popular_breeds.png')
    print("Top 10 popular breeds plot saved")
else:
    print("No popularity-related column found. Looking for alternative...")
    # If no explicit popularity column, use a proxy like registration numbers if available
    numerical_columns = dog_data.select_dtypes(include=[np.number]).columns.tolist()
    if numerical_columns:
        print(f"Using {numerical_columns[0]} as a proxy for popularity")
        top_popular = dog_data.sort_values(by=numerical_columns[0], ascending=False).head(10)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.barplot(x=numerical_columns[0], y='Breed', data=top_popular, ax=ax)
        ax.set_title(f'Top 10 Dog Breeds by {numerical_columns[0]}')
        
        save_figure(fig, 'top10_proxy_popular_breeds.png')
        print("Top 10 proxy popular breeds plot saved")

# Analysis 2: Top 10 most expensive breeds
# Assuming there's a column related to price or cost
price_columns = [col for col in dog_data.columns if any(word in col.lower() for word in ['price', 'cost', 'expense'])]
if price_columns:
    price_column = price_columns[0]
    print(f"\nAnalyzing price using column: {price_column}")
    
    # Sort by price and get top 10
    top_expensive = dog_data.sort_values(by=price_column, ascending=False).head(10)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=price_column, y='Breed', data=top_expensive, ax=ax)
    ax.set_title('Top 10 Most Expensive Dog Breeds')
    ax.set_xlabel('Price/Cost')
    
    # Save figure
    save_figure(fig, 'top10_expensive_breeds.png')
    print("Top 10 expensive breeds plot saved")
else:
    print("No price-related column found")

# Analysis 3: Top 10 dog score by breed
# Assuming there's a column related to score or rating
score_columns = [col for col in dog_data.columns if any(word in col.lower() for word in ['score', 'rate', 'rating', 'rank'])]
if score_columns:
    score_column = score_columns[0]
    print(f"\nAnalyzing score using column: {score_column}")
    
    # Sort by score and get top 10
    top_score = dog_data.sort_values(by=score_column, ascending=False).head(10)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=score_column, y='Breed', data=top_score, ax=ax)
    ax.set_title('Top 10 Dog Breeds by Score')
    ax.set_xlabel('Score')
    
    # Save figure
    save_figure(fig, 'top10_score_breeds.png')
    print("Top 10 breeds by score plot saved")
else:
    print("No score-related column found")

print("\nDog breeds analysis completed!") 