# Genre-ator

A python script that extracts a playlist or a series of videos from a youtube channel, search for each song in spotify
and add them to a playlist either by genre or by user's choice.

## Technologies & Documentation:
* Python

* Youtube Data API - https://developers.google.com/youtube/v3

* Spotify API - https://developer.spotify.com/documentation/web-api/

* Spotipy - https://spotipy.readthedocs.io/en/2.19.0/

## Requirements:
You will need to a developer's account with Youtube/google and Spotify to obtain API credentials.
For spotify, you will be looking for a Client_ID and a Client_Secret code. Store these in a secrets file.

Once you set up your google developer's account, you would then want to create a new project and select Youtube's
DATA API. Obtaining an API key, you then want to store this in the same secrets file.

MAKE SURE YOU ADD THIS FILE TO YOUR .gitignore to prevent it from being push to your git repository.

## Instructions:

Genre-ator will first ask you for your spotify username -- It'll then go through a validation to make sure such user exists on spotify so that it's able to obtain information and add to playlist accordingly.

![](/screenshots/welcome2.png)

To obtain a channel ID, go to a page that you would like, for demonstration purposes, I will choose the music library channel MrSuicideSheep.

* Navigating to their page, we obtain a link -- https://www.youtube.com/channel/UC5nc_ZtjKW1htCVZVRxlQAQ
* The channel ID then be 'UC5nc_ZtjKW1htCVZVRxlQAQ'.
* Enter this when choosing option '02' in the main menu.
* Then the program will extract up to n amount of videos from the channel, where n is the determined limit.
* The program will then search through spotify and add it to an existing playlist
* NOTE that a lot of YouTube's music are bootlegs, unofficial, or some artists are not on spotify yet. This means that the search is not perfect.
* Genre-ator has a name filter implemented to streamline the search. This means that if there exists an official version of the song on spotify, Genre-ator will search for that, BUT NOT the remix/bootleg version. I would recommend trying to find a playlist or channel that has official music.

![](/screenshots/extraction.png)

## Goals (for future implementation):
* Finish create a playlist option
* Add generated songs to that particular playlist
* Implement a more streamline channel search (instead of having users manually search for the ID or convert to an ID)
