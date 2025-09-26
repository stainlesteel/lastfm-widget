import fastapi as fp
import fastapi.middleware.cors as cors
import dotenv as env
from pylast import User, LastFMNetwork
import os
import json
import logging

app = fp.FastAPI()

env.load_dotenv()

LASTFM_API_KEY = os.getenv('LASTFM_API_KEY')

nwtrk = LastFMNetwork(
    api_key=LASTFM_API_KEY,
    api_secret="b"
)

orgs = [
    'http://localhost',
    'http://localhost:8080',
]
try:
    with open('urls.json', 'rt') as f:
        json_data = json.loads(f)
    
    print('Retrieved URL data: ', json_data)

    for json in json_data:
        orgs.append(json)
except FileNotFoundError:
    logging.warning('You have not provided a urls.json. App will be accessible only to loopback address.') 
except json.JSONDecodeError:
    logging.error('Failed to parse urls.json. Either there is no such file or it has incorrect syntax.')
    raise SystemExit()

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=orgs,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/main")
async def main(user: str):
    user = User(user, nwtrk) 

    playing = user.get_recent_tracks(limit=1)

    if playing:
        title = playing[0].track.title
        artist = playing[0].track.artist.name
        cops = {'title': title, 'artist': artist}
        return cops
    else:
        return None
        
