import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page settings
st.set_page_config(
    page_title="SafeScroll",
    page_icon="🛡️",
    layout="centered"
)

# Sidebar
st.sidebar.title("🛡️ SafeScroll")

st.sidebar.info(
    "AI-powered emotional manipulation detection system using NLP and Machine Learning."
)

st.sidebar.success("Model Accuracy: ~85%")

# Main Title
st.title("🛡️ SafeScroll")
st.subheader("AI Emotional Manipulation Detector")

st.write(
    "Detects emotional manipulation in social media posts, messages, headlines, and advertisements."
)

# Example section
st.markdown("## Try Example Messages")

example_messages = [
    "⚠️ Warning! Your account may be hacked 😨",
    "⏳ Hurry! Offer ends in 5 minutes!",
    "🤯 You won’t believe this shocking secret!",
    "😔 If you care about others, share this now.",
    "📚 Class starts at 10 AM tomorrow."
]

selected_example = st.selectbox(
    "Choose an example:",
    [""] + example_messages
)

# Text input
user_input = st.text_area(
    "Enter text to analyze:",
    value=selected_example,
    height=150
)

# Trigger words dictionary
trigger_dict = {

    "fear": [
        "danger",
        "warning",
        "risk",
        "hacked",
        "virus",
        "threat",
        "security",
        "suspicious"
    ],

    "guilt": [
        "care",
        "ignore",
        "selfish",
        "support",
        "family",
        "help",
        "share",
        "responsible"
    ],

    "clickbait": [
        "secret",
        "shocking",
        "unbelievable",
        "viral",
        "surprise",
        "amazing",
        "crazy",
        "hidden"
    ],

    "urgency": [
        "act now",
        "claim now",
        "immediately",
        "hurry",
        "limited",
        "last chance",
        "today",
        "urgent",
        "quickly"
    ]
}

# Explanations
explanations = {

    "fear": "This text uses fear or threat-based language.",

    "guilt": "This text applies emotional pressure or shame.",

    "clickbait": "This text uses curiosity-driven attention tactics.",

    "urgency": "This text pressures immediate action.",

    "neutral": "This text appears informational and non-manipulative."
}

# Risk levels
risk_map = {

    "fear": "High",

    "guilt": "Medium",

    "clickbait": "Medium",

    "urgency": "Medium",

    "neutral": "Low"
}

# Analyze button
if st.button("Analyze Text"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")

    else:

        # Convert text
        input_vector = vectorizer.transform([user_input])

        # Prediction
        prediction = model.predict(input_vector)[0]

        # Probability
        probability = model.predict_proba(input_vector).max()

        confidence = round(probability * 100, 2)

        # Risk level
        risk = risk_map.get(prediction)

        # Trigger words
        found_triggers = []

        lower_text = user_input.lower()

        for word in trigger_dict.get(prediction, []):

            if word in lower_text:
                found_triggers.append(word)

        # Success
        st.success("Analysis Complete")

        # Prediction
        st.markdown("## Prediction")
        st.write(prediction.upper())

        # Confidence
        st.markdown("## Confidence")
        st.write(f"{confidence}%")

        # Progress bar
        st.progress(int(confidence))

        # Risk Level
        st.markdown("## Risk Level")

        if risk == "High":
            st.error(risk)

        elif risk == "Medium":
            st.warning(risk)

        else:
            st.success(risk)

        # Trigger words
        st.markdown("## Trigger Words")

        if found_triggers:

            for word in found_triggers:
                st.write(f"• {word}")

        else:
            st.write("No trigger words detected.")

        # Final Result
        emoji_map = {

            "fear": "⚠️",

            "guilt": "😔",

            "clickbait": "🎯",

            "urgency": "⏳",

            "neutral": "✅"
        }

        st.markdown("## Final Result")

        st.write(
            f"{emoji_map.get(prediction)} This text is classified as **{prediction.upper()}**."
        )

        # Explanation
        st.markdown("## Explanation")

        st.write(
            explanations.get(prediction)
        )

# Footer
st.markdown("---")

st.caption(
    "Developed as part of the SafeScroll Digital Awareness CSP Project"
)

