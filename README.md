# University Postgraduate Reviews Scraper

This Python script scrapes postgraduate university course reviews from [Whatuni](https://www.whatuni.com) for personal use and analysis.

## Purpose

The purpose of this project is to gather data from Whatuni's website to investigate the factors contributing to a satisfactory experience in university study for postgraduate students. The scraped data will be used solely for personal research and analysis and will not be used for any commercial purposes.

## Usage

### Prerequisites
- Python 3.x
- Scrapy library

### Installation

```bash
pip install scrapy
```

### Running the Scraper

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the scraper using the following command:

```bash
scrapy crawl unireview -o reviews.csv
```

This will scrape the postgraduate university course reviews from Whatuni and save the results to a CSV file named `reviews.csv`.

## Disclaimer

This scraper is intended for personal use only and is not intended for commercial purposes. By using this scraper, you agree to comply with Whatuni's [Terms of Service](https://www.whatuni.com/terms-of-use/) and use the scraped data responsibly.

## Acknowledgement
[Whatuni](https://www.whatuni.com) is a leading platform for university reviews, rankings, and information for prospective students.
I acknowledge that all content, including but not limited to course reviews, ratings, and comments, scraped from Whatuni's website belongs to Whatuni. Whatuni is the rightful owner of the intellectual property rights associated with the content provided on its platform. This scraping exercise is conducted with full respect for Whatuni's ownership of the data and in compliance with their Terms of Service. I appreciate Whatuni's contribution to providing valuable information to prospective students and researchers.
