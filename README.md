# CALORIE_ADVISOR
# 🥗 Food Calorie Checker - Powered by Gemini 1.5 ✨

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-brightgreen.svg)](https://streamlit.io)
[![Google AI](https://img.shields.io/badge/Google_AI-Gemini_1.5-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) A simple yet powerful web application built with Streamlit that leverages Google's Gemini 1.5 Pro vision model to analyze images of food. Upload a picture, and get an estimated calorie count, nutritional assessment, and more!

---

## 📸 Preview

*Replace this section with an actual screenshot of your running application!*

![App Screenshot](placeholder_screenshot.png)
*(Caption: The Food Calorie Checker interface after analyzing a food image.)*

---

## 🚀 Features

* **🖼️ Easy Image Upload:** Supports JPG, PNG, and JPEG formats.
* **👁️ Food Identification:** Detects the main food items present in the uploaded image.
* **📊 Calorie Estimation:** Provides an approximate calorie count based on the visual portion size.
* **❤️ Health Assessment:** Offers a brief overview of the food's general healthiness (e.g., high sugar, good protein source, etc.).
* **💡 Serving Suggestions (Optional):** May suggest healthier alternatives or preparation methods.
* **🤖 AI-Powered:** Utilizes the advanced multimodal capabilities of Google Gemini 1.5 Flash.
* **💻 Simple Web Interface:** Clean and user-friendly UI built with Streamlit.

---

## 🤔 How It Works

1.  **Upload:** The user uploads an image file containing food via the Streamlit interface.
2.  **Process:** The application uses the Pillow library to open and handle the image.
3.  **Analyze:** The image, along with a structured prompt, is sent to the Google Gemini 1.5 Flash API.
4.  **Respond:** The Gemini model analyzes the image based on the prompt and returns text containing:
    * Identified food(s).
    * Estimated calories (with assumed portion size).
    * Health assessment.
    * Optional suggestions.
5.  **Display:** Streamlit displays the analysis results clearly to the user.

---

## ⚙️ Setup & Installation

Follow these steps to get the Food Calorie Checker running locally:

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Create a `requirements.txt` file with the following content:
    ```txt
    streamlit
    google-generativeai
    python-dotenv
    Pillow
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key:**
    * Obtain a Google API key enabled for the Gemini API from the [Google AI Studio](https://aistudio.google.com/app/apikey).
    * Create a file named `.env` in the project's root directory.
    * Add your API key to the `.env` file like this:
        ```env
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```
    > **Important:** Add `.env` to your `.gitignore` file to avoid committing your secret key!

---

## ▶️ Usage

Once the setup is complete, run the Streamlit application from your terminal:

```bash
streamlit run your_script_name.py
