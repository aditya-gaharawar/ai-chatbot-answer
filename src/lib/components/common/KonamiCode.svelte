<script lang="ts">
	import { onMount } from 'svelte';
	import { surpriseAPI } from '$lib/apis/surprises';

	let activated = false;
	let showMessage = false;

	// Konami Code: ↑ ↑ ↓ ↓ ← → ← → B A
	const konamiCode = [
		'ArrowUp',
		'ArrowUp',
		'ArrowDown',
		'ArrowDown',
		'ArrowLeft',
		'ArrowRight',
		'ArrowLeft',
		'ArrowRight',
		'b',
		'a'
	];

	let konamiIndex = 0;

	function handleKeyPress(event: KeyboardEvent) {
		const key = event.key.toLowerCase();

		if (key === konamiCode[konamiIndex] || event.key === konamiCode[konamiIndex]) {
			konamiIndex++;

			if (konamiIndex === konamiCode.length) {
				activateKonamiCode();
				konamiIndex = 0;
			}
		} else {
			konamiIndex = 0;
		}
	}

	function activateKonamiCode() {
		if (activated) return;

		activated = true;
		showMessage = true;

		// Create rainbow effect on body
		document.body.style.animation = 'rainbow 3s linear infinite';

		// Show message for 5 seconds
		setTimeout(() => {
			showMessage = false;
			document.body.style.animation = '';
			setTimeout(() => {
				activated = false;
			}, 1000);
		}, 5000);
	}

	onMount(() => {
		window.addEventListener('keydown', handleKeyPress);

		// Add rainbow animation to document if not exists
		if (!document.getElementById('konami-styles')) {
			const style = document.createElement('style');
			style.id = 'konami-styles';
			style.textContent = `
        @keyframes rainbow {
          0% { filter: hue-rotate(0deg); }
          100% { filter: hue-rotate(360deg); }
        }
        @keyframes konami-bounce {
          0%, 100% { transform: scale(1) rotate(0deg); }
          25% { transform: scale(1.1) rotate(-5deg); }
          75% { transform: scale(1.1) rotate(5deg); }
        }
      `;
			document.head.appendChild(style);
		}

		return () => {
			window.removeEventListener('keydown', handleKeyPress);
		};
	});
</script>

{#if showMessage}
	<div class="konami-message">
		<div class="konami-content">
			<div class="konami-title">🎮 KONAMI CODE ACTIVATED! 🎮</div>
			<div class="konami-subtitle">↑ ↑ ↓ ↓ ← → ← → B A</div>
			<div class="konami-text">You've unlocked the secret rainbow mode! ✨</div>
			<div class="konami-emoji">🌈 🎉 🌈 🎉 🌈</div>
		</div>
	</div>
{/if}

<style>
	.konami-message {
		position: fixed;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		z-index: 9999;
		background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
		padding: 40px 60px;
		border-radius: 20px;
		box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
		animation: konami-bounce 0.5s ease-in-out;
		text-align: center;
		color: white;
	}

	.konami-content {
		display: flex;
		flex-direction: column;
		gap: 15px;
		align-items: center;
	}

	.konami-title {
		font-size: 32px;
		font-weight: bold;
		text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
		animation: konami-bounce 1s ease-in-out infinite;
	}

	.konami-subtitle {
		font-size: 24px;
		font-family: monospace;
		background: rgba(255, 255, 255, 0.2);
		padding: 10px 20px;
		border-radius: 10px;
	}

	.konami-text {
		font-size: 18px;
		opacity: 0.9;
	}

	.konami-emoji {
		font-size: 36px;
		animation: konami-bounce 0.8s ease-in-out infinite;
	}

	@media (max-width: 768px) {
		.konami-message {
			padding: 30px 40px;
		}

		.konami-title {
			font-size: 24px;
		}

		.konami-subtitle {
			font-size: 18px;
		}

		.konami-text {
			font-size: 16px;
		}

		.konami-emoji {
			font-size: 28px;
		}
	}
</style>
