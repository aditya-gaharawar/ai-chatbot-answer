"""
Surprise Feature Router - Because everyone loves a good surprise! 🎉
"""

import random
from datetime import datetime
from typing import Dict, Any

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from answerai.config import ENABLE_ADMIN_CHAT_ACCESS
from answerai.utils.auth import get_verified_user
from answerai.models.auths import UserModel


router = APIRouter()


class SurpriseResponse(BaseModel):
    type: str
    content: Dict[str, Any]
    timestamp: str


# Collection of surprises
INSPIRATIONAL_QUOTES = [
    {"quote": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"quote": "Code is like humor. When you have to explain it, it's bad.", "author": "Cory House"},
    {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
    {"quote": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
    {"quote": "Make it work, make it right, make it fast.", "author": "Kent Beck"},
    {"quote": "The only way to learn a new programming language is by writing programs in it.", "author": "Dennis Ritchie"},
    {"quote": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
    {"quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "author": "Martin Fowler"},
]

TECH_JOKES = [
    {"setup": "Why do programmers prefer dark mode?", "punchline": "Because light attracts bugs! 🐛"},
    {"setup": "Why do Java developers wear glasses?", "punchline": "Because they can't C# 😎"},
    {"setup": "How many programmers does it take to change a light bulb?", "punchline": "None. It's a hardware problem! 💡"},
    {"setup": "What's a programmer's favorite place?", "punchline": "Foo Bar! 🍺"},
    {"setup": "Why did the programmer quit his job?", "punchline": "Because he didn't get arrays! 💰"},
    {"setup": "What do you call a programmer from Finland?", "punchline": "Nerdic! 🇫🇮"},
]

FUN_FACTS = [
    "The first computer bug was an actual bug! In 1947, a moth was found trapped in a relay of the Harvard Mark II computer.",
    "The first computer programmer was Ada Lovelace in the 1840s, about 100 years before the first modern computer was built!",
    "The first 1GB hard drive, released in 1980, weighed over 500 pounds and cost $40,000.",
    "Python was named after Monty Python's Flying Circus, not the snake! 🐍",
    "The original name of Windows was 'Interface Manager'.",
    "The first domain ever registered was Symbolics.com on March 15, 1985.",
    "The first email was sent in 1971 by Ray Tomlinson to himself as a test.",
]

ASCII_ART = [
    {
        "name": "Robot",
        "art": """
    ╔═══╗
    ║ ◉ ║  Beep boop!
    ╚═╤═╝  I'm here to help!
      ║
    ╔═╧═╗
    ║   ║
    ╚═══╝
        """
    },
    {
        "name": "Computer",
        "art": """
    ┌─────────────────┐
    │ > Code is Art  │
    │ > Keep Coding! │
    └─────────────────┘
         │││││││
        ═══════════
        """
    },
    {
        "name": "Trophy",
        "art": """
        ___
       '   `
      |  ★  |  You're
       '._.‚   Awesome!
        ║║║
       ═════
        """
    },
    {
        "name": "Rocket",
        "art": """
         /\\
        |  |
        |  |   To the moon! 🚀
       /____\\
      | o  o |
      |______|
       /|  |\\
        """
    },
    {
        "name": "Cat",
        "art": """
     /\\_/\\
    ( o.o )  Meow!
     > ^ <   *purr*
    /|   |\\
        """
    }
]

CODING_CHALLENGES = [
    {
        "challenge": "Write a function that reverses a string without using built-in reverse methods",
        "difficulty": "Easy",
        "hint": "Try using a loop and string concatenation!"
    },
    {
        "challenge": "Implement a function to check if a number is prime",
        "difficulty": "Easy",
        "hint": "A prime number is only divisible by 1 and itself"
    },
    {
        "challenge": "Create a function that finds the longest palindrome in a string",
        "difficulty": "Medium",
        "hint": "Consider expanding around each character"
    },
    {
        "challenge": "Write a function to detect if two strings are anagrams",
        "difficulty": "Easy",
        "hint": "Anagrams have the same characters in different orders"
    },
]

MINI_GAMES = [
    {
        "name": "Number Guessing Game",
        "description": "I'm thinking of a number between 1 and 100!",
        "secret_number": random.randint(1, 100),
        "instructions": "Try to guess it! Use the chat to make your guesses."
    }
]

MOTIVATIONAL_MESSAGES = [
    "🌟 You're doing amazing! Keep up the great work!",
    "💪 Every expert was once a beginner. Keep learning!",
    "🚀 Your code today is better than your code yesterday!",
    "✨ Debugging is just another way of learning!",
    "🎯 Small progress is still progress. Keep going!",
    "🌈 Your creativity makes the world better through code!",
    "⚡ You've got this! One line of code at a time!",
]


def generate_inspirational_quote() -> Dict[str, Any]:
    """Generate a random inspirational quote"""
    quote_data = random.choice(INSPIRATIONAL_QUOTES)
    return {
        "type": "quote",
        "content": {
            "quote": quote_data["quote"],
            "author": quote_data["author"],
            "emoji": "💭"
        }
    }


def generate_tech_joke() -> Dict[str, Any]:
    """Generate a random tech joke"""
    joke = random.choice(TECH_JOKES)
    return {
        "type": "joke",
        "content": {
            "setup": joke["setup"],
            "punchline": joke["punchline"],
            "emoji": "😄"
        }
    }


def generate_fun_fact() -> Dict[str, Any]:
    """Generate a random fun fact"""
    fact = random.choice(FUN_FACTS)
    return {
        "type": "fact",
        "content": {
            "fact": fact,
            "emoji": "🤓"
        }
    }


def generate_ascii_art() -> Dict[str, Any]:
    """Generate random ASCII art"""
    art = random.choice(ASCII_ART)
    return {
        "type": "ascii_art",
        "content": {
            "name": art["name"],
            "art": art["art"],
            "emoji": "🎨"
        }
    }


def generate_coding_challenge() -> Dict[str, Any]:
    """Generate a random coding challenge"""
    challenge = random.choice(CODING_CHALLENGES)
    return {
        "type": "challenge",
        "content": {
            "challenge": challenge["challenge"],
            "difficulty": challenge["difficulty"],
            "hint": challenge["hint"],
            "emoji": "💻"
        }
    }


def generate_mini_game() -> Dict[str, Any]:
    """Generate a mini game"""
    game = MINI_GAMES[0].copy()
    game["secret_number"] = random.randint(1, 100)
    return {
        "type": "game",
        "content": {
            "name": game["name"],
            "description": game["description"],
            "instructions": game["instructions"],
            "emoji": "🎮"
        }
    }


def generate_motivational_message() -> Dict[str, Any]:
    """Generate a motivational message"""
    message = random.choice(MOTIVATIONAL_MESSAGES)
    return {
        "type": "motivation",
        "content": {
            "message": message,
            "emoji": "✨"
        }
    }


def generate_celebration() -> Dict[str, Any]:
    """Generate a celebration message with confetti"""
    return {
        "type": "celebration",
        "content": {
            "message": "🎉 Surprise! You're awesome! 🎉",
            "confetti": True,
            "emoji": "🎊"
        }
    }


SURPRISE_GENERATORS = [
    generate_inspirational_quote,
    generate_tech_joke,
    generate_fun_fact,
    generate_ascii_art,
    generate_coding_challenge,
    generate_motivational_message,
    generate_celebration,
]


@router.get("/random")
async def get_random_surprise(user: UserModel = Depends(get_verified_user)):
    """
    Get a random surprise!
    Can be a quote, joke, fact, ASCII art, challenge, or celebration.
    """
    generator = random.choice(SURPRISE_GENERATORS)
    surprise = generator()

    return SurpriseResponse(
        type=surprise["type"],
        content=surprise["content"],
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/quote")
async def get_inspirational_quote(user: UserModel = Depends(get_verified_user)):
    """Get an inspirational quote"""
    surprise = generate_inspirational_quote()
    return SurpriseResponse(
        type=surprise["type"],
        content=surprise["content"],
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/joke")
async def get_tech_joke(user: UserModel = Depends(get_verified_user)):
    """Get a tech joke"""
    surprise = generate_tech_joke()
    return SurpriseResponse(
        type=surprise["type"],
        content=surprise["content"],
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/fact")
async def get_fun_fact(user: UserModel = Depends(get_verified_user)):
    """Get a fun tech fact"""
    surprise = generate_fun_fact()
    return SurpriseResponse(
        type=surprise["type"],
        content=surprise["content"],
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/art")
async def get_ascii_art(user: UserModel = Depends(get_verified_user)):
    """Get ASCII art"""
    surprise = generate_ascii_art()
    return SurpriseResponse(
        type=surprise["type"],
        content=surprise["content"],
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/challenge")
async def get_coding_challenge(user: UserModel = Depends(get_verified_user)):
    """Get a coding challenge"""
    surprise = generate_coding_challenge()
    return SurpriseResponse(
        type=surprise["type"],
        content=surprise["content"],
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/celebrate")
async def get_celebration(user: UserModel = Depends(get_verified_user)):
    """Trigger a celebration!"""
    surprise = generate_celebration()
    return SurpriseResponse(
        type=surprise["type"],
        content=surprise["content"],
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/daily")
async def get_daily_inspiration(user: UserModel = Depends(get_verified_user)):
    """
    Get daily inspiration based on the current date
    Same surprise for the same day
    """
    # Use date as seed for consistent daily surprise
    today = datetime.utcnow().date()
    seed = int(today.strftime("%Y%m%d"))
    random.seed(seed)

    generator = random.choice(SURPRISE_GENERATORS)
    surprise = generator()

    # Reset random seed
    random.seed()

    return SurpriseResponse(
        type=f"daily_{surprise['type']}",
        content={**surprise["content"], "daily": True},
        timestamp=datetime.utcnow().isoformat()
    )
