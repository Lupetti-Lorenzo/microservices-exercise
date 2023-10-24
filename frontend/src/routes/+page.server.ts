/** @type {import('./$types').PageServerLoad} */
export async function load() {
	const res = await fetch(
		`http://${process.env.API_IP || "localhost"}:${process.env.API_PORT || 80}`
	);
	const data = await res.text();
	return { hello: data };
}
