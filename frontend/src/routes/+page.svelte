<script>
	/** @type {import('./$types').PageData} */
	export let data;
	const hello = data.hello;
	const hostname = data.hostname;

	// store for the messages
	import { writable } from "svelte/store";

	const messages = writable(["ciao"]);

	const reciveMessage = async () => {
		try {
			const response = await fetch("/api/reciveMessage"); // Replace with your API endpoint
			if (response.ok) {
				// Handle the successful response here
				const message = await response.text();
				messages.set([...$messages, message]);
			} else {
				// Handle errors
			}
		} catch (error) {
			// Handle network or other errors
		}
		console.log(JSON.stringify($messages));
	};
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

Message from api-server: {hello} <br />
pod name: {hostname}
<br /> <br />
<button on:click={reciveMessage}>QueueMessage</button>

{#each $messages as msg}
	<p>{msg}</p>
{/each}
