<script>
	/** @type {import('./$types').PageData} */
	export let data;
	const hello = data.hello;
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

Message from api-server: {hello}
