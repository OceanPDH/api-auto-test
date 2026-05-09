'''
import requests
from config.config import BASE_URL, TIMEOUT


class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, timeout=self.timeout)
        return response

    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=json, timeout=self.timeout)
        return response

    def put(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=json, timeout=self.timeout)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, timeout=self.timeout)
        return response
'''
'''日志封装'''
import requests
from config.config import BASE_URL, TIMEOUT
from utils.logger import get_logger

logger = get_logger()


class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        response = requests.get(url, params=params, timeout=self.timeout)
        logger.info(f"Response: {response.status_code}")
        return response

    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} | Body: {json}")
        response = requests.post(url, json=json, timeout=self.timeout)
        logger.info(f"Response: {response.status_code}")
        return response

    def put(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url} | Body: {json}")
        response = requests.put(url, json=json, timeout=self.timeout)
        logger.info(f"Response: {response.status_code}")
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = requests.delete(url, timeout=self.timeout)
        logger.info(f"Response: {response.status_code}")
        return response