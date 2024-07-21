# Password Manager

A simple, GUI-based password manager built with Python and Tkinter.

## Features

- Add and store passwords for various websites and usernames
- View stored passwords in a convenient table format
- Reveal passwords securely when needed
- Basic encryption of stored passwords
- User-friendly interface

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the `password_manager.py` file.
2. Ensure you have Python 3.x installed on your system.

## Usage

1. Run the script:
2. The Password Manager window will open.
3. To add a new password:
- Enter the website, username, and password in the respective fields
- Click "Add Password"
4. To view a password:
- Select the entry in the table
- Click "Show Password"
- A pop-up will display the decrypted password

## Security Note

This password manager uses basic Base64 encoding for password obfuscation. While this provides a layer of obscurity, it is not secure encryption. For real-world use, implement stronger encryption methods and additional security measures.

## File Structure

- `password_manager.py`: Main Python script containing the password manager application
- `passwords.json`: JSON file where passwords are stored (created upon first use)

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-your-issues-page) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Disclaimer

