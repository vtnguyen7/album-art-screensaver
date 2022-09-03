# album-art-screensaver

iTunes style screensaver which displays album art from your favourite local music player for linux. It was designed with [lollypop](https://wiki.gnome.org/Apps/Lollypop) in mind, however it should work with any music player which caches its album art somewhere sensible.

## Running

just run screensaver.py using `./screensaver.py`

## Config

Configuration is by a json file. An example file can be found in the repo. Put it in `~/.config/album-art-screensaver/album-art-screensaver.json` in order for the script to read it.

If you are not using lollypop, change the directory to the one in which your album art lies. Please note this will **NOT** scrape your music library to find your album art, or anything of the sort. There are probably other scripts which do that.
