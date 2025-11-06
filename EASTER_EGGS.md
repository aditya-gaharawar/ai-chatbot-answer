# 🥚 Easter Eggs Guide

Shhh! 🤫 This is a secret list of Easter eggs hidden in AnswerAI. But since you found this file, you deserve to know them all!

## 🎮 Chat Easter Eggs

Try typing these exact phrases in the chat (case-insensitive):

### Greetings
- `hello there` or `hi there` or `hey there` - Get a Star Wars reference!

### Pop Culture References
- `the answer to life, the universe, and everything` - For Hitchhiker's Guide fans
- `what is love` or `baby don't hurt me` - Get that song stuck in your head!
- `konami` or `up up down down` - Classic gamer code
- `it's over 9000!` - Dragon Ball Z reference
- `show me the money` or `show me the code` - Jerry Maguire meets coding

### Fun Commands
- `sudo make me a sandwich` - Classic XKCD reference
- `tell me a joke` or `make me laugh` - Get a programming joke
- `coffee` or `i need coffee` - Get a virtual coffee and a fun fact!
- `pizza` or `i'm hungry` - Virtual pizza delivery!

### Questions
- `do you like coding?` - Ask about coding passion
- `are you a robot?` or `are you robot?` - Find out the truth!
- `where are the bugs?` - Get a philosophical response
- `you're awesome` or `you are amazing` - Positivity gets positivity back!

### Gratitude
- `thank you` or `thanks` - Get a warm response

## ✨ The Surprise Button

The floating sparkly button in the bottom-right corner provides random surprises:

1. **Inspirational Quotes** from famous developers
2. **Tech Jokes** to make you smile
3. **Fun Facts** about computing history
4. **ASCII Art** for text-based beauty
5. **Coding Challenges** to test your skills
6. **Motivational Messages** for tough days
7. **Celebrations** with confetti effects!

### Hidden Behavior
- The button **wiggles every 30 seconds** to grab your attention
- It has a ripple effect when you hover over it
- The tooltip appears when you hover

## 🎯 API Easter Eggs

Developers can call these endpoints directly:

```bash
# Get a random surprise
GET /api/v1/surprises/random

# Get a specific type
GET /api/v1/surprises/quote
GET /api/v1/surprises/joke
GET /api/v1/surprises/fact
GET /api/v1/surprises/art
GET /api/v1/surprises/challenge
GET /api/v1/surprises/celebrate

# Get the same surprise all day
GET /api/v1/surprises/daily
```

## 🎨 Visual Surprises

### Confetti Animation
- Triggered by celebration surprises
- 150 colorful confetti pieces fall from the top
- Physics-based animation with gravity and tilt

### Modal Animations
- The surprise modal pops in with a bounce effect
- Gradient headers for visual appeal
- Smooth transitions and hover effects

## 🏆 Achievement System (Coming Soon!)

While not fully implemented, the codebase includes:
- Achievement messages for finding Easter eggs
- ASCII art for celebrations
- Trophy, rocket, party, and success ASCII art

## 💡 Tips for Easter Egg Hunters

1. **Read the code** - The source is full of comments and fun messages
2. **Try variations** - Some commands have multiple triggers
3. **Check the console** - Sometimes there are hidden messages there too
4. **Be creative** - Not all Easter eggs are documented! 😉

## 🎭 Philosophy

These Easter eggs exist because:
- Coding should be fun
- Surprises make people smile
- Hidden features reward curious users
- A little whimsy goes a long way
- Life is too short for boring software

## 🔮 Undocumented Features

Some Easter eggs aren't listed here... You'll have to find them yourself! Here are some hints:

- Try talking to the AI in different languages
- Look for special dates and times
- Pay attention to button click counts
- Check what happens on your birthday (if configured)
- Some messages might respond to emojis...

## 🎁 Adding Your Own Easter Eggs

Want to contribute? Here's how:

1. **For chat Easter eggs**: Edit `/src/lib/utils/easterEggs.ts`
2. **For surprises**: Edit `/backend/answerai/routers/surprises.py`
3. **For UI effects**: Add to Svelte components with fun animations

Follow the existing patterns, keep it lighthearted, and remember: Easter eggs should delight, not confuse!

---

*Remember: The best Easter eggs are the ones that make you smile unexpectedly!* 😊✨

**Now go forth and discover!** 🚀
