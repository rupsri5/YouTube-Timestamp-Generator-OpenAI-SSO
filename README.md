
# YouTube Timestamp Generator

Welcome to the YouTube Timestamp Generator! This web application allows you to easily generate timestamps for YouTube videos based on their transcripts. With the integration of the OpenAI API, we use transcripts from videos as input, which enables you to create precise timestamps for different sections of the video content. Additionally, our website offers seamless authentication through Google Single Sign-On (SSO), ensuring a hassle-free login/signup process using your Google email ID and also custom login/signup option using username, email and password.

## Features
1. Transcript Fetching: Utilizing the power of the python libraries, we automatically fetch transcripts for YouTube videos, saving you time and effort.

2. Timestamp Generation: Once the transcript is fetched, you can easily create timestamps for the video by simply pasting the video link and clicking on the submit button.

3. Google SSO Integration: Sign up or log in effortlessly using your Google email ID through Google Single Sign-On. No need to remember additional passwords!

## How to use
1. Sign Up/Log In: If you're new to our platform, click on the "Sign Up with Google" button to create an account using your Google email ID. If you're an existing user, simply log in using the same method.

2. Paste YouTube Video Link: Once logged in, paste the link to the YouTube video for which you want to generate timestamps into the designated input field.

5. Create Timestamps: To create timestamps, simply click on the submit button after pasting the link. The generated timestamps will be displayed.

7. Copy/Paste Timestamps: Once you're satisfied with the timestamps, you can use them in your video.

## Getting Started

To run this ```YouTube Timestamp Generator``` locally, follow these steps:

#### 1. Clone the Repository:
```powershell
git clone git@github.com:rupsri5/YouTube-Timestamp-Generator-OpenAI-SSO.git
```

#### 2. Create a Python environment:
Navigate to the Directory and Create Python environment
```powershell
python -m venv venv
```

Activate environment in bash
```bash
source venv/bin/Activate
```
or in powershell
```powershell
.\venv\scripts\Activate
```

#### 3. Install Dependencies:
```powershell
pip install -r requirements.txt
```

#### 4. Set up the keys in a .env file
##### OpenAI API Key
- Firstly, create your OpenAI API key; you can do the same from here https://openai.com/ 
- visit the website login/signup through your account, then select API option. 
- After that you'll be redirected to the page where you can find ```API keys``` option on left navigation bar.
  
##### Google SSO Key
- Go to Google Cloud Console: Visit the Google Cloud Console at console.cloud.google.com.

- Create a Project: If you haven't already, create a new project or select an existing one where you want to set up Google SSO.

- Enable Google Identity Service: In the sidebar menu, navigate to "APIs & Services" > "Credentials". Click on "Create credentials" and select "OAuth client ID".

- Configure OAuth Consent Screen: Choose the application type, provide a name for your application, and configure the required OAuth consent screen details such as user email and product logo.

- Set Up OAuth Client ID: Choose "Web application" as the application type. Enter the authorized redirect URIs where Google will redirect users after authentication (e.g., http://127.0.0.1:8000/oauth/complete/google-oauth2/ for local development). Once configured, Google will provide you with a client ID and client secret.

###### .env file example: Create and add ```your_key``` here: 

```powershell
GOOGLE-AUTH-KEY=""
GOOGLE-AUTH-SECRET=""
OPENAI_API_KEY=""
```

#### 5. Run the App:
```powershell
python manage.py runserver
```

#### 6. Open the App in Your Browser:
Once the app is running, you can access it by opening your web browser and navigating to http://localhost:8000.

