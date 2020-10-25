import json
import re
import datetime
import aiohttp

API_URL = "https://srhpyqt94yxb.statuspage.io/api/v2/summary.json"
TIME_FORMAT = re.compile(r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}).(\d{3})-07:00$")
# ex: 2020-10-22T03:09:28.892-07:00
TIMEZONE_TIJUANA = datetime.timezone(datetime.timedelta(hours=-7))


class DiscordStatus:
    def __init__(self, base_json: dict):
        self._sort(base_json)

    @classmethod
    async def request(cls):
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL) as resp:
                text = await resp.text()
                base_dict = json.loads(text)
                return cls(base_dict)

    def _sort(self, base_json: dict):
        # updated_at
        updated_time_re = TIME_FORMAT.match(base_json["page"]["updated_at"])
        updated_time = datetime.datetime(*map(int, updated_time_re.groups()), TIMEZONE_TIJUANA)
        self.updated_at = updated_time
