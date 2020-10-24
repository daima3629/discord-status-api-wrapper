import json
import re
import datetime
import aiohttp

API_URL = "https://srhpyqt94yxb.statuspage.io/api/v2/summary.json"
TIME_FORMAT = re.compile(r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):({\d{2}}):({\d{2}}).(\d{3})-07:00$")
# ex: 2020-10-22T03:09:28.892-07:00
TIMEZONE_TIJUANA = datetime.timedelta(hours=-7)


class DiscordStatus:
    def __init__(self, base_json: dict):
        pass

    @classmethod
    async def request(cls):
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL) as resp:
                base_dict = json.loads(resp.text())
                return cls(base_dict)

    def _sort(self, base_json: dict):
        updated_time_re = TIME_FORMAT.match(base_json)
        update_time = datetime.datetime(*map(int, updated_time_re.groups(0, 1, 2, 3, 4, 5, 6)), TIMEZONE_TIJUANA)
        self.uptate_at = update_time
