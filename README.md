# aicomb
Creating software to bring your different AI LLMs together into one

Requirements:
- needs to provide LLM switching
- Dark UI
- API abstraction - this is so that one LLMs API does not decide how the application work. i.e., the app cannot be tailored to one LLMs API, but rather be generalised
- design:
    - allow switching of LLMs easily
    - allow user to enter input

front-end - PyQt
    - sidebar to select LLMs with its name and a settings button to access each individual settings
    - text box to enter prompt
    - button to send the prompt

Back-end - LLMClient base class to abstract the interface
    - sub classes for each individual LLM. e.t., GPTClient, GrokClient...
    - Each subclass knows how to format requests and parse responses from the API
    - ClientFactory to pick the right client depending on what the user chooses
    - Using threads to handle synchronous requests to different LLMs
    - Show a loading screen or "typing.." while waiting
    - A message to say if a client is not working - needs to be checked when application is started and before sending a request
    - Needs to store API keys securely
    - Allow per model settings control such as temperature/max tokens etc.
    - Maintaining a chat history using JSON files for loading/unloading
    - Append text as it arrives - streaming responses
    - Allowing multi tab chats for LLM's that support it

Design Choices
    - Using PyQt's QPallette for the style - as it is only 1 view, we dont need to use a css like sheet

Tools and Libraries:
- Requests for API calls
- QThread for background tasks




dev updates:
25/08/2025
will be using pyqt as the base library for the UI.
I will design the UI first then add the options to have multiple LLMs on the application




resources:
https://platform.openai.com/docs/quickstart



Project at a standstill as I need to pay to use OpenAI's API.