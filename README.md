# Logistic Load Optimization Using Dynamic Programming

## Overview

This project implements a Dynamic Programming based 0/1 Knapsack Optimization System to optimize product shipment selection over 10,000+ Amazon product records.

The goal is to compare how well Dynamic Programming performs over a Greedy Baseline on Large Scale Logistics Datasets.

The system allows users to enter a Container Capacity in grams and automatically finds the best combination of products that maximizes total shipment value while staying within the weight limit.

Example:

Input: Enter Container Capacity in grams: 10000

Output:

DYNAMIC PROGRAMMING KNAPSACK RESULTS:

• Total Items Packed: 241

• Total Shipment Value: $8432

• Total Weight Used: 10000 grams

• Capacity Utilization: 100.00%

---

## Dataset

The project uses the Amazon Products Dataset, which contains more than 10,000 product records.

Source: https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset

Each product includes several metadata fields:

Product Name
Product Price
Product Information
Product Category
Product Ratings

Since this is a real world dataset, it contains noise such as:

Prices stored as text with currency symbols (£24.99).
Product weights hidden inside large text descriptions.
Different weight formats like kg, g, lb, and oz.
Missing values in several product fields.
Broken or malformed rows inside the CSV file.

---

## Preprocessing

Before running the optimization algorithm, the dataset undergoes a cleaning pipeline to handle the noise:

Removes invalid or corrupted rows from the dataset.

Extracts product prices from noisy text formats.

Extracts product weights from product descriptions using Regular Expressions.

Converts all weight formats into grams for consistency.

Removes products with missing or unrealistic weights.

Cleans product names and removes formatting inconsistencies.

---

## Algorithm Used

The main algorithm used is Dynamic Programming using the 0/1 Knapsack Algorithm.

The system attempts to maximize the total shipment value while ensuring the total product weight does not exceed the container capacity.

Why use Dynamic Programming?

Greedy Baseline: Chooses products using a simple heuristic approach.

Dynamic Programming: Evaluates combinations of products and guarantees the globally optimal shipment selection.

Result: Dynamic Programming consistently produces the best possible shipment value under the same container weight constraint.

---

## Features

Optimizes shipment selection across 10,000+ products.

Maximizes shipment value under strict weight constraints.

Supports real-world noisy logistics datasets.

Automatically extracts and standardizes product weights.

Compares Dynamic Programming against a Greedy Baseline.

---

## Project Structure

main.py → Main application (Loads dataset, cleans data, and runs optimization).

Amazon_Products.csv → The raw Amazon products dataset.

README.md → Instructions and project documentation.

proposal.pdf → The project proposal.

---

## How to Run

Install dependency: pip install pandas  

Run program: python main.py  

---

## Key Learning Outcomes

1. Understanding the 0/1 Knapsack Optimization Problem.
2. Implementing Dynamic Programming for large scale optimization.
3. Solving noisy real-world data preprocessing challenges.
4. Extracting structured information from unstructured product descriptions.
5. Comparing exact optimization algorithms against heuristic approaches.

---

## Conclusion

This project demonstrates that Dynamic Programming is an effective method for solving large scale logistics optimization problems.

Dynamic Programming consistently produces better shipment configurations than Greedy based selection methods under the same capacity constraints.

---

## AI Usage Statement

I used AI for guidance during development.  I used AI to understand the search interface.

No AI Used for Core Logic. All the core logic, Dynamic Programming implementation, preprocessing logic for noisy data handling, optimization workflow, and dataset processing logic are manually implemented by me.

The Documentation in Code, Comments, READ ME are manually authored.
