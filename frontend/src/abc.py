import gradio as gr

# Define a simple function
def sentiment_analysis(text):
    if "good" in text.lower():
        return "Positive Sentiment 😊"
    elif "bad" in text.lower():
        return "Negative Sentiment 😞"
    else:
        return "Neutral Sentiment 😐"

# Create Gradio interface
interface = gr.Interface(
    fn=sentiment_analysis,
    inputs="text",
    outputs="text",
    title="Sentiment Analysis",
    description="Enter a sentence, and the app will determine its sentiment."
)

# Launch the app
interface.launch()
