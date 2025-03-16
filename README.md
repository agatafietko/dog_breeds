# Dog Breeds Analysis

This project analyzes the "Best in Show - Data About Dogs" dataset from Kaggle to visualize and understand characteristics of different dog breeds.

## Analyses Performed

1. **Top 10 Popular Breeds**: Visualization of the most popular dog breeds based on available data.
2. **Top 10 Most Expensive Breeds**: Visualization of the most expensive dog breeds.
3. **Top 10 Dog Score by Breed**: Visualization of breeds with the highest scores according to the dataset.

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

## Dataset

The dataset is downloaded automatically from Kaggle using the kagglehub library:
```python
kagglehub.dataset_download("paultimothymooney/best-in-show-data-about-dogs")
```

## Usage

Simply run the Python script:
```
python dog_breeds_analysis.py
```

The script will:
1. Download the dataset from Kaggle
2. Process the data
3. Generate visualizations in the `dog_figures` directory

## Outputs

All visualizations are saved in the `dog_figures` directory:
- `top10_popular_breeds.png`: Bar chart of the most popular dog breeds
- `top10_expensive_breeds.png`: Bar chart of the most expensive dog breeds
- `top10_score_breeds.png`: Bar chart of the highest-scoring dog breeds

If a specific column isn't found in the dataset, the script will try to use alternatives or proxies based on the available data.

## Note

The script is designed to be adaptive, as the column names in the dataset may vary. It will try to identify the most appropriate columns for the analyses based on keywords in the column names. 