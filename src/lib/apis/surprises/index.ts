/**
 * Surprise API Client
 * Because life is better with surprises! ✨
 */

export interface SurpriseContent {
	[key: string]: any;
}

export interface SurpriseResponse {
	type: string;
	content: SurpriseContent;
	timestamp: string;
}

export class SurpriseAPI {
	private baseUrl: string;

	constructor(baseUrl: string = '') {
		this.baseUrl = baseUrl;
	}

	/**
	 * Get a random surprise
	 */
	async getRandomSurprise(token: string): Promise<SurpriseResponse> {
		const response = await fetch(`${this.baseUrl}/api/v1/surprises/random`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});

		if (!response.ok) {
			throw new Error(`Failed to get surprise: ${response.statusText}`);
		}

		return await response.json();
	}

	/**
	 * Get an inspirational quote
	 */
	async getQuote(token: string): Promise<SurpriseResponse> {
		const response = await fetch(`${this.baseUrl}/api/v1/surprises/quote`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});

		if (!response.ok) {
			throw new Error(`Failed to get quote: ${response.statusText}`);
		}

		return await response.json();
	}

	/**
	 * Get a tech joke
	 */
	async getJoke(token: string): Promise<SurpriseResponse> {
		const response = await fetch(`${this.baseUrl}/api/v1/surprises/joke`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});

		if (!response.ok) {
			throw new Error(`Failed to get joke: ${response.statusText}`);
		}

		return await response.json();
	}

	/**
	 * Get a fun fact
	 */
	async getFact(token: string): Promise<SurpriseResponse> {
		const response = await fetch(`${this.baseUrl}/api/v1/surprises/fact`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});

		if (!response.ok) {
			throw new Error(`Failed to get fact: ${response.statusText}`);
		}

		return await response.json();
	}

	/**
	 * Get ASCII art
	 */
	async getArt(token: string): Promise<SurpriseResponse> {
		const response = await fetch(`${this.baseUrl}/api/v1/surprises/art`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});

		if (!response.ok) {
			throw new Error(`Failed to get art: ${response.statusText}`);
		}

		return await response.json();
	}

	/**
	 * Get a coding challenge
	 */
	async getChallenge(token: string): Promise<SurpriseResponse> {
		const response = await fetch(`${this.baseUrl}/api/v1/surprises/challenge`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});

		if (!response.ok) {
			throw new Error(`Failed to get challenge: ${response.statusText}`);
		}

		return await response.json();
	}

	/**
	 * Trigger a celebration
	 */
	async celebrate(token: string): Promise<SurpriseResponse> {
		const response = await fetch(`${this.baseUrl}/api/v1/surprises/celebrate`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});

		if (!response.ok) {
			throw new Error(`Failed to celebrate: ${response.statusText}`);
		}

		return await response.json();
	}

	/**
	 * Get daily inspiration
	 */
	async getDailyInspiration(token: string): Promise<SurpriseResponse> {
		const response = await fetch(`${this.baseUrl}/api/v1/surprises/daily`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});

		if (!response.ok) {
			throw new Error(`Failed to get daily inspiration: ${response.statusText}`);
		}

		return await response.json();
	}
}

// Export singleton instance
export const surpriseAPI = new SurpriseAPI();
