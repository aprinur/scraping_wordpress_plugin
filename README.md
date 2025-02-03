# WordPress Plugins Scraper

<br>

## What kind of program is this ?
<p> As written on the title, this is a program to scrape Plugins from WordPress.org</p>

## How this program works?
<p> This program works using WordPress API to fetch plugin data page by page, store it into sqlite database and export it into Excel and CSV file, exported file will automatically store in "C:\Users\...\Downloads" folder. 
This program will fetch name, release date, last update, number of rating, average rating and plugin link</p>

## How to use this program?

<p>1. You must have Python 3.8+ and sqlite database installed in your device</p>
<p>2. Create venv (optional)</p>
<p>3. Install requirements.txt</p>

```
pip install requirements.txt
```
<p>4. Run main.py</p>

```
main.py
```

## Feature
<p> When main.py is running, you will find 4 options </p>

<ol>
<li> Scrape Plugins</li>
<p> This is the option to choose if you want to scrape the plugin. This option will ask for amount of page to scrape and tabel name to store the data in database, 
  and if you want to save it to Excel and CSV you'll need to fill certain parameters as in option 2</p>
  
<li> Export database into Excel and CSV</li>
<p> If you have already scraped and about to export the data you can choose this option. This option will ask for a few parameters</p>
<ol>
   1. Table name
  <p> Tables from database will be displayed, and you need to choose which table to export</p>
   2. File name (optional)
  <p> File name from the table to export, you can leave it empty and the code will fill it automatically</p>
   3. Sheet title (optional
  <p> This is a title to be displayed on top of the seet when opening the file, if you leave it empty program will fill it automatically</p>
   4. Sheet desc (optional)
  <p> Sheet description will place under the title, program will fill this form automatically if you leave it empty</p>
</ol>

<li> Delete table</li>
<p> After exporting data from a table, you can delete the table from database in case you want to save some space in your device. 
  When choosing this option, and you want to abort, keep the form empty and press enter, and it will return to main menu </p>

<li> Quit</li>
<p> Just like the name, it will stop the program</p>
</ol>
