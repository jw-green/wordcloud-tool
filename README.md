# Word Cloud Tool

Uses the package `wordcloud` to generate WordClouds.

## Structure

```plaintext
.
|-- README.md
|-- ref
|   |-- input_images
|   |   `-- example.png
|   |-- srcTxt
|   |   `-- example.txt
|   `-- typefaces
|       `-- Raleway-Light.ttf
`-- wordCloud.py
```

## Installation Instructions

It may be preferable to create a new virtual environment to avoid modifying global python packages:

```plaintext
virtualenv [app-name]
```

The script also requires `scipy` and `wordcloud`.

```plaintext
pip install scipy
```

```plaintext
pip install wordcloud
```

## Usage

On run, the script will present a few mandatory fields:

1. Input File Name (Text)
1. Image File Name (Image)
1. Output File Name (Image)

As suggested by the folder names, any images that are intended for use as the word cloud background should go in the `ref/input_images` folder.

Text files (in .txt format) should be placed into the `ref/srcTxt` folder.

Any additional typefaces can be placed in the `ref/typefaces` folder, but for use, must be amended in the main script. Configuration file to follow to make this more convenient.

## Background