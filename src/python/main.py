import fastapi as fp
import fastapi.middleware.cors as cors
import dotenv as env
from pylast import User
import os

app = fp.FastAPI()

env.load_dotenv()

LASTFM_API_KEY = os.getenv('LASTFM_API_KEY')

user = User()

orgs = [
    'http://localhost',
    'http://localhost:8080',
    'https://stainlesteel.github.io',
    'https://stainlesteel.netlify.app',
]

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=orgs,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#
#@app.get("/main")
#async def main(user: str):
#
breakpoint()
