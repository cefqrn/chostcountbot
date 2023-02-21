from urllib.request import Request, urlopen
from json import dumps
from os import environ

USER_AGENT = "chostcountbot ( contact: cefqrn@gmail.com )"


class WebhookNotFoundError(Exception): ...


try:
    webhook = environ["CHOSTCOUNTBOT_DISCORD_WEBHOOK"]
except KeyError:
    raise WebhookNotFoundError(
        "CHOSTCOUNTBOT_DISCORD_WEBHOOK environment variable not set."
    )


def ping(message: str):
    with urlopen(
        Request(
            url=webhook,
            data=dumps({"content": message}, separators=(",", ":")).encode(),
            headers={
                "Content-Type": "application/json",
                "User-Agent": USER_AGENT
            },
            method="POST"
        )
    ):
        pass