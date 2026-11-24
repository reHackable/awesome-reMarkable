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
  ![Last Commit](https://img.shields.io/github/last-commit/bsdz/google-drive-remarkable-sync) ![License](https://img.shields.io/github/license/bsdz/google-drive-remarkable-sync) ![Stars](https://img.shields.io/github/stars/bsdz/google-drive-remarkable-sync) ![Forks](https://img.shields.io/github/forks/bsdz/google-drive-remarkable-sync)

- [jrmapi](https://github.com/jlarriba/jrmapi) - A Java API for the reMarkable Cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/jlarriba/jrmapi) ![License](https://img.shields.io/github/license/jlarriba/jrmapi) ![Stars](https://img.shields.io/github/stars/jlarriba/jrmapi) ![Forks](https://img.shields.io/github/forks/jlarriba/jrmapi)

- (Unmaintained) [reMarkableAPI](https://github.com/splitbrain/ReMarkableAPI) - Docs and implementation of the reMarkable file sync API.
  ![Last Commit](https://img.shields.io/github/last-commit/splitbrain/ReMarkableAPI) ![License](https://img.shields.io/github/license/splitbrain/ReMarkableAPI) ![Stars](https://img.shields.io/github/stars/splitbrain/ReMarkableAPI) ![Forks](https://img.shields.io/github/forks/splitbrain/ReMarkableAPI)

- (Unmaintained) [reMarkable-typescript](https://github.com/Ogdentrod/reMarkable-typescript) - TypeScript API for reMarkable Cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/Ogdentrod/reMarkable-typescript) ![License](https://img.shields.io/github/license/Ogdentrod/reMarkable-typescript) ![Stars](https://img.shields.io/github/stars/Ogdentrod/reMarkable-typescript) ![Forks](https://img.shields.io/github/forks/Ogdentrod/reMarkable-typescript)

- [Remarkable.jl](https://github.com/theogf/Remarkable.jl) - Julia API Interface to the reMarkable cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/theogf/Remarkable.jl) ![License](https://img.shields.io/github/license/theogf/Remarkable.jl) ![Stars](https://img.shields.io/github/stars/theogf/Remarkable.jl) ![Forks](https://img.shields.io/github/forks/theogf/Remarkable.jl)

- [remarkdav](https://github.com/hansegucker/remarkdav) - A tool to sync PDF files from a WebDAV directory to the reMarkable Cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/hansegucker/remarkdav) ![License](https://img.shields.io/github/license/hansegucker/remarkdav) ![Stars](https://img.shields.io/github/stars/hansegucker/remarkdav) ![Forks](https://img.shields.io/github/forks/hansegucker/remarkdav)

- [rMAPI](https://github.com/ddvk/rmapi) ReMarkable Cloud Go API.
  ![Last Commit](https://img.shields.io/github/last-commit/ddvk/rmapi) ![License](https://img.shields.io/github/license/ddvk/rmapi) ![Stars](https://img.shields.io/github/stars/ddvk/rmapi) ![Forks](https://img.shields.io/github/forks/ddvk/rmapi)

- (Unmaintained) [rmapy](https://github.com/subutux/rmapy) - ReMarkable Cloud Python API.
  ![Last Commit](https://img.shields.io/github/last-commit/subutux/rmapy) ![License](https://img.shields.io/github/license/subutux/rmapy) ![Stars](https://img.shields.io/github/stars/subutux/rmapy) ![Forks](https://img.shields.io/github/forks/subutux/rmapy)

- [rmcl](https://github.com/rschroll/rmcl)- Asynchronous Python library for the reMarkable Cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/rschroll/rmcl) ![License](https://img.shields.io/github/license/rschroll/rmcl) ![Stars](https://img.shields.io/github/stars/rschroll/rmcl) ![Forks](https://img.shields.io/github/forks/rschroll/rmcl)

- [rmfakecloud](https://github.com/ddvk/rmfakecloud) - Fake Cloud Sync, server implementation of the Cloud API.
  ![Last Commit](https://img.shields.io/github/last-commit/ddvk/rmfakecloud) ![License](https://img.shields.io/github/license/ddvk/rmfakecloud) ![Stars](https://img.shields.io/github/stars/ddvk/rmfakecloud) ![Forks](https://img.shields.io/github/forks/ddvk/rmfakecloud)


### Lines Format

- [librm_lines](https://github.com/RedTTGMoss/librm_lines) - A C++ library for reading & writing & rendering v6 files with the original reMarkable quill library, includes multiple languages wrappers for python and npm.
  ![Last Commit](https://img.shields.io/github/last-commit/RedTTGMoss/librm_lines) ![License](https://img.shields.io/github/license/RedTTGMoss/librm_lines) ![Stars](https://img.shields.io/github/stars/RedTTGMoss/librm_lines) ![Forks](https://img.shields.io/github/forks/RedTTGMoss/librm_lines)

- [lines-are-beautiful](https://github.com/ax3l/lines-are-beautiful) - C++ File API for the reMarkable tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/ax3l/lines-are-beautiful) ![License](https://img.shields.io/github/license/ax3l/lines-are-beautiful) ![Stars](https://img.shields.io/github/stars/ax3l/lines-are-beautiful) ![Forks](https://img.shields.io/github/forks/ax3l/lines-are-beautiful)

- [lines-are-rusty](https://github.com/ax3l/lines-are-rusty) - Rust File API for the reMarkable tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/ax3l/lines-are-rusty) ![License](https://img.shields.io/github/license/ax3l/lines-are-rusty) ![Stars](https://img.shields.io/github/stars/ax3l/lines-are-rusty) ![Forks](https://img.shields.io/github/forks/ax3l/lines-are-rusty)

- [reMarkable-kaitai](https://github.com/matomatical/reMarkable-kaitai) - [Kaitai Struct](https://kaitai.io/) format specification for the binary lines format.
  ![Last Commit](https://img.shields.io/github/last-commit/matomatical/reMarkable-kaitai) ![License](https://img.shields.io/github/license/matomatical/reMarkable-kaitai) ![Stars](https://img.shields.io/github/stars/matomatical/reMarkable-kaitai) ![Forks](https://img.shields.io/github/forks/matomatical/reMarkable-kaitai)

- (Unmaintained) [reMarkable-layers](https://github.com/bsdz/remarkable-layers) - Python API for reading & writing reMarkable Lines format. Supports very basic conversion of PDFs and SVGs to Lines format.
  ![Last Commit](https://img.shields.io/github/last-commit/bsdz/remarkable-layers) ![License](https://img.shields.io/github/license/bsdz/remarkable-layers) ![Stars](https://img.shields.io/github/stars/bsdz/remarkable-layers) ![Forks](https://img.shields.io/github/forks/bsdz/remarkable-layers)

- [rmrl](https://github.com/rschroll/rmrl) - The reMarkable Rendering Library for Python converts annotated documents to PDF files.
  ![Last Commit](https://img.shields.io/github/last-commit/rschroll/rmrl) ![License](https://img.shields.io/github/license/rschroll/rmrl) ![Stars](https://img.shields.io/github/stars/rschroll/rmrl) ![Forks](https://img.shields.io/github/forks/rschroll/rmrl)

- [rmscene](https://github.com/ricklupton/rmscene) - Python library to read v6 files / software version 3.
  ![Last Commit](https://img.shields.io/github/last-commit/ricklupton/rmscene) ![License](https://img.shields.io/github/license/ricklupton/rmscene) ![Stars](https://img.shields.io/github/stars/ricklupton/rmscene) ![Forks](https://img.shields.io/github/forks/ricklupton/rmscene)


### Other APIs

- [libreMarkable](https://github.com/canselcik/libremarkable) - A framework for developing applications with native refresh support for reMarkable Tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/canselcik/libremarkable) ![License](https://img.shields.io/github/license/canselcik/libremarkable) ![Stars](https://img.shields.io/github/stars/canselcik/libremarkable) ![Forks](https://img.shields.io/github/forks/canselcik/libremarkable)


## Applications

- [harmony](https://rmkit.dev/apps/harmony) - a low latency sketching app with procedural brushes.
- [KOReader](https://github.com/koreader/koreader) - An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats.
  ![Last Commit](https://img.shields.io/github/last-commit/koreader/koreader) ![License](https://img.shields.io/github/license/koreader/koreader) ![Stars](https://img.shields.io/github/stars/koreader/koreader) ![Forks](https://img.shields.io/github/forks/koreader/koreader)

- [darvin/plato](https://github.com/darvin/plato) [LinusCDE/plato](https://github.com/LinusCDE/plato) - Plato reader port. Supports pdfs, epubs, many other formats.
  ![Last Commit](https://img.shields.io/github/last-commit/darvin/plato) ![License](https://img.shields.io/github/license/darvin/plato) ![Stars](https://img.shields.io/github/stars/darvin/plato) ![Forks](https://img.shields.io/github/forks/darvin/plato)

- [Rebook](https://github.com/fsniper/ReBook) - The missing book store for reMarkable.
  ![Last Commit](https://img.shields.io/github/last-commit/fsniper/ReBook) ![License](https://img.shields.io/github/license/fsniper/ReBook) ![Stars](https://img.shields.io/github/stars/fsniper/ReBook) ![Forks](https://img.shields.io/github/forks/fsniper/ReBook)

- [reGenda](https://github.com/tenJirka/reGenda) - An agenda-based calendar for reMarkable.
  ![Last Commit](https://img.shields.io/github/last-commit/tenJirka/reGenda) ![License](https://img.shields.io/github/license/tenJirka/reGenda) ![Stars](https://img.shields.io/github/stars/tenJirka/reGenda) ![Forks](https://img.shields.io/github/forks/tenJirka/reGenda)

- [reMarkable keywriter](https://github.com/dps/remarkable-keywriter) - A distraction free keyboard notes app.
  ![Last Commit](https://img.shields.io/github/last-commit/dps/remarkable-keywriter) ![License](https://img.shields.io/github/license/dps/remarkable-keywriter) ![Stars](https://img.shields.io/github/stars/dps/remarkable-keywriter) ![Forks](https://img.shields.io/github/forks/dps/remarkable-keywriter)

- [reMarkable SSH explorer](https://github.com/iacobucci/rm-ssh-explorer) - An on-device ssh explorer for downloading pdf files from a server to the reMarkable tablet
  ![Last Commit](https://img.shields.io/github/last-commit/iacobucci/rm-ssh-explorer) ![License](https://img.shields.io/github/license/iacobucci/rm-ssh-explorer) ![Stars](https://img.shields.io/github/stars/iacobucci/rm-ssh-explorer) ![Forks](https://img.shields.io/github/forks/iacobucci/rm-ssh-explorer)

- [reMarkable wikipedia](https://github.com/dps/remarkable-wikipedia) - Offline wikipedia reader for reMarkable.
  ![Last Commit](https://img.shields.io/github/last-commit/dps/remarkable-wikipedia) ![License](https://img.shields.io/github/license/dps/remarkable-wikipedia) ![Stars](https://img.shields.io/github/stars/dps/remarkable-wikipedia) ![Forks](https://img.shields.io/github/forks/dps/remarkable-wikipedia)

- (Unmaintained) [remarkaBot](https://github.com/Davide95/remarkaBot) - Fetch your documents from Telegram.
  ![Last Commit](https://img.shields.io/github/last-commit/Davide95/remarkaBot) ![License](https://img.shields.io/github/license/Davide95/remarkaBot) ![Stars](https://img.shields.io/github/stars/Davide95/remarkaBot) ![Forks](https://img.shields.io/github/forks/Davide95/remarkaBot)

- [whiteboard-hypercard](https://github.com/fenollp/reMarkable-tools) - Live collaboration, drawing, chat, whiteboarding.
  ![Last Commit](https://img.shields.io/github/last-commit/fenollp/reMarkable-tools) ![License](https://img.shields.io/github/license/fenollp/reMarkable-tools) ![Stars](https://img.shields.io/github/stars/fenollp/reMarkable-tools) ![Forks](https://img.shields.io/github/forks/fenollp/reMarkable-tools)

- [Writerdeck for reMarkable 1](https://github.com/bjornte/Writerdeck-for-reMarkable) - Distraction-free Markdown word processor with keyboard support via a companion app or usb. With optional syncing and encryption of documents.
  ![Last Commit](https://img.shields.io/github/last-commit/bjornte/Writerdeck-for-reMarkable) ![License](https://img.shields.io/github/license/bjornte/Writerdeck-for-reMarkable) ![Stars](https://img.shields.io/github/stars/bjornte/Writerdeck-for-reMarkable) ![Forks](https://img.shields.io/github/forks/bjornte/Writerdeck-for-reMarkable)


### Browser extensions

- [rePub](https://github.com/hafaio/repub) - unofficial browser extension that creates ePubs from websites and can either upload them to reMarkable cloud or save them locally, currently for Chrome only
  ![Last Commit](https://img.shields.io/github/last-commit/hafaio/repub) ![License](https://img.shields.io/github/license/hafaio/repub) ![Stars](https://img.shields.io/github/stars/hafaio/repub) ![Forks](https://img.shields.io/github/forks/hafaio/repub)

- [rePubfox](https://github.com/jrockwar/repubfox) - a hard fork of rePub for Firefox
  ![Last Commit](https://img.shields.io/github/last-commit/jrockwar/repubfox) ![License](https://img.shields.io/github/license/jrockwar/repubfox) ![Stars](https://img.shields.io/github/stars/jrockwar/repubfox) ![Forks](https://img.shields.io/github/forks/jrockwar/repubfox)


### Games

- [chessMarkable](https://github.com/LinusCDE/chessmarkable) - Play chess against a bot or a friend.
  ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/chessmarkable) ![License](https://img.shields.io/github/license/LinusCDE/chessmarkable) ![Stars](https://img.shields.io/github/stars/LinusCDE/chessmarkable) ![Forks](https://img.shields.io/github/forks/LinusCDE/chessmarkable)

- [DOOMarkable](https://github.com/LinusCDE/doomarkable) - Play DOOM on the reMarkable 1.
  ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/doomarkable) ![License](https://img.shields.io/github/license/LinusCDE/doomarkable) ![Stars](https://img.shields.io/github/stars/LinusCDE/doomarkable) ![Forks](https://img.shields.io/github/forks/LinusCDE/doomarkable)

- [minesweeper](https://rmkit.dev/apps/minesweeper) - A mine detection game.
- [recrossable](https://github.com/sandsmark/recrossable) - Crossword game with simplistic handwriting recognition and automatic generation of crosswords.
  ![Last Commit](https://img.shields.io/github/last-commit/sandsmark/recrossable) ![License](https://img.shields.io/github/license/sandsmark/recrossable) ![Stars](https://img.shields.io/github/stars/sandsmark/recrossable) ![Forks](https://img.shields.io/github/forks/sandsmark/recrossable)

- [retris](https://github.com/LinusCDE/retris) - Play a clone of the popular block stacking game with either buttons or swipe guestures.
  ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/retris) ![License](https://img.shields.io/github/license/LinusCDE/retris) ![Stars](https://img.shields.io/github/stars/LinusCDE/retris) ![Forks](https://img.shields.io/github/forks/LinusCDE/retris)


### Launchers

- [draft-reMarkable](https://github.com/dixonary/draft-reMarkable) - A launcher for the reMarkable tablet, which wraps around the standard interface.
  ![Last Commit](https://img.shields.io/github/last-commit/dixonary/draft-reMarkable) ![License](https://img.shields.io/github/license/dixonary/draft-reMarkable) ![Stars](https://img.shields.io/github/stars/dixonary/draft-reMarkable) ![Forks](https://img.shields.io/github/forks/dixonary/draft-reMarkable)

- [oxide](https://oxide.eeems.codes) - A launcher application for the reMarkable tablet.
- [remux](https://rmkit.dev/apps/remux) - A multi-tasking launcher for the reMarkable tablet.


## Cloud Tools

- [AgentNews-RemarkableRSSReader](https://github.com/eksubin/AgentNews-RemarkableRSSReader) - An AI agent for processing RSS news feeds and sending them to reMarkable via Google Drive API.
  ![Last Commit](https://img.shields.io/github/last-commit/eksubin/AgentNews-RemarkableRSSReader) ![License](https://img.shields.io/github/license/eksubin/AgentNews-RemarkableRSSReader) ![Stars](https://img.shields.io/github/stars/eksubin/AgentNews-RemarkableRSSReader) ![Forks](https://img.shields.io/github/forks/eksubin/AgentNews-RemarkableRSSReader)

- [Aviary](https://github.com/rmitchellscott/aviary) - A webhook-driven document uploader for reMarkable Cloud and rmfakecloud, featuring a static UI and a Go backend. Optional integration for email via AWS SES.
  ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/aviary) ![License](https://img.shields.io/github/license/rmitchellscott/aviary) ![Stars](https://img.shields.io/github/stars/rmitchellscott/aviary) ![Forks](https://img.shields.io/github/forks/rmitchellscott/aviary)

- [CUPS Printing](https://github.com/ofosos/scratch/tree/master/remarkable-cups) - Script to print directly to reMarkable Cloud from CUPS using rMAPI.
  ![Last Commit](https://img.shields.io/github/last-commit/ofosos/scratch) ![License](https://img.shields.io/github/license/ofosos/scratch) ![Stars](https://img.shields.io/github/stars/ofosos/scratch) ![Forks](https://img.shields.io/github/forks/ofosos/scratch)

- [mendeley-rMsync](https://github.com/anilkyelam/mendeley-rMsync) - Script to sync PDFs (with annotations) from/to a [Mendeley](https://www.mendeley.com/) folder.
  ![Last Commit](https://img.shields.io/github/last-commit/anilkyelam/mendeley-rMsync) ![License](https://img.shields.io/github/license/anilkyelam/mendeley-rMsync) ![Stars](https://img.shields.io/github/stars/anilkyelam/mendeley-rMsync) ![Forks](https://img.shields.io/github/forks/anilkyelam/mendeley-rMsync)

- [Moss](https://github.com/RedTTGMoss/moss-desktop) - An app for working with your documents in the reMarkable/rmFakeCloud cloud
  ![Last Commit](https://img.shields.io/github/last-commit/RedTTGMoss/moss-desktop) ![License](https://img.shields.io/github/license/RedTTGMoss/moss-desktop) ![Stars](https://img.shields.io/github/stars/RedTTGMoss/moss-desktop) ![Forks](https://img.shields.io/github/forks/RedTTGMoss/moss-desktop)

- [pdf2remarkable](https://github.com/teticio/pdf2remarkable) - Script to upload PDFs to the reMarkable Cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/teticio/pdf2remarkable) ![License](https://img.shields.io/github/license/teticio/pdf2remarkable) ![Stars](https://img.shields.io/github/stars/teticio/pdf2remarkable) ![Forks](https://img.shields.io/github/forks/teticio/pdf2remarkable)

- (Unmaintained) [reCatchable](https://github.com/lapwat/reCatchable) - Turn websites into ebooks, upload them to reMarkable.
  ![Last Commit](https://img.shields.io/github/last-commit/lapwat/reCatchable) ![License](https://img.shields.io/github/license/lapwat/reCatchable) ![Stars](https://img.shields.io/github/stars/lapwat/reCatchable) ![Forks](https://img.shields.io/github/forks/lapwat/reCatchable)

- [reGitable](https://github.com/after-eight/regitable) - Backup your reMarkable with git and sync changes to a remote repository automatically.
  ![Last Commit](https://img.shields.io/github/last-commit/after-eight/regitable) ![License](https://img.shields.io/github/license/after-eight/regitable) ![Stars](https://img.shields.io/github/stars/after-eight/regitable) ![Forks](https://img.shields.io/github/forks/after-eight/regitable)

- [Remarcal](https://remarcal.com/) - Sync Google, Outlook, Apple, and more calendars to reMarkable.
- [reMarkable Morning News_2](https://github.com/ktibr0/Remarkable_morning_news_2) - Automatically sends daily news to your reMarkable tablet. Standalone web application with persistent storage.
  ![Last Commit](https://img.shields.io/github/last-commit/ktibr0/Remarkable_morning_news_2) ![License](https://img.shields.io/github/license/ktibr0/Remarkable_morning_news_2) ![Stars](https://img.shields.io/github/stars/ktibr0/Remarkable_morning_news_2) ![Forks](https://img.shields.io/github/forks/ktibr0/Remarkable_morning_news_2)

- [reMarkable RSS](https://github.com/eksubin/Remarkable-RSS-Feed) - Read RSS feeds on reMarkable via google drive integration. Automated Script to convert RSS-feeds as PDFs and upload to google drive.
  ![Last Commit](https://img.shields.io/github/last-commit/eksubin/Remarkable-RSS-Feed) ![License](https://img.shields.io/github/license/eksubin/Remarkable-RSS-Feed) ![Stars](https://img.shields.io/github/stars/eksubin/Remarkable-RSS-Feed) ![Forks](https://img.shields.io/github/forks/eksubin/Remarkable-RSS-Feed)

- [remarkable-mcp](https://github.com/SamMorrowDrums/remarkable-mcp) - Model Context Protocol server enabling AI assistants to read and browse your reMarkable documents via SSH (no subscription required) or Cloud API. [Blog post](https://sam-morrow.com/blog/building-an-mcp-server-for-remarkable).
  ![Last Commit](https://img.shields.io/github/last-commit/SamMorrowDrums/remarkable-mcp) ![License](https://img.shields.io/github/license/SamMorrowDrums/remarkable-mcp) ![Stars](https://img.shields.io/github/stars/SamMorrowDrums/remarkable-mcp) ![Forks](https://img.shields.io/github/forks/SamMorrowDrums/remarkable-mcp)

- [remarkable_simplenote](https://github.com/bgribble/remarkable_simplenote) - Sync simplenote notes to reMarkable (currently one-way)
  ![Last Commit](https://img.shields.io/github/last-commit/bgribble/remarkable_simplenote) ![License](https://img.shields.io/github/license/bgribble/remarkable_simplenote) ![Stars](https://img.shields.io/github/stars/bgribble/remarkable_simplenote) ![Forks](https://img.shields.io/github/forks/bgribble/remarkable_simplenote)

- [reMarkable-Sink](http://github.com/hmenzagh/reMarkable-Sink) - Turn a folder into a wormhole to your reMarkable.
  ![Last Commit](https://img.shields.io/github/last-commit/hmenzagh/reMarkable-Sink) ![License](https://img.shields.io/github/license/hmenzagh/reMarkable-Sink) ![Stars](https://img.shields.io/github/stars/hmenzagh/reMarkable-Sink) ![Forks](https://img.shields.io/github/forks/hmenzagh/reMarkable-Sink)

- [remarkable-substack](https://github.com/jwoglom/remarkable-substack/) - Syncs unread Substack posts to the reMarkable Cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/jwoglom/remarkable-substack) ![License](https://img.shields.io/github/license/jwoglom/remarkable-substack) ![Stars](https://img.shields.io/github/stars/jwoglom/remarkable-substack) ![Forks](https://img.shields.io/github/forks/jwoglom/remarkable-substack)

- [reMarkable_syncthing](http://github.com/evidlo/remarkable_syncthing) - Syncthing on reMarkable.
  ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_syncthing) ![License](https://img.shields.io/github/license/evidlo/remarkable_syncthing) ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_syncthing) ![Forks](https://img.shields.io/github/forks/evidlo/remarkable_syncthing)

- [reMarkable Todoist and Calendar Sync](https://github.com/usuallycwdillon/remarkable-calendar) Puts Todoist tasks and Google calendar events on a calendar then pushes to reMarkable.
  ![Last Commit](https://img.shields.io/github/last-commit/usuallycwdillon/remarkable-calendar) ![License](https://img.shields.io/github/license/usuallycwdillon/remarkable-calendar) ![Stars](https://img.shields.io/github/stars/usuallycwdillon/remarkable-calendar) ![Forks](https://img.shields.io/github/forks/usuallycwdillon/remarkable-calendar)

- [remarkable-zapier](https://github.com/artes-dev/remarkable-zapier) - Zapier Integration for reMarkable Cloud
  ![Last Commit](https://img.shields.io/github/last-commit/artes-dev/remarkable-zapier) ![License](https://img.shields.io/github/license/artes-dev/remarkable-zapier) ![Stars](https://img.shields.io/github/stars/artes-dev/remarkable-zapier) ![Forks](https://img.shields.io/github/forks/artes-dev/remarkable-zapier)

- [remarking](https://github.com/sabidib/remarking) - CLI tool to extract highlights from any document in the reMarkable cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/sabidib/remarking) ![License](https://img.shields.io/github/license/sabidib/remarking) ![Stars](https://img.shields.io/github/stars/sabidib/remarking) ![Forks](https://img.shields.io/github/forks/sabidib/remarking)

- [rm-brain](https://github.com/gabrielanhaia/remarkable-brain) - Turns your reMarkable notebooks into a local-first, searchable second brain you query through Claude Desktop.
  ![Last Commit](https://img.shields.io/github/last-commit/gabrielanhaia/remarkable-brain) ![License](https://img.shields.io/github/license/gabrielanhaia/remarkable-brain) ![Stars](https://img.shields.io/github/stars/gabrielanhaia/remarkable-brain) ![Forks](https://img.shields.io/github/forks/gabrielanhaia/remarkable-brain)

- [rm-pdf-tools](https://github.com/skius/rm-pdf-tools) - Service that allows users to insert and delete pages from annotated PDFs on the device.
  ![Last Commit](https://img.shields.io/github/last-commit/skius/rm-pdf-tools) ![License](https://img.shields.io/github/license/skius/rm-pdf-tools) ![Stars](https://img.shields.io/github/stars/skius/rm-pdf-tools) ![Forks](https://img.shields.io/github/forks/skius/rm-pdf-tools)

- [rM-sync](https://github.com/simonschllng/rm-sync) - Sync script for reMarkable paper tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/simonschllng/rm-sync) ![License](https://img.shields.io/github/license/simonschllng/rm-sync) ![Stars](https://img.shields.io/github/stars/simonschllng/rm-sync) ![Forks](https://img.shields.io/github/forks/simonschllng/rm-sync)

- [RMfuse](https://github.com/rschroll/rmfuse) - FUSE filesystem for the reMarkable Cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/rschroll/rmfuse) ![License](https://img.shields.io/github/license/rschroll/rmfuse) ![Stars](https://img.shields.io/github/stars/rschroll/rmfuse) ![Forks](https://img.shields.io/github/forks/rschroll/rmfuse)

- [rss2remarkable](https://codeberg.org/akselmo/rss2remarkable) - Generates PDF of given RSS feeds and send is to your reMarkable cloud.
  ![Last Commit](https://img.shields.io/gitea/last-commit/akselmo/rss2remarkable?gitea_url=https://codeberg.org) ![Stars](https://img.shields.io/gitea/stars/akselmo/rss2remarkable?gitea_url=https://codeberg.org) ![Forks](https://img.shields.io/gitea/forks/akselmo/rss2remarkable?gitea_url=https://codeberg.org)

- [send-to-remarkable](https://github.com/zegevlier/send-to-remarkable) - Upload documents to the reMarkable from an email, like send to Kindle.
  ![Last Commit](https://img.shields.io/github/last-commit/zegevlier/send-to-remarkable) ![License](https://img.shields.io/github/license/zegevlier/send-to-remarkable) ![Stars](https://img.shields.io/github/stars/zegevlier/send-to-remarkable) ![Forks](https://img.shields.io/github/forks/zegevlier/send-to-remarkable)

- [sync_zotero_remarkable](https://github.com/danijoo/sync_zotero_remarkable) - Sync PDFs from Zotero to reMarkable.
  ![Last Commit](https://img.shields.io/github/last-commit/danijoo/sync_zotero_remarkable) ![License](https://img.shields.io/github/license/danijoo/sync_zotero_remarkable) ![Stars](https://img.shields.io/github/stars/danijoo/sync_zotero_remarkable) ![Forks](https://img.shields.io/github/forks/danijoo/sync_zotero_remarkable)

- [Syncthing-for-reMarkable-AppLoad](https://github.com/paviro/Syncthing-for-reMarkable) - Syncthing appload app for reMarkable (incl. Paper Pro and Paper Pro Move).
  ![Last Commit](https://img.shields.io/github/last-commit/paviro/Syncthing-for-reMarkable) ![License](https://img.shields.io/github/license/paviro/Syncthing-for-reMarkable) ![Stars](https://img.shields.io/github/stars/paviro/Syncthing-for-reMarkable) ![Forks](https://img.shields.io/github/forks/paviro/Syncthing-for-reMarkable)

- [url2epub](https://github.com/fishy/url2epub) - Telegram bot to generate ePub out of URL and send directly to reMarkable Cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/fishy/url2epub) ![License](https://img.shields.io/github/license/fishy/url2epub) ![Stars](https://img.shields.io/github/stars/fishy/url2epub) ![Forks](https://img.shields.io/github/forks/fishy/url2epub)

- [zotero-reMarkable](https://github.com/michaelmior/zotero-remarkable) - Script to sync PDFs from the [Zotero](https://www.zotero.org/) reference manager.
  ![Last Commit](https://img.shields.io/github/last-commit/michaelmior/zotero-remarkable) ![License](https://img.shields.io/github/license/michaelmior/zotero-remarkable) ![Stars](https://img.shields.io/github/stars/michaelmior/zotero-remarkable) ![Forks](https://img.shields.io/github/forks/michaelmior/zotero-remarkable)

- (Unmaintained) [Zotero2reMarkable Bridge](https://github.com/opal06/zotero2remarkable_bridge) - Sync files from Zotero to reMarkable and back based on tags; supports v2.7< highlights.
  ![Last Commit](https://img.shields.io/github/last-commit/opal06/zotero2remarkable_bridge) ![License](https://img.shields.io/github/license/opal06/zotero2remarkable_bridge) ![Stars](https://img.shields.io/github/stars/opal06/zotero2remarkable_bridge) ![Forks](https://img.shields.io/github/forks/opal06/zotero2remarkable_bridge)


## Custom Templates

- [blank_slate_pdf](https://github.com/sowcow/blank_slate_pdf) - Flexible PDFs for nested lists or experiments with no predefined template, separate simple calendar, customization using ruby code.
  ![Last Commit](https://img.shields.io/github/last-commit/sowcow/blank_slate_pdf) ![License](https://img.shields.io/github/license/sowcow/blank_slate_pdf) ![Stars](https://img.shields.io/github/stars/sowcow/blank_slate_pdf) ![Forks](https://img.shields.io/github/forks/sowcow/blank_slate_pdf)

- [latex-yearly-planner](https://github.com/kudrykv/latex-yearly-planner) - PDF planner designed for e-ink devices.
  ![Last Commit](https://img.shields.io/github/last-commit/kudrykv/latex-yearly-planner) ![License](https://img.shields.io/github/license/kudrykv/latex-yearly-planner) ![Stars](https://img.shields.io/github/stars/kudrykv/latex-yearly-planner) ![Forks](https://img.shields.io/github/forks/kudrykv/latex-yearly-planner)

- (Unmaintained) [ReCalendar](https://github.com/klimeryk/recalendar) - Highly customizable calendar generator in PHP optimized for reMarkable.
  ![Last Commit](https://img.shields.io/github/last-commit/klimeryk/recalendar) ![License](https://img.shields.io/github/license/klimeryk/recalendar) ![Stars](https://img.shields.io/github/stars/klimeryk/recalendar) ![Forks](https://img.shields.io/github/forks/klimeryk/recalendar)

- [reMarkable-bujo](https://github.com/vonneudeck/remarkable-bujo) - "Bullet Journal" templates.
  ![Last Commit](https://img.shields.io/github/last-commit/vonneudeck/remarkable-bujo) ![License](https://img.shields.io/github/license/vonneudeck/remarkable-bujo) ![Stars](https://img.shields.io/github/stars/vonneudeck/remarkable-bujo) ![Forks](https://img.shields.io/github/forks/vonneudeck/remarkable-bujo)

- [remarkable-engineering](https://gitlab.com/asciipip/remarkable-engineering) - Engineering-style grid templates.
  ![Last Commit](https://img.shields.io/gitlab/last-commit/asciipip/remarkable-engineering) ![License](https://img.shields.io/gitlab/license/asciipip/remarkable-engineering) ![Stars](https://img.shields.io/gitlab/stars/asciipip/remarkable-engineering) ![Forks](https://img.shields.io/gitlab/forks/asciipip/remarkable-engineering)

- [reMarkable-gtd-templates](https://github.com/BartKeulen/remarkable-gtd-templates) - "Getting Things Done" templates.
  ![Last Commit](https://img.shields.io/github/last-commit/BartKeulen/remarkable-gtd-templates) ![License](https://img.shields.io/github/license/BartKeulen/remarkable-gtd-templates) ![Stars](https://img.shields.io/github/stars/BartKeulen/remarkable-gtd-templates) ![Forks](https://img.shields.io/github/forks/BartKeulen/remarkable-gtd-templates)

- [reMarkable_templates](https://github.com/steka/reMarkable_templates) - White lines/squares on gray background.
  ![Last Commit](https://img.shields.io/github/last-commit/steka/reMarkable_templates) ![License](https://img.shields.io/github/license/steka/reMarkable_templates) ![Stars](https://img.shields.io/github/stars/steka/reMarkable_templates) ![Forks](https://img.shields.io/github/forks/steka/reMarkable_templates)

- [reMarkabletemplates](https://github.com/equivocates/remarkabletemplates/) - Planner per 1 or 3 weeks.
  ![Last Commit](https://img.shields.io/github/last-commit/equivocates/remarkabletemplates) ![License](https://img.shields.io/github/license/equivocates/remarkabletemplates) ![Stars](https://img.shields.io/github/stars/equivocates/remarkabletemplates) ![Forks](https://img.shields.io/github/forks/equivocates/remarkabletemplates)

- [rM2Mods templates](https://github.com/DanielRunningen/rM2Mods/tree/main/assests/templates) - Collection of different templates. E.g., micro dots/grids, checklists, budgeting,  boxes.
  ![Last Commit](https://img.shields.io/github/last-commit/DanielRunningen/rM2Mods) ![License](https://img.shields.io/github/license/DanielRunningen/rM2Mods) ![Stars](https://img.shields.io/github/stars/DanielRunningen/rM2Mods) ![Forks](https://img.shields.io/github/forks/DanielRunningen/rM2Mods)

- [reMarkable planning/journaling templates](https://github.com/msencer/remarkable_templates) - Collection of daily/weekly planning, journaling templates
  ![Last Commit](https://img.shields.io/github/last-commit/msencer/remarkable_templates) ![License](https://img.shields.io/github/license/msencer/remarkable_templates) ![Stars](https://img.shields.io/github/stars/msencer/remarkable_templates) ![Forks](https://img.shields.io/github/forks/msencer/remarkable_templates)

- [re-Planner](https://github.com/PepikVaio/reMarkable_re-Planner) - Watermarked PDF calendar for reMarkable 1 and 2. You can pay to remove the watermark, and to receive a customized version.
  ![Last Commit](https://img.shields.io/github/last-commit/PepikVaio/reMarkable_re-Planner) ![License](https://img.shields.io/github/license/PepikVaio/reMarkable_re-Planner) ![Stars](https://img.shields.io/github/stars/PepikVaio/reMarkable_re-Planner) ![Forks](https://img.shields.io/github/forks/PepikVaio/reMarkable_re-Planner)

- [Mobile UX Sketching Templates](https://github.com/Martes-Delta-Co/Remarkable-Mobile-Prototyping-Templates) - Mobile phone templates with 12 column layouts, grids, and multiple combinations of 1/2/4-up layouts with space for note-taking, in iPhone and Android flavors, in Methods format, so you can swap templates on each page of a notebook
  ![Last Commit](https://img.shields.io/github/last-commit/Martes-Delta-Co/Remarkable-Mobile-Prototyping-Templates) ![License](https://img.shields.io/github/license/Martes-Delta-Co/Remarkable-Mobile-Prototyping-Templates) ![Stars](https://img.shields.io/github/stars/Martes-Delta-Co/Remarkable-Mobile-Prototyping-Templates) ![Forks](https://img.shields.io/github/forks/Martes-Delta-Co/Remarkable-Mobile-Prototyping-Templates)


### Template Builders

- [Daily Journal / Wardley Maps / Figma template](https://www.figma.com/community/file/1389237140795352688) - A daily planner/journal, Wardley Map, and forkable general starter kit for building custom templates with Figma.
- [ReCalendar.me](https://recalendar.me/) - Highly customizable online calendar generator optimized for reMarkable.
- [Remarkable Grid Template Generator](https://xosh.org/remarkable-grid-template/) - Generate pixel perfect line grid and dotted grid templates
- [Remarkably Planner Builder](https://remarkably-organized.pages.dev/) - Generate hyperlinked pdf planners
- [reMarkable Template Builder](https://templarian.github.io/remarkable/) - Generate Isometric and Grid templates of all sizes

## Device Tools

- [paginator](https://github.com/aflusche/paginator) - Physical foot pedal to turn pages on the device with no hands (e.g. for playing sheet music).
  ![Last Commit](https://img.shields.io/github/last-commit/aflusche/paginator) ![License](https://img.shields.io/github/license/aflusche/paginator) ![Stars](https://img.shields.io/github/stars/aflusche/paginator) ![Forks](https://img.shields.io/github/forks/aflusche/paginator)

- (Unmaintained)[remarvin](https://github.com/plan5/remarvin) - Profile and file encryption manager that allows to manage notebooks for different users and to optionally protect the files with a password through gocryptfs-based encryption (device only).
- [reExecute](https://github.com/Slenderman00/reExecute) - Persistent code execution bootstrap for reMarkable Paper Pro Move using the MDM agent config.
  ![Last Commit](https://img.shields.io/github/last-commit/Slenderman00/reExecute) ![License](https://img.shields.io/github/license/Slenderman00/reExecute) ![Stars](https://img.shields.io/github/stars/Slenderman00/reExecute) ![Forks](https://img.shields.io/github/forks/Slenderman00/reExecute)

- [rm-version-switcher](https://github.com/rmitchellscott/rm-version-switcher) - An interactive CLI application for switching between installed reMarkable OS versions.
  ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/rm-version-switcher) ![License](https://img.shields.io/github/license/rmitchellscott/rm-version-switcher) ![Stars](https://img.shields.io/github/stars/rmitchellscott/rm-version-switcher) ![Forks](https://img.shields.io/github/forks/rmitchellscott/rm-version-switcher)

- [rmtemplate](https://github.com/zer0trip/rmtemplate) - CLI to upload and manage custom templates on reMarkable Paper Pro and Paper Pro Move devices over SSH.
  ![Last Commit](https://img.shields.io/github/last-commit/zer0trip/rmtemplate) ![License](https://img.shields.io/github/license/zer0trip/rmtemplate) ![Stars](https://img.shields.io/github/stars/zer0trip/rmtemplate) ![Forks](https://img.shields.io/github/forks/zer0trip/rmtemplate)

- [rmtree](https://github.com/rmitchellscott/rmtree) - Unix-style tree command for the reMarkable's document filesystem.
  ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/rmtree) ![License](https://img.shields.io/github/license/rmitchellscott/rmtree) ![Stars](https://img.shields.io/github/stars/rmitchellscott/rmtree) ![Forks](https://img.shields.io/github/forks/rmitchellscott/rmtree)

- [splash.dat converter](https://gist.github.com/iTrooz/fddfcce03c1c44b04231be73d6e7982a) - Simple script to convert an image to the rM2 .dat format for a splash screen.

## GUI Clients

- [asTounding](https://github.com/jlarriba/astounding) -  A multiplatform GUI application for the reMarkable cloud, including Linux.
  ![Last Commit](https://img.shields.io/github/last-commit/jlarriba/astounding) ![License](https://img.shields.io/github/license/jlarriba/astounding) ![Stars](https://img.shields.io/github/stars/jlarriba/astounding) ![Forks](https://img.shields.io/github/forks/jlarriba/astounding)

- [reManager](https://github.com/rmitchellscott/reManager) - Linux, MacOS, and Windows desktop app for managing mods on reMarkable tablets using the [Vellum](https://github.com/vellum-dev/vellum) package manager.
  ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/reManager) ![License](https://img.shields.io/github/license/rmitchellscott/reManager) ![Stars](https://img.shields.io/github/stars/rmitchellscott/reManager) ![Forks](https://img.shields.io/github/forks/rmitchellscott/reManager)

- [RemaPy](https://github.com/peerdavid/remapy) - GUI to browse, download/upload files and backup the tablet (also on Linux) using the cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/peerdavid/remapy) ![License](https://img.shields.io/github/license/peerdavid/remapy) ![Stars](https://img.shields.io/github/stars/peerdavid/remapy) ![Forks](https://img.shields.io/github/forks/peerdavid/remapy)

- [reMarkable Connection Utility (RCU)](http://www.davisr.me/projects/rcu/) - Cross-platform local/offline client for managing backups, screenshots, notebooks, templates, wallpaper, firmware, and third-party software. Typed text and snap highlight extraction. Virtual printer for native print-to-tablet.
- [reMarkable Remember](https://github.com/ds160/remarkable-remember) - A cross-platform client for offline management of backups, notebooks, templates and hand writing recognition via MyScript.
  ![Last Commit](https://img.shields.io/github/last-commit/ds160/remarkable-remember) ![License](https://img.shields.io/github/license/ds160/remarkable-remember) ![Stars](https://img.shields.io/github/stars/ds160/remarkable-remember) ![Forks](https://img.shields.io/github/forks/ds160/remarkable-remember)

- [reMarkable-assistant](https://github.com/richeymichael/remarkable-assistant) - Manage templates, splash screens, and settings on your reMarkable tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/richeymichael/remarkable-assistant) ![License](https://img.shields.io/github/license/richeymichael/remarkable-assistant) ![Stars](https://img.shields.io/github/stars/richeymichael/remarkable-assistant) ![Forks](https://img.shields.io/github/forks/richeymichael/remarkable-assistant)

- [reMarkable-hyutilities](https://github.com/moovida/remarkable-hyutilities) - A GUI written in java to backup your device, upload templates and modify splash screens.
  ![Last Commit](https://img.shields.io/github/last-commit/moovida/remarkable-hyutilities) ![License](https://img.shields.io/github/license/moovida/remarkable-hyutilities) ![Stars](https://img.shields.io/github/stars/moovida/remarkable-hyutilities) ![Forks](https://img.shields.io/github/forks/moovida/remarkable-hyutilities)

- [ReMy](https://github.com/bordaigorl/remy) - A GUI to browse, preview documents, export documents with custom settings, all via SSH (no cloud needed); works from local raw backups too.
  ![Last Commit](https://img.shields.io/github/last-commit/bordaigorl/remy) ![License](https://img.shields.io/github/license/bordaigorl/remy) ![Stars](https://img.shields.io/github/stars/bordaigorl/remy) ![Forks](https://img.shields.io/github/forks/bordaigorl/remy)

- [RMHook](https://github.com/NohamR/RMHook) - A dynamic library injection tool for the reMarkable Desktop macOS application, enabling connection to self-hosted rmfakecloud servers.
  ![Last Commit](https://img.shields.io/github/last-commit/NohamR/RMHook) ![License](https://img.shields.io/github/license/NohamR/RMHook) ![Stars](https://img.shields.io/github/stars/NohamR/RMHook) ![Forks](https://img.shields.io/github/forks/NohamR/RMHook)

- [RMHook-iOS](https://github.com/NohamR/RMHook-iOS/) - A hooking tool for the reMarkable iOS application, enabling connection to self-hosted rmfakecloud servers.
  ![Last Commit](https://img.shields.io/github/last-commit/NohamR/RMHook-iOS) ![License](https://img.shields.io/github/license/NohamR/RMHook-iOS) ![Stars](https://img.shields.io/github/stars/NohamR/RMHook-iOS) ![Forks](https://img.shields.io/github/forks/NohamR/RMHook-iOS)

- [RMHook-Win](https://github.com/NohamR/RMHook-Win) - A hooking tool for the reMarkable Desktop Windows application, enabling connection to self-hosted rmfakecloud servers.
  ![Last Commit](https://img.shields.io/github/last-commit/NohamR/RMHook-Win) ![License](https://img.shields.io/github/license/NohamR/RMHook-Win) ![Stars](https://img.shields.io/github/stars/NohamR/RMHook-Win) ![Forks](https://img.shields.io/github/forks/NohamR/RMHook-Win)

- [rm-exporter](https://github.com/chopikus/rm-exporter) - Exports any combination of folders and large notes locally, supports Windows/MacOS/Linux.
  ![Last Commit](https://img.shields.io/github/last-commit/chopikus/rm-exporter) ![License](https://img.shields.io/github/license/chopikus/rm-exporter) ![Stars](https://img.shields.io/github/stars/chopikus/rm-exporter) ![Forks](https://img.shields.io/github/forks/chopikus/rm-exporter)

- [rM2 Template Helper](https://www.freeremarkabletools.com/) Windows tool for template management, and to download community templates. 
- [rMExplorer](https://github.com/bruot/pyrmexplorer/wiki) - GUI to browse, download/upload files and backup the tablet without using the cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/bruot/pyrmexplorer) ![License](https://img.shields.io/github/license/bruot/pyrmexplorer) ![Stars](https://img.shields.io/github/stars/bruot/pyrmexplorer) ![Forks](https://img.shields.io/github/forks/bruot/pyrmexplorer)

- [rmUploader](https://github.com/lobre/rmuploader) - Simple web app to upload epub or pdf files to the reMarkable tablet via drag and drop.
  ![Last Commit](https://img.shields.io/github/last-commit/lobre/rmuploader) ![License](https://img.shields.io/github/license/lobre/rmuploader) ![Stars](https://img.shields.io/github/stars/lobre/rmuploader) ![Forks](https://img.shields.io/github/forks/lobre/rmuploader)

- (Unmaintained) [Slithin](https://github.com/furesoft/Slithin) - Free Management Application for Windows/Linux/MacOS.
  ![Last Commit](https://img.shields.io/github/last-commit/furesoft/Slithin) ![License](https://img.shields.io/github/license/furesoft/Slithin) ![Stars](https://img.shields.io/github/stars/furesoft/Slithin) ![Forks](https://img.shields.io/github/forks/furesoft/Slithin)


## Interface Customization

- [AppLoad](https://github.com/asivery/rm-appload) - Enables windowed and fullscreen apps inside the reMarkable interface.
  ![Last Commit](https://img.shields.io/github/last-commit/asivery/rm-appload) ![License](https://img.shields.io/github/license/asivery/rm-appload) ![Stars](https://img.shields.io/github/stars/asivery/rm-appload) ![Forks](https://img.shields.io/github/forks/asivery/rm-appload)

- [Book-safe](https://github.com/dvdsk/Book-safe) - Hide books/documents between a given time period.
  ![Last Commit](https://img.shields.io/github/last-commit/dvdsk/Book-safe) ![License](https://img.shields.io/github/license/dvdsk/Book-safe) ![Stars](https://img.shields.io/github/stars/dvdsk/Book-safe) ![Forks](https://img.shields.io/github/forks/dvdsk/Book-safe)

- [Crazy Cow](https://github.com/machinelevel/sp425-crazy-cow) - Typewriter input from USB keyboard directly into reMarkable interface.
  ![Last Commit](https://img.shields.io/github/last-commit/machinelevel/sp425-crazy-cow) ![License](https://img.shields.io/github/license/machinelevel/sp425-crazy-cow) ![Stars](https://img.shields.io/github/stars/machinelevel/sp425-crazy-cow) ![Forks](https://img.shields.io/github/forks/machinelevel/sp425-crazy-cow)

- [ReCept](https://github.com/funkey/recept/) - Fix for the rM2 jagged line issue.
  ![Last Commit](https://img.shields.io/github/last-commit/funkey/recept) ![License](https://img.shields.io/github/license/funkey/recept) ![Stars](https://img.shields.io/github/stars/funkey/recept) ![Forks](https://img.shields.io/github/forks/funkey/recept)

- [reLuminate](https://github.com/unreMarkableLabs/reLuminate) - Enable enhanced screen brightness levels on the reMarkable Paper Pro.
  ![Last Commit](https://img.shields.io/github/last-commit/unreMarkableLabs/reLuminate) ![License](https://img.shields.io/github/license/unreMarkableLabs/reLuminate) ![Stars](https://img.shields.io/github/stars/unreMarkableLabs/reLuminate) ![Forks](https://img.shields.io/github/forks/unreMarkableLabs/reLuminate)

- [RemarkableLamyEraser](https://github.com/isaacwisdom/RemarkableLamyEraser/) - Supports Lamy Al Star stylus button to erase or undo for reMarkable tablets.
  ![Last Commit](https://img.shields.io/github/last-commit/isaacwisdom/RemarkableLamyEraser) ![License](https://img.shields.io/github/license/isaacwisdom/RemarkableLamyEraser) ![Stars](https://img.shields.io/github/stars/isaacwisdom/RemarkableLamyEraser) ![Forks](https://img.shields.io/github/forks/isaacwisdom/RemarkableLamyEraser)

- [remarkable-shortcuts](https://github.com/martinetd/remarkable-shortcuts) - Add extra 'gestures' (currently double taps) for easier navigation.
  ![Last Commit](https://img.shields.io/github/last-commit/martinetd/remarkable-shortcuts) ![License](https://img.shields.io/github/license/martinetd/remarkable-shortcuts) ![Stars](https://img.shields.io/github/stars/martinetd/remarkable-shortcuts) ![Forks](https://img.shields.io/github/forks/martinetd/remarkable-shortcuts)

- [rM Hacks](https://github.com/mb1986/rm-hacks) - Small improvements and tweaks for rM devices.
  ![Last Commit](https://img.shields.io/github/last-commit/mb1986/rm-hacks) ![License](https://img.shields.io/github/license/mb1986/rm-hacks) ![Stars](https://img.shields.io/github/stars/mb1986/rm-hacks) ![Forks](https://img.shields.io/github/forks/mb1986/rm-hacks)

- [rM Hacks (QLMDiff)](https://github.com/asivery/rm-hacks-qmd) - Port of rmhacks for xovi.
  ![Last Commit](https://img.shields.io/github/last-commit/asivery/rm-hacks-qmd) ![License](https://img.shields.io/github/license/asivery/rm-hacks-qmd) ![Stars](https://img.shields.io/github/stars/asivery/rm-hacks-qmd) ![Forks](https://img.shields.io/github/forks/asivery/rm-hacks-qmd)

- [rm-hacks-xovi-qmd (Samarkin)](https://github.com/Samarkin/rm-hacks-xovi-qmd)
  ![Last Commit](https://img.shields.io/github/last-commit/Samarkin/rm-hacks-xovi-qmd) ![License](https://img.shields.io/github/license/Samarkin/rm-hacks-xovi-qmd) ![Stars](https://img.shields.io/github/stars/Samarkin/rm-hacks-xovi-qmd) ![Forks](https://img.shields.io/github/forks/Samarkin/rm-hacks-xovi-qmd)

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
  ![Last Commit](https://img.shields.io/github/last-commit/Barabazs/rM-signature-patch) ![License](https://img.shields.io/github/license/Barabazs/rM-signature-patch) ![Stars](https://img.shields.io/github/stars/Barabazs/rM-signature-patch) ![Forks](https://img.shields.io/github/forks/Barabazs/rM-signature-patch)

- [rm-xovi-extensions](https://github.com/asivery/rm-xovi-extensions) - extensions for the reMarkable tablets, which utilize the xovi framework
  ![Last Commit](https://img.shields.io/github/last-commit/asivery/rm-xovi-extensions) ![License](https://img.shields.io/github/license/asivery/rm-xovi-extensions) ![Stars](https://img.shields.io/github/stars/asivery/rm-xovi-extensions) ![Forks](https://img.shields.io/github/forks/asivery/rm-xovi-extensions)

  - `framebuffer-spy` - Exposes the address of the system framebuffer.
  - `qt-command-executor` - Injects a Qt module to execute shell commands from QML.
  - `qt-resource-rebuilder` - Injects into Qt and rebuilds resource databases on the fly, allowing QML/image replacement or addition.
  - `random-suspend-screen` - Randomize your reMarkable tablet's suspend screens.
  - `webserver-remote` - Exposes the USB webserver to all interfaces, with a confirmation dialog for inbound connections.
- [Signature-rM](https://github.com/rM-self-serve/signature-rM) - Remove the signature from the bottom of emails sent from the device.
  ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/signature-rM) ![License](https://img.shields.io/github/license/rM-self-serve/signature-rM) ![Stars](https://img.shields.io/github/stars/rM-self-serve/signature-rM) ![Forks](https://img.shields.io/github/forks/rM-self-serve/signature-rM)

- [WebInterface-OnBoot](https://github.com/rM-self-serve/webinterface-onboot) - Enable the web interface on boot.
  ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/webinterface-onboot) ![License](https://img.shields.io/github/license/rM-self-serve/webinterface-onboot) ![Stars](https://img.shields.io/github/stars/rM-self-serve/webinterface-onboot) ![Forks](https://img.shields.io/github/forks/rM-self-serve/webinterface-onboot)

- [webinterface-rmpp](https://github.com/t3rminalV/webinterface-rmpp) - Enable web interface on boot and over wifi on the reMarkable Paper Pro. Includes authentication and SSL.
  ![Last Commit](https://img.shields.io/github/last-commit/t3rminalV/webinterface-rmpp) ![License](https://img.shields.io/github/license/t3rminalV/webinterface-rmpp) ![Stars](https://img.shields.io/github/stars/t3rminalV/webinterface-rmpp) ![Forks](https://img.shields.io/github/forks/t3rminalV/webinterface-rmpp)

- [WebInterface-Upload-Button](https://github.com/rM-self-serve/webinterface-upload-button) - Upload button for the web interface, alternative to drag and drop.
  ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/webinterface-upload-button) ![License](https://img.shields.io/github/license/rM-self-serve/webinterface-upload-button) ![Stars](https://img.shields.io/github/stars/rM-self-serve/webinterface-upload-button) ![Forks](https://img.shields.io/github/forks/rM-self-serve/webinterface-upload-button)

- [WebInterface-Wifi](https://github.com/rM-self-serve/webinterface-wifi) - View the web interface if running, over wifi.
  ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/webinterface-wifi) ![License](https://img.shields.io/github/license/rM-self-serve/webinterface-wifi) ![Stars](https://img.shields.io/github/stars/rM-self-serve/webinterface-wifi) ![Forks](https://img.shields.io/github/forks/rM-self-serve/webinterface-wifi)

- [xovi-extensions (FouzR)](https://github.com/FouzR/xovi-extensions)
  ![Last Commit](https://img.shields.io/github/last-commit/FouzR/xovi-extensions) ![License](https://img.shields.io/github/license/FouzR/xovi-extensions) ![Stars](https://img.shields.io/github/stars/FouzR/xovi-extensions) ![Forks](https://img.shields.io/github/forks/FouzR/xovi-extensions)

  - `favTagButton` - Adds quick access buttons for Favourites and Tagged files.
  - `floating` - Adds a floating toolbar.
  - `gestures` - Adds several useful gestures.
  - `recentsTagged` - New menu showing tagged files, sorted by last modified.
  - `selectionErase` - Enables deleting a stroke via selection tool.
  - `selectionStuff` - Adds "select everything above the line."
- [xovi-qmd-extensions (ingatellent)](https://github.com/ingatellent/xovi-qmd-extensions)
  ![Last Commit](https://img.shields.io/github/last-commit/ingatellent/xovi-qmd-extensions) ![License](https://img.shields.io/github/license/ingatellent/xovi-qmd-extensions) ![Stars](https://img.shields.io/github/stars/ingatellent/xovi-qmd-extensions) ![Forks](https://img.shields.io/github/forks/ingatellent/xovi-qmd-extensions)

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
  ![Last Commit](https://img.shields.io/github/last-commit/NohamR/xovi-qmd-extensions) ![License](https://img.shields.io/github/license/NohamR/xovi-qmd-extensions) ![Stars](https://img.shields.io/github/stars/NohamR/xovi-qmd-extensions) ![Forks](https://img.shields.io/github/forks/NohamR/xovi-qmd-extensions)

  - `clock` - Adds a live clock to the library sidebar; tap the entry to toggle seconds display.
  - `convertToText_remover` - Removes the Convert to text option from selection menus and the toolbar.
  - `favoriteButton` - Restores a Favorite action in the document list header for faster pinning.
  - `forceSync` - Adds a cloud button in Quick Settings that forces a library sync when tapped.
  - `hideDocumentClose` - Hides the close button in the document toolbar to prevent accidental exits.
  - `quickSettingsClock` - Injects a tappable clock into the Quick Settings header; tap to toggle between minute and second.
  - `tagButton` - Puts a Tag action next to other list controls to open the tag editor directly.
  - `uncompressDock` - Replaces the condensed More menu in the new document dock with dedicated buttons for notebook, folder, and quick sheet creation.
- [xovi-qmd-extensions (rmitchellscott)](https://github.com/rmitchellscott/xovi-qmd-extensions)
  ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/xovi-qmd-extensions) ![License](https://img.shields.io/github/license/rmitchellscott/xovi-qmd-extensions) ![Stars](https://img.shields.io/github/stars/rmitchellscott/xovi-qmd-extensions) ![Forks](https://img.shields.io/github/forks/rmitchellscott/xovi-qmd-extensions)

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
  ![Last Commit](https://img.shields.io/github/last-commit/StarNumber12046/xovi-qmd-extensions) ![License](https://img.shields.io/github/license/StarNumber12046/xovi-qmd-extensions) ![Stars](https://img.shields.io/github/stars/StarNumber12046/xovi-qmd-extensions) ![Forks](https://img.shields.io/github/forks/StarNumber12046/xovi-qmd-extensions)

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
  ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/xovi-tripletap) ![License](https://img.shields.io/github/license/rmitchellscott/xovi-tripletap) ![Stars](https://img.shields.io/github/stars/rmitchellscott/xovi-tripletap) ![Forks](https://img.shields.io/github/forks/rmitchellscott/xovi-tripletap)


## Other

- (Unmaintained) [Calibre-Remarkable-Device-Driver-Plugin](https://github.com/naclander/Calibre-Remarkable-Device-Driver-Plugin) - A Calibre Plugin to Manage your Remarkable Books.
  ![Last Commit](https://img.shields.io/github/last-commit/naclander/Calibre-Remarkable-Device-Driver-Plugin) ![License](https://img.shields.io/github/license/naclander/Calibre-Remarkable-Device-Driver-Plugin) ![Stars](https://img.shields.io/github/stars/naclander/Calibre-Remarkable-Device-Driver-Plugin) ![Forks](https://img.shields.io/github/forks/naclander/Calibre-Remarkable-Device-Driver-Plugin)

- (Unmaintained) [reHackable/scripts](https://github.com/reHackable/scripts) - A set of bash scripts that may enhance your reMarkable experience.
  ![Last Commit](https://img.shields.io/github/last-commit/reHackable/scripts) ![License](https://img.shields.io/github/license/reHackable/scripts) ![Stars](https://img.shields.io/github/stars/reHackable/scripts) ![Forks](https://img.shields.io/github/forks/reHackable/scripts)

- (Unmaintained) [reMarkable-tweak](https://github.com/morngrar/remarkable-tweak) - Tweak tool for the reMarkable paper tablet. Lets you organize your templates with no fuss.
  ![Last Commit](https://img.shields.io/github/last-commit/morngrar/remarkable-tweak) ![License](https://img.shields.io/github/license/morngrar/remarkable-tweak) ![Stars](https://img.shields.io/github/stars/morngrar/remarkable-tweak) ![Forks](https://img.shields.io/github/forks/morngrar/remarkable-tweak)

- [chiappa](https://github.com/gitman-101111/chiappa) - e-Ink bridge/miscellaneous scripts and tools to port other OS's to a reMarkable Pro Paper Move.
  ![Last Commit](https://img.shields.io/github/last-commit/gitman-101111/chiappa) ![License](https://img.shields.io/github/license/gitman-101111/chiappa) ![Stars](https://img.shields.io/github/stars/gitman-101111/chiappa) ![Forks](https://img.shields.io/github/forks/gitman-101111/chiappa)

- [Drawj2d](https://drawj2d.sourceforge.io/) - Create technical line drawings on an editable reMarkable notebook page. ([Guidance how to upload](https://sourceforge.net/p/drawj2d/wiki/reMarkable/) the page to the device using rMAPI.)
- [Ephemeris](https://github.com/rmitchellscott/ephemeris) - A Python-based tool that generates clean, daily schedules using ICS calendar data. Designed with e-ink tablets like reMarkable in mind.
  ![Last Commit](https://img.shields.io/github/last-commit/rmitchellscott/ephemeris) ![License](https://img.shields.io/github/license/rmitchellscott/ephemeris) ![Stars](https://img.shields.io/github/stars/rmitchellscott/ephemeris) ![Forks](https://img.shields.io/github/forks/rmitchellscott/ephemeris)

- [Epistolary](https://github.com/j6k4m8/epistolary) - Emails on the reMarkable. Read and respond to your email inbox in handwriting (auto-converts to text before sending).
  ![Last Commit](https://img.shields.io/github/last-commit/j6k4m8/epistolary) ![License](https://img.shields.io/github/license/j6k4m8/epistolary) ![Stars](https://img.shields.io/github/stars/j6k4m8/epistolary) ![Forks](https://img.shields.io/github/forks/j6k4m8/epistolary)

- [ePUB to reMarkable PDF](https://github.com/suntorytimed/epub_to_remarkable) - Self hostable web service for turning an EPUB into a reMarkable optimised PDF.
  ![Last Commit](https://img.shields.io/github/last-commit/suntorytimed/epub_to_remarkable) ![License](https://img.shields.io/github/license/suntorytimed/epub_to_remarkable) ![Stars](https://img.shields.io/github/stars/suntorytimed/epub_to_remarkable) ![Forks](https://img.shields.io/github/forks/suntorytimed/epub_to_remarkable)

- [Funcky reMarkable Exporter](https://github.com/simonbaudart/Funcky.Remarkable.Exporter) - Export notes from a reMarkable Tablet to File System and External Services.
  ![Last Commit](https://img.shields.io/github/last-commit/simonbaudart/Funcky.Remarkable.Exporter) ![License](https://img.shields.io/github/license/simonbaudart/Funcky.Remarkable.Exporter) ![Stars](https://img.shields.io/github/stars/simonbaudart/Funcky.Remarkable.Exporter) ![Forks](https://img.shields.io/github/forks/simonbaudart/Funcky.Remarkable.Exporter)

- [Goosepaper](https://github.com/j6k4m8/goosepaper): Deliver prettily-formatted RSS feeds, news articles, Wikipedia articles-of-the-day, and more to your reMarkable tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/j6k4m8/goosepaper) ![License](https://img.shields.io/github/license/j6k4m8/goosepaper) ![Stars](https://img.shields.io/github/stars/j6k4m8/goosepaper) ![Forks](https://img.shields.io/github/forks/j6k4m8/goosepaper)

- [instapaper-as-pdf-to-reMarkable](https://github.com/fabianmu/instapaper-as-pdf-to-remarkable) - Export Instapaper-Articles to PDF and send them to a connected rM tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/fabianmu/instapaper-as-pdf-to-remarkable) ![License](https://img.shields.io/github/license/fabianmu/instapaper-as-pdf-to-remarkable) ![Stars](https://img.shields.io/github/stars/fabianmu/instapaper-as-pdf-to-remarkable) ![Forks](https://img.shields.io/github/forks/fabianmu/instapaper-as-pdf-to-remarkable)

- [landscape-pdf](https://github.com/nmoran/landscape-pdf) - Utility to convert pdf documents to read in landscape mode. Useful for papers and text books.
  ![Last Commit](https://img.shields.io/github/last-commit/nmoran/landscape-pdf) ![License](https://img.shields.io/github/license/nmoran/landscape-pdf) ![Stars](https://img.shields.io/github/stars/nmoran/landscape-pdf) ![Forks](https://img.shields.io/github/forks/nmoran/landscape-pdf)

- [mail2rm](https://github.com/glatzor/mail2rm) - Mail PDF documents to your reMarkable cloud using your mail transport agent e.g. postfix.
  ![Last Commit](https://img.shields.io/github/last-commit/glatzor/mail2rm) ![License](https://img.shields.io/github/license/glatzor/mail2rm) ![Stars](https://img.shields.io/github/stars/glatzor/mail2rm) ![Forks](https://img.shields.io/github/forks/glatzor/mail2rm)

- [microSD](http://www.davisr.me/projects/remarkable-microsd/) - Tutorial for adding a microSD card reader to the reMarkable 1.
- [morningpaper2reMarkable](https://github.com/jessfraz/morningpaper2remarkable) - A bot to sync the morning paper to a reMarkable tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/jessfraz/morningpaper2remarkable) ![License](https://img.shields.io/github/license/jessfraz/morningpaper2remarkable) ![Stars](https://img.shields.io/github/stars/jessfraz/morningpaper2remarkable) ![Forks](https://img.shields.io/github/forks/jessfraz/morningpaper2remarkable)

- [neofetch](https://github.com/rM-self-serve/neofetch-rM) - A command-line system information tool written in bash 3.2+.
  ![Last Commit](https://img.shields.io/github/last-commit/rM-self-serve/neofetch-rM) ![License](https://img.shields.io/github/license/rM-self-serve/neofetch-rM) ![Stars](https://img.shields.io/github/stars/rM-self-serve/neofetch-rM) ![Forks](https://img.shields.io/github/forks/rM-self-serve/neofetch-rM)

- [nix-remarkable](https://github.com/siraben/nix-remarkable) - Nix expressions for the reMarkable tablet leveraging the company's toolchain.
  ![Last Commit](https://img.shields.io/github/last-commit/siraben/nix-remarkable) ![License](https://img.shields.io/github/license/siraben/nix-remarkable) ![Stars](https://img.shields.io/github/stars/siraben/nix-remarkable) ![Forks](https://img.shields.io/github/forks/siraben/nix-remarkable)

- [paper2reMarkable](https://github.com/GjjvdBurg/paper2remarkable) - Download an academic paper or HTML article, crop it, and send it to the reMarkable with a single command.
  ![Last Commit](https://img.shields.io/github/last-commit/GjjvdBurg/paper2remarkable) ![License](https://img.shields.io/github/license/GjjvdBurg/paper2remarkable) ![Stars](https://img.shields.io/github/stars/GjjvdBurg/paper2remarkable) ![Forks](https://img.shields.io/github/forks/GjjvdBurg/paper2remarkable)

- [Parabola-rM](http://www.davisr.me/projects/parabola-rm/) - A Desktop GNU/Linux-libre replacement OS with fast partial refreshing and USB OTG.
- [pdf2rmnotebook](https://github.com/JCN-9000/pdf2rmnotebook) - Creates a reMarkable Notebook from multiple PDF files.
  ![Last Commit](https://img.shields.io/github/last-commit/JCN-9000/pdf2rmnotebook) ![License](https://img.shields.io/github/license/JCN-9000/pdf2rmnotebook) ![Stars](https://img.shields.io/github/stars/JCN-9000/pdf2rmnotebook) ![Forks](https://img.shields.io/github/forks/JCN-9000/pdf2rmnotebook)

- [pocket2rm](https://github.com/glidergeek/pocket2rm) - Synchronize articles from read-later platform pocket in PDF and epub.
  ![Last Commit](https://img.shields.io/github/last-commit/glidergeek/pocket2rm) ![License](https://img.shields.io/github/license/glidergeek/pocket2rm) ![Stars](https://img.shields.io/github/stars/glidergeek/pocket2rm) ![Forks](https://img.shields.io/github/forks/glidergeek/pocket2rm)

- [reCalibre-Driver](https://github.com/zer0trip/reCalibre) - A Calibre plugin for syncing books to a reMarkable, via KOReader or the native UI.
  ![Last Commit](https://img.shields.io/github/last-commit/zer0trip/reCalibre) ![License](https://img.shields.io/github/license/zer0trip/reCalibre) ![Stars](https://img.shields.io/github/stars/zer0trip/reCalibre) ![Forks](https://img.shields.io/github/forks/zer0trip/reCalibre)

- [reHackable/maxio](https://github.com/reHackable/maxio) - Companion daemon for the reMarkable paper tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/reHackable/maxio) ![License](https://img.shields.io/github/license/reHackable/maxio) ![Stars](https://img.shields.io/github/stars/reHackable/maxio) ![Forks](https://img.shields.io/github/forks/reHackable/maxio)

- [remailable](https://github.com/j6k4m8/remailable) - Email PDFs directly to your reMarkable. ([Free publicly-hosted version available](https://remailable.getneutrality.org/)).
  ![Last Commit](https://img.shields.io/github/last-commit/j6k4m8/remailable) ![License](https://img.shields.io/github/license/j6k4m8/remailable) ![Stars](https://img.shields.io/github/stars/j6k4m8/remailable) ![Forks](https://img.shields.io/github/forks/j6k4m8/remailable)

- [reMarkable CLI tooling](https://github.com/cherti/remarkable-cli-tooling) - CLI-tooling to sync documents to a reMarkable, to clean deleted files etc. without needing cloud access
  ![Last Commit](https://img.shields.io/github/last-commit/cherti/remarkable-cli-tooling) ![License](https://img.shields.io/github/license/cherti/remarkable-cli-tooling) ![Stars](https://img.shields.io/github/stars/cherti/remarkable-cli-tooling) ![Forks](https://img.shields.io/github/forks/cherti/remarkable-cli-tooling)

- [remarkable-api](https://github.com/Penguin-Guru/remarkable-api) - A simple bash script to interact with reMarkable devices' USB Web Interface.
  ![Last Commit](https://img.shields.io/github/last-commit/Penguin-Guru/remarkable-api) ![License](https://img.shields.io/github/license/Penguin-Guru/remarkable-api) ![Stars](https://img.shields.io/github/stars/Penguin-Guru/remarkable-api) ![Forks](https://img.shields.io/github/forks/Penguin-Guru/remarkable-api)

- [reMarkable-crosswords](https://github.com/shapeshed/remarkable-crosswords) - Get crosswords freshly delivered to your Remarkable every morning.
  ![Last Commit](https://img.shields.io/github/last-commit/shapeshed/remarkable-crosswords) ![License](https://img.shields.io/github/license/shapeshed/remarkable-crosswords) ![Stars](https://img.shields.io/github/stars/shapeshed/remarkable-crosswords) ![Forks](https://img.shields.io/github/forks/shapeshed/remarkable-crosswords)

- [reMarkable-fs](https://github.com/nick8325/remarkable-fs) - A FUSE filesystem wrapper for the reMarkable tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/nick8325/remarkable-fs) ![License](https://img.shields.io/github/license/nick8325/remarkable-fs) ![Stars](https://img.shields.io/github/stars/nick8325/remarkable-fs) ![Forks](https://img.shields.io/github/forks/nick8325/remarkable-fs)

- [remarkable-nixos](https://github.com/gitman-101111/remarkable-nixos) - Run NixOS on your reMarkable Pro Paper Move (others possible)
  ![Last Commit](https://img.shields.io/github/last-commit/gitman-101111/remarkable-nixos) ![License](https://img.shields.io/github/license/gitman-101111/remarkable-nixos) ![Stars](https://img.shields.io/github/stars/gitman-101111/remarkable-nixos) ![Forks](https://img.shields.io/github/forks/gitman-101111/remarkable-nixos)

- [reMarkable-random-screens](https://github.com/Neurone/reMarkable) - Change your poweroff and suspend screens every 5 minutes with random images of your choice
  ![Last Commit](https://img.shields.io/github/last-commit/Neurone/reMarkable) ![License](https://img.shields.io/github/license/Neurone/reMarkable) ![Stars](https://img.shields.io/github/stars/Neurone/reMarkable) ![Forks](https://img.shields.io/github/forks/Neurone/reMarkable)

- [reMarkable-tablet-driver](https://github.com/FreeCap23/reMarkable-tablet-driver) - Use your reMarkable as a drawing tablet in Linux with pressure sensitivity and tilt. Works in Wayland.
  ![Last Commit](https://img.shields.io/github/last-commit/FreeCap23/reMarkable-tablet-driver) ![License](https://img.shields.io/github/license/FreeCap23/reMarkable-tablet-driver) ![Stars](https://img.shields.io/github/stars/FreeCap23/reMarkable-tablet-driver) ![Forks](https://img.shields.io/github/forks/FreeCap23/reMarkable-tablet-driver)

- [reMarkable-touchgestures](https://github.com/ddvk/remarkable-touchgestures) - Touch gestures (swipe/touch) for easy page navigation.
  ![Last Commit](https://img.shields.io/github/last-commit/ddvk/remarkable-touchgestures) ![License](https://img.shields.io/github/license/ddvk/remarkable-touchgestures) ![Stars](https://img.shields.io/github/stars/ddvk/remarkable-touchgestures) ![Forks](https://img.shields.io/github/forks/ddvk/remarkable-touchgestures)

- [reMarkable_entware](http://github.com/evidlo/remarkable_entware) - Package manager for reMarkable.  Install common Unix utilities through the command line.
  ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_entware) ![License](https://img.shields.io/github/license/evidlo/remarkable_entware) ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_entware) ![Forks](https://img.shields.io/github/forks/evidlo/remarkable_entware)

- [reMarkable_keyboard](https://github.com/Evidlo/remarkable_keyboard) - Software to use rM as wireless keyboard/mouse.
  ![Last Commit](https://img.shields.io/github/last-commit/Evidlo/remarkable_keyboard) ![License](https://img.shields.io/github/license/Evidlo/remarkable_keyboard) ![Stars](https://img.shields.io/github/stars/Evidlo/remarkable_keyboard) ![Forks](https://img.shields.io/github/forks/Evidlo/remarkable_keyboard)

- [reMarkable_mouse](https://github.com/evidlo/remarkable_mouse) - Use your reMarkable as a graphics tablet.
  ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_mouse) ![License](https://img.shields.io/github/license/evidlo/remarkable_mouse) ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_mouse) ![Forks](https://img.shields.io/github/forks/evidlo/remarkable_mouse)

- [remarkable_news](https://github.com/evidlo/remarkable_news) - Use daily news/comics/images as the suspend screen.
  ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_news) ![License](https://img.shields.io/github/license/evidlo/remarkable_news) ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_news) ![Forks](https://img.shields.io/github/forks/evidlo/remarkable_news)

- [reMarkable_pdflets](https://github.com/evidlo/remarkable_pdflets) - Dynamically updating PDFs.
  ![Last Commit](https://img.shields.io/github/last-commit/evidlo/remarkable_pdflets) ![License](https://img.shields.io/github/license/evidlo/remarkable_pdflets) ![Stars](https://img.shields.io/github/stars/evidlo/remarkable_pdflets) ![Forks](https://img.shields.io/github/forks/evidlo/remarkable_pdflets)

- [remarkable_printer](https://github.com/Evidlo/remarkable_printer) - Print from any device to reMarkable without browser extensions or reMarkable cloud.
  ![Last Commit](https://img.shields.io/github/last-commit/Evidlo/remarkable_printer) ![License](https://img.shields.io/github/license/Evidlo/remarkable_printer) ![Stars](https://img.shields.io/github/stars/Evidlo/remarkable_printer) ![Forks](https://img.shields.io/github/forks/Evidlo/remarkable_printer)

- [reMarkablePocket](https://github.com/nov1n/RemarkablePocket) - Synchronize articles from read-later platform Pocket in epub format.
  ![Last Commit](https://img.shields.io/github/last-commit/nov1n/RemarkablePocket) ![License](https://img.shields.io/github/license/nov1n/RemarkablePocket) ![Stars](https://img.shields.io/github/stars/nov1n/RemarkablePocket) ![Forks](https://img.shields.io/github/forks/nov1n/RemarkablePocket)

- [remarkable-ssh](https://github.com/Penguin-Guru/remarkable-ssh) - A bash script to manage files on reMarkable devices via CLI and SSH.
  ![Last Commit](https://img.shields.io/github/last-commit/Penguin-Guru/remarkable-ssh) ![License](https://img.shields.io/github/license/Penguin-Guru/remarkable-ssh) ![Stars](https://img.shields.io/github/stars/Penguin-Guru/remarkable-ssh) ![Forks](https://img.shields.io/github/forks/Penguin-Guru/remarkable-ssh)

- [reMarkableSync](https://github.com/jamesf91/reMarkableSync) - A Microsoft OneNote addin for importing notebooks from reMarkable as text or images.
  ![Last Commit](https://img.shields.io/github/last-commit/jamesf91/reMarkableSync) ![License](https://img.shields.io/github/license/jamesf91/reMarkableSync) ![Stars](https://img.shields.io/github/stars/jamesf91/reMarkableSync) ![Forks](https://img.shields.io/github/forks/jamesf91/reMarkableSync)

- [remarks](https://github.com/Scrybbling-together/remarks) - Extract highlights, scribbles, and annotations from PDFs. Export to Markdown, PNG, and SVG.
  ![Last Commit](https://img.shields.io/github/last-commit/Scrybbling-together/remarks) ![License](https://img.shields.io/github/license/Scrybbling-together/remarks) ![Stars](https://img.shields.io/github/stars/Scrybbling-together/remarks) ![Forks](https://img.shields.io/github/forks/Scrybbling-together/remarks)

- [reMouseable](https://github.com/kevinconway/remouseable) - Use your reMarkable tablet as a mouse.
  ![Last Commit](https://img.shields.io/github/last-commit/kevinconway/remouseable) ![License](https://img.shields.io/github/license/kevinconway/remouseable) ![Stars](https://img.shields.io/github/stars/kevinconway/remouseable) ![Forks](https://img.shields.io/github/forks/kevinconway/remouseable)

- [remt](https://gitlab.com/wrobell/remt) - reMarkable tablet command-line tools.
  ![Last Commit](https://img.shields.io/gitlab/last-commit/wrobell/remt) ![License](https://img.shields.io/gitlab/license/wrobell/remt) ![Stars](https://img.shields.io/gitlab/stars/wrobell/remt) ![Forks](https://img.shields.io/gitlab/forks/wrobell/remt)

- [reSnap](https://github.com/cloudsftp/reSnap) - Take snapshots of your reMarkable screen over SSH.
  ![Last Commit](https://img.shields.io/github/last-commit/cloudsftp/reSnap) ![License](https://img.shields.io/github/license/cloudsftp/reSnap) ![Stars](https://img.shields.io/github/stars/cloudsftp/reSnap) ![Forks](https://img.shields.io/github/forks/cloudsftp/reSnap)

- [rM-dl-annotated](https://github.com/jmptable/rm-dl-annotated) - Export annotated PDFs from reMarkable tablets.
  ![Last Commit](https://img.shields.io/github/last-commit/jmptable/rm-dl-annotated) ![License](https://img.shields.io/github/license/jmptable/rm-dl-annotated) ![Stars](https://img.shields.io/github/stars/jmptable/rm-dl-annotated) ![Forks](https://img.shields.io/github/forks/jmptable/rm-dl-annotated)

- [rm-pySAS](https://github.com/tenJirka/rm-pySAS) - Python wrapper for [simple](https://rmkit.dev/apps/sas).
  ![Last Commit](https://img.shields.io/github/last-commit/tenJirka/rm-pySAS) ![License](https://img.shields.io/github/license/tenJirka/rm-pySAS) ![Stars](https://img.shields.io/github/stars/tenJirka/rm-pySAS) ![Forks](https://img.shields.io/github/forks/tenJirka/rm-pySAS)

- [rm2anki](https://github.com/stelzch/rm2anki) - Convert reMarkable notebooks into an Anki card decks.
  ![Last Commit](https://img.shields.io/github/last-commit/stelzch/rm2anki) ![License](https://img.shields.io/github/license/stelzch/rm2anki) ![Stars](https://img.shields.io/github/stars/stelzch/rm2anki) ![Forks](https://img.shields.io/github/forks/stelzch/rm2anki)

- [rmathlab](https://github.com/Samdney/rmathlab) - A Linux toolset for the reMarkable 2 tablet, which enables math handwriting recognition and LaTeX generation over USB via Mathpix.
  ![Last Commit](https://img.shields.io/github/last-commit/Samdney/rmathlab) ![License](https://img.shields.io/github/license/Samdney/rmathlab) ![Stars](https://img.shields.io/github/stars/Samdney/rmathlab) ![Forks](https://img.shields.io/github/forks/Samdney/rmathlab)

- [rmirro](https://github.com/hersle/rmirro) - A script that synchronizes PDFs of documents between a Remarkable and a computer folder that mirrors its file structure without cloud access.
  ![Last Commit](https://img.shields.io/github/last-commit/hersle/rmirro) ![License](https://img.shields.io/github/license/hersle/rmirro) ![Stars](https://img.shields.io/github/stars/hersle/rmirro) ![Forks](https://img.shields.io/github/forks/hersle/rmirro)

- [RMPP Entware](https://github.com/hmenzagh/rmpp-entware) - Package manager for reMarkable Paper Pro.  Install okpg package manager.
  ![Last Commit](https://img.shields.io/github/last-commit/hmenzagh/rmpp-entware) ![License](https://img.shields.io/github/license/hmenzagh/rmpp-entware) ![Stars](https://img.shields.io/github/stars/hmenzagh/rmpp-entware) ![Forks](https://img.shields.io/github/forks/hmenzagh/rmpp-entware)

- [rMsync](https://github.com/lschwetlick/rMsync) - Synchronisation script with a local dedicated "library" folder.
  ![Last Commit](https://img.shields.io/github/last-commit/lschwetlick/rMsync) ![License](https://img.shields.io/github/license/lschwetlick/rMsync) ![Stars](https://img.shields.io/github/stars/lschwetlick/rMsync) ![Forks](https://img.shields.io/github/forks/lschwetlick/rMsync)

- [rmTabletDriver](https://github.com/LinusCDE/rmTabletDriver) - Application that allows you to simulate/clone rM input on your computer.
  ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/rmTabletDriver) ![License](https://img.shields.io/github/license/LinusCDE/rmTabletDriver) ![Stars](https://img.shields.io/github/stars/LinusCDE/rmTabletDriver) ![Forks](https://img.shields.io/github/forks/LinusCDE/rmTabletDriver)

- [rmWacomToMouse](https://github.com/LinusCDE/rmWacomToMouse) - Use the wacom pen as a mouse to draw on your pc.
  ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/rmWacomToMouse) ![License](https://img.shields.io/github/license/LinusCDE/rmWacomToMouse) ![Stars](https://img.shields.io/github/stars/LinusCDE/rmWacomToMouse) ![Forks](https://img.shields.io/github/forks/LinusCDE/rmWacomToMouse)

- [rmWebUiTools](https://github.com/LinusCDE/rmWebUiTools) - View a file tree, see statistics and export/backup all files with some simple scripts utilizing the web ui.
  ![Last Commit](https://img.shields.io/github/last-commit/LinusCDE/rmWebUiTools) ![License](https://img.shields.io/github/license/LinusCDE/rmWebUiTools) ![Stars](https://img.shields.io/github/stars/LinusCDE/rmWebUiTools) ![Forks](https://img.shields.io/github/forks/LinusCDE/rmWebUiTools)

- [send_by_rmapi](https://github.com/LisaGlaser/send_by_rmapi) - A Calibre plugin to send books to your reMarkable, making use of rmapi.
  ![Last Commit](https://img.shields.io/github/last-commit/LisaGlaser/send_by_rmapi) ![License](https://img.shields.io/github/license/LisaGlaser/send_by_rmapi) ![Stars](https://img.shields.io/github/stars/LisaGlaser/send_by_rmapi) ![Forks](https://img.shields.io/github/forks/LisaGlaser/send_by_rmapi)


## Screen Sharing/Streaming

- [AppLoad-RMStream](https://github.com/asivery/appload-rmstream) - An AppLoad application for streaming your reMarkable tablet's screen over HTTP.
  ![Last Commit](https://img.shields.io/github/last-commit/asivery/appload-rmstream) ![License](https://img.shields.io/github/license/asivery/appload-rmstream) ![Stars](https://img.shields.io/github/stars/asivery/appload-rmstream) ![Forks](https://img.shields.io/github/forks/asivery/appload-rmstream)

- [goMarkableStream](https://github.com/owulveryck/goMarkableStream) - Stream the screen of the reMarkable 2 (FW 2.5) easily (client/server in Go with no installation) along with the colors (with FW > 2.11.x).
  ![Last Commit](https://img.shields.io/github/last-commit/owulveryck/goMarkableStream) ![License](https://img.shields.io/github/license/owulveryck/goMarkableStream) ![Stars](https://img.shields.io/github/stars/owulveryck/goMarkableStream) ![Forks](https://img.shields.io/github/forks/owulveryck/goMarkableStream)

- [pipes and paper](https://gitlab.com/afandian/pipes-and-paper) - Stream pen strokes to browser canvas via websockets ([blog post](https://blog.afandian.com/2020/10/pipes-and-paper-remarkable/)). Uses Python and SSH, nothing to compile or install on the reMarkable device.
  ![Last Commit](https://img.shields.io/gitlab/last-commit/afandian/pipes-and-paper) ![License](https://img.shields.io/gitlab/license/afandian/pipes-and-paper) ![Stars](https://img.shields.io/gitlab/stars/afandian/pipes-and-paper) ![Forks](https://img.shields.io/gitlab/forks/afandian/pipes-and-paper)

- [pipes and paper enhanced](https://github.com/Pyrrhu5/pipes-and-paper-enhanced/tree/stable) - Share the pen strokes to a browser without installling anything on the ReMarkable (a revived fork of the previous link with pen colors and eraser support, responsive interface).
  ![Last Commit](https://img.shields.io/github/last-commit/Pyrrhu5/pipes-and-paper-enhanced) ![License](https://img.shields.io/github/license/Pyrrhu5/pipes-and-paper-enhanced) ![Stars](https://img.shields.io/github/stars/Pyrrhu5/pipes-and-paper-enhanced) ![Forks](https://img.shields.io/github/forks/Pyrrhu5/pipes-and-paper-enhanced)

- (Unmaintained) [pipes and rust](https://github.com/AnyTimeTraveler/pipes-and-rust) - (Made for rM2) Stream pen strokes to browser. A single executable on the reMarkable that hosts a tiny webserver in the local WLAN.
  ![Last Commit](https://img.shields.io/github/last-commit/AnyTimeTraveler/pipes-and-rust) ![License](https://img.shields.io/github/license/AnyTimeTraveler/pipes-and-rust) ![Stars](https://img.shields.io/github/stars/AnyTimeTraveler/pipes-and-rust) ![Forks](https://img.shields.io/github/forks/AnyTimeTraveler/pipes-and-rust)

- [reStream](https://github.com/rien/reStream) - Stream your reMarkable screen over SSH.
  ![Last Commit](https://img.shields.io/github/last-commit/rien/reStream) ![License](https://img.shields.io/github/license/rien/reStream) ![Stars](https://img.shields.io/github/stars/rien/reStream) ![Forks](https://img.shields.io/github/forks/rien/reStream)

- [rMview](https://github.com/bordaigorl/rmview) - A fast GUI to stream your reMarkable screen over vanilla-SSH or VNC.
  ![Last Commit](https://img.shields.io/github/last-commit/bordaigorl/rmview) ![License](https://img.shields.io/github/license/bordaigorl/rmview) ![Stars](https://img.shields.io/github/stars/bordaigorl/rmview) ![Forks](https://img.shields.io/github/forks/bordaigorl/rmview)

- [rM-vnc-server](https://github.com/peter-sa/rM-vnc-server) - A fast & efficient damage-tracking (sending only updated regions) VNC server for streaming the reMarkable's screen.
  ![Last Commit](https://img.shields.io/github/last-commit/peter-sa/rM-vnc-server) ![License](https://img.shields.io/github/license/peter-sa/rM-vnc-server) ![Stars](https://img.shields.io/github/stars/peter-sa/rM-vnc-server) ![Forks](https://img.shields.io/github/forks/peter-sa/rM-vnc-server)

- [srvfb](https://github.com/merovius/srvfb) - Alternative screen-streaming software. Written in Go.
  ![Last Commit](https://img.shields.io/github/last-commit/merovius/srvfb) ![License](https://img.shields.io/github/license/merovius/srvfb) ![Stars](https://img.shields.io/github/stars/merovius/srvfb) ![Forks](https://img.shields.io/github/forks/merovius/srvfb)

- [VNSee](https://github.com/matteodelabre/vnsee) - VNC client for the reMarkable tablet allowing you to use the device as a second screen.
  ![Last Commit](https://img.shields.io/github/last-commit/matteodelabre/vnsee) ![License](https://img.shields.io/github/license/matteodelabre/vnsee) ![Stars](https://img.shields.io/github/stars/matteodelabre/vnsee) ![Forks](https://img.shields.io/github/forks/matteodelabre/vnsee)

