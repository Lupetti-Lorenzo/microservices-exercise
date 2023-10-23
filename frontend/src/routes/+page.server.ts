export const prerender = true;

/** @type {import('./$types').PageServerLoad} */
export async function load() {
	return {
		API_IP: JSON.stringify(process.env)
	};
}
