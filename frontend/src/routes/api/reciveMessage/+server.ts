import * as amqp from "amqplib";

/** @type {import('./$types').RequestHandler} */
export async function GET() {
	const msg = await receiveMessage();
	return new Response(msg);
}

// get message from rabbitmq placed by the api at the startup
async function receiveMessage() {
	try {
		// open connection to rabbitmq server
		const connection = await amqp.connect("amqp://rabbit-mq");
		const channel = await connection.createChannel();

		const queueName = "hello";
		// get message from queue
		const message = await channel.get(queueName, { noAck: true });
		// check if message is not null
		let msg = "No messages in the queue";
		if (message) {
			// Process the message
			console.log("Received message:", message.content.toString());
			msg = JSON.stringify(message.content.toString());
		} else {
			console.log(msg);
		}

		// close connection
		await channel.close();
		await connection.close();

		return msg;
	} catch (error) {
		console.error("Error:", error);
		return "Error comunicating with the queue";
	}
}
