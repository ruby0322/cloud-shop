# CloudShop CLI

A command-line marketplace platform that allows users to buy and sell items.

## Requirements

- Python 3.8 or higher
- No external dependencies required

## Setup

1. Clone the repository
2. Make the build and run scripts executable:

```bash
chmod +x build.sh run.sh
```
3. Build the project:

```bash
./build.sh
```
4. Run the application:
   
```bash
./run.sh
```

## Usage

The application accepts the following commands:

- `REGISTER <username>` - Register a new user
- `CREATE_LISTING <username> <title> <description> <price> <category>` - Create a new listing
- `DELETE_LISTING <username> <listing_id>` - Delete a listing
- `GET_LISTING <username> <listing_id>` - Get listing details
- `GET_CATEGORY <username> <category>` - Get all listings in a category
- `GET_TOP_CATEGORY <username>` - Get category with most listings

## Project Structure

```
.
|-- src/
|   |-- models/         # Data models
|   |-- services/       # Business logic
|   |-- main.py         # Entry point
|-- build.sh           # Build script
|-- run.sh            # Run script
|-- README.md         # This file
``` 