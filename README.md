#Spotify Playlist Fetcher with Flask
This is a simple Flask web application that integrates with the Spotify Web API to fetch and display a user's playlists. The app allows users to authenticate with their Spotify account via OAuth2, and once authenticated, it fetches and displays the playlists associated with their account.
Features
Spotify Authentication: Users are redirected to the Spotify authorization page to grant access to their Spotify account using OAuth2 authentication.
Fetch Playlists: After authentication, the app fetches the user's playlists and displays them along with their Spotify URLs.
Session Management: The app uses Flask sessions to store the authentication token, allowing users to access their playlists without re-authenticating until the token expires.
Logout: A logout route is provided to clear the session and log out users.
Tech Stack
Flask: A lightweight Python web framework used for building the web application.
Spotipy: A Python library for interacting with the Spotify Web API, used here to authenticate and fetch playlists.
Spotify Web API: The official API provided by Spotify to interact with user data, such as playlists, albums, and tracks.
Prerequisites
Before running this application, ensure you have the following installed:

Python 3.x
pip (Python's package installer)
Additionally, you'll need to create a Spotify Developer account and set up an application to get your client_id and client_secret. These will be used to authenticate with the Spotify API.

Setup and Installation
Clone the repository:

 
  
git clone https://github.com/yourusername/spotify-playlist-fetcher.git
cd spotify-playlist-fetcher
Create a virtual environment (optional but recommended):

 
  
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

 
  
pip install -r requirements.txt
Configure Spotify Developer Application:

Go to the Spotify Developer Dashboard.
Create a new application and get your client_id and client_secret.
Add http://localhost:5000/callback as the Redirect URI.
Set up environment variables (optional but recommended): You can either update the code directly with your client_id, client_secret, and redirect_uri, or set them as environment variables for better security:

 
  
export SPOTIPY_CLIENT_ID="your_client_id"
export SPOTIPY_CLIENT_SECRET="your_client_secret"
export SPOTIPY_REDIRECT_URI="http://localhost:5000/callback"
Run the Flask app:

 
  
python main.py
Access the app: Open a web browser and go to http://localhost:5000/. You will be prompted to log in to your Spotify account and grant access to the app. Once authenticated, your playlists will be displayed.

How it Works
Home Route (/): When you visit the homepage (/), the app checks if the user is already authenticated by validating the stored access token. If not, it redirects the user to the Spotify authorization page.

Callback Route (/callback): After the user grants permission on the Spotify authorization page, Spotify redirects the user back to the app's callback route. The app then retrieves the access token and stores it in the session.

Get Playlists Route (/get_playlists): Once authenticated, this route fetches the user's playlists from Spotify and displays them in the browser as a list with their respective Spotify URLs.

Logout Route (/logout): This route clears the session, logging the user out, and redirects them to the home page.

Error Handling
If there's an issue fetching the playlists (e.g., invalid token or API issues), the app will display an error message on the page.

Future Improvements
Add pagination support for large numbers of playlists.
Display more detailed playlist information (e.g., track names, cover images).
Use JavaScript or AJAX for more dynamic, real-time interaction without page reloads.
