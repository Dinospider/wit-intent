# wit-intent

The app is designed to process user input to categorizing text into different intents. The intents may be of four types if any – weather, distance, directions, and time taken.

NOTE: The given code contains only the back-end of the application. See _Implementation_ for more details.

## Working

A wit app was created at https://wit.ai and the app was trained to recognize text and categorize them into four intents. 
The user input is accepted and is sent to the wit app using wit’s message API.
The wit app responds with the intent, if found. 

For example, if the user enters "How long does it take to bake a cake?", the trained wit app identifies the *intent* as "time taken."

## Implementation

For a complete working implementation of the app, check out https://github.com/sidhuparas/WitApp.

## Other details

The source code is located in the folder ‘microservices/app/src ‘

This application was developed as part of the Hasura Product Development Fellowship (HPDF).
