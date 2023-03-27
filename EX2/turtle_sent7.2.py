class PostOffice:
    """A Post Office class. Allows users to message each other.

            Args:
                usernames (list): Users for which we should create PO Boxes.

            Attributes:
                message_id (int): Incremental id of the last message sent.
                boxes (dict): Users' inboxes.
                history (dict): Users' messages read.
            """
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        self.history = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.

                Args:
                    sender (str): The message sender's username.
                    recipient (str): The message recipient's username.
                    message_title (str) The title of the message.
                    message_body (str): The body of the message.
                    urgent (bool, optional): The urgency of the message.
                                            Urgent messages appear first.

                Returns:
                    int: The message ID, auto incremented number.

                Raises:
                    KeyError: If the recipient does not exist.

                Examples:
                    After creating a PO box and sending a letter,
                    the recipient should have 1 message in the
                    inbox.

                """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': message_title,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, n=0):
        """Read n messages from the user inbox.

                Args:
                    username (str): The username.
                    n (int): The number of messages to read, default = 0 - read all the inbox.

                Returns:
                    list: The first n messages from the user inbox to read.

                Raises:
                    KeyError: If the username does not exist.

                Examples:
                    After reading 1 message,
                    if inbox had 2 messages and history was empty,
                    now the username should have only the second message in the inbox
                    and the first inbox message in history.

                """
        user_box = self.boxes[username]
        if n == 0:
            n = len(user_box)

        msgs_to_read = user_box[:n]
        self.history[username].append(msgs_to_read)
        self.boxes[username] = user_box[n:]
        return msgs_to_read

    def search_inbox(self, username, text):
        """Read all messages that contains the text.

                Args:
                    username (str): The username.
                    text (str): The text the message needs to contain.

                Returns:
                    list: All the messages from the user inbox that contains the text
                    in their title or in thier body.

                Raises:
                    KeyError: If the username does not exist.

                Examples:
                    After reading 1 message,
                    if inbox had 2 messages and history was empty,
                    now the username should have only the second message in the inbox
                    and the first inbox message in history.

                """
        return [msg for msg in self.boxes[username] if text in msg['body'] or text in msg['title']]


def main():
    po_box = PostOffice(['a', 'b'])
    po_box.send_message('a', 'b', 'Hello!', 'How are you?')
    po_box.send_message('a', 'b', 'Bye!', 'Good luck')
    print("search luck:", po_box.search_inbox('b', 'luck'))
    print("boxes before read", po_box.boxes['b'])
    print("history before read", po_box.history['b'])
    x = po_box.read_inbox('b', 1)
    print("boxes after read", po_box.boxes['b'])
    print("history after read", po_box.history['b'])
    print(x)


if __name__ == "__main__":
    main()
