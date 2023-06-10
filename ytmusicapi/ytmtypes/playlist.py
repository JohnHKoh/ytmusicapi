from pydantic import BaseModel
from typing import Optional
from ytmusicapi.ytmtypes.thumbnail import Thumbnail
from ytmusicapi.ytmtypes.author import Author

class Playlist(BaseModel):
    title: str
    playlistId: str
    thumbnails: list[Thumbnail]
    description: str
    count: Optional[str] = None
    author: Optional[list[Author]] = None