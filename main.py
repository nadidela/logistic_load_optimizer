import pandas as pd
import numpy as np
import re
import time

# load dataset
file_path = "Amazon_Products.csv"

df = pd.read_csv(
    file_path,
    engine="python",
    on_bad_lines="skip"
)

print("Original Dataset Shape:", df.shape)

# selecting relevant columns
columns_needed = [
    'product_name',
    'price',
    'product_information',
    'amazon_category_and_sub_category',
    'average_review_rating'
]

columns_needed = [col for col in columns_needed if col in df.columns]
df = df[columns_needed].copy()

print("After Column Selection:", df.shape)

#cleaning the price column
def clean_price(price):
    if pd.isna(price):
        return np.nan

    price = str(price)
    match = re.search(r'[\d,.]+', price)

    if match:
        return float(match.group(0).replace(',', ''))

    return np.nan


df['price_cleaned'] = df['price'].apply(clean_price)
df.dropna(subset=['price_cleaned'], inplace=True)

#extracting product weights
def extract_weight(text):
    if pd.isna(text):
        return np.nan

    text = str(text).lower()

    kg_match = re.search(r'(\d+\.?\d*)\s*kg', text)
    if kg_match:
        return float(kg_match.group(1)) * 1000

    g_match = re.search(r'(\d+\.?\d*)\s*g', text)
    if g_match:
        return float(g_match.group(1))

    lb_match = re.search(r'(\d+\.?\d*)\s*lb', text)
    if lb_match:
        return float(lb_match.group(1)) * 453.592

    oz_match = re.search(r'(\d+\.?\d*)\s*oz', text)
    if oz_match:
        return float(oz_match.group(1)) * 28.3495

    return np.nan


df['weight_grams'] = df['product_information'].apply(extract_weight)
df.dropna(subset=['weight_grams'], inplace=True)
