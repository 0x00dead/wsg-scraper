1. Get the catalog JSON file.
	* Use Requests to get the JSON.
	* "Optimize" the process.
	* Pretty-print the JSON file.
	
2. Scrape that JSON file to find our preferred threads.
	* if preferred thread then store in database according to table.
	
3. Pipe that data into database.db (ID, thread number).

4. Load the preferred threads by thread number.

5. Get the webms ONLY (save the filenames as well).
	* Don't overwrite if we already have it downloaded.
	
6. Arrange them into folders by content-type (eg. YLYL, YGYL, Slav, etc).
