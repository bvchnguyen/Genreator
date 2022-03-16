# Genreator

A python script that extracts a playlist or a series of videos from a youtube channel, search for each song in spotify
and add them to a playlist either by genre or by user's choice.

### Technologies:
Python
Youtube Data API
Spotify API
Spotipy

### Requirements
You will need to a developer's account with Youtube/google and Spotify to obtain API credentials.
For spotify, you will be looking for a Client_ID and a Client_Secret code. Store these in a secrets file.

Once you set up your google developer's account, you would then want to create a new project and select Youtube's
DATA API. Obtaining an API key, you then want to store this in the same secrets file.

MAKE SURE YOU ADD THIS FILE TO YOUR .gitignore to prevent it from being push to your git repository.

### Instructions

To obtain a channel ID, go to a page that you would like, for demonstration purposes, I will choose Chelsea Cutler's youtube page.

* Navigating to her page, we obtain a link -- https://www.youtube.com/channel/UCL7hBIFFV1RAkmyvoXdyzjg
* The channel ID then be 'UCL7hBIFFV1RAkmyvoXdyzjg'.
* Enter this when choosing option '02' in the main menu.
* Then the program will extract up to n amount of videos from the channel, where n is the determined limit.
* The program will then search through spotify and add it to an existing playlist

### Goals (for future implementation)
* Finish create a playlist option
* Add generated songs to that particular playlist
* Implement a more streamline channel search (instead of having users manually search for the ID or convert to an ID)
