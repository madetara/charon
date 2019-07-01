# charon

Charon is a simple tool built with python, that helps you manage your telegram chats by [archiving](https://telegram.org/blog/archive-and-new-design) them automatically.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install charon.

```bash
pip install dk.charon
```

## Usage

### Important notes

- charon will need you to provide [app-id and api-hash](https://my.telegram.org/apps) to work
- it will also authenticate you
- it's not designed for everyday use, thus will *NOT* store session info, and will automatically logout

Usage is quite simple.
The following command will archive all chats that were unactive for 30 days or longer.

```bash
charon archive -d 30
```

## Contributing

Any pull requests are welcome, including:

- refactoring
- test coverage
- new features
- CI setup

For major changes, please open an issue first to discuss what you would like to change.

## License

[GPL3](https://choosealicense.com/licenses/gpl-3.0/)
