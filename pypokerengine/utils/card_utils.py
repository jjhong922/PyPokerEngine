import random

from pypokerengine.engine.card import Card
from pypokerengine.engine.deck import Deck
from pypokerengine.engine.hand_evaluator import HandEvaluator

def gen_cards(cards_str):
    return [Card.from_str(s) for s in cards_str]

def gen_deck(exclude_cards=None):
    deck_ids = range(1, 53)
    if exclude_cards:
        assert isinstance(exclude_cards, list)
        if isinstance(exclude_cards[0], str):
            exclude_cards = [Card.from_str(s) for s in exclude_cards]
        exclude_ids = [card.to_id() for card in exclude_cards]
        deck_ids = [i for i in deck_ids if not i in exclude_ids]
    return Deck(deck_ids)
