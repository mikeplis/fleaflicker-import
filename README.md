# fleaflicker-import

This is a command line script that can be used to import your player rankings to Fleaflicker

# Dependencies

This script depends on the mechanize python library, so follow the download instructions [here](http://wwwsearch.sourceforge.net/mechanize/download.html).

# Getting Your Rankings Ready

This script expects your rankings to be in a file that looks similar to the [sample rankings file](https://github.com/mplis/fleaflicker-import/blob/master/sample-rankings.txt) in this repository. There should be one player per line and the spelling of each name **must match the spelling on Fleaflicker**. If the spelling does not match, that player will be skipped.

**This file is expected to be located in the same directory as `main.py`**

# Running The Script

This script expects the following arguments in this order:

* League ID
* Team ID
* Email 
* Password
* Rankings Filename

"League ID" and "Team ID" can be found in the URL when looking at your team page on Fleaflicker. For example, my team page can be found at http://www.fleaflicker.com/nfl/leagues/156387/teams/1170258, so my league ID would be 156387 and my team ID would be 1170258.

"Email" and "Password" are your Fleaflicker login credentials. Don't worry, these aren't saved or stored anywhere.

"Rankings Filename" is the name of the file where you stored your personal player rankings.

Once you have all the information, run the script with a command like this:

`python main.py 156387 1170258 myemail@example.com "mypassword" rankings.txt`

If your password contains special characters, you'll have to enclose it in quotation marks as shown above.

After running the script, you are encouraged to go to Fleaflicker and check that your rankings were successfully imported.
