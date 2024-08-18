import base64
import json
from typing import List, Optional
from urllib.parse import urlencode

import requests
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message


class RestClient:

    def __init__(self, rest_address: str):
        self._session = requests.session()
        self.rest_address = rest_address

    def get(
        self,
        url_base_path: str,
        request: Optional[Message] = None,
        used_params: Optional[List[str]] = None,
    ) -> bytes:
        url = self._make_url(
            url_base_path=url_base_path, request=request, used_params=used_params
        )

        response = self._session.get(url=url)
        if response.status_code != 200:
            raise RuntimeError(
                f"Error when sending a GET request.\n Response: {response.status_code}, {str(response.content)})"
            )
        return response.content

    def _make_url(
        self,
        url_base_path: str,
        request: Optional[Message] = None,
        used_params: Optional[List[str]] = None,
    ) -> str:
        json_request = MessageToDict(request) if request else {}

        # Remove params that are already in url_base_path
        for param in used_params or []:
            json_request.pop(param)

        url_encoded_request = self._url_encode(json_request)

        url = f"{self.rest_address}{url_base_path}"
        if url_encoded_request:
            url = f"{url}?{url_encoded_request}"

        return url

    def post(self, url_base_path: str, request: Message) -> bytes:
        json_request = MessageToDict(request)

        # Workaround
        if "tx" in json_request:
            if "body" in json_request["tx"]:
                if "messages" in json_request["tx"]["body"]:
                    for message in json_request["tx"]["body"]["messages"]:
                        if "msg" in message:
                            message["msg"] = json.loads(
                                base64.b64decode(message["msg"])
                            )

        headers = {"Content-type": "application/json", "Accept": "application/json"}
        response = self._session.post(
            url=f"{self.rest_address}{url_base_path}",
            json=json_request,
            headers=headers,
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Error when sending a POST request.\n Request: {json_request}\n Response: {response.status_code}, {str(response.content)})"
            )
        return response.content

    @staticmethod
    def _url_encode(json_request):
        for outer_k, outer_v in json_request.copy().items():
            if isinstance(outer_v, dict):
                for inner_k, inner_v in outer_v.items():
                    json_request[f"{outer_k}.{inner_k}"] = inner_v
                json_request.pop(outer_k)

        return urlencode(json_request, doseq=True)

    def __del__(self):
        self._session.close()
