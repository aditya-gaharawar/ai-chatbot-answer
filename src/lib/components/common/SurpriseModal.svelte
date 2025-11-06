<script lang="ts">
	import { createEventDispatcher, onMount } from 'svelte';
	import type { SurpriseResponse } from '$lib/apis/surprises';

	export let surprise: SurpriseResponse | null = null;
	export let show = false;

	const dispatch = createEventDispatcher();

	let confettiCanvas: HTMLCanvasElement;
	let confettiInterval: number;

	interface Confetti {
		x: number;
		y: number;
		r: number;
		d: number;
		color: string;
		tilt: number;
		tiltAngleIncrement: number;
		tiltAngle: number;
	}

	function startConfetti() {
		if (!confettiCanvas) return;

		const ctx = confettiCanvas.getContext('2d');
		if (!ctx) return;

		confettiCanvas.width = window.innerWidth;
		confettiCanvas.height = window.innerHeight;

		const confetti: Confetti[] = [];
		const confettiCount = 150;
		const gravity = 0.5;
		const terminalVelocity = 5;
		const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#f9ca24', '#6c5ce7', '#fd79a8'];

		for (let i = 0; i < confettiCount; i++) {
			confetti.push({
				x: Math.random() * confettiCanvas.width,
				y: Math.random() * confettiCanvas.height - confettiCanvas.height,
				r: Math.random() * 6 + 4,
				d: Math.random() * confettiCount,
				color: colors[Math.floor(Math.random() * colors.length)],
				tilt: Math.floor(Math.random() * 10) - 10,
				tiltAngleIncrement: Math.random() * 0.07 + 0.05,
				tiltAngle: 0
			});
		}

		function drawConfetti() {
			if (!ctx) return;
			ctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);

			for (let i = 0; i < confettiCount; i++) {
				const c = confetti[i];
				ctx.beginPath();
				ctx.lineWidth = c.r / 2;
				ctx.strokeStyle = c.color;
				ctx.moveTo(c.x + c.tilt + c.r / 4, c.y);
				ctx.lineTo(c.x + c.tilt, c.y + c.tilt + c.r / 4);
				ctx.stroke();

				c.tiltAngle += c.tiltAngleIncrement;
				c.y += (Math.cos(c.d) + 1 + c.r / 2) / 2;
				c.tilt = Math.sin(c.tiltAngle) * 15;

				if (c.y > confettiCanvas.height) {
					confetti[i] = {
						x: Math.random() * confettiCanvas.width,
						y: -10,
						r: c.r,
						d: c.d,
						color: c.color,
						tilt: c.tilt,
						tiltAngleIncrement: c.tiltAngleIncrement,
						tiltAngle: c.tiltAngle
					};
				}
			}
		}

		confettiInterval = setInterval(drawConfetti, 20) as unknown as number;
	}

	function stopConfetti() {
		if (confettiInterval) {
			clearInterval(confettiInterval);
		}
	}

	function close() {
		show = false;
		stopConfetti();
		dispatch('close');
	}

	$: if (show && surprise?.content?.confetti) {
		setTimeout(() => startConfetti(), 100);
	} else {
		stopConfetti();
	}

	onMount(() => {
		return () => stopConfetti();
	});
</script>

