{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter, BeautifulSoup, Regular Expression, and Time\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import re\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "'which' is not recognized as an internal or external command,\n",
      "operable program or batch file.\n"
     ]
    }
   ],
   "source": [
    "# Path to chromedriver\n",
    "!which chromedriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set the executable path and initialize the chrome browser in splinter\n",
    "executable_path = {'executable_path': 'chromedriver'}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Visit the NASA mars news site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<li class=\"slide\"><div class=\"image_and_description_container\"><a href=\"/news/8678/the-detective-aboard-nasas-perseverance-rover/\" target=\"_self\"><div class=\"rollover_description\"><div class=\"rollover_description_inner\">An instrument called SHERLOC will, with the help of its partner WATSON, hunt for signs of ancient life by detecting organic molecules and minerals.</div><div class=\"overlay_arrow\"><img alt=\"More\" src=\"/assets/overlay-arrow.png\"/></div></div><div class=\"list_image\"><img alt=\"This artist's concept depicts NASA's Mars 2020 rover exploring Mars. \" src=\"/system/news_items/list_view_images/8678_21379_PIA22107-320x240.jpg\"/></div><div class=\"bottom_gradient\"><div><h3>The Detective Aboard NASA's Perseverance Rover</h3></div></div></a><div class=\"list_text\"><div class=\"list_date\">May 26, 2020</div><div class=\"content_title\"><a href=\"/news/8678/the-detective-aboard-nasas-perseverance-rover/\" target=\"_self\">The Detective Aboard NASA's Perseverance Rover</a></div><div class=\"article_teaser_body\">An instrument called SHERLOC will, with the help of its partner WATSON, hunt for signs of ancient life by detecting organic molecules and minerals.</div></div></div></li>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert the browser html to a soup object and then quit the browser\n",
    "html = browser.html\n",
    "news_soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "slide_elem = news_soup.select_one('ul.item_list li.slide')\n",
    "slide_elem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.7.4 64-bit ('super': virtualenv)",
   "language": "python",
   "name": "python37464bitsupervirtualenve687e24a3a4141a8b6a9e2b32ae60551"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
