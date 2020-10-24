import json
import aiohttp

API_URL = "https://srhpyqt94yxb.statuspage.io/api/v2/summary.json"

class DiscordStatus:
    def __init__(self, json: dict):
        pass

    @classmethod
    async def request(cls):
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL) as resp:
                base_dict = json.loads(resp.text())
                return cls(base_dict)
