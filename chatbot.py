import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am fine, thank you!', 'Doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created by you.', 'You can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!']),
]

reflections = {
    'i am': 'you are',
    'i was': 'you were',
    'i': 'you',
    'i\'d': 'you would',
    'i\'ve': 'you have',
    'i\'ll': 'you will',
    'my': 'your',
    'you are': 'I am',
    'you\'re': 'I am',
    'you\'ve': 'I have',
    'you\'ll': 'I will',
    'your': 'my',
    'yours': 'mine',
    'you': 'me',
    'me': 'you'
}
def chatbot():
    print("Hi, I am your chatbot. How can I help you?")
    chat = Chat(patterns, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()