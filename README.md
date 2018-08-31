# wsg-scraper
## This poorly-written Python script scrapes 4chan's /wsg/ board for webms.
This is my **_first_** ever project I wrote in Python.

*scraper.py* is supposed to:
* Fetch the current catalog from 4chan.org/wsg/.
* Save the pretty-printed version to pretty.json.
* Scrape the catalog for preferred threads (which was done manually and there probably is a much better way to do it, please hmu).
* Put the ID of the threads in a SQLite databse.

*clear_tables.py* is supposed to:
* Can you guess what?
## TO-DO:
* Save the webms only into seperated folders.
* Figure out how to use ffmpeg to stream a continous stream.
* Figure out how to overlay video with text (Now playing: xyz.webm from xyz) ontop of the stream.
* Probably ditch the idea of using a database and use JSON instead.
* Make a website for the project with a chat.
Will I do these? Probably not.
Please help me make the code better and prettyier, it's a clusterfark right now.
