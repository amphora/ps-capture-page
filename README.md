# ps-capture-page

A simple script to capture a web page in PatentSafe. Useful on it's own and also as inspiration for other scripts.

This uses PatentSafe's inbuilt web page capture functionality. You could if you wanted to capture a web page in a different way e.g. via a browser automation tool like Selenium.

## Usage

```bash
python ps-capture-page.py \
    --server https://your.patentsafe.com \
    --username albert \
    URL_TO_CAPTURE
```

### Parameters

- `--server`: The URL of your PatentSafe server (required)
- `--username`: Your PatentSafe username (required)
- `URL_TO_CAPTURE`: The URL of the webpage you want to capture (required)

### Example
```bash
python ps-capture-page.py \
    --server https://your.patentsafe.com \
    --username albert \
    https://www.google.com
```

Will:

- Capture the web page in PatentSafe
- Create a metadata item "URL" with the value of the URL
- Create a metadata item "Last Modified" with the value returned by the header "Last-Modified"

## Environment

- I've created a DevContainer for my own convenience. You might enjoy. 



