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


<img width="1889" height="829" alt="image" src="https://github.com/user-attachments/assets/1be6721d-f943-4670-9077-fdb135e77cb9" />
results

<img width="1895" height="818" alt="image" src="https://github.com/user-attachments/assets/d7287218-9c1e-4901-a578-dd6befd65453" />\

pi char
<img width="1870" height="668" alt="image" src="https://github.com/user-attachments/assets/6bc17291-e013-4c18-8326-c583a8a83c7a" />

detailed analysis
<img width="1867" height="770" alt="image" src="https://github.com/user-attachments/assets/5336f157-26db-4423-94fd-c954f5c4e335" />


## 🧰 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/spamshield-sentiment-analyzer.git
cd spamshield-sentiment-analyzer





