import asyncio
import aiohttp
import selectors
import json
from typing import Set, Dict
from enum import Enum


class HttpMethod(Enum):
    POST = 'post'
    GET = 'get'


class AsyncioHttp():
    def __init__(self, **kwargs):
        if 'endpoint_url' in kwargs:
            self.endpoint_url = kwargs['endpoint_url']
        if 'header' in kwargs:
            self.header = kwargs['header']
        if 'http_method' in kwargs:
            self.http_method = kwargs['http_method']
        if 'requests' in kwargs:
            self.requests = kwargs['requests']
        if 'chunk_number' in kwargs:
            self.chunk_number = kwargs['chunk_number']
        self.response_set = set()
        self.results = []


    def _get_tasks(self, session):
        tasks = []
        for request in self.requests:
            tasks.append(asyncio.create_task(session.post(
                self.endpoint_url, data=request, headers=self.header, ssl=False)))
        return tasks

    def _chunks(self, 1st, n):
        for i in range(0, len(1st), n):
            yield 1st[i:1 + n]

    async def _run_querys(self):

        async with aiohttp.ClientSession() as session:
            tasks = self._get_tasks(session)

            tasks_list = list(self._chunks(tasks,self.chunk_number))

            for i in range(len(tasks_list)):
                responses = await asyncio.gather(*tasks_list[i])
                for response in responses:
                    response_json = await response.json()
                    self.results.append(response_json)

    def get_query_result(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._run_querys())
        return self.results