{#if show && surprise}
	<div class="fixed inset-0 z-50 flex items-center justify-center p-4">
		<!-- Backdrop -->
		<div class="absolute inset-0 bg-black/50 backdrop-blur-sm" on:click={close} />

		<!-- Confetti Canvas -->
		{#if surprise.content.confetti}
			<canvas
				bind:this={confettiCanvas}
				class="absolute inset-0 pointer-events-none"
				style="z-index: 51;"
			/>
		{/if}

		<!-- Modal Content -->
		<div
			class="relative z-[52] max-w-2xl w-full bg-white dark:bg-gray-800 rounded-2xl shadow-2xl overflow-hidden animate-modal-pop"
		>
			<!-- Header -->
			<div class="bg-gradient-to-r from-purple-500 to-pink-500 p-6 text-white">
				<div class="flex items-center justify-between">
					<div class="flex items-center gap-3">
						<span class="text-4xl">{surprise.content.emoji || '✨'}</span>
						<h2 class="text-2xl font-bold">
							{#if surprise.type === 'quote'}
								Inspirational Quote
							{:else if surprise.type === 'joke'}
								Tech Humor
							{:else if surprise.type === 'fact'}
								Fun Fact
							{:else if surprise.type === 'ascii_art'}
								ASCII Art
							{:else if surprise.type === 'challenge'}
								Coding Challenge
							{:else if surprise.type === 'motivation'}
								Daily Motivation
							{:else if surprise.type === 'celebration'}
								Celebration!
							{:else}
								Surprise!
							{/if}
						</h2>
					</div>
					<button
						on:click={close}
						class="text-white/80 hover:text-white transition-colors"
						aria-label="Close"
					>
						<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						</svg>
					</button>
				</div>
			</div>

			<!-- Body -->
			<div class="p-8">
				{#if surprise.type === 'quote'}
					<blockquote class="text-xl italic text-gray-700 dark:text-gray-300 mb-4">
						"{surprise.content.quote}"
					</blockquote>
					<p class="text-right text-gray-600 dark:text-gray-400">
						— {surprise.content.author}
					</p>
				{:else if surprise.type === 'joke'}
					<div class="space-y-4">
						<p class="text-lg text-gray-700 dark:text-gray-300">
							{surprise.content.setup}
						</p>
						<p class="text-xl font-semibold text-purple-600 dark:text-purple-400">
							{surprise.content.punchline}
						</p>
					</div>
				{:else if surprise.type === 'fact'}
					<p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
						{surprise.content.fact}
					</p>
				{:else if surprise.type === 'ascii_art'}
					<div>
						<h3 class="text-lg font-semibold mb-4 text-gray-800 dark:text-gray-200">
							{surprise.content.name}
						</h3>
						<pre
							class="text-sm font-mono bg-gray-100 dark:bg-gray-900 p-4 rounded-lg overflow-x-auto">{surprise.content.art}</pre>
					</div>
				{:else if surprise.type === 'challenge'}
					<div class="space-y-4">
						<div>
							<span
								class="inline-block px-3 py-1 rounded-full text-sm font-semibold
                  {surprise.content.difficulty === 'Easy'
									? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'
									: surprise.content.difficulty === 'Medium'
										? 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200'
										: 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200'}"
							>
								{surprise.content.difficulty}
							</span>
						</div>
						<p class="text-lg text-gray-700 dark:text-gray-300">
							{surprise.content.challenge}
						</p>
						<div class="bg-blue-50 dark:bg-blue-900/30 p-4 rounded-lg">
							<p class="text-sm text-blue-700 dark:text-blue-300">
								💡 Hint: {surprise.content.hint}
							</p>
						</div>
					</div>
				{:else if surprise.type === 'motivation'}
					<p class="text-2xl text-center text-gray-700 dark:text-gray-300 leading-relaxed">
						{surprise.content.message}
					</p>
				{:else if surprise.type === 'celebration'}
					<p class="text-3xl text-center text-gray-700 dark:text-gray-300 font-bold">
						{surprise.content.message}
					</p>
				{/if}

				{#if surprise.content.daily}
					<div class="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700">
						<p class="text-sm text-gray-500 dark:text-gray-400 text-center">
							🌅 Your daily inspiration for today
						</p>
					</div>
				{/if}
			</div>

			<!-- Footer -->
			<div class="bg-gray-50 dark:bg-gray-900 px-8 py-4">
				<button
					on:click={close}
					class="w-full bg-gradient-to-r from-purple-500 to-pink-500 text-white py-3 rounded-lg font-semibold hover:shadow-lg transition-all duration-200 hover:scale-105"
				>
					Thanks! 💜
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	@keyframes modal-pop {
		0% {
			transform: scale(0.8);
			opacity: 0;
		}
		50% {
			transform: scale(1.05);
		}
		100% {
			transform: scale(1);
			opacity: 1;
		}
	}

	.animate-modal-pop {
		animation: modal-pop 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
	}
</style>
