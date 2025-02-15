# Movie Database CLI

This is a command-line application that allows users to manage a movie database. Users can add, delete, update, and search for movies, as well as generate a website displaying their collection.

## Features

### Menu Options:

```
=== Menu: ===
	0. Exit
	1. List movies
	2. Add movies
	3. Delete movie
	4. Update movie
	5. Stats
	6. Random movie
	7. Search movie
	8. Movies sorted by rating
	9. Movies sorted by year
	10. Filter movies
	11. Create website
```

## Data Handling

- The movie data is fetched from the OMDb API. However, since the API data does not always have the correct format, values are converted before being stored.
- If a value cannot be converted correctly (e.g., `year: 2012-2013`to an `int`), a default value is assigned to prevent errors.

## Storage

- Users can choose between storing movie data in a JSON or CSV file.
- However, there is currently no functionality to change the storage format during runtime.
- The default storage is `json`.

## Installation

### Requirements

Ensure you have Python installed. Then, install the necessary dependencies using:

```sh
pip install -r requirements.txt
```

## Usage

Run the program using:

```sh
python main.py
```

## Generating the Website

The program allows you to generate a simple HTML website displaying all stored movies with their posters.

## API Usage

This program retrieves movie data from the [OMDb API](https://www.omdbapi.com/).  An API key comes with in the program.

## License

This project is open-source and available under the MIT License.

