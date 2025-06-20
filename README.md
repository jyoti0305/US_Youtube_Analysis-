# 📊 YouTube Trending Video Analysis (US)

A data analysis project that explores the dynamics of trending videos on YouTube in the United States — analyzing **views, likes, comments, tags, and categories** using Python, Pandas, Seaborn, and Matplotlib.

![Project Banner](https://img.shields.io/badge/status-completed-green?style=flat-square)  
![Python](https://img.shields.io/badge/Python-3.10-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📁 Dataset Used

- [`USvideos.csv`](https://www.kaggle.com/datasets/datasnaek/youtube-new)  
- `US_category_id.json` (contains category names for mapping)

---

## 🚀 Key Features

- Cleans and preprocesses raw YouTube video metadata
- Maps category IDs to readable category names
- Extracts day of week from publish time
- Calculates how long videos take to trend
- Uses **correlation analysis**, **scatter plots**, and **box plots** for insights

---

## 📌 Questions Answered

1. What are the **top trending video categories**?
2. Do videos with tags get **more views**?
3. How many days does it take a video to **start trending**?
4. Is there a **correlation between likes and comments**?
5. Does publishing day affect video popularity?

---

## 📊 Visualization

### 🎯 Top 10 Trending Categories
        ![top_10_treanding_categories](https://github.com/user-attachments/assets/3bb1f9e0-c783-432f-9888-21a0c8eb4752)

### ⏱️ Days to Trend vs Views
        ![Days_to_trend_vs_views](https://github.com/user-attachments/assets/4974f7a4-b267-4e54-ba77-32ae4660ec24)
 
### 💬 Comments vs Likes (Log-Scale)
        ![likes_vs_comments](https://github.com/user-attachments/assets/657775c3-e479-4aaf-adfb-2312b2de6766)

### 🏷️ Tags vs Views
        ![correlation](https://github.com/user-attachments/assets/7a4d1273-c818-4f4e-a780-f116d84b6ab7)

---

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| `Python` | Core scripting and analysis |
| `Pandas` | Data cleaning & manipulation |
| `Matplotlib`, `Seaborn` | Data visualization |
| `JSON` | Category mapping |
| `Git & GitHub` | Version control & hosting |

---

## 🗂️ File Structure
youtube-trending-analysis/
│
├── data/
│ ├── USvideos.csv
│ └── US_category_id.json
│
├── Youtube.py # Main analysis script
├── youtube_trending_cleaned.csv
└── README.md



---

## 🔍 Insights

- 👍 **High correlation (0.80)** between likes and comments — suggesting active viewer engagement.
- 📅 Videos with **tags** tend to perform better in terms of views.
- 📈 Some videos take **days or even weeks** to appear on the trending page.

---


📤 **Optional Large Dataset Link
🔗 Download full dataset via Google Drive**
US_category_id.json  :  https://drive.google.com/file/d/1KRTpOodzOdv0KSsN1a-6jKP1qNSZdUTf/view?usp=drive_link
USvideos.csv  :  https://drive.google.com/file/d/1WA6MDPvJtg65PmGYJE5xWztrNDN-cbR8/view?usp=drive_link
youtube_trending_cleaned.csv : https://drive.google.com/file/d/14tpL203ZBYwbZ_PwXgFUjzvyFaKLuxfo/view?usp=drive_link

---






