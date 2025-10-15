# 🧠 SpamShield Sentiment Analyzer

**SpamShield Sentiment Analyzer** is an AI-powered web application that analyzes **YouTube video comments** to detect **spam** and determine **overall audience sentiment** in real time.  
It combines Natural Language Processing (NLP) and Machine Learning (ML) to deliver meaningful insights from user-generated content.

---

## 🚀 Features

- 🔗 **YouTube Video Integration** – Fetches comments using the YouTube Data API v3  
- 💬 **AI Sentiment Analysis** – Classifies comments as Positive, Negative, or Neutral using NLP models  
- 🚫 **Spam Detection** – Identifies and filters spam or promotional comments via ML classifier  
- ⚡ **Real-Time Insights** – Instant analysis upon submitting a YouTube link  
- 📊 **Detailed Reports** – Displays categorized results with explanations  
- 💡 **User-Friendly Interface** – Clean, responsive web UI for quick interaction  

---

## 🧩 Tech Stack

**Frontend:**  
- HTML5, CSS3, JavaScript, Bootstrap  

**Backend:**  
- Python (Flask)  
- YouTube Data API v3  

**Machine Learning / NLP:**  
- NLTK  
- Scikit-learn  
- TextBlob / VADER  
- TF-IDF Vectorizer  

**Database (optional):**  
- SQLite (for saving analyzed results)

**Deployment & Tools:**  
- Git, GitHub, Render / Heroku  

---

## 🤖 AI & ML Highlights

- Utilized **Natural Language Processing (NLP)** for text cleaning, tokenization, and sentiment scoring  
- Implemented **Machine Learning models (Naive Bayes, Logistic Regression)** for spam classification  
- Leveraged **TF-IDF feature extraction** to transform textual data into numeric features  
- Fine-tuned and validated models for higher accuracy using **Scikit-learn**  
- Integrated the trained model into Flask backend for **real-time inference**  
- Provides **AI-driven explanations** for each spam detection and sentiment classification  

---

## 🧮 Project Workflow

1. Enter a **YouTube video URL** in the web interface  
2. App fetches comments using **YouTube Data API v3**  
3. Comments are preprocessed via NLP pipeline (tokenization, stopword removal, stemming)  
4. **Spam Detection** model predicts if a comment is spam  
5. **Sentiment Analysis** model categorizes emotions as Positive, Negative, or Neutral  
6. Results are displayed in a detailed table with explanation  

---

## 🧰 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/spamshield-sentiment-analyzer.git
cd spamshield-sentiment-analyzer
