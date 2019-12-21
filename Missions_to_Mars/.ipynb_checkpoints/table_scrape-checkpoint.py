{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pandas as pd\n",
    "import time\n",
    "\n",
    "\n",
    "def init_browser():\n",
    "    # @NOTE: Replace the path with your actual path to the chromedriver\n",
    "    executable_path = {\"executable_path\": \"chromedriver\"}\n",
    "    return Browser(\"chrome\", **executable_path, headless=False)\n",
    "\n",
    "\n",
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    mars_data={}\n",
    "    #Facts table with pandas\n",
    "    path = \"https://space-facts.com/mars/\"\n",
    "    table = pd.read_html(path)\n",
    "    df = table[0]  \n",
    "    fact = df.rename(columns={0:\"Description\",1:\"Value\"})\n",
    "    fact_table= fact.set_index(\"Description\")\n",
    "    fact_table.to_html()\n",
    "    mars_data[\"fact_table\"] = fact_table\n",
    "    \n",
    "    browser.quit()\n",
    "    return mars_data"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
