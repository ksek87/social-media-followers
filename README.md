# social-media-followers
Use this tool to determine who doesn't follow you back, so you can cleanup your social media feeds.

Currently, designed for use with Instagram's JSON files.

## Acquire your Instagram data
1. On the browser version of Instagram, select [Account 'Privacy and Security'](https://www.instagram.com/accounts/privacy_and_security/)
2. Under Data Download, select 'Request Download' and choose the JSON format
3. Instagram will send you an email once the zip file is prepared!
4. Extract the downloaded data, and copy the followers.JSON and following.JSON files from the followers_and_following directory
5. Place these files in a new directory called 'data' in this code repository

## Requirements
- Python
- Numpy library
- JSON library

## Running the script
1. Ensure the followers.JSON and following.JSON files are in the '/data' folder in the root repository (Use mkdir to create a new folder otherwise)
2. Run the script in temrminal using the following command
   ``` 
   python src/main.py > output.txt
   ```
3. View the output file with the list of users who do not follow you back
