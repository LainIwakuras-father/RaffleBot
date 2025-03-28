import aiohttp


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
    async def get_raffle(self, randomizer_id: int):
        async with aiohttp.ClientSession() as session:
            response = await session.get(f"{self.base_url}/raffle/{randomizer_id}")
            return await response.json()