# URL Shortener

A simple command-line URL shortener built in Python that converts long URLs into short, easy-to-share codes and tracks visit statistics.

## Project Description

This URL Shortener takes long, unwieldy URLs (e.g., `https://www.examplesite.com/s?k=#435`) and converts them into compact short codes (e.g., `bit.ly/5345`). It also records the date each URL was generated and maintains a click report to track how often each shortened link is visited.

The project solves the common problem of sharing lengthy URLs that are difficult to read, type, or fit into limited character spaces. Whether you're sharing links in messages, emails, or social media, this tool makes URLs concise and manageable.

I built this project as a hobby to practice Python file handling, JSON data storage, and CSV reporting while creating a practical utility I can use and extend over time.

## Features

- **Shorten URLs** — Convert any long URL into a 6-character alphanumeric short code.
- **Automatic Deduplication** — If the same long URL is submitted again, the existing short code is returned instead of creating a duplicate.
- **Visit Tracking** — Optionally track clicks per URL and store statistics in a CSV report.
- **JSON-Based Storage** — All URL mappings are stored in a local `urls.json` file for simplicity and portability.
- **Input Validation** — Ensures URLs start with `http://` or `https://` before processing.

## Installation / Getting Started

### Prerequisites

- **Python 3.7+** installed on your system.
- No external libraries or API keys are required — the project uses only Python's built-in standard library.

### Installation Steps

1. **Clone the repository:**

```bash
git clone https://github.com/Omk4314/progress-on-python.git
cd url-shortener
```

2. **(Optional) Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate   # On Windows
```

3. **Run the application:**

```bash
python url_shortener.py
```

> **Note:** No `requirements.txt` or `pip install` is needed, as this project relies solely on Python's built-in modules (`json`, `random`, `time`, `os`, `csv`).

## Usage

### Shortening a URL

When you run the script, you'll be prompted to enter a URL. The system validates the input and generates a short code.

**Example:**

```bash
$ python url_shortener.py
Enter URL: https://very-long-link.com/page?id=12345
bit.ly/a3k9m2
Do you want to visit the short URL?(yes/no): yes
```

**Output:**
- A short URL like `bit.ly/a3k9m2` is printed to the console.
- The mapping is saved to `urls.json`.
- If you choose to visit the link, the click counter is updated in `clicked_report.csv`.

### Data Storage Format

Each shortened URL is stored in `urls.json` as:

```json
{
    "a3k9m2": {
        "long_url": "https://very-long-link.com/page?id=12345",
        "short_code": "a3k9m2",
        "created_at": "Wed Jun 10 14:32:05 2026"
    }
}
```

### Click Report

Visit statistics are tracked in `clicked_report.csv`:

```csv
url,clicks
https://very-long-link.com/page?id=12345,1
```

### Handling Duplicate URLs

If you submit a URL that has already been shortened, the existing short code is returned:

```bash
$ python url_shortener.py
Enter URL: https://very-long-link.com/page?id=12345
URL already exists: bit.ly/a3k9m2
```

## Feedback

I'd love to hear your thoughts on this project! Whether it's a bug report, feature suggestion, or general feedback, feel free to reach out:

- **GitHub Issues** — Comment directly on the repository.
- **LinkedIn** — Send me a message at [linkedin.com/in/om-kolhapure-0572603b6](https://www.linkedin.com/in/om-kolhapure-0572603b6).

## Contact / Authors

- **Om Kolhapure**
- **Email:** [kolhapureom4314@gmail.com](mailto:kolhapureom4314@gmail.com)
- **LinkedIn:** [linkedin.com/in/om-kolhapure-0572603b6](https://www.linkedin.com/in/om-kolhapure-0572603b6)

---

*Built with Python as a hobby project.*
