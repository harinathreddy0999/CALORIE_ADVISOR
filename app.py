import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image, UnidentifiedImageError

# Load environment variables
load_dotenv()

# Configure Google Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found. Please set GOOGLE_API_KEY in your .env file.")
    st.stop()

try:
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Error configuring the Google Gemini API: {e}")
    st.stop()

# Function to load Gemini 1.5 model and get response
def get_gemini_response(input_prompt, image_object):
    """
    Sends the prompt and image to the Gemini 1.5 model.

    Args:
        input_prompt (str): The text prompt for the model.
        image_object (PIL.Image.Image): The image to analyze.

    Returns:
        str: The text response from the model or an error message.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model
        response = model.generate_content([input_prompt, image_object])

        if not response.parts:
            try:
                feedback = response.prompt_feedback
                block_reason = feedback.block_reason
                safety_ratings = feedback.safety_ratings
                return f"Error: Response generation failed. Reason: {block_reason}. Safety Ratings: {safety_ratings}"
            except (AttributeError, IndexError):
                return "Error: Could not generate response. The content might be blocked or the API returned an unexpected empty response."

        return response.text
    except Exception as e:
        return f"Error during Gemini API call: {str(e)}"

# --- Streamlit UI ---
st.set_page_config(page_title="Food Calorie Checker", page_icon="🥗")
st.title("🥗 Food Calorie Checker - Powered by Gemini 1.5")

uploaded_file = st.file_uploader("📤 Upload an image of your food", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)

        st.write("⏳ Analyzing the food image...")

        input_prompt = """
        Analyze the food item(s) in this image. Please provide the following information:
        1.  **Food Identification:** Identify the main food item(s) visible.
        2.  **Estimated Calories:** Provide an estimated calorie count for the portion shown in the image. If possible, mention the approximate portion size you are assuming (e.g., grams, cups, ounces).
        3.  **Health Assessment:** Briefly explain whether the food, as depicted, is generally considered healthy or unhealthy. Mention key nutritional aspects (e.g., high in sugar, good source of fiber/protein, vitamins, saturated fats, etc.).
        4.  **Serving Suggestion (Optional):** If relevant, suggest a healthier alternative or a way to make the meal healthier.

        Present the information clearly, perhaps using bullet points or distinct sections.
        """

        response_text = get_gemini_response(input_prompt, image)

        st.write("---")
        st.subheader("🍽️ Food Analysis Results:")
        st.write(response_text)

    except UnidentifiedImageError:
        st.error("Error: Could not identify or open the image file. Please upload a valid image (JPG, PNG, JPEG). The file might be corrupted.")
    except Exception as e:
        st.error(f"An unexpected error occurred while processing the image: {str(e)}")
else:
    st.info("☝️ Upload an image containing food to get started!")
