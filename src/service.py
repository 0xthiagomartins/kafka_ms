from nameko_kafka import consume


class MyService:
    """
    My microservice
    """

    name = "my-service"

    @consume("kafka-topic", group_id="my-group", bootstrap_servers="localhost:1234")
    def method(self, message):
        # Your message handler
        handle_message(message)
