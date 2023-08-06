import asyncio
import aiohttp
import logging
import sys
from prometheus_client import start_http_server, Summary, Counter, Gauge, Histogram
import logging
import sys
import datetime

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
logger = root

URL = 'http://web/ping'
REQUEST_TIME = Histogram('request_timings', 'timings', buckets=(i * 200 for i in range(100)))
OKS = Gauge('oks', '200')
ERRORS = Gauge('errors', '500')


async def request():
    start = datetime.datetime.now()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as resp:
                if resp.status == 200:
                    OKS.inc(1)
                else:
                    ERRORS.inc(1)
    except Exception as exc:
        logger.info(f'Error {exc}')
    finally:
        await asyncio.sleep(0.1)
        logger.info('Sleeping completed')
        end = datetime.datetime.now()
        logger.info('Timer ended')
        delta = (end - start).total_seconds() * 1000
        logger.info(f'Timedelta: {delta}')
        REQUEST_TIME.observe(delta)


async def main():
    logger.info('Start job')
    start_http_server(8000)
    logger.info('Prometheus started')
    while True:
        tasks = [request() for _ in range(10)]
        await asyncio.gather(*tasks)
        logger.info('Iteration completed')


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
