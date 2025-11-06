<script lang="ts">
	import { surpriseAPI, type SurpriseResponse } from '$lib/apis/surprises';
	import { onMount } from 'svelte';
	import SurpriseModal from './SurpriseModal.svelte';

	export let token: string = '';

	let showModal = false;
	let currentSurprise: SurpriseResponse | null = null;
	let loading = false;
	let buttonElement: HTMLButtonElement;

	// Add a fun wiggle animation on mount
	let isWiggling = false;

	async function handleSurprise() {
		if (!token || loading) return;

		loading = true;
		try {
			currentSurprise = await surpriseAPI.getRandomSurprise(token);
			showModal = true;
		} catch (error) {
			console.error('Failed to get surprise:', error);
		} finally {
			loading = false;
		}
	}

	// Easter egg: wiggle the button every 30 seconds to attract attention
	onMount(() => {
		const wiggleInterval = setInterval(() => {
			isWiggling = true;
			setTimeout(() => {
				isWiggling = false;
			}, 1000);
		}, 30000); // Every 30 seconds

		return () => clearInterval(wiggleInterval);
	});
</script>

<div class="surprise-button-container">
	<button
		bind:this={buttonElement}
		on:click={handleSurprise}
		disabled={loading || !token}
		class="surprise-button {isWiggling ? 'wiggle' : ''} {loading ? 'loading' : ''}"
		title="Click for a surprise! ✨"
		aria-label="Get a surprise"
	>
		{#if loading}
			<svg class="animate-spin h-6 w-6" fill="none" viewBox="0 0 24 24">
				<circle
					class="opacity-25"
					cx="12"
					cy="12"
					r="10"
					stroke="currentColor"
					stroke-width="4"
				/>
				<path
					class="opacity-75"
					fill="currentColor"
					d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
				/>
			</svg>
		{:else}
			<span class="text-2xl">✨</span>
		{/if}
	</button>

	<div class="tooltip">
		Surprise Me!
	</div>
</div>

<SurpriseModal bind:show={showModal} surprise={currentSurprise} />

<style>
	.surprise-button-container {
		position: relative;
		display: inline-block;
	}

	.surprise-button {
		width: 56px;
		height: 56px;
		border-radius: 50%;
		background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
		border: none;
		color: white;
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
		box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
		transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
		position: relative;
		overflow: hidden;
	}

	.surprise-button::before {
		content: '';
		position: absolute;
		top: 50%;
		left: 50%;
		width: 0;
		height: 0;
		border-radius: 50%;
		background: rgba(255, 255, 255, 0.3);
		transform: translate(-50%, -50%);
		transition: width 0.6s, height 0.6s;
	}

	.surprise-button:hover:not(:disabled)::before {
		width: 300px;
		height: 300px;
	}

	.surprise-button:hover:not(:disabled) {
		transform: scale(1.1);
		box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
	}

	.surprise-button:active:not(:disabled) {
		transform: scale(0.95);
	}

	.surprise-button:disabled {
		opacity: 0.6;
		cursor: not-allowed;
	}

	.surprise-button.loading {
		background: linear-gradient(135deg, #a8b8f0 0%, #b197ca 100%);
	}

	@keyframes wiggle {
		0%,
		100% {
			transform: rotate(0deg);
		}
		10%,
		30%,
		50%,
		70%,
		90% {
			transform: rotate(-10deg);
		}
		20%,
		40%,
		60%,
		80% {
			transform: rotate(10deg);
		}
	}

	.surprise-button.wiggle {
		animation: wiggle 1s ease-in-out;
	}

	.tooltip {
		position: absolute;
		bottom: 100%;
		left: 50%;
		transform: translateX(-50%) translateY(-8px);
		background: rgba(0, 0, 0, 0.8);
		color: white;
		padding: 6px 12px;
		border-radius: 6px;
		font-size: 12px;
		white-space: nowrap;
		opacity: 0;
		pointer-events: none;
		transition: opacity 0.3s;
	}

	.tooltip::after {
		content: '';
		position: absolute;
		top: 100%;
		left: 50%;
		transform: translateX(-50%);
		border: 5px solid transparent;
		border-top-color: rgba(0, 0, 0, 0.8);
	}

	.surprise-button-container:hover .tooltip {
		opacity: 1;
	}

	@media (max-width: 768px) {
		.surprise-button {
			width: 48px;
			height: 48px;
		}

		.surprise-button span {
			font-size: 1.5rem;
		}
	}
</style>
