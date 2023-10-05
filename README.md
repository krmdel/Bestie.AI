# BestieAI - Your Shopping Assistant Chatbot

![BestieAI Logo](./assets/bestie_logo.png)

BestieAI is a state-of-the-art LLM-based chatbot tailored for shopping and product recommendation. Acting as your personal sales assistant, it simplifies your shopping journey by understanding your needs, searching for the best options, and listing the top 3 choices.

## Features

- **Seamless Integration**: Built with Streamlit, BestieAI offers an intuitive user interface, making shopping easy and fun.
- **Smart Recommendations**: Uses the power of LLMs to understand your shopping needs and provide accurate product suggestions.
- **Personalization**: Enter your desired product and price range, and let BestieAI do the heavy lifting!
- **Safe Transactions**: With a built-in shopping cart feature, BestieAI ensures a smooth and secure shopping experience.

## Upcoming Features

- **Web Search Integration**: BestieAI will soon have the capability to search the web and fetch product details in real-time.
- **Product Database**: An integrated product database to provide more refined and diverse product recommendations.

## Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    cd YOUR_REPO_NAME
    ```

2. **Install Dependencies**:
    Ensure you have `streamlit`, `langchain`, and other required libraries. You can install them using pip:
    ```bash
    pip install streamlit langchain
    ```

3. **Set API Key**:
    Ensure your OpenAI API key is set in the Streamlit secrets. Update the `st.secrets["OPENAI_API_KEY"]` with your OpenAI API key.

4. **Run the Application**:
    ```bash
    streamlit run your_script_name.py
    ```

## Usage

1. Launch BestieAI and you'll be greeted with a user-friendly interface.
2. Type in the product you're looking for in the text area.
3. Set your desired price range using the slider.
4. Hit the 'Search...' button.
5. BestieAI will provide you with the top 3 product recommendations based on your input.

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Ensure to update tests as appropriate.

## License

[MIT License](https://choosealicense.com/licenses/mit/)

---

Remember to replace placeholders like `YOUR_USERNAME`, `YOUR_REPO_NAME`, and `your_script_name.py` with actual values. Additionally, you might want to add a logo image for BestieAI and place it in an `assets` directory to use it in the README.
