# DeepSolv Assignment

## Overview

This project is designed to develop and deploy a chatbot application using the OpenAI GPT-3 API. The application involves scraping web content and extracting YouTube transcripts, which are then used for generating responses through the chatbot.

## Installation

### Prerequisites

Ensure you have Python 3.8+ installed. Install the required packages using:

```bash
pip install -r requirements.txt

### Environment Variables
Create a .env file in the root directory and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key

## Running the Application
To start the application, run:
python app.py
This will initialize the chatbot and begin the interactive session.

## Code Explanation
### app.py
This is the main entry point of the application. It initializes the chatbot and runs the application using environment variables loaded from the .env file.

### src/chatbot/chatbot_interface.py
Defines the main function for the chatbot interface, which is used to interact with the user and handle chatbot queries.

### src/chatbot/query_gpt3.py
Contains the function to query the OpenAI GPT-3 API and retrieve responses based on user input.

### src/data_extraction/get_youtube_transcript.py
Handles extraction of transcripts from YouTube videos.

### src/data_extraction/scrape_website.py
Scrapes and extracts text content from websites.

### src/utils/config.py
Stores configuration details, including API keys and other settings.

## License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.

## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Create a new Pull Request.

## Contact
For any inquiries or support, please reach out to shubhamdaskgp@gmail.com.