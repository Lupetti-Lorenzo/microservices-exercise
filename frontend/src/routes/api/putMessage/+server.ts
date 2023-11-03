/** @type {import('./$types').RequestHandler} */

export async function PUT() {
	const msg = await putMessage();
	return new Response(msg);
}

// call the api that will put the message in the queue
async function putMessage(): Promise<string> {
	const requestOptions = {
		method: "PUT"
	};
	const res = await fetch(`http://api-service:80/api/putMessage`, requestOptions);
	const data = await res.text();
	return data;
}
