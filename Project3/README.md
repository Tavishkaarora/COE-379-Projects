# **Project 3 – Social Media Sentiment & Stock Return Prediction**

This project explores whether retail investor sentiment, extracted from Reddit’s *WallStreetBets*, contains a useful signal for predicting short-term stock returns. We build and evaluate multiple machine learning models using sentiment features, historical price data, and event-aware filtering to study the limits of sentiment-driven prediction.

---

## **Project Structure**

```
Project3/
├── data/
│   └── Processed datasets used by notebooks
│
├── notebooks/
│   ├── 01_wsb_preproc_no_sentiment.ipynb
│   ├── 02_stock_data_preproc.ipynb
│   ├── 02_wsb_preproc_add_sentiment.ipynb
│   ├── 03_data_composition.ipynb
│   ├── 04_data_aggregation.ipynb
│   ├── 05_price_to_price_prediction.ipynb
│   ├── 05_price_to_sentiment_prediction.ipynb
│   ├── 05_sentiment_to_price_prediction.ipynb
│   ├── 05_sentiment_and_historical_composite_to_price_prediction.ipynb
│   ├── 06_model_profitability.ipynb
│   ├── model_profitability.py
│   ├── parquet_files.py
│   ├── models/
│   └── presentation/
│
├── written_materials/
│   ├── proposal.pdf
│   ├── Social_Media_Sentiment_As_A_Predictor_Of_U_S_Stock_Market_Returns.pdf
│   ├── ML Final.pdf
│   └── Use of AI.pdf
│
└── .gitignore
```

---

## **What We Did**

* Collected and processed **Reddit WallStreetBets discussion data** and **historical stock price data**
* Constructed **domain-specific sentiment features** (custom WSB lexicon) and **transformer-based sentiment scores** (FinBERT)
* Evaluated multiple prediction tasks:

  * Price → price
  * Price → sentiment
  * Sentiment → price
  * Sentiment + historical features → price
* Tested **Ridge Regression**, **XGBoost**, a **TCN-based model**, as well as others
* Evaluated performance across **1-7-day horizons**
* Applied **event-aware filtering** to reduce earnings and corporate action noise

---

## **Key Takeaway**

While small patterns between price movements and community sentiment exist, predictive performance is weak and highly uncertain. The project highlights both the limits of sentiment-based return prediction and the challenges of modeling noisy, behavior-driven financial data.

---

## **Additional Documentation**

* Full methodology, results, and discussion are provided in the **final paper** and **presentation** located in **written_materials/**
* AI usage is documented in **Use of AI.pdf** per course requirements

---

