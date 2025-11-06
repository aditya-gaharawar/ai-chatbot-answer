/**
 * Easter Eggs & Hidden Features
 * Because every great app needs a few secrets! 🥚✨
 */

export interface EasterEgg {
	trigger: string | RegExp;
	response: string;
	action?: () => void;
	emoji?: string;
}

/**
 * Collection of Easter eggs
 */
export const EASTER_EGGS: EasterEgg[] = [
	{
		trigger: /^(hello|hi|hey)\s+there$/i,
		response: "General Kenobi! 👋 (Oops, wrong franchise... but hello to you too!)",
		emoji: "👋"
	},
	{
		trigger: /^the answer to life,? the universe,? and everything$/i,
		response: "42! 🌌 (Don't forget your towel!)",
		emoji: "🌌"
	},
	{
		trigger: /^do you like coding\??$/i,
		response: "I love it! It's like poetry, but with more semicolons. 💻✨",
		emoji: "💻"
	},
	{
		trigger: /^sudo make me a sandwich$/i,
		response: "🥪 Here's your sandwich! (With extra permissions on the side)",
		emoji: "🥪"
	},
	{
		trigger: /^(tell me a joke|make me laugh)$/i,
		response: "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😄",
		emoji: "😄"
	},
	{
		trigger: /^(you('re| are) (awesome|amazing|great))$/i,
		response: "No, YOU'RE awesome! 🌟 Now get back to building something amazing!",
		emoji: "🌟"
	},
	{
		trigger: /^(thank you|thanks)$/i,
		response: "You're welcome! Remember: happy coding is the best coding! 😊",
		emoji: "😊"
	},
	{
		trigger: /^(what is love|baby don't hurt me)$/i,
		response: "🎵 Baby don't hurt me... don't hurt me... no more! 🎵 (Now that's stuck in your head!)",
		emoji: "🎵"
	},
	{
		trigger: /^(konami|up up down down)$/i,
		response: "↑ ↑ ↓ ↓ ← → ← → B A START! 🎮 You've unlocked... absolutely nothing! (But you tried, and that's what counts)",
		emoji: "🎮"
	},
	{
		trigger: /^(where are the bugs\??)$/i,
		response: "They're not bugs, they're undocumented features! 🐛✨",
		emoji: "🐛"
	},
	{
		trigger: /^(coffee|i need coffee)$/i,
		response: "☕ Here's a virtual coffee! Fun fact: The first webcam was created at Cambridge to monitor a coffee pot!",
		emoji: "☕"
	},
	{
		trigger: /^(pizza|i('m| am) hungry)$/i,
		response: "🍕 Virtual pizza incoming! No calories, all the satisfaction!",
		emoji: "🍕"
	},
	{
		trigger: /^(are you (a )?robot\??)$/i,
		response: "Beep boop! 🤖 Just kidding... or am I? *winks in binary*",
		emoji: "🤖"
	},
	{
		trigger: /^(show me the (money|code))$/i,
		response: "💰 The best code is the code you don't have to write! But here's a $ anyway.",
		emoji: "💰"
	},
	{
		trigger: /^(it'?s? over 9000!?)$/i,
		response: "WHAT?! 9000?! ⚡ *crushes scouter* There's no way that can be right!",
		emoji: "⚡"
	}
];

/**
 * Check if a message triggers an Easter egg
 */
export function checkEasterEgg(message: string): EasterEgg | null {
	const trimmedMessage = message.trim();

	for (const egg of EASTER_EGGS) {
		if (typeof egg.trigger === 'string') {
			if (trimmedMessage.toLowerCase() === egg.trigger.toLowerCase()) {
				return egg;
			}
		} else if (egg.trigger instanceof RegExp) {
			if (egg.trigger.test(trimmedMessage)) {
				return egg;
			}
		}
	}

	return null;
}

/**
 * Get a random Easter egg response
 */
export function getRandomEasterEggHint(): string {
	const hints = [
		"💡 Psst... try typing 'sudo make me a sandwich'",
		"🎮 Know any Konami codes?",
		"🌌 What's the answer to life, the universe, and everything?",
		"☕ Sometimes saying 'coffee' helps...",
		"🥚 There might be some hidden commands... just saying!",
		"✨ Type 'tell me a joke' for a surprise!"
	];

	return hints[Math.floor(Math.random() * hints.length)];
}

/**
 * ASCII art for special occasions
 */
export const ASCII_CELEBRATIONS = {
	rocket: `
    🚀
   /|\\
  / | \\
 /  |  \\
    |
   / \\
  /   \\
`,
	party: `
  🎉 🎊 🎉
    🎈
   PARTY!
    🎈
  🎊 🎉 🎊
`,
	trophy: `
    ___
   |   |
   | ★ |
   |___|
    |||
   =====
`,
	success: `
   ✓ ✓ ✓
  SUCCESS!
   ✓ ✓ ✓
`
};

/**
 * Special message responses for achievements
 */
export const ACHIEVEMENT_MESSAGES = [
	"🏆 Achievement Unlocked: Easter Egg Hunter!",
	"⭐ You found a secret! Have a virtual high-five! ✋",
	"🎯 Bulls-eye! You discovered a hidden feature!",
	"🔍 Detective skills: Level 100!",
	"🎪 You found the fun! Keep exploring!"
];

/**
 * Get a random achievement message
 */
export function getAchievementMessage(): string {
	return ACHIEVEMENT_MESSAGES[Math.floor(Math.random() * ACHIEVEMENT_MESSAGES.length)];
}
