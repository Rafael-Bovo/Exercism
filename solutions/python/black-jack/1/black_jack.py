"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """

    if card == 'J' or card == 'Q' or card == 'K' :
        return 10

    if card == 'A':
        return 1

    card = int(card)
    return card


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    if card_one in ('J', 'Q', 'K'):
        card_one_numerical = 10

    elif card_one in ('A'):
        card_one_numerical = 1

    elif card_one.isdigit() and int(card_one) >= 2:
        card_one_numerical = int(card_one)

    
    if card_two in ('J', 'Q', 'K'):
        card_two_numerical = 10

    elif card_two in ('A'):
        card_two_numerical = 1

    elif card_two.isdigit() and int(card_two) >= 2:
        card_two_numerical = int(card_two)

    if card_one_numerical == card_two_numerical:
        return (card_one, card_two)

    elif card_one_numerical > card_two_numerical:
        return(card_one)

    return(card_two)

            
        


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    if card_one in ('J', 'Q', 'K'):
        card_one_numerical = 10

    elif card_one in ('A'):
        card_one_numerical = 11
        
    elif card_one.isdigit() and int(card_one) >= 2:
        card_one_numerical = int(card_one)

    
    if card_two in ('J', 'Q', 'K'):
        card_two_numerical = 10

    elif card_two in ('A'):
        card_two_numerical = 11

    elif card_two.isdigit() and int(card_two) >= 2:
        card_two_numerical = int(card_two)

    cards_sum = card_one_numerical + card_two_numerical

    if cards_sum + 11 <= 21:
        return 11
    return 1
        

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    if card_one in ('J', 'Q', 'K'):
        card_one_value = 10

    elif card_one == 'A':
        card_one_value = 11

    elif card_one.isdigit() and int(card_one) >= 2:
         card_one_value = int(card_one)

    if card_two in ('J', 'Q', 'K'):
        card_two_value = 10

    elif card_two == 'A':
        card_two_value = 11

    elif card_two.isdigit() and int(card_two) >= 2:
         card_two_value = int(card_two)

    if card_one_value + card_two_value == 21:
        return True

    return False



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """


    if card_one in ('J', 'Q', 'K'):
        card_one_value = 10

    elif card_one == 'A':
        card_one_value = 11

    elif card_one.isdigit() and int(card_one) >= 2:
         card_one_value = int(card_one)

    if card_two in ('J', 'Q', 'K'):
        card_two_value = 10

    elif card_two == 'A':
        card_two_value = 11

    elif card_two.isdigit() and int(card_two) >= 2:
         card_two_value = int(card_two)

    if card_one_value == card_two_value:
        return True

    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if card_one in ('J', 'Q', 'K'):
        card_one_value = 10

    elif card_one == 'A':
        card_one_value = 1

    elif card_one.isdigit() and int(card_one) >= 2:
         card_one_value = int(card_one)

    if card_two in ('J', 'Q', 'K'):
        card_two_value = 10

    elif card_two == 'A':
        card_two_value = 1

    elif card_two.isdigit() and int(card_two) >= 2:
         card_two_value = int(card_two)

    if card_one_value + card_two_value in (9,10,11):
        return True

    return False