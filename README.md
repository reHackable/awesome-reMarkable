# Awesome reMarkable [![Discord](https://img.shields.io/discord/385916768696139794.svg?label=reMarkable&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/u3P9sDW)


# [<img src="Awesome.png"></p>](https://github.com/sindresorhus/awesome)

The [reMarkable](https://www.remarkable.com) is a paper tablet for those who prefer writing on paper. Its remarkably fast paper-white display, Linux based operating system and awesome community make it highly attractive amongst hackers and developers.

*Contributions are welcome as long as they follow the [guidelines](CONTRIBUTING.md).*

## Disclaimer

No project here is affiliated or endorsed by [reMarkable AS](https://github.com/remarkable). If you modify your device official support might refuse to help you.

### Write down your SSH password

**:warning: WARNING, READ THIS FIRST :warning:**

**Make sure you have saved your SSH password somewhere secure, or you have setup a [SSH key](https://remarkable.guide/guide/access/ssh.html#creating-a-ssh-key)**

You can find the SSH password in your settings: `Settings > Help > Copyrights and licenses > General information (scroll down)`.

Failure to do so could result in a **soft-bricked device** that requires [emergency recovery](https://remarkable.guide/tech/recovery.html).

### Factory reset may brick your device

This function may not do what you are expecting. While it resets all user data, it will not restore the device to the original factory condition. It will reset your SSH password and remove all SSH keys, which may make it impossible to connect to your device if it is malfunctioning.

See [remarkable.guide](https://remarkable.guide/tech/factory-reset.html) for more information on how to properly factory reset your device.

### Take special care if you are using a reMarkable 2.

- System recovery requires some hardware. See https://remarkable.guide/tech/recovery.html#remarkable-2-recovery for more information.
- The screen on rm2 and rm1 are different. Workarounds have been developed to interact with the rM2 framebuffer but some projects might not work on it. See [ddvk/remarkable2-framebuffer](https://github.com/ddvk/remarkable2-framebuffer) and [ddvk/remarkable2-framebuffer#14](https://github.com/ddvk/remarkable2-framebuffer/issues/14).


## Contents

- [APIs](#apis)
  - [Cloud API](#cloud-api)
  - [Lines Format](#lines-format)
  - [Other APIs](#other-apis)
- [Applications](#applications)
  - [Games](#games)
  - [Launchers](#launchers)
- [Cloud Tools](#cloud-tools)
- [Custom Templates](#custom-templates)
- [Device Tools](#device-tools)
- [GUI Clients](#gui-clients)
- [Interface Customization](#interface-customization)
- [Other](#other)
- [Screen Sharing/Streaming](#screen-sharingstreaming)

## APIs

### Cloud API

- (Unmaintained) [google-drive-remarkable-sync](https://github.com/bsdz/google-drive-remarkable-sync) - Apps Script API for reMarkable Cloud. Includes Synchronizer capability to automate mirroring of documents from Google Drive to reMarkable Cloud.
  ![Stars](https://img.shields.io/github/stars/bsdz/google-drive-remarkable-sync?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/bsdz/google-drive-remarkable-sync?style=flat-square) ![License](https://img.shields.io/github/license/bsdz/google-drive-remarkable-sync?style=flat-square)

- [jrmapi](https://github.com/jlarriba/jrmapi) - A Java API for the reMarkable Cloud.
  ![Stars](https://img.shields.io/github/stars/jlarriba/jrmapi?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/jlarriba/jrmapi?style=flat-square) ![License](https://img.shields.io/github/license/jlarriba/jrmapi?style=flat-square)

- (Unmaintained) [reMarkableAPI](https://github.com/splitbrain/ReMarkableAPI) - Docs and implementation of the reMarkable file sync API.
  ![Stars](https://img.shields.io/github/stars/splitbrain/ReMarkableAPI?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/splitbrain/ReMarkableAPI?style=flat-square) ![License](https://img.shields.io/github/license/splitbrain/ReMarkableAPI?style=flat-square)

- (Unmaintained) [reMarkable-typescript](https://github.com/Ogdentrod/reMarkable-typescript) - TypeScript API for reMarkable Cloud.
  ![Stars](https://img.shields.io/github/stars/Ogdentrod/reMarkable-typescript?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Ogdentrod/reMarkable-typescript?style=flat-square) ![License](https://img.shields.io/github/license/Ogdentrod/reMarkable-typescript?style=flat-square)

- [Remarkable.jl](https://github.com/theogf/Remarkable.jl) - Julia API Interface to the reMarkable cloud.
  ![Stars](https://img.shields.io/github/stars/theogf/Remarkable.jl?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/theogf/Remarkable.jl?style=flat-square) ![License](https://img.shields.io/github/license/theogf/Remarkable.jl?style=flat-square)

- [remarkdav](https://github.com/hansegucker/remarkdav) - A tool to sync PDF files from a WebDAV directory to the reMarkable Cloud.
  ![Stars](https://img.shields.io/github/stars/hansegucker/remarkdav?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/hansegucker/remarkdav?style=flat-square) ![License](https://img.shields.io/github/license/hansegucker/remarkdav?style=flat-square)

- [rMAPI](https://github.com/ddvk/rmapi) ReMarkable Cloud Go API.
  ![Stars](https://img.shields.io/github/stars/ddvk/rmapi?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ddvk/rmapi?style=flat-square) ![License](https://img.shields.io/github/license/ddvk/rmapi?style=flat-square)

- (Unmaintained) [rmapy](https://github.com/subutux/rmapy) - ReMarkable Cloud Python API.
  ![Stars](https://img.shields.io/github/stars/subutux/rmapy?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/subutux/rmapy?style=flat-square) ![License](https://img.shields.io/github/license/subutux/rmapy?style=flat-square)

- [rmcl](https://github.com/rschroll/rmcl)- Asynchronous Python library for the reMarkable Cloud.
  ![Stars](https://img.shields.io/github/stars/rschroll/rmcl?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rschroll/rmcl?style=flat-square) ![License](https://img.shields.io/github/license/rschroll/rmcl?style=flat-square)

- [rmfakecloud](https://github.com/ddvk/rmfakecloud) - Fake Cloud Sync, server implementation of the Cloud API.
  ![Stars](https://img.shields.io/github/stars/ddvk/rmfakecloud?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ddvk/rmfakecloud?style=flat-square) ![License](https://img.shields.io/github/license/ddvk/rmfakecloud?style=flat-square)


### Lines Format

- [librm_lines](https://github.com/RedTTGMoss/librm_lines) - A C++ library for reading & writing & rendering v6 files with the original reMarkable quill library, includes multiple languages wrappers for python and npm.
  ![Stars](https://img.shields.io/github/stars/RedTTGMoss/librm_lines?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/RedTTGMoss/librm_lines?style=flat-square) ![License](https://img.shields.io/github/license/RedTTGMoss/librm_lines?style=flat-square)

- [lines-are-beautiful](https://github.com/ax3l/lines-are-beautiful) - C++ File API for the reMarkable tablet.
  ![Stars](https://img.shields.io/github/stars/ax3l/lines-are-beautiful?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ax3l/lines-are-beautiful?style=flat-square) ![License](https://img.shields.io/github/license/ax3l/lines-are-beautiful?style=flat-square)

- [lines-are-rusty](https://github.com/ax3l/lines-are-rusty) - Rust File API for the reMarkable tablet.
  ![Stars](https://img.shields.io/github/stars/ax3l/lines-are-rusty?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ax3l/lines-are-rusty?style=flat-square) ![License](https://img.shields.io/github/license/ax3l/lines-are-rusty?style=flat-square)

- [reMarkable-kaitai](https://github.com/matomatical/reMarkable-kaitai) - [Kaitai Struct](https://kaitai.io/) format specification for the binary lines format.
  ![Stars](https://img.shields.io/github/stars/matomatical/reMarkable-kaitai?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/matomatical/reMarkable-kaitai?style=flat-square) ![License](https://img.shields.io/github/license/matomatical/reMarkable-kaitai?style=flat-square)

- (Unmaintained) [reMarkable-layers](https://github.com/bsdz/remarkable-layers) - Python API for reading & writing reMarkable Lines format. Supports very basic conversion of PDFs and SVGs to Lines format.
  ![Stars](https://img.shields.io/github/stars/bsdz/remarkable-layers?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/bsdz/remarkable-layers?style=flat-square) ![License](https://img.shields.io/github/license/bsdz/remarkable-layers?style=flat-square)

- [rmrl](https://github.com/rschroll/rmrl) - The reMarkable Rendering Library for Python converts annotated documents to PDF files.
  ![Stars](https://img.shields.io/github/stars/rschroll/rmrl?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rschroll/rmrl?style=flat-square) ![License](https://img.shields.io/github/license/rschroll/rmrl?style=flat-square)

- [rmscene](https://github.com/ricklupton/rmscene) - Python library to read v6 files / software version 3.
  ![Stars](https://img.shields.io/github/stars/ricklupton/rmscene?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ricklupton/rmscene?style=flat-square) ![License](https://img.shields.io/github/license/ricklupton/rmscene?style=flat-square)


### Other APIs

- [libreMarkable](https://github.com/canselcik/libremarkable) - A framework for developing applications with native refresh support for reMarkable Tablet.
  ![Stars](https://img.shields.io/github/stars/canselcik/libremarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/canselcik/libremarkable?style=flat-square) ![License](https://img.shields.io/github/license/canselcik/libremarkable?style=flat-square)


## Applications

- [harmony](https://rmkit.dev/apps/harmony) - a low latency sketching app with procedural brushes.
- [KOReader](https://github.com/koreader/koreader) - An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats.
  ![Stars](https://img.shields.io/github/stars/koreader/koreader?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/koreader/koreader?style=flat-square) ![License](https://img.shields.io/github/license/koreader/koreader?style=flat-square)

- [darvin/plato](https://github.com/darvin/plato) [LinusCDE/plato](https://github.com/LinusCDE/plato) - Plato reader port. Supports pdfs, epubs, many other formats.
  ![Stars](https://img.shields.io/github/stars/darvin/plato?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/darvin/plato?style=flat-square) ![License](https://img.shields.io/github/license/darvin/plato?style=flat-square)

- [Rebook](https://github.com/fsniper/ReBook) - The missing book store for reMarkable.
  ![Stars](https://img.shields.io/github/stars/fsniper/ReBook?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/fsniper/ReBook?style=flat-square) ![License](https://img.shields.io/github/license/fsniper/ReBook?style=flat-square)

- [reGenda](https://github.com/tenJirka/reGenda) - An agenda-based calendar for reMarkable.
  ![Stars](https://img.shields.io/github/stars/tenJirka/reGenda?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/tenJirka/reGenda?style=flat-square) ![License](https://img.shields.io/github/license/tenJirka/reGenda?style=flat-square)

- [reMarkable keywriter](https://github.com/dps/remarkable-keywriter) - A distraction free keyboard notes app.
  ![Stars](https://img.shields.io/github/stars/dps/remarkable-keywriter?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/dps/remarkable-keywriter?style=flat-square) ![License](https://img.shields.io/github/license/dps/remarkable-keywriter?style=flat-square)

- [reMarkable SSH explorer](https://github.com/iacobucci/rm-ssh-explorer) - An on-device ssh explorer for downloading pdf files from a server to the reMarkable tablet
  ![Stars](https://img.shields.io/github/stars/iacobucci/rm-ssh-explorer?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/iacobucci/rm-ssh-explorer?style=flat-square) ![License](https://img.shields.io/github/license/iacobucci/rm-ssh-explorer?style=flat-square)

- [reMarkable wikipedia](https://github.com/dps/remarkable-wikipedia) - Offline wikipedia reader for reMarkable.
  ![Stars](https://img.shields.io/github/stars/dps/remarkable-wikipedia?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/dps/remarkable-wikipedia?style=flat-square) ![License](https://img.shields.io/github/license/dps/remarkable-wikipedia?style=flat-square)

- (Unmaintained) [remarkaBot](https://github.com/Davide95/remarkaBot) - Fetch your documents from Telegram.
  ![Stars](https://img.shields.io/github/stars/Davide95/remarkaBot?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Davide95/remarkaBot?style=flat-square) ![License](https://img.shields.io/github/license/Davide95/remarkaBot?style=flat-square)

- [whiteboard-hypercard](https://github.com/fenollp/reMarkable-tools) - Live collaboration, drawing, chat, whiteboarding.
  ![Stars](https://img.shields.io/github/stars/fenollp/reMarkable-tools?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/fenollp/reMarkable-tools?style=flat-square) ![License](https://img.shields.io/github/license/fenollp/reMarkable-tools?style=flat-square)

- [Writerdeck for reMarkable 1](https://github.com/bjornte/Writerdeck-for-reMarkable) - Distraction-free Markdown word processor with keyboard support via a companion app or usb. With optional syncing and encryption of documents.
  ![Stars](https://img.shields.io/github/stars/bjornte/Writerdeck-for-reMarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/bjornte/Writerdeck-for-reMarkable?style=flat-square) ![License](https://img.shields.io/github/license/bjornte/Writerdeck-for-reMarkable?style=flat-square)


### Browser extensions

- [rePub](https://github.com/hafaio/repub) - unofficial browser extension that creates ePubs from websites and can either upload them to reMarkable cloud or save them locally, currently for Chrome only
  ![Stars](https://img.shields.io/github/stars/hafaio/repub?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/hafaio/repub?style=flat-square) ![License](https://img.shields.io/github/license/hafaio/repub?style=flat-square)

- [rePubfox](https://github.com/jrockwar/repubfox) - a hard fork of rePub for Firefox
  ![Stars](https://img.shields.io/github/stars/jrockwar/repubfox?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/jrockwar/repubfox?style=flat-square) ![License](https://img.shields.io/github/license/jrockwar/repubfox?style=flat-square)


### Games

- [chessMarkable](https://github.com/LinusCDE/chessmarkable) - Play chess against a bot or a friend.
  ![Stars](https://img.shields.io/github/stars/LinusCDE/chessmarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/chessmarkable?style=flat-square) ![License](https://img.shields.io/github/license/LinusCDE/chessmarkable?style=flat-square)

- [DOOMarkable](https://github.com/LinusCDE/doomarkable) - Play DOOM on the reMarkable 1.
  ![Stars](https://img.shields.io/github/stars/LinusCDE/doomarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/doomarkable?style=flat-square) ![License](https://img.shields.io/github/license/LinusCDE/doomarkable?style=flat-square)

- [minesweeper](https://rmkit.dev/apps/minesweeper) - A mine detection game.
- [recrossable](https://github.com/sandsmark/recrossable) - Crossword game with simplistic handwriting recognition and automatic generation of crosswords.
  ![Stars](https://img.shields.io/github/stars/sandsmark/recrossable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/sandsmark/recrossable?style=flat-square) ![License](https://img.shields.io/github/license/sandsmark/recrossable?style=flat-square)

- [retris](https://github.com/LinusCDE/retris) - Play a clone of the popular block stacking game with either buttons or swipe guestures.
  ![Stars](https://img.shields.io/github/stars/LinusCDE/retris?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/retris?style=flat-square) ![License](https://img.shields.io/github/license/LinusCDE/retris?style=flat-square)


### Launchers

- [draft-reMarkable](https://github.com/dixonary/draft-reMarkable) - A launcher for the reMarkable tablet, which wraps around the standard interface.
  ![Stars](https://img.shields.io/github/stars/dixonary/draft-reMarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/dixonary/draft-reMarkable?style=flat-square) ![License](https://img.shields.io/github/license/dixonary/draft-reMarkable?style=flat-square)

- [oxide](https://oxide.eeems.codes) - A launcher application for the reMarkable tablet.
- [remux](https://rmkit.dev/apps/remux) - A multi-tasking launcher for the reMarkable tablet.


## Cloud Tools

- [AgentNews-RemarkableRSSReader](https://github.com/eksubin/AgentNews-RemarkableRSSReader) - An AI agent for processing RSS news feeds and sending them to reMarkable via Google Drive API.
  ![Stars](https://img.shields.io/github/stars/eksubin/AgentNews-RemarkableRSSReader?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/eksubin/AgentNews-RemarkableRSSReader?style=flat-square) ![License](https://img.shields.io/github/license/eksubin/AgentNews-RemarkableRSSReader?style=flat-square)

- [Aviary](https://github.com/rmitchellscott/aviary) - A webhook-driven document uploader for reMarkable Cloud and rmfakecloud, featuring a static UI and a Go backend. Optional integration for email via AWS SES.
  ![Stars](https://img.shields.io/github/stars/rmitchellscott/aviary?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/aviary?style=flat-square) ![License](https://img.shields.io/github/license/rmitchellscott/aviary?style=flat-square)

- [CUPS Printing](https://github.com/ofosos/scratch/tree/master/remarkable-cups) - Script to print directly to reMarkable Cloud from CUPS using rMAPI.
  ![Stars](https://img.shields.io/github/stars/ofosos/scratch?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ofosos/scratch?style=flat-square) ![License](https://img.shields.io/github/license/ofosos/scratch?style=flat-square)

- [mendeley-rMsync](https://github.com/anilkyelam/mendeley-rMsync) - Script to sync PDFs (with annotations) from/to a [Mendeley](https://www.mendeley.com/) folder.
  ![Stars](https://img.shields.io/github/stars/anilkyelam/mendeley-rMsync?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/anilkyelam/mendeley-rMsync?style=flat-square) ![License](https://img.shields.io/github/license/anilkyelam/mendeley-rMsync?style=flat-square)

- [Moss](https://github.com/RedTTGMoss/moss-desktop) - An app for working with your documents in the reMarkable/rmFakeCloud cloud
  ![Stars](https://img.shields.io/github/stars/RedTTGMoss/moss-desktop?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/RedTTGMoss/moss-desktop?style=flat-square) ![License](https://img.shields.io/github/license/RedTTGMoss/moss-desktop?style=flat-square)

- [pdf2remarkable](https://github.com/teticio/pdf2remarkable) - Script to upload PDFs to the reMarkable Cloud.
  ![Stars](https://img.shields.io/github/stars/teticio/pdf2remarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/teticio/pdf2remarkable?style=flat-square) ![License](https://img.shields.io/github/license/teticio/pdf2remarkable?style=flat-square)

- (Unmaintained) [reCatchable](https://github.com/lapwat/reCatchable) - Turn websites into ebooks, upload them to reMarkable.
  ![Stars](https://img.shields.io/github/stars/lapwat/reCatchable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/lapwat/reCatchable?style=flat-square) ![License](https://img.shields.io/github/license/lapwat/reCatchable?style=flat-square)

- [reGitable](https://github.com/after-eight/regitable) - Backup your reMarkable with git and sync changes to a remote repository automatically.
  ![Stars](https://img.shields.io/github/stars/after-eight/regitable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/after-eight/regitable?style=flat-square) ![License](https://img.shields.io/github/license/after-eight/regitable?style=flat-square)

- [Remarcal](https://remarcal.com/) - Sync Google, Outlook, Apple, and more calendars to reMarkable.
- [reMarkable Morning News_2](https://github.com/ktibr0/Remarkable_morning_news_2) - Automatically sends daily news to your reMarkable tablet. Standalone web application with persistent storage.
  ![Stars](https://img.shields.io/github/stars/ktibr0/Remarkable_morning_news_2?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ktibr0/Remarkable_morning_news_2?style=flat-square) ![License](https://img.shields.io/github/license/ktibr0/Remarkable_morning_news_2?style=flat-square)

- [reMarkable RSS](https://github.com/eksubin/Remarkable-RSS-Feed) - Read RSS feeds on reMarkable via google drive integration. Automated Script to convert RSS-feeds as PDFs and upload to google drive.
  ![Stars](https://img.shields.io/github/stars/eksubin/Remarkable-RSS-Feed?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/eksubin/Remarkable-RSS-Feed?style=flat-square) ![License](https://img.shields.io/github/license/eksubin/Remarkable-RSS-Feed?style=flat-square)

- [remarkable-mcp](https://github.com/SamMorrowDrums/remarkable-mcp) - Model Context Protocol server enabling AI assistants to read and browse your reMarkable documents via SSH (no subscription required) or Cloud API. [Blog post](https://sam-morrow.com/blog/building-an-mcp-server-for-remarkable).
  ![Stars](https://img.shields.io/github/stars/SamMorrowDrums/remarkable-mcp?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/SamMorrowDrums/remarkable-mcp?style=flat-square) ![License](https://img.shields.io/github/license/SamMorrowDrums/remarkable-mcp?style=flat-square)

- [remarkable_simplenote](https://github.com/bgribble/remarkable_simplenote) - Sync simplenote notes to reMarkable (currently one-way)
  ![Stars](https://img.shields.io/github/stars/bgribble/remarkable_simplenote?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/bgribble/remarkable_simplenote?style=flat-square) ![License](https://img.shields.io/github/license/bgribble/remarkable_simplenote?style=flat-square)

- [reMarkable-Sink](http://github.com/hmenzagh/reMarkable-Sink) - Turn a folder into a wormhole to your reMarkable.
  ![Stars](https://img.shields.io/github/stars/hmenzagh/reMarkable-Sink?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/hmenzagh/reMarkable-Sink?style=flat-square) ![License](https://img.shields.io/github/license/hmenzagh/reMarkable-Sink?style=flat-square)

- [remarkable-substack](https://github.com/jwoglom/remarkable-substack/) - Syncs unread Substack posts to the reMarkable Cloud.
  ![Stars](https://img.shields.io/github/stars/jwoglom/remarkable-substack?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/jwoglom/remarkable-substack?style=flat-square) ![License](https://img.shields.io/github/license/jwoglom/remarkable-substack?style=flat-square)

- [reMarkable_syncthing](http://github.com/evidlo/remarkable_syncthing) - Syncthing on reMarkable.
  ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_syncthing?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_syncthing?style=flat-square) ![License](https://img.shields.io/github/license/evidlo/remarkable_syncthing?style=flat-square)

- [reMarkable Todoist and Calendar Sync](https://github.com/usuallycwdillon/remarkable-calendar) Puts Todoist tasks and Google calendar events on a calendar then pushes to reMarkable.
  ![Stars](https://img.shields.io/github/stars/usuallycwdillon/remarkable-calendar?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/usuallycwdillon/remarkable-calendar?style=flat-square) ![License](https://img.shields.io/github/license/usuallycwdillon/remarkable-calendar?style=flat-square)

- [remarkable-zapier](https://github.com/artes-dev/remarkable-zapier) - Zapier Integration for reMarkable Cloud
  ![Stars](https://img.shields.io/github/stars/artes-dev/remarkable-zapier?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/artes-dev/remarkable-zapier?style=flat-square) ![License](https://img.shields.io/github/license/artes-dev/remarkable-zapier?style=flat-square)

- [remarking](https://github.com/sabidib/remarking) - CLI tool to extract highlights from any document in the reMarkable cloud.
  ![Stars](https://img.shields.io/github/stars/sabidib/remarking?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/sabidib/remarking?style=flat-square) ![License](https://img.shields.io/github/license/sabidib/remarking?style=flat-square)

- [rm-brain](https://github.com/gabrielanhaia/remarkable-brain) - Turns your reMarkable notebooks into a local-first, searchable second brain you query through Claude Desktop.
  ![Stars](https://img.shields.io/github/stars/gabrielanhaia/remarkable-brain?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/gabrielanhaia/remarkable-brain?style=flat-square) ![License](https://img.shields.io/github/license/gabrielanhaia/remarkable-brain?style=flat-square)

- [rm-pdf-tools](https://github.com/skius/rm-pdf-tools) - Service that allows users to insert and delete pages from annotated PDFs on the device.
  ![Stars](https://img.shields.io/github/stars/skius/rm-pdf-tools?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/skius/rm-pdf-tools?style=flat-square) ![License](https://img.shields.io/github/license/skius/rm-pdf-tools?style=flat-square)

- [rM-sync](https://github.com/simonschllng/rm-sync) - Sync script for reMarkable paper tablet.
  ![Stars](https://img.shields.io/github/stars/simonschllng/rm-sync?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/simonschllng/rm-sync?style=flat-square) ![License](https://img.shields.io/github/license/simonschllng/rm-sync?style=flat-square)

- [RMfuse](https://github.com/rschroll/rmfuse) - FUSE filesystem for the reMarkable Cloud.
  ![Stars](https://img.shields.io/github/stars/rschroll/rmfuse?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rschroll/rmfuse?style=flat-square) ![License](https://img.shields.io/github/license/rschroll/rmfuse?style=flat-square)

- [rss2remarkable](https://codeberg.org/akselmo/rss2remarkable) - Generates PDF of given RSS feeds and send is to your reMarkable cloud.
  ![Stars](https://img.shields.io/gitea/stars/akselmo/rss2remarkable?gitea_url=https://codeberg.org&style=flat-square) ![Last Commit](https://img.shields.io/gitea/last-commit/akselmo/rss2remarkable?gitea_url=https://codeberg.org&style=flat-square)

- [send-to-remarkable](https://github.com/zegevlier/send-to-remarkable) - Upload documents to the reMarkable from an email, like send to Kindle.
  ![Stars](https://img.shields.io/github/stars/zegevlier/send-to-remarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/zegevlier/send-to-remarkable?style=flat-square) ![License](https://img.shields.io/github/license/zegevlier/send-to-remarkable?style=flat-square)

- [sync_zotero_remarkable](https://github.com/danijoo/sync_zotero_remarkable) - Sync PDFs from Zotero to reMarkable.
  ![Stars](https://img.shields.io/github/stars/danijoo/sync_zotero_remarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/danijoo/sync_zotero_remarkable?style=flat-square) ![License](https://img.shields.io/github/license/danijoo/sync_zotero_remarkable?style=flat-square)

- [Syncthing-for-reMarkable-AppLoad](https://github.com/paviro/Syncthing-for-reMarkable) - Syncthing appload app for reMarkable (incl. Paper Pro and Paper Pro Move).
  ![Stars](https://img.shields.io/github/stars/paviro/Syncthing-for-reMarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/paviro/Syncthing-for-reMarkable?style=flat-square) ![License](https://img.shields.io/github/license/paviro/Syncthing-for-reMarkable?style=flat-square)

- [url2epub](https://github.com/fishy/url2epub) - Telegram bot to generate ePub out of URL and send directly to reMarkable Cloud.
  ![Stars](https://img.shields.io/github/stars/fishy/url2epub?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/fishy/url2epub?style=flat-square) ![License](https://img.shields.io/github/license/fishy/url2epub?style=flat-square)

- [zotero-reMarkable](https://github.com/michaelmior/zotero-remarkable) - Script to sync PDFs from the [Zotero](https://www.zotero.org/) reference manager.
  ![Stars](https://img.shields.io/github/stars/michaelmior/zotero-remarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/michaelmior/zotero-remarkable?style=flat-square) ![License](https://img.shields.io/github/license/michaelmior/zotero-remarkable?style=flat-square)

- (Unmaintained) [Zotero2reMarkable Bridge](https://github.com/opal06/zotero2remarkable_bridge) - Sync files from Zotero to reMarkable and back based on tags; supports v2.7< highlights.
  ![Stars](https://img.shields.io/github/stars/opal06/zotero2remarkable_bridge?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/opal06/zotero2remarkable_bridge?style=flat-square) ![License](https://img.shields.io/github/license/opal06/zotero2remarkable_bridge?style=flat-square)


## Custom Templates

- [blank_slate_pdf](https://github.com/sowcow/blank_slate_pdf) - Flexible PDFs for nested lists or experiments with no predefined template, separate simple calendar, customization using ruby code.
  ![Stars](https://img.shields.io/github/stars/sowcow/blank_slate_pdf?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/sowcow/blank_slate_pdf?style=flat-square) ![License](https://img.shields.io/github/license/sowcow/blank_slate_pdf?style=flat-square)

- [latex-yearly-planner](https://github.com/kudrykv/latex-yearly-planner) - PDF planner designed for e-ink devices.
  ![Stars](https://img.shields.io/github/stars/kudrykv/latex-yearly-planner?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/kudrykv/latex-yearly-planner?style=flat-square) ![License](https://img.shields.io/github/license/kudrykv/latex-yearly-planner?style=flat-square)

- (Unmaintained) [ReCalendar](https://github.com/klimeryk/recalendar) - Highly customizable calendar generator in PHP optimized for reMarkable.
  ![Stars](https://img.shields.io/github/stars/klimeryk/recalendar?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/klimeryk/recalendar?style=flat-square) ![License](https://img.shields.io/github/license/klimeryk/recalendar?style=flat-square)

- [reMarkable-bujo](https://github.com/vonneudeck/remarkable-bujo) - "Bullet Journal" templates.
  ![Stars](https://img.shields.io/github/stars/vonneudeck/remarkable-bujo?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/vonneudeck/remarkable-bujo?style=flat-square) ![License](https://img.shields.io/github/license/vonneudeck/remarkable-bujo?style=flat-square)

- [remarkable-engineering](https://gitlab.com/asciipip/remarkable-engineering) - Engineering-style grid templates.
  ![Stars](https://img.shields.io/gitlab/stars/asciipip/remarkable-engineering?style=flat-square) ![Last Commit](https://img.shields.io/gitlab/last-commit/asciipip/remarkable-engineering?style=flat-square) ![License](https://img.shields.io/gitlab/license/asciipip/remarkable-engineering?style=flat-square)

- [reMarkable-gtd-templates](https://github.com/BartKeulen/remarkable-gtd-templates) - "Getting Things Done" templates.
  ![Stars](https://img.shields.io/github/stars/BartKeulen/remarkable-gtd-templates?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/BartKeulen/remarkable-gtd-templates?style=flat-square) ![License](https://img.shields.io/github/license/BartKeulen/remarkable-gtd-templates?style=flat-square)

- [reMarkable_templates](https://github.com/steka/reMarkable_templates) - White lines/squares on gray background.
  ![Stars](https://img.shields.io/github/stars/steka/reMarkable_templates?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/steka/reMarkable_templates?style=flat-square) ![License](https://img.shields.io/github/license/steka/reMarkable_templates?style=flat-square)

- [reMarkabletemplates](https://github.com/equivocates/remarkabletemplates/) - Planner per 1 or 3 weeks.
  ![Stars](https://img.shields.io/github/stars/equivocates/remarkabletemplates?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/equivocates/remarkabletemplates?style=flat-square) ![License](https://img.shields.io/github/license/equivocates/remarkabletemplates?style=flat-square)

- [rM2Mods templates](https://github.com/DanielRunningen/rM2Mods/tree/main/assests/templates) - Collection of different templates. E.g., micro dots/grids, checklists, budgeting,  boxes.
  ![Stars](https://img.shields.io/github/stars/DanielRunningen/rM2Mods?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/DanielRunningen/rM2Mods?style=flat-square) ![License](https://img.shields.io/github/license/DanielRunningen/rM2Mods?style=flat-square)

- [reMarkable planning/journaling templates](https://github.com/msencer/remarkable_templates) - Collection of daily/weekly planning, journaling templates
  ![Stars](https://img.shields.io/github/stars/msencer/remarkable_templates?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/msencer/remarkable_templates?style=flat-square) ![License](https://img.shields.io/github/license/msencer/remarkable_templates?style=flat-square)

- [re-Planner](https://github.com/PepikVaio/reMarkable_re-Planner) - Watermarked PDF calendar for reMarkable 1 and 2. You can pay to remove the watermark, and to receive a customized version.
  ![Stars](https://img.shields.io/github/stars/PepikVaio/reMarkable_re-Planner?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/PepikVaio/reMarkable_re-Planner?style=flat-square) ![License](https://img.shields.io/github/license/PepikVaio/reMarkable_re-Planner?style=flat-square)

- [Mobile UX Sketching Templates](https://github.com/Martes-Delta-Co/Remarkable-Mobile-Prototyping-Templates) - Mobile phone templates with 12 column layouts, grids, and multiple combinations of 1/2/4-up layouts with space for note-taking, in iPhone and Android flavors, in Methods format, so you can swap templates on each page of a notebook
  ![Stars](https://img.shields.io/github/stars/Martes-Delta-Co/Remarkable-Mobile-Prototyping-Templates?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Martes-Delta-Co/Remarkable-Mobile-Prototyping-Templates?style=flat-square) ![License](https://img.shields.io/github/license/Martes-Delta-Co/Remarkable-Mobile-Prototyping-Templates?style=flat-square)


### Template Builders

- [Daily Journal / Wardley Maps / Figma template](https://www.figma.com/community/file/1389237140795352688) - A daily planner/journal, Wardley Map, and forkable general starter kit for building custom templates with Figma.
- [ReCalendar.me](https://recalendar.me/) - Highly customizable online calendar generator optimized for reMarkable.
- [Remarkable Grid Template Generator](https://xosh.org/remarkable-grid-template/) - Generate pixel perfect line grid and dotted grid templates
- [Remarkably Planner Builder](https://remarkably-organized.pages.dev/) - Generate hyperlinked pdf planners
- [reMarkable Template Builder](https://templarian.github.io/remarkable/) - Generate Isometric and Grid templates of all sizes

## Device Tools

- [paginator](https://github.com/aflusche/paginator) - Physical foot pedal to turn pages on the device with no hands (e.g. for playing sheet music).
  ![Stars](https://img.shields.io/github/stars/aflusche/paginator?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/aflusche/paginator?style=flat-square) ![License](https://img.shields.io/github/license/aflusche/paginator?style=flat-square)

- (Unmaintained)[remarvin](https://github.com/plan5/remarvin) - Profile and file encryption manager that allows to manage notebooks for different users and to optionally protect the files with a password through gocryptfs-based encryption (device only).
- [reExecute](https://github.com/Slenderman00/reExecute) - Persistent code execution bootstrap for reMarkable Paper Pro Move using the MDM agent config.
  ![Stars](https://img.shields.io/github/stars/Slenderman00/reExecute?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Slenderman00/reExecute?style=flat-square) ![License](https://img.shields.io/github/license/Slenderman00/reExecute?style=flat-square)

- [rm-version-switcher](https://github.com/rmitchellscott/rm-version-switcher) - An interactive CLI application for switching between installed reMarkable OS versions.
  ![Stars](https://img.shields.io/github/stars/rmitchellscott/rm-version-switcher?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/rm-version-switcher?style=flat-square) ![License](https://img.shields.io/github/license/rmitchellscott/rm-version-switcher?style=flat-square)

- [rmtemplate](https://github.com/zer0trip/rmtemplate) - CLI to upload and manage custom templates on reMarkable Paper Pro and Paper Pro Move devices over SSH.
  ![Stars](https://img.shields.io/github/stars/zer0trip/rmtemplate?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/zer0trip/rmtemplate?style=flat-square) ![License](https://img.shields.io/github/license/zer0trip/rmtemplate?style=flat-square)

- [rmtree](https://github.com/rmitchellscott/rmtree) - Unix-style tree command for the reMarkable's document filesystem.
  ![Stars](https://img.shields.io/github/stars/rmitchellscott/rmtree?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/rmtree?style=flat-square) ![License](https://img.shields.io/github/license/rmitchellscott/rmtree?style=flat-square)

- [splash.dat converter](https://gist.github.com/iTrooz/fddfcce03c1c44b04231be73d6e7982a) - Simple script to convert an image to the rM2 .dat format for a splash screen.

## GUI Clients

- [asTounding](https://github.com/jlarriba/astounding) -  A multiplatform GUI application for the reMarkable cloud, including Linux.
  ![Stars](https://img.shields.io/github/stars/jlarriba/astounding?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/jlarriba/astounding?style=flat-square) ![License](https://img.shields.io/github/license/jlarriba/astounding?style=flat-square)

- [reManager](https://github.com/rmitchellscott/reManager) - Linux, MacOS, and Windows desktop app for managing mods on reMarkable tablets using the [Vellum](https://github.com/vellum-dev/vellum) package manager.
  ![Stars](https://img.shields.io/github/stars/rmitchellscott/reManager?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/reManager?style=flat-square) ![License](https://img.shields.io/github/license/rmitchellscott/reManager?style=flat-square)

- [RemaPy](https://github.com/peerdavid/remapy) - GUI to browse, download/upload files and backup the tablet (also on Linux) using the cloud.
  ![Stars](https://img.shields.io/github/stars/peerdavid/remapy?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/peerdavid/remapy?style=flat-square) ![License](https://img.shields.io/github/license/peerdavid/remapy?style=flat-square)

- [reMarkable Connection Utility (RCU)](http://www.davisr.me/projects/rcu/) - Cross-platform local/offline client for managing backups, screenshots, notebooks, templates, wallpaper, firmware, and third-party software. Typed text and snap highlight extraction. Virtual printer for native print-to-tablet.
- [reMarkable Remember](https://github.com/ds160/remarkable-remember) - A cross-platform client for offline management of backups, notebooks, templates and hand writing recognition via MyScript.
  ![Stars](https://img.shields.io/github/stars/ds160/remarkable-remember?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ds160/remarkable-remember?style=flat-square) ![License](https://img.shields.io/github/license/ds160/remarkable-remember?style=flat-square)

- [reMarkable-assistant](https://github.com/richeymichael/remarkable-assistant) - Manage templates, splash screens, and settings on your reMarkable tablet.
  ![Stars](https://img.shields.io/github/stars/richeymichael/remarkable-assistant?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/richeymichael/remarkable-assistant?style=flat-square) ![License](https://img.shields.io/github/license/richeymichael/remarkable-assistant?style=flat-square)

- [reMarkable-hyutilities](https://github.com/moovida/remarkable-hyutilities) - A GUI written in java to backup your device, upload templates and modify splash screens.
  ![Stars](https://img.shields.io/github/stars/moovida/remarkable-hyutilities?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/moovida/remarkable-hyutilities?style=flat-square) ![License](https://img.shields.io/github/license/moovida/remarkable-hyutilities?style=flat-square)

- [ReMy](https://github.com/bordaigorl/remy) - A GUI to browse, preview documents, export documents with custom settings, all via SSH (no cloud needed); works from local raw backups too.
  ![Stars](https://img.shields.io/github/stars/bordaigorl/remy?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/bordaigorl/remy?style=flat-square) ![License](https://img.shields.io/github/license/bordaigorl/remy?style=flat-square)

- [RMHook](https://github.com/NohamR/RMHook) - A dynamic library injection tool for the reMarkable Desktop macOS application, enabling connection to self-hosted rmfakecloud servers.
  ![Stars](https://img.shields.io/github/stars/NohamR/RMHook?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/NohamR/RMHook?style=flat-square) ![License](https://img.shields.io/github/license/NohamR/RMHook?style=flat-square)

- [RMHook-iOS](https://github.com/NohamR/RMHook-iOS/) - A hooking tool for the reMarkable iOS application, enabling connection to self-hosted rmfakecloud servers.
  ![Stars](https://img.shields.io/github/stars/NohamR/RMHook-iOS?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/NohamR/RMHook-iOS?style=flat-square) ![License](https://img.shields.io/github/license/NohamR/RMHook-iOS?style=flat-square)

- [RMHook-Win](https://github.com/NohamR/RMHook-Win) - A hooking tool for the reMarkable Desktop Windows application, enabling connection to self-hosted rmfakecloud servers.
  ![Stars](https://img.shields.io/github/stars/NohamR/RMHook-Win?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/NohamR/RMHook-Win?style=flat-square) ![License](https://img.shields.io/github/license/NohamR/RMHook-Win?style=flat-square)

- [rm-exporter](https://github.com/chopikus/rm-exporter) - Exports any combination of folders and large notes locally, supports Windows/MacOS/Linux.
  ![Stars](https://img.shields.io/github/stars/chopikus/rm-exporter?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/chopikus/rm-exporter?style=flat-square) ![License](https://img.shields.io/github/license/chopikus/rm-exporter?style=flat-square)

- [rM2 Template Helper](https://www.freeremarkabletools.com/) Windows tool for template management, and to download community templates. 
- [rMExplorer](https://github.com/bruot/pyrmexplorer/wiki) - GUI to browse, download/upload files and backup the tablet without using the cloud.
  ![Stars](https://img.shields.io/github/stars/bruot/pyrmexplorer?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/bruot/pyrmexplorer?style=flat-square) ![License](https://img.shields.io/github/license/bruot/pyrmexplorer?style=flat-square)

- [rmUploader](https://github.com/lobre/rmuploader) - Simple web app to upload epub or pdf files to the reMarkable tablet via drag and drop.
  ![Stars](https://img.shields.io/github/stars/lobre/rmuploader?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/lobre/rmuploader?style=flat-square) ![License](https://img.shields.io/github/license/lobre/rmuploader?style=flat-square)

- (Unmaintained) [Slithin](https://github.com/furesoft/Slithin) - Free Management Application for Windows/Linux/MacOS.
  ![Stars](https://img.shields.io/github/stars/furesoft/Slithin?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/furesoft/Slithin?style=flat-square) ![License](https://img.shields.io/github/license/furesoft/Slithin?style=flat-square)


## Interface Customization

- [AppLoad](https://github.com/asivery/rm-appload) - Enables windowed and fullscreen apps inside the reMarkable interface.
  ![Stars](https://img.shields.io/github/stars/asivery/rm-appload?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/asivery/rm-appload?style=flat-square) ![License](https://img.shields.io/github/license/asivery/rm-appload?style=flat-square)

- [Book-safe](https://github.com/dvdsk/Book-safe) - Hide books/documents between a given time period.
  ![Stars](https://img.shields.io/github/stars/dvdsk/Book-safe?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/dvdsk/Book-safe?style=flat-square) ![License](https://img.shields.io/github/license/dvdsk/Book-safe?style=flat-square)

- [Crazy Cow](https://github.com/machinelevel/sp425-crazy-cow) - Typewriter input from USB keyboard directly into reMarkable interface.
  ![Stars](https://img.shields.io/github/stars/machinelevel/sp425-crazy-cow?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/machinelevel/sp425-crazy-cow?style=flat-square) ![License](https://img.shields.io/github/license/machinelevel/sp425-crazy-cow?style=flat-square)

- [ReCept](https://github.com/funkey/recept/) - Fix for the rM2 jagged line issue.
  ![Stars](https://img.shields.io/github/stars/funkey/recept?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/funkey/recept?style=flat-square) ![License](https://img.shields.io/github/license/funkey/recept?style=flat-square)

- [reLuminate](https://github.com/unreMarkableLabs/reLuminate) - Enable enhanced screen brightness levels on the reMarkable Paper Pro.
  ![Stars](https://img.shields.io/github/stars/unreMarkableLabs/reLuminate?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/unreMarkableLabs/reLuminate?style=flat-square) ![License](https://img.shields.io/github/license/unreMarkableLabs/reLuminate?style=flat-square)

- [RemarkableLamyEraser](https://github.com/isaacwisdom/RemarkableLamyEraser/) - Supports Lamy Al Star stylus button to erase or undo for reMarkable tablets.
  ![Stars](https://img.shields.io/github/stars/isaacwisdom/RemarkableLamyEraser?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/isaacwisdom/RemarkableLamyEraser?style=flat-square) ![License](https://img.shields.io/github/license/isaacwisdom/RemarkableLamyEraser?style=flat-square)

- [remarkable-shortcuts](https://github.com/martinetd/remarkable-shortcuts) - Add extra 'gestures' (currently double taps) for easier navigation.
  ![Stars](https://img.shields.io/github/stars/martinetd/remarkable-shortcuts?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/martinetd/remarkable-shortcuts?style=flat-square) ![License](https://img.shields.io/github/license/martinetd/remarkable-shortcuts?style=flat-square)

- [rM Hacks](https://github.com/mb1986/rm-hacks) - Small improvements and tweaks for rM devices.
  ![Stars](https://img.shields.io/github/stars/mb1986/rm-hacks?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/mb1986/rm-hacks?style=flat-square) ![License](https://img.shields.io/github/license/mb1986/rm-hacks?style=flat-square)

- [rM Hacks (QLMDiff)](https://github.com/asivery/rm-hacks-qmd) - Port of rmhacks for xovi.
  ![Stars](https://img.shields.io/github/stars/asivery/rm-hacks-qmd?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/asivery/rm-hacks-qmd?style=flat-square) ![License](https://img.shields.io/github/license/asivery/rm-hacks-qmd?style=flat-square)

- [rm-hacks-xovi-qmd (Samarkin)](https://github.com/Samarkin/rm-hacks-xovi-qmd)
  ![Stars](https://img.shields.io/github/stars/Samarkin/rm-hacks-xovi-qmd?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Samarkin/rm-hacks-xovi-qmd?style=flat-square) ![License](https://img.shields.io/github/license/Samarkin/rm-hacks-xovi-qmd?style=flat-square)

  - `clearScreenBeforeLocking` - Fixes ghosting when using custom suspend screen.
  - `enableExtraPenOnMove` - Adds a slot for the second pen on Paper Pro Move.
  - `eraseSelection` - Adds an option to delete selection without losing clipboard contents.
  - `forceRefreshGesture` - Adds a gesture to force refresh the screen to eliminate accumulated ghosting.
  - `frontLightIcon` - Adds a front light status indicator to document mode.
  - `gestures` - Adds gestures to switch between two pens and selection tool without the need to show toolbar.
  - `hideCloseButton` - Hides the close button in document view to allow for more space on Paper Pro Move.
  - `instantFavorites` - Removes the delayed refresh of document drawer at the cost of not showing the latest list.
  - `toolbarIcon` - Modifies the show toolbar button to display color of the current tool.
  - `uncompressDock` - Replaces the '+' button in the navigator view with the actual icons.
- [rM-signature-patch](https://github.com/Barabazs/rM-signature-patch) - Simple script to remove that pesky advert at the bottom of a mail originating from a reMarkable.
  ![Stars](https://img.shields.io/github/stars/Barabazs/rM-signature-patch?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Barabazs/rM-signature-patch?style=flat-square) ![License](https://img.shields.io/github/license/Barabazs/rM-signature-patch?style=flat-square)

- [rm-xovi-extensions](https://github.com/asivery/rm-xovi-extensions) - extensions for the reMarkable tablets, which utilize the xovi framework
  ![Stars](https://img.shields.io/github/stars/asivery/rm-xovi-extensions?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/asivery/rm-xovi-extensions?style=flat-square) ![License](https://img.shields.io/github/license/asivery/rm-xovi-extensions?style=flat-square)

  - `framebuffer-spy` - Exposes the address of the system framebuffer.
  - `qt-command-executor` - Injects a Qt module to execute shell commands from QML.
  - `qt-resource-rebuilder` - Injects into Qt and rebuilds resource databases on the fly, allowing QML/image replacement or addition.
  - `random-suspend-screen` - Randomize your reMarkable tablet's suspend screens.
  - `webserver-remote` - Exposes the USB webserver to all interfaces, with a confirmation dialog for inbound connections.
- [Signature-rM](https://github.com/rM-self-serve/signature-rM) - Remove the signature from the bottom of emails sent from the device.
  ![Stars](https://img.shields.io/github/stars/rM-self-serve/signature-rM?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/signature-rM?style=flat-square) ![License](https://img.shields.io/github/license/rM-self-serve/signature-rM?style=flat-square)

- [WebInterface-OnBoot](https://github.com/rM-self-serve/webinterface-onboot) - Enable the web interface on boot.
  ![Stars](https://img.shields.io/github/stars/rM-self-serve/webinterface-onboot?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/webinterface-onboot?style=flat-square) ![License](https://img.shields.io/github/license/rM-self-serve/webinterface-onboot?style=flat-square)

- [webinterface-rmpp](https://github.com/t3rminalV/webinterface-rmpp) - Enable web interface on boot and over wifi on the reMarkable Paper Pro. Includes authentication and SSL.
  ![Stars](https://img.shields.io/github/stars/t3rminalV/webinterface-rmpp?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/t3rminalV/webinterface-rmpp?style=flat-square) ![License](https://img.shields.io/github/license/t3rminalV/webinterface-rmpp?style=flat-square)

- [WebInterface-Upload-Button](https://github.com/rM-self-serve/webinterface-upload-button) - Upload button for the web interface, alternative to drag and drop.
  ![Stars](https://img.shields.io/github/stars/rM-self-serve/webinterface-upload-button?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/webinterface-upload-button?style=flat-square) ![License](https://img.shields.io/github/license/rM-self-serve/webinterface-upload-button?style=flat-square)

- [WebInterface-Wifi](https://github.com/rM-self-serve/webinterface-wifi) - View the web interface if running, over wifi.
  ![Stars](https://img.shields.io/github/stars/rM-self-serve/webinterface-wifi?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/webinterface-wifi?style=flat-square) ![License](https://img.shields.io/github/license/rM-self-serve/webinterface-wifi?style=flat-square)

- [xovi-extensions (FouzR)](https://github.com/FouzR/xovi-extensions)
  ![Stars](https://img.shields.io/github/stars/FouzR/xovi-extensions?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/FouzR/xovi-extensions?style=flat-square) ![License](https://img.shields.io/github/license/FouzR/xovi-extensions?style=flat-square)

  - `favTagButton` - Adds quick access buttons for Favourites and Tagged files.
  - `floating` - Adds a floating toolbar.
  - `gestures` - Adds several useful gestures.
  - `recentsTagged` - New menu showing tagged files, sorted by last modified.
  - `selectionErase` - Enables deleting a stroke via selection tool.
  - `selectionStuff` - Adds "select everything above the line."
- [xovi-qmd-extensions (ingatellent)](https://github.com/ingatellent/xovi-qmd-extensions)
  ![Stars](https://img.shields.io/github/stars/ingatellent/xovi-qmd-extensions?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ingatellent/xovi-qmd-extensions?style=flat-square) ![License](https://img.shields.io/github/license/ingatellent/xovi-qmd-extensions?style=flat-square)

  - `changeVerticalJump` - Increase page scroll distance.
  - `delayStrokeRefresh` - Delay refresh after a colored stroke.
  - `enableAllColors` - Enable full color palette on greyscale devices.
  - `enableExtraPenOnMove` - Adds an extra pen slot to the toolbar
  - `enableShortcuts` - Add keyboard shortcuts for navigation.
  - `enableShortcutsWithScrollOrChangePage` - Adds keyboard shortcuts when used with gestures.
  - `feverLightSteps` - Change brightness slider behavior from 5 to 4 levels.
  - `gestures` - Gestures for zoom, toolbar toggle, navigation, contrast filter.
  - `hideDocumentClose` - Hide the close button in documents.
  - `hidePageLabelsInFullscreen` - Hide page numbers at the bottom of the screen when the toolbar is hidden.
  - `hideShowToolbar` - Hide the button for showing/hiding the toolbar.
  - `miniLightSleep` - Show a line of text at the bottom right corner instead of the light sleep banner.
- [xovi-qmd-extensions (NohamR)](https://github.com/NohamR/xovi-qmd-extensions)
  ![Stars](https://img.shields.io/github/stars/NohamR/xovi-qmd-extensions?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/NohamR/xovi-qmd-extensions?style=flat-square) ![License](https://img.shields.io/github/license/NohamR/xovi-qmd-extensions?style=flat-square)

  - `clock` - Adds a live clock to the library sidebar; tap the entry to toggle seconds display.
  - `convertToText_remover` - Removes the Convert to text option from selection menus and the toolbar.
  - `favoriteButton` - Restores a Favorite action in the document list header for faster pinning.
  - `forceSync` - Adds a cloud button in Quick Settings that forces a library sync when tapped.
  - `hideDocumentClose` - Hides the close button in the document toolbar to prevent accidental exits.
  - `quickSettingsClock` - Injects a tappable clock into the Quick Settings header; tap to toggle between minute and second.
  - `tagButton` - Puts a Tag action next to other list controls to open the tag editor directly.
  - `uncompressDock` - Replaces the condensed More menu in the new document dock with dedicated buttons for notebook, folder, and quick sheet creation.
- [xovi-qmd-extensions (rmitchellscott)](https://github.com/rmitchellscott/xovi-qmd-extensions)
  ![Stars](https://img.shields.io/github/stars/rmitchellscott/xovi-qmd-extensions?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/xovi-qmd-extensions?style=flat-square) ![License](https://img.shields.io/github/license/rmitchellscott/xovi-qmd-extensions?style=flat-square)

  - `createPagesPaperProSize` - Override new page creation to use Paper Pro dimensions.
  - `createPagesRM2Size` - Override new page creation to use reMarkable 2 dimensions.
  - `disableSelectionAutoScroll` - Disable auto scrolling when moving a selection.
  - `hideDevModeIcon` - Hide the developer mode icon next to the battery icon.
  - `hideZoomIndicator` - Auto-hide zoom indicator after 4 seconds.
  - `miniLightSleep` - Replaces the light sleep banner with text saying "Sleeping" with a white background at the top right of the screen.
  - `preventNotebookZoomOut` - Forces all notebook pages to start at 1x zoom with optional horizontal offset. Designed for the Paper Pro Move.
  - `quickSettingsScreenshot` - Adds a screenshot button to the quick settings menu.
  - `unlockMethodsContent` - Bypass subscription check for using on-device Methods templates and documents.
- [xovi-qmd-extensions (StarNumber12046)](https://github.com/StarNumber12046/xovi-qmd-extensions)
  ![Stars](https://img.shields.io/github/stars/StarNumber12046/xovi-qmd-extensions?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/StarNumber12046/xovi-qmd-extensions?style=flat-square) ![License](https://img.shields.io/github/license/StarNumber12046/xovi-qmd-extensions?style=flat-square)

  - `autoNewPage` - Removes the "New Page" button when swiping past end.
  - `clock` - Adds a sidebar clock.
  - `hideDocumentClose` - Removes document close button.
  - `hideShowToolbar` - Hides the "Show Toolbar" button.
  - `miniLightSleep` - Replaces light sleep banner with "Zzz…" text.
  - `pagesIndicator` - Displays page count in sidebar.
  - `quickSettingsClock` - Adds a clock to the quick settings menu.
  - `thickness` - Adds more pen thickness options.
  - `uncompressCreate` - Expands "+" menu with separate folder/notebook/page options.
- [xovi-tripletap](https://github.com/rmitchellscott/xovi-tripletap) - Start xovi with a triple-press of the power button.
  ![Stars](https://img.shields.io/github/stars/rmitchellscott/xovi-tripletap?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/xovi-tripletap?style=flat-square) ![License](https://img.shields.io/github/license/rmitchellscott/xovi-tripletap?style=flat-square)


## Other

- (Unmaintained) [Calibre-Remarkable-Device-Driver-Plugin](https://github.com/naclander/Calibre-Remarkable-Device-Driver-Plugin) - A Calibre Plugin to Manage your Remarkable Books.
  ![Stars](https://img.shields.io/github/stars/naclander/Calibre-Remarkable-Device-Driver-Plugin?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/naclander/Calibre-Remarkable-Device-Driver-Plugin?style=flat-square) ![License](https://img.shields.io/github/license/naclander/Calibre-Remarkable-Device-Driver-Plugin?style=flat-square)

- (Unmaintained) [reHackable/scripts](https://github.com/reHackable/scripts) - A set of bash scripts that may enhance your reMarkable experience.
  ![Stars](https://img.shields.io/github/stars/reHackable/scripts?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/reHackable/scripts?style=flat-square) ![License](https://img.shields.io/github/license/reHackable/scripts?style=flat-square)

- (Unmaintained) [reMarkable-tweak](https://github.com/morngrar/remarkable-tweak) - Tweak tool for the reMarkable paper tablet. Lets you organize your templates with no fuss.
  ![Stars](https://img.shields.io/github/stars/morngrar/remarkable-tweak?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/morngrar/remarkable-tweak?style=flat-square) ![License](https://img.shields.io/github/license/morngrar/remarkable-tweak?style=flat-square)

- [chiappa](https://github.com/gitman-101111/chiappa) - e-Ink bridge/miscellaneous scripts and tools to port other OS's to a reMarkable Pro Paper Move.
  ![Stars](https://img.shields.io/github/stars/gitman-101111/chiappa?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/gitman-101111/chiappa?style=flat-square) ![License](https://img.shields.io/github/license/gitman-101111/chiappa?style=flat-square)

- [Drawj2d](https://drawj2d.sourceforge.io/) - Create technical line drawings on an editable reMarkable notebook page. ([Guidance how to upload](https://sourceforge.net/p/drawj2d/wiki/reMarkable/) the page to the device using rMAPI.)
- [Ephemeris](https://github.com/rmitchellscott/ephemeris) - A Python-based tool that generates clean, daily schedules using ICS calendar data. Designed with e-ink tablets like reMarkable in mind.
  ![Stars](https://img.shields.io/github/stars/rmitchellscott/ephemeris?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/ephemeris?style=flat-square) ![License](https://img.shields.io/github/license/rmitchellscott/ephemeris?style=flat-square)

- [Epistolary](https://github.com/j6k4m8/epistolary) - Emails on the reMarkable. Read and respond to your email inbox in handwriting (auto-converts to text before sending).
  ![Stars](https://img.shields.io/github/stars/j6k4m8/epistolary?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/j6k4m8/epistolary?style=flat-square) ![License](https://img.shields.io/github/license/j6k4m8/epistolary?style=flat-square)

- [ePUB to reMarkable PDF](https://github.com/suntorytimed/epub_to_remarkable) - Self hostable web service for turning an EPUB into a reMarkable optimised PDF.
  ![Stars](https://img.shields.io/github/stars/suntorytimed/epub_to_remarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/suntorytimed/epub_to_remarkable?style=flat-square) ![License](https://img.shields.io/github/license/suntorytimed/epub_to_remarkable?style=flat-square)

- [Funcky reMarkable Exporter](https://github.com/simonbaudart/Funcky.Remarkable.Exporter) - Export notes from a reMarkable Tablet to File System and External Services.
  ![Stars](https://img.shields.io/github/stars/simonbaudart/Funcky.Remarkable.Exporter?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/simonbaudart/Funcky.Remarkable.Exporter?style=flat-square) ![License](https://img.shields.io/github/license/simonbaudart/Funcky.Remarkable.Exporter?style=flat-square)

- [Goosepaper](https://github.com/j6k4m8/goosepaper): Deliver prettily-formatted RSS feeds, news articles, Wikipedia articles-of-the-day, and more to your reMarkable tablet.
  ![Stars](https://img.shields.io/github/stars/j6k4m8/goosepaper?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/j6k4m8/goosepaper?style=flat-square) ![License](https://img.shields.io/github/license/j6k4m8/goosepaper?style=flat-square)

- [instapaper-as-pdf-to-reMarkable](https://github.com/fabianmu/instapaper-as-pdf-to-remarkable) - Export Instapaper-Articles to PDF and send them to a connected rM tablet.
  ![Stars](https://img.shields.io/github/stars/fabianmu/instapaper-as-pdf-to-remarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/fabianmu/instapaper-as-pdf-to-remarkable?style=flat-square) ![License](https://img.shields.io/github/license/fabianmu/instapaper-as-pdf-to-remarkable?style=flat-square)

- [landscape-pdf](https://github.com/nmoran/landscape-pdf) - Utility to convert pdf documents to read in landscape mode. Useful for papers and text books.
  ![Stars](https://img.shields.io/github/stars/nmoran/landscape-pdf?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/nmoran/landscape-pdf?style=flat-square) ![License](https://img.shields.io/github/license/nmoran/landscape-pdf?style=flat-square)

- [mail2rm](https://github.com/glatzor/mail2rm) - Mail PDF documents to your reMarkable cloud using your mail transport agent e.g. postfix.
  ![Stars](https://img.shields.io/github/stars/glatzor/mail2rm?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/glatzor/mail2rm?style=flat-square) ![License](https://img.shields.io/github/license/glatzor/mail2rm?style=flat-square)

- [microSD](http://www.davisr.me/projects/remarkable-microsd/) - Tutorial for adding a microSD card reader to the reMarkable 1.
- [morningpaper2reMarkable](https://github.com/jessfraz/morningpaper2remarkable) - A bot to sync the morning paper to a reMarkable tablet.
  ![Stars](https://img.shields.io/github/stars/jessfraz/morningpaper2remarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/jessfraz/morningpaper2remarkable?style=flat-square) ![License](https://img.shields.io/github/license/jessfraz/morningpaper2remarkable?style=flat-square)

- [neofetch](https://github.com/rM-self-serve/neofetch-rM) - A command-line system information tool written in bash 3.2+.
  ![Stars](https://img.shields.io/github/stars/rM-self-serve/neofetch-rM?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/neofetch-rM?style=flat-square) ![License](https://img.shields.io/github/license/rM-self-serve/neofetch-rM?style=flat-square)

- [nix-remarkable](https://github.com/siraben/nix-remarkable) - Nix expressions for the reMarkable tablet leveraging the company's toolchain.
  ![Stars](https://img.shields.io/github/stars/siraben/nix-remarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/siraben/nix-remarkable?style=flat-square) ![License](https://img.shields.io/github/license/siraben/nix-remarkable?style=flat-square)

- [paper2reMarkable](https://github.com/GjjvdBurg/paper2remarkable) - Download an academic paper or HTML article, crop it, and send it to the reMarkable with a single command.
  ![Stars](https://img.shields.io/github/stars/GjjvdBurg/paper2remarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/GjjvdBurg/paper2remarkable?style=flat-square) ![License](https://img.shields.io/github/license/GjjvdBurg/paper2remarkable?style=flat-square)

- [Parabola-rM](http://www.davisr.me/projects/parabola-rm/) - A Desktop GNU/Linux-libre replacement OS with fast partial refreshing and USB OTG.
- [pdf2rmnotebook](https://github.com/JCN-9000/pdf2rmnotebook) - Creates a reMarkable Notebook from multiple PDF files.
  ![Stars](https://img.shields.io/github/stars/JCN-9000/pdf2rmnotebook?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/JCN-9000/pdf2rmnotebook?style=flat-square) ![License](https://img.shields.io/github/license/JCN-9000/pdf2rmnotebook?style=flat-square)

- [pocket2rm](https://github.com/glidergeek/pocket2rm) - Synchronize articles from read-later platform pocket in PDF and epub.
  ![Stars](https://img.shields.io/github/stars/glidergeek/pocket2rm?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/glidergeek/pocket2rm?style=flat-square) ![License](https://img.shields.io/github/license/glidergeek/pocket2rm?style=flat-square)

- [reCalibre-Driver](https://github.com/zer0trip/reCalibre) - A Calibre plugin for syncing books to a reMarkable, via KOReader or the native UI.
  ![Stars](https://img.shields.io/github/stars/zer0trip/reCalibre?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/zer0trip/reCalibre?style=flat-square) ![License](https://img.shields.io/github/license/zer0trip/reCalibre?style=flat-square)

- [reHackable/maxio](https://github.com/reHackable/maxio) - Companion daemon for the reMarkable paper tablet.
  ![Stars](https://img.shields.io/github/stars/reHackable/maxio?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/reHackable/maxio?style=flat-square) ![License](https://img.shields.io/github/license/reHackable/maxio?style=flat-square)

- [remailable](https://github.com/j6k4m8/remailable) - Email PDFs directly to your reMarkable. ([Free publicly-hosted version available](https://remailable.getneutrality.org/)).
  ![Stars](https://img.shields.io/github/stars/j6k4m8/remailable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/j6k4m8/remailable?style=flat-square) ![License](https://img.shields.io/github/license/j6k4m8/remailable?style=flat-square)

- [reMarkable CLI tooling](https://github.com/cherti/remarkable-cli-tooling) - CLI-tooling to sync documents to a reMarkable, to clean deleted files etc. without needing cloud access
  ![Stars](https://img.shields.io/github/stars/cherti/remarkable-cli-tooling?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/cherti/remarkable-cli-tooling?style=flat-square) ![License](https://img.shields.io/github/license/cherti/remarkable-cli-tooling?style=flat-square)

- [remarkable-api](https://github.com/Penguin-Guru/remarkable-api) - A simple bash script to interact with reMarkable devices' USB Web Interface.
  ![Stars](https://img.shields.io/github/stars/Penguin-Guru/remarkable-api?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Penguin-Guru/remarkable-api?style=flat-square) ![License](https://img.shields.io/github/license/Penguin-Guru/remarkable-api?style=flat-square)

- [reMarkable-crosswords](https://github.com/shapeshed/remarkable-crosswords) - Get crosswords freshly delivered to your Remarkable every morning.
  ![Stars](https://img.shields.io/github/stars/shapeshed/remarkable-crosswords?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/shapeshed/remarkable-crosswords?style=flat-square) ![License](https://img.shields.io/github/license/shapeshed/remarkable-crosswords?style=flat-square)

- [reMarkable-fs](https://github.com/nick8325/remarkable-fs) - A FUSE filesystem wrapper for the reMarkable tablet.
  ![Stars](https://img.shields.io/github/stars/nick8325/remarkable-fs?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/nick8325/remarkable-fs?style=flat-square) ![License](https://img.shields.io/github/license/nick8325/remarkable-fs?style=flat-square)

- [remarkable-nixos](https://github.com/gitman-101111/remarkable-nixos) - Run NixOS on your reMarkable Pro Paper Move (others possible)
  ![Stars](https://img.shields.io/github/stars/gitman-101111/remarkable-nixos?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/gitman-101111/remarkable-nixos?style=flat-square) ![License](https://img.shields.io/github/license/gitman-101111/remarkable-nixos?style=flat-square)

- [reMarkable-random-screens](https://github.com/Neurone/reMarkable) - Change your poweroff and suspend screens every 5 minutes with random images of your choice
  ![Stars](https://img.shields.io/github/stars/Neurone/reMarkable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Neurone/reMarkable?style=flat-square) ![License](https://img.shields.io/github/license/Neurone/reMarkable?style=flat-square)

- [reMarkable-tablet-driver](https://github.com/FreeCap23/reMarkable-tablet-driver) - Use your reMarkable as a drawing tablet in Linux with pressure sensitivity and tilt. Works in Wayland.
  ![Stars](https://img.shields.io/github/stars/FreeCap23/reMarkable-tablet-driver?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/FreeCap23/reMarkable-tablet-driver?style=flat-square) ![License](https://img.shields.io/github/license/FreeCap23/reMarkable-tablet-driver?style=flat-square)

- [reMarkable-touchgestures](https://github.com/ddvk/remarkable-touchgestures) - Touch gestures (swipe/touch) for easy page navigation.
  ![Stars](https://img.shields.io/github/stars/ddvk/remarkable-touchgestures?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ddvk/remarkable-touchgestures?style=flat-square) ![License](https://img.shields.io/github/license/ddvk/remarkable-touchgestures?style=flat-square)

- [reMarkable_entware](http://github.com/evidlo/remarkable_entware) - Package manager for reMarkable.  Install common Unix utilities through the command line.
  ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_entware?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_entware?style=flat-square) ![License](https://img.shields.io/github/license/evidlo/remarkable_entware?style=flat-square)

- [reMarkable_keyboard](https://github.com/Evidlo/remarkable_keyboard) - Software to use rM as wireless keyboard/mouse.
  ![Stars](https://img.shields.io/github/stars/Evidlo/remarkable_keyboard?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Evidlo/remarkable_keyboard?style=flat-square) ![License](https://img.shields.io/github/license/Evidlo/remarkable_keyboard?style=flat-square)

- [reMarkable_mouse](https://github.com/evidlo/remarkable_mouse) - Use your reMarkable as a graphics tablet.
  ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_mouse?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_mouse?style=flat-square) ![License](https://img.shields.io/github/license/evidlo/remarkable_mouse?style=flat-square)

- [remarkable_news](https://github.com/evidlo/remarkable_news) - Use daily news/comics/images as the suspend screen.
  ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_news?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_news?style=flat-square) ![License](https://img.shields.io/github/license/evidlo/remarkable_news?style=flat-square)

- [reMarkable_pdflets](https://github.com/evidlo/remarkable_pdflets) - Dynamically updating PDFs.
  ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_pdflets?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_pdflets?style=flat-square) ![License](https://img.shields.io/github/license/evidlo/remarkable_pdflets?style=flat-square)

- [remarkable_printer](https://github.com/Evidlo/remarkable_printer) - Print from any device to reMarkable without browser extensions or reMarkable cloud.
  ![Stars](https://img.shields.io/github/stars/Evidlo/remarkable_printer?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Evidlo/remarkable_printer?style=flat-square) ![License](https://img.shields.io/github/license/Evidlo/remarkable_printer?style=flat-square)

- [reMarkablePocket](https://github.com/nov1n/RemarkablePocket) - Synchronize articles from read-later platform Pocket in epub format.
  ![Stars](https://img.shields.io/github/stars/nov1n/RemarkablePocket?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/nov1n/RemarkablePocket?style=flat-square) ![License](https://img.shields.io/github/license/nov1n/RemarkablePocket?style=flat-square)

- [remarkable-ssh](https://github.com/Penguin-Guru/remarkable-ssh) - A bash script to manage files on reMarkable devices via CLI and SSH.
  ![Stars](https://img.shields.io/github/stars/Penguin-Guru/remarkable-ssh?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Penguin-Guru/remarkable-ssh?style=flat-square) ![License](https://img.shields.io/github/license/Penguin-Guru/remarkable-ssh?style=flat-square)

- [reMarkableSync](https://github.com/jamesf91/reMarkableSync) - A Microsoft OneNote addin for importing notebooks from reMarkable as text or images.
  ![Stars](https://img.shields.io/github/stars/jamesf91/reMarkableSync?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/jamesf91/reMarkableSync?style=flat-square) ![License](https://img.shields.io/github/license/jamesf91/reMarkableSync?style=flat-square)

- [remarks](https://github.com/Scrybbling-together/remarks) - Extract highlights, scribbles, and annotations from PDFs. Export to Markdown, PNG, and SVG.
  ![Stars](https://img.shields.io/github/stars/Scrybbling-together/remarks?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Scrybbling-together/remarks?style=flat-square) ![License](https://img.shields.io/github/license/Scrybbling-together/remarks?style=flat-square)

- [reMouseable](https://github.com/kevinconway/remouseable) - Use your reMarkable tablet as a mouse.
  ![Stars](https://img.shields.io/github/stars/kevinconway/remouseable?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/kevinconway/remouseable?style=flat-square) ![License](https://img.shields.io/github/license/kevinconway/remouseable?style=flat-square)

- [remt](https://gitlab.com/wrobell/remt) - reMarkable tablet command-line tools.
  ![Stars](https://img.shields.io/gitlab/stars/wrobell/remt?style=flat-square) ![Last Commit](https://img.shields.io/gitlab/last-commit/wrobell/remt?style=flat-square) ![License](https://img.shields.io/gitlab/license/wrobell/remt?style=flat-square)

- [reSnap](https://github.com/cloudsftp/reSnap) - Take snapshots of your reMarkable screen over SSH.
  ![Stars](https://img.shields.io/github/stars/cloudsftp/reSnap?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/cloudsftp/reSnap?style=flat-square) ![License](https://img.shields.io/github/license/cloudsftp/reSnap?style=flat-square)

- [rM-dl-annotated](https://github.com/jmptable/rm-dl-annotated) - Export annotated PDFs from reMarkable tablets.
  ![Stars](https://img.shields.io/github/stars/jmptable/rm-dl-annotated?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/jmptable/rm-dl-annotated?style=flat-square) ![License](https://img.shields.io/github/license/jmptable/rm-dl-annotated?style=flat-square)

- [rm-pySAS](https://github.com/tenJirka/rm-pySAS) - Python wrapper for [simple](https://rmkit.dev/apps/sas).
  ![Stars](https://img.shields.io/github/stars/tenJirka/rm-pySAS?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/tenJirka/rm-pySAS?style=flat-square) ![License](https://img.shields.io/github/license/tenJirka/rm-pySAS?style=flat-square)

- [rm2anki](https://github.com/stelzch/rm2anki) - Convert reMarkable notebooks into an Anki card decks.
  ![Stars](https://img.shields.io/github/stars/stelzch/rm2anki?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/stelzch/rm2anki?style=flat-square) ![License](https://img.shields.io/github/license/stelzch/rm2anki?style=flat-square)

- [rmathlab](https://github.com/Samdney/rmathlab) - A Linux toolset for the reMarkable 2 tablet, which enables math handwriting recognition and LaTeX generation over USB via Mathpix.
  ![Stars](https://img.shields.io/github/stars/Samdney/rmathlab?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Samdney/rmathlab?style=flat-square) ![License](https://img.shields.io/github/license/Samdney/rmathlab?style=flat-square)

- [rmirro](https://github.com/hersle/rmirro) - A script that synchronizes PDFs of documents between a Remarkable and a computer folder that mirrors its file structure without cloud access.
  ![Stars](https://img.shields.io/github/stars/hersle/rmirro?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/hersle/rmirro?style=flat-square) ![License](https://img.shields.io/github/license/hersle/rmirro?style=flat-square)

- [RMPP Entware](https://github.com/hmenzagh/rmpp-entware) - Package manager for reMarkable Paper Pro.  Install okpg package manager.
  ![Stars](https://img.shields.io/github/stars/hmenzagh/rmpp-entware?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/hmenzagh/rmpp-entware?style=flat-square) ![License](https://img.shields.io/github/license/hmenzagh/rmpp-entware?style=flat-square)

- [rMsync](https://github.com/lschwetlick/rMsync) - Synchronisation script with a local dedicated "library" folder.
  ![Stars](https://img.shields.io/github/stars/lschwetlick/rMsync?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/lschwetlick/rMsync?style=flat-square) ![License](https://img.shields.io/github/license/lschwetlick/rMsync?style=flat-square)

- [rmTabletDriver](https://github.com/LinusCDE/rmTabletDriver) - Application that allows you to simulate/clone rM input on your computer.
  ![Stars](https://img.shields.io/github/stars/LinusCDE/rmTabletDriver?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/rmTabletDriver?style=flat-square) ![License](https://img.shields.io/github/license/LinusCDE/rmTabletDriver?style=flat-square)

- [rmWacomToMouse](https://github.com/LinusCDE/rmWacomToMouse) - Use the wacom pen as a mouse to draw on your pc.
  ![Stars](https://img.shields.io/github/stars/LinusCDE/rmWacomToMouse?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/rmWacomToMouse?style=flat-square) ![License](https://img.shields.io/github/license/LinusCDE/rmWacomToMouse?style=flat-square)

- [rmWebUiTools](https://github.com/LinusCDE/rmWebUiTools) - View a file tree, see statistics and export/backup all files with some simple scripts utilizing the web ui.
  ![Stars](https://img.shields.io/github/stars/LinusCDE/rmWebUiTools?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/rmWebUiTools?style=flat-square) ![License](https://img.shields.io/github/license/LinusCDE/rmWebUiTools?style=flat-square)

- [send_by_rmapi](https://github.com/LisaGlaser/send_by_rmapi) - A Calibre plugin to send books to your reMarkable, making use of rmapi.
  ![Stars](https://img.shields.io/github/stars/LisaGlaser/send_by_rmapi?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/LisaGlaser/send_by_rmapi?style=flat-square) ![License](https://img.shields.io/github/license/LisaGlaser/send_by_rmapi?style=flat-square)


## Screen Sharing/Streaming

- [AppLoad-RMStream](https://github.com/asivery/appload-rmstream) - An AppLoad application for streaming your reMarkable tablet's screen over HTTP.
  ![Stars](https://img.shields.io/github/stars/asivery/appload-rmstream?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/asivery/appload-rmstream?style=flat-square) ![License](https://img.shields.io/github/license/asivery/appload-rmstream?style=flat-square)

- [goMarkableStream](https://github.com/owulveryck/goMarkableStream) - Stream the screen of the reMarkable 2 (FW 2.5) easily (client/server in Go with no installation) along with the colors (with FW > 2.11.x).
  ![Stars](https://img.shields.io/github/stars/owulveryck/goMarkableStream?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/owulveryck/goMarkableStream?style=flat-square) ![License](https://img.shields.io/github/license/owulveryck/goMarkableStream?style=flat-square)

- [pipes and paper](https://gitlab.com/afandian/pipes-and-paper) - Stream pen strokes to browser canvas via websockets ([blog post](https://blog.afandian.com/2020/10/pipes-and-paper-remarkable/)). Uses Python and SSH, nothing to compile or install on the reMarkable device.
  ![Stars](https://img.shields.io/gitlab/stars/afandian/pipes-and-paper?style=flat-square) ![Last Commit](https://img.shields.io/gitlab/last-commit/afandian/pipes-and-paper?style=flat-square) ![License](https://img.shields.io/gitlab/license/afandian/pipes-and-paper?style=flat-square)

- [pipes and paper enhanced](https://github.com/Pyrrhu5/pipes-and-paper-enhanced/tree/stable) - Share the pen strokes to a browser without installling anything on the ReMarkable (a revived fork of the previous link with pen colors and eraser support, responsive interface).
  ![Stars](https://img.shields.io/github/stars/Pyrrhu5/pipes-and-paper-enhanced?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/Pyrrhu5/pipes-and-paper-enhanced?style=flat-square) ![License](https://img.shields.io/github/license/Pyrrhu5/pipes-and-paper-enhanced?style=flat-square)

- (Unmaintained) [pipes and rust](https://github.com/AnyTimeTraveler/pipes-and-rust) - (Made for rM2) Stream pen strokes to browser. A single executable on the reMarkable that hosts a tiny webserver in the local WLAN.
  ![Stars](https://img.shields.io/github/stars/AnyTimeTraveler/pipes-and-rust?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/AnyTimeTraveler/pipes-and-rust?style=flat-square) ![License](https://img.shields.io/github/license/AnyTimeTraveler/pipes-and-rust?style=flat-square)

- [reStream](https://github.com/rien/reStream) - Stream your reMarkable screen over SSH.
  ![Stars](https://img.shields.io/github/stars/rien/reStream?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/rien/reStream?style=flat-square) ![License](https://img.shields.io/github/license/rien/reStream?style=flat-square)

- [rMview](https://github.com/bordaigorl/rmview) - A fast GUI to stream your reMarkable screen over vanilla-SSH or VNC.
  ![Stars](https://img.shields.io/github/stars/bordaigorl/rmview?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/bordaigorl/rmview?style=flat-square) ![License](https://img.shields.io/github/license/bordaigorl/rmview?style=flat-square)

- [rM-vnc-server](https://github.com/peter-sa/rM-vnc-server) - A fast & efficient damage-tracking (sending only updated regions) VNC server for streaming the reMarkable's screen.
  ![Stars](https://img.shields.io/github/stars/peter-sa/rM-vnc-server?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/peter-sa/rM-vnc-server?style=flat-square) ![License](https://img.shields.io/github/license/peter-sa/rM-vnc-server?style=flat-square)

- [srvfb](https://github.com/merovius/srvfb) - Alternative screen-streaming software. Written in Go.
  ![Stars](https://img.shields.io/github/stars/merovius/srvfb?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/merovius/srvfb?style=flat-square) ![License](https://img.shields.io/github/license/merovius/srvfb?style=flat-square)

- [VNSee](https://github.com/matteodelabre/vnsee) - VNC client for the reMarkable tablet allowing you to use the device as a second screen.
  ![Stars](https://img.shields.io/github/stars/matteodelabre/vnsee?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/matteodelabre/vnsee?style=flat-square) ![License](https://img.shields.io/github/license/matteodelabre/vnsee?style=flat-square)

