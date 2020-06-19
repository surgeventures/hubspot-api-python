import os
from trello import TrelloClient
from services.redis import redis

TOKEN_KEY = "trello_token"


def get_auth_url(key: str, return_url: str, name="HubSpot", expiration="30days", scope="read", response_type="token"):
    return "https://trello.com/1/authorize?key={}&name={}&expiration={}&response_type={}&scope={}&return_url={}".format(
        key, name, expiration, response_type, scope, return_url
    )


def save_token(token):
    redis.set(TOKEN_KEY, token)

    return token


def is_authorized():
    return redis.exists(TOKEN_KEY)


def get_token():
    return redis.get(TOKEN_KEY)


def get_client():
    return TrelloClient(
        api_key=os.getenv("TRELLO_API_KEY"),
        token=get_token(),
    )


def fetch_cards(board_name: str, limit=3):
    client = get_client()
    all_boards = client.list_boards()
    board = next((board for board in all_boards if board.name.lower() == board_name.lower()), None)

    cards = []
    for list in board.list_lists():
        if len(cards) >= limit:
            break
        for card in list.list_cards():
            cards.append(card)
            if len(cards) >= limit:
                break

    return cards
