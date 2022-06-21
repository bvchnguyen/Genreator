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
* For spotify, you will be looking for a Client_ID and a Client_Secret.
* For Youtube, you will need to obtain an API Key after you created a your new project.
* If you plan on using features that requires account access (adding to playlist, etc), then make sure to set up your spotipy object to include
user authentification. You can read more about it in the spotipy README on [github](https://github.com/plamere/spotipy).
## Instructions:

Genre-ator will first ask you for your spotify username -- It'll then go through a validation to make sure such user exists on spotify so that it's able to obtain information and add to playlist accordingly.

![](/screenshots/welcome2.png)

To obtain a channel ID, go to a page that you would like, for demonstration purposes, I will choose the music library channel MrSuicideSheep.

1. Navigating to their page, we obtain a link -- https://www.youtube.com/channel/UC5nc_ZtjKW1htCVZVRxlQAQ
2. The channel ID then be 'UC5nc_ZtjKW1htCVZVRxlQAQ'.
3. Enter this when choosing option '02' in the main menu.
4. Then the program will extract the 10 most recent videos from the channel.
5. The program will search through spotify to validate the song exists, and add it to a generated playlist.

![](/screenshots/transfer.jpg)

## Constraints:
* NOTE that a lot of YouTube's music are bootlegs, unofficial, or some artists are not on spotify yet. This means that the search is not perfect.
* Genre-ator has a name filter implemented to streamline the search. This means that if there exists an official version of the song on spotify, Genre-ator will search for that, BUT NOT the remix/bootleg version. I would recommend trying to find a playlist or channel that has official music.

## Goals:
Finish create a playlist option. :white_check_mark: 

Add generated songs to that particular playlist. 

Implement auto generate function for playlist. :white_check_mark:

Implement a more streamline channel search (instead of having users manually search for the ID or convert to an ID). :o: 

Implement a basic UI and/or switch over to a web stack :o:
