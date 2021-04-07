<!-- PROJECT LOGO -->
<br />


  <h3 align="center">InstagramQuote</h3>

  <p align="center">
  A simple Python script that generate images with quotes and post them on Instagram
  </p>
</p>



<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

A simple Python script that generates images with quotes and posts them on Instagram. 
It has been built by using:

- Python Imaging Library (PIL): for creating and saving the image
- BeautifulSoup and Selenium: for scraping the quotes
- InstaBot: for uploading the image on Instagram 

<!-- GETTING STARTED -->



## Getting Started

### Prerequisites

The script needs the Chromedriver that must be place in the same folder of the script. 
Chromedriver can be found here:

https://chromedriver.chromium.org

Be sure that the version of Chromedriver is the same of your Chrome application. 

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/lorenzodegiorgi/InstagramQuote
   ```
   
2. Install libraries
   ```sh
   pip install instabot
   pip install Pillow
   pip install selenium
   pip install beautifulsoup4
   ```
   
3. Insert Instagram credentials in instagramquote.py:

   ```
   user_name = 'your_instagram_username'
   password = 'your_instagram_password'
   ```

4. Eventually, change the font in instagramquote.py:

   ```
   FONT = 'your_favorite_font'
   ```

<!-- USAGE EXAMPLES -->



## Usage

Simply run the script:

```sh
python3 instagramquote.py
```



## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.


