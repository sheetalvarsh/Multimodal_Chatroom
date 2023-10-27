# Multimodal_Chatroom
Multi-Modal Chat Application: Voice-Bot

Overview

This project aims to develop a multi-modal chatbot application that enables users to engage in conversations with the chatbot using both speech and text-based inputs. The chatbot will utilize speech recognition to convert user speech into text and employ text-to-speech technology to respond to users audibly.

Problem Space

This project aims to solve the issue of managing calls while engaged in other activities. It helps individuals avoid distractions and ensures a safer interaction with callers when answering isn't feasible.

Version 1: Text-to-Speech Conversions and message storage

This initial version of the application will be designed as a web-based platform. Users can provide input in speech, which will be converted into text. Subsequently, this text will be transformed back into speech, allowing users to audibly hear the chatbot's responses. This version focuses on creating a web interface for seamless speech-to-text and text-to-speech interactions, enhancing user engagement and accessibility.

Features

• Web-based Application: Develop a web-based interface for user interaction. • Speech Recognition: Implement speech-to-text technology to convert user speech inputs into text. • Text-to-Speech Conversion: Utilize text-to-speech technology to transform chatbot responses into audible speech for users.

Purpose

• Enhance User Accessibility: Provide a user-friendly platform for speech-based interactions. • Improve User Experience: Ensure clear and comprehensible communication by converting text responses into text and speech.

Task Vignettes (User activity "flow") Task 1: User Input

Description: The user initiates a conversation by sending a message to the app. Steps:

User opens the chat interface within the app.
User speaks or types a message to communicate with the chatbot.
User clicks on a "Send" button to submit the message.
Task 2: Speech-to-Text Conversion

Description: The app employs speech-to-text technology to convert the spoken message into text for processing. Steps:

The app receives the user's spoken message.
The app utilizes speech recognition to convert the spoken message into text.
The converted text message is displayed on the screen.
Task 3: Text Response

Description: The app displays the converted text message, allowing the user to respond via text. Steps:

The user views the converted text message displayed on the app's interface.
The user formulates a response by typing a text message.
The user clicks on a "Send" button to submit the text response.
Task 4: Text-to-Speech Conversion

Description: The user-generated text response is transformed back into speech using text-to-speech technology. Steps:

The app receives the user's text response.
The app utilizes text-to-speech technology to convert the text response into audible speech.
The synthesized speech response is prepared for playback.
Technical Flow

Develop a web-based interface using HTML, CSS, and JavaScript to interact with users.
Implement a speech recognition module (e.g., using libraries or APIs) to capture user speech inputs.
Utilize speech recognition technology to convert captured speech into text format.
Process the text input and forward it to the chatbot module for further handling.
Users can convert messages via this platform in both speech and text inputs.
Technologies and Tools

• Speech Recognition: Utilize speech recognition libraries or APIs (such as Whisper). • Text-to-Speech: Integrate text-to-speech engines for speech synthesis. • Web Development: Create a user-friendly web interface using HTML, CSS, and JavaScript. • Version Control: Use Git for project management and version control.

Version 2: Speech-to-Text conversions and message storage

In this next phase of development, I will be introducing a new feature of speech-to-text to further enhance the capabilities of this application:

• Speech-to-Text Conversion: I will implement a feature that enables users to convert spoken language into text. This means that users can simply speak into their microphone, and the chatbot will instantly transcribe their words into text for processing. • Live Microphone Input: With this feature, users will be able to engage with the chatbot in real time by using a live microphone input. It will provide a convenient and hands-free way to interact with the chatbot. • Message Logging in CSV Format: I will also implement a system to store all chatbot interactions, including both text-to-speech and speech-to-text messages, in a CSV file. This will allow users to keep a record of their conversation history and review past interactions with the chatbot.

These enhancements are aimed at making the chatbot application more versatile and comprehensive, ultimately providing a more engaging and user-friendly experience.
