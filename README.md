# 🛡️ SafeScroll — AI Emotional Manipulation Detector

SafeScroll is an AI-powered NLP web application that detects emotionally manipulative content in social media posts, online messages, headlines, and advertisements.

The system classifies text into categories such as:

* ⚠️ Fear
* ⏳ Urgency
* 🎯 Clickbait
* 😔 Guilt
* ✅ Neutral

This project was developed as part of the **SafeScroll: Promoting Healthy Digital Awareness Across Generations** CSP project.

---

# 🚀 Features

* Real-time text analysis
* Emotional manipulation detection
* NLP-based text classification
* Confidence score prediction
* Trigger word detection
* Risk level analysis
* Streamlit web interface
* Deployed online using Streamlit Cloud

---

# 🧠 Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* TF-IDF Vectorization
* Logistic Regression
* Pickle

---

# 📂 Project Structure

```text
SafeScroll/
│
├── app.py
├── dataset.csv
├── train_model.py
├── requirements.txt
├── model.pkl
├── vectorizer.pkl
```

---

# ⚙️ How It Works

1. User enters text into the application
2. Text is converted into numerical vectors using TF-IDF
3. Logistic Regression model predicts the category
4. App displays:

   * Prediction
   * Confidence score
   * Risk level
   * Trigger words
   * Explanation

---

# 📊 Categories Detected

| Category  | Description                            |
| --------- | -------------------------------------- |
| Fear      | Threat or danger-based manipulation    |
| Urgency   | Pressures immediate action             |
| Clickbait | Uses curiosity or sensationalism       |
| Guilt     | Applies emotional pressure or shame    |
| Neutral   | Informational non-manipulative content |

---

# ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the app:

```bash
streamlit run app.py
```

---

# 🌐 Deployment

The project is deployed using Streamlit Community Cloud.

---

# 📌 Example Inputs

### Fear

```text
⚠️ Warning! Your account may be hacked.
```

### Urgency

```text
⏳ Hurry! Offer ends today!
```

### Clickbait

```text
🤯 You won’t believe this shocking secret!
```

### Guilt

```text
😔 If you care about others, share this now.
```

### Neutral

```text
📚 Class starts at 10 AM tomorrow.
```

---

# 🎯 Future Improvements

* Improved dataset size
* Better UI/UX design
* Analytics dashboard
* Multi-language support
* Advanced NLP models

---

# 👩‍💻 Developed By

Sadiya Banu Syed

AI/ML Student Project
