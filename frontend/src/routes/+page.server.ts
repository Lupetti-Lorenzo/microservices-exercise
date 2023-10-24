/** @type {import('./$types').PageServerLoad} */
export async function load() {
	if (process.env.HOSTNAME) {
		// get data from api-service
		const res = await fetch(`http://api-service:80`);
		const data = await res.text();
		return { hello: data, hostname: process.env.HOSTNAME };
	}
}
