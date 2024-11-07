# Link O Matic

A Python script that generates and displays a list of social media links based on a given username. The user can navigate through the list, search for a specific link, and copy the URL to the clipboard.

## Features

- Generate social media links for popular platforms like Facebook, Twitter, Instagram, LinkedIn, GitHub, and many more.
- Display links in a paginated manner for easier navigation.
- Search for specific links by typing a query and copy the corresponding URL to the clipboard.
- Navigate through pages using commands.
- Copy selected URLs to the clipboard.
- Exit the program with the `matrixout` command.

## Supported Social Media Platforms

The script generates links for the following social media platforms (and more):

- Facebook
- Twitter
- Instagram
- LinkedIn
- YouTube
- TikTok
- GitHub
- Stack Overflow
- Medium
- Reddit
- Discord
- Telegram
- Twitch
- Vimeo
- Patreon
- Ko-fi
- And many others...

## Requirements

- Python 3.x
- `pyperclip` library for copying to clipboard
- `fuzzywuzzy` library for fuzzy searching

You can install the required libraries using the following command:

```bash
pip install pyperclip fuzzywuzzy
```
  
## Usage

1.	Clone the repository or download the script to your local machine.
2.	Run the script with Python:
  ```bash
  python main.py
  ```
3.	Enter your username when prompted. The script will generate the social media links based on your username.
4.	Use the following commands to navigate and interact with the links:
  •	L: Move to the next page of links.
  •	H: Go back to the previous page of links.
  •	S: Search for a specific social media platform.
  •	Matrixout: Exit the program.
  •	Any number from the list: Copy the corresponding URL to the clipboard.

 ## License
  This project is licensed under the MIT License - see the LICENSE file for details.

 ## Contributing
 Feel free to fork the repository and submit pull requests. Contributions are welcome!

