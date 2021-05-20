# Awesome reMarkable [![Discord](https://img.shields.io/discord/385916768696139794.svg?label=reMarkable&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/u3P9sDW)


# [<img src="Awesome.png"></p>](https://github.com/sindresorhus/awesome)

The [reMarkable](https://www.remarkable.com) is a paper tablet for those who prefer writing on paper, rather than keyboards. Its remarkably fast paper-white display, Linux based operating system and awesome community make it highly attractive amongst hackers and developers.

*Contributions are welcome as long as they follow the [guidelines](CONTRIBUTING.md).*

## Disclaimer

No project here is affiliated or endorsed by [reMarkable AS](https://github.com/remarkable). If you modify your device official support might refuse to help you. 

### Factory reset may brick your device

This function may not do what you are expecting. While it resets all user data, it will not restore the device to the original factory condition. It will reset your SSH password and remove all SSH keys, which may make it impossible to connect to your device if it is malfunctioning.

### Take special care if you are using a reMarkable 2.

- System recovery requires some hardware. Check [ddvk/remarkable2-recovery](https://github.com/ddvk/remarkable2-recovery) for what to do in case you lose ssh access.
- The screen on rm2 and rm1 are different. Workarounds have been developed to interact with the rM2 framebuffer but some projects might not work on it. See [remarkable2-framebuffer repo](https://github.com/ddvk/remarkable2-framebuffer) and [#14](https://github.com/ddvk/remarkable2-framebuffer/issues/14).


## Contents

- [APIs](#apis)
- - [Cloud API](#cloud-api)
- - [Lines Format](#lines-format)
- - [Other APIs](#other-apis)
- [Applications](#applications)
- - [Games](#games)
- - [Launchers](#launchers)
- [Cloud Tools](#cloud-tools)
- [Device Tools](#device-tools)
- [GUI Clients](#gui-clients)
- [Other](#other)
- [Screen Sharing/Streaming](#screen-sharingstreaming)
- [Custom Templates](#custom-templates)

## APIs

### Cloud API

- [google-drive-remarkable-sync](https://github.com/bsdz/google-drive-remarkable-sync) - Apps Script API for reMarkable Cloud. Includes Synchronizer capability to automate mirroring of documents from Google Drive to reMarkable Cloud.
- [jrmapi](https://github.com/jlarriba/jrmapi) - A Java API for the reMarkable Cloud.
- [reMarkableAPI](https://github.com/splitbrain/ReMarkableAPI) - Docs and implementation of the reMarkable file sync API.
- [reMarkable-typescript](https://github.com/Ogdentrod/reMarkable-typescript) - TypeScript API for reMarkable Cloud.
- [Remarkable.jl](https://github.com/theogf/Remarkable.jl) - Julia API Interface to the reMarkable cloud.
- [remarkdav](https://github.com/hansegucker/remarkdav) - A tool to sync PDF files from a WebDAV directory to the reMarkable Cloud.
- [rMAPI](https://github.com/juruen/rmapi) - ReMarkable Cloud Go API.
- [rmapy](https://github.com/subutux/rmapy) - ReMarkable Cloud Python API.
- [rmcl](https://github.com/rschroll/rmcl)- Asynchronous Python library for the reMarkable Cloud.
- [rmfakecloud](https://github.com/ddvk/rmfakecloud) - Fake Cloud Sync, server implementation of the Cloud API.

### Lines Format

- [lines-are-beautiful](https://github.com/ax3l/lines-are-beautiful) - C++ File API for the reMarkable tablet.
- [lines-are-rusty](https://github.com/ax3l/lines-are-rusty) - Rust File API for the reMarkable tablet.
- [reMarkable-layers](https://github.com/bsdz/remarkable-layers) - Python API for reading & writing reMarkable Lines format. Supports very basic conversion of PDFs and SVGs to Lines format.
- [rmrl](https://github.com/rschroll/rmrl) - The reMarkable Rendering Library for Python converts annotated documents to PDF files.

### Other APIs

- [libreMarkable](https://github.com/canselcik/libremarkable) - A framework for developing applications with native refresh support for reMarkable Tablet.

## Applications

- [harmony](https://rmkit.dev/apps/harmony) - a low latency sketching app with procedural brushes.
- [KOReader](https://github.com/koreader/koreader) - An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats.
- [darvin/plato](https://github.com/darvin/plato) [LinusCDE/plato](https://github.com/LinusCDE/plato) - Plato reader port. Supports pdfs, epubs, many other formats.
- [Rebook](https://github.com/fsniper/ReBook) - The missing book store for reMarkable.
- [reMarkable keywriter](https://github.com/dps/remarkable-keywriter) - A distraction free keyboard notes app.
- [reMarkable wikipedia](https://github.com/dps/remarkable-wikipedia) - Offline wikipedia reader for reMarkable.
- [whiteboard-hypercard](https://github.com/fenollp/reMarkable-tools) - Live collaboration, drawing, chat, whiteboarding.

### Games

- [chessMarkable](https://github.com/LinusCDE/chessmarkable) - Play chess against a bot or a friend.
- [minesweeper](https://rmkit.dev/apps/minesweeper) - A mine detection game.
- [recrossable](https://github.com/sandsmark/recrossable) - Crossword game with simplistic handwriting recognition and automatic generation of crosswords.
- [retris](https://github.com/LinusCDE/retris) - Play a clone of the popular block stacking game with either buttons or swipe guestures.

### Launchers

- [draft-reMarkable](https://github.com/dixonary/draft-reMarkable) - A launcher for the reMarkable tablet, which wraps around the standard interface.
- [oxide](https://github.com/Eeems/oxide/releases) - A launcher application for the reMarkable tablet.
- [remux](https://rmkit.dev/apps/remux) - A multi-tasking launcher for the reMarkable tablet.


## Cloud Tools

- [CUPS Printing](https://ofosos.org/2018/10/22/printing-to-remarkable-cloud-from-cups/) - Script to print directly to reMarkable Cloud from CUPS using rMAPI.
- [reCatchable](https://github.com/lapwat/reCatchable) - Turn websites into ebooks, upload them to reMarkable.
- [reGitable](https://github.com/after-eight/regitable) - Backup your reMarkable with git and sync changes to a remote repository automatically.
- [remarkable_simplenote](https://github.com/bgribble/remarkable_simplenote) - Sync simplenote notes to reMarkable (currently one-way)
- [reMarkable-Sink](http://github.com/hmenzagh/reMarkable-Sink) - Turn a folder into a wormhole to your reMarkable.
- [reMarkable_syncthing](http://github.com/evidlo/remarkable_syncthing) - Syncthing on reMarkable.
- [remarkable-zapier](https://github.com/artes-dev/remarkable-zapier) - Zapier Integration for reMarkable Cloud
- [rM-sync](https://github.com/simonschllng/rm-sync) - Sync script for reMarkable paper tablet.
- [RMfuse](https://github.com/rschroll/rmfuse) - FUSE filesystem for the reMarkable Cloud.
- [sync_zotero_remarkable](https://github.com/danijoo/sync_zotero_remarkable) - Sync PDFs from Zotero to reMarkable.
- [zotero-reMarkable](https://github.com/michaelmior/zotero-remarkable) - Script to sync PDFs from the [Zotero](https://www.zotero.org/) reference manager.

## Device Tools
- [ReCept](https://github.com/funkey/recept/) - Fix for the rM2 jagged line issue.
- [rM-signature-patch](https://github.com/Barabazs/rM-signature-patch) - Simple script to remove that pesky advert at the bottom of a mail originating from a reMarkable.

## GUI Clients

- [asTounding](https://github.com/jlarriba/astounding) -  A multiplatform GUI application for the reMarkable cloud, including Linux.
- [RemaDroid](https://play.google.com/store/apps/details?id=org.remadroid) - An alternative Android app to upload documents, webpages or images to the reMarkable tablet.
- [RemaPy](https://github.com/peerdavid/remapy) - GUI to browse, download/upload files and backup the tablet (also on Linux) using the cloud.
- [reMarkable-assistant](https://github.com/richeymichael/remarkable-assistant) - Manage templates, splash screens, and settings on your reMarkable tablet.
- [reMarkable Connection Utility (RCU)](http://www.davisr.me/projects/rcu/) - A cross-platform client for offline management of backups, screenshots, notebooks, templates, wallpaper, and third-party software.
- [reMarkable-hyutilities](https://github.com/moovida/remarkable-hyutilities) - A GUI written in java to backup your device, upload templates and modify splash screens.
- [ReMy](https://github.com/bordaigorl/remy) - A GUI to browse, preview documents, export documents with custom settings, all via SSH (no cloud needed); works from local raw backups too.
- [rMExplorer](https://github.com/bruot/pyrmexplorer/wiki) - GUI to browse, download/upload files and backup the tablet without using the cloud.
- [rmUploader](https://github.com/lobre/rmuploader) - Simple web app to upload epub or pdf files to the reMarkable tablet via drag and drop.

## Other

- [Crazy Cow](https://github.com/machinelevel/sp425-crazy-cow) - Typewriter input from USB keyboard directly into reMarkable interface.
- [Drawj2d](https://drawj2d.sourceforge.io/) - Create technical line drawings on an editable reMarkable notebook page. ([Guidance how to upload](https://sourceforge.net/p/drawj2d/wiki/reMarkable/) the page to the device using rMAPI.)
- [Funcky reMarkable Exporter](https://github.com/simonbaudart/Funcky.Remarkable.Exporter) - Export notes from a reMarkable Tablet to File System and External Services.
- [Goosepaper](https://github.com/j6k4m8/goosepaper): Deliver prettily-formatted RSS feeds, news articles, Wikipedia articles-of-the-day, and more to your reMarkable tablet.
- [instapaper-as-pdf-to-reMarkable](https://github.com/fabianmu/instapaper-as-pdf-to-remarkable) - Export Instapaper-Articles to PDF and send them to a connected rM tablet.
- [landscape-pdf](https://github.com/nmoran/landscape-pdf) - Utility to convert pdf documents to read in landscape mode. Useful for papers and text books.
- [morningpaper2reMarkable](https://github.com/jessfraz/morningpaper2remarkable) - A bot to sync the morning paper to a reMarkable tablet.
- [nix-remarkable](https://github.com/siraben/nix-remarkable) - Nix expressions for the reMarkable tablet leveraging the company's toolchain.
- [paper2reMarkable](https://github.com/GjjvdBurg/paper2remarkable) - Download an academic paper or HTML article, crop it, and send it to the reMarkable with a single command.
- [mail2rm](https://github.com/glatzor/mail2rm) - Mail PDF documents to your reMarkable cloud using your mail transport agent e.g. postfix.
- [Parabola-rM](http://www.davisr.me/projects/parabola-rm/) - A Desktop GNU/Linux-libre replacement OS with fast partial refreshing and USB OTG.
- [pocket2rm](https://github.com/glidergeek/pocket2rm) - Synchronize articles from read-later platform pocket in PDF and epub.
- [remailable](https://github.com/j6k4m8/remailable) - Email PDFs directly to your reMarkable. ([Free publicly-hosted version available](https://remailable.getneutrality.org/)).
- [reHackable/maxio](https://github.com/reHackable/maxio) - Companion daemon for the reMarkable paper tablet.
- [reHackable/scripts](https://github.com/reHackable/scripts) - A set of bash scripts that may enhance your reMarkable experience.
- [reMarkable_entware](http://github.com/evidlo/remarkable_entware) - Package manager for reMarkable.  Install common Unix utilities through the command line.
- [reMarkable_keyboard](https://github.com/Evidlo/remarkable_keyboard) - Software to use rM as wireless keyboard/mouse.
- [reMarkable_mouse](https://github.com/evidlo/remarkable_mouse) - Use your reMarkable as a graphics tablet.
- [remarkable_news](https://github.com/evidlo/remarkable_news) - Use daily news/comics/images as the suspend screen.
- [reMarkable_pdflets](https://github.com/evidlo/remarkable_pdflets) - Dynamically updating PDFs.
- [remarkable_printer](https://github.com/Evidlo/remarkable_printer) - Print from any device to reMarkable without browser extensions or reMarkable cloud.
- [reMarkable-fs](https://github.com/nick8325/remarkable-fs) - A FUSE filesystem wrapper for the reMarkable tablet.
- [reMarkable-random-screens](https://github.com/Neurone/reMarkable) - Change your poweroff and suspend screens every 5 minutes with random images of your choice
- [reMarkable-touchgestures](https://github.com/ddvk/remarkable-touchgestures) - Touch gestures (swipe/touch) for easy page navigation.
- [reMarkable-tweak](https://github.com/morngrar/remarkable-tweak) - Tweak tool for the reMarkable paper tablet. Lets you organize your templates with no fuss.
- [remarks](https://github.com/lucasrla/remarks) - Extract highlights, scribbles, and annotations from PDFs. Export to Markdown, PNG, and SVG.
- [reMouseable](https://github.com/kevinconway/remouseable) - Use your reMarkable tablet as a mouse.
- [remt](https://gitlab.com/wrobell/remt) - reMarkable tablet command-line tools.
- [reSnap](https://github.com/cloudsftp/reSnap) - Take snapshots of your reMarkable screen over SSH.
- [rM-dl-annotated](https://github.com/jmptable/rm-dl-annotated) - Export annotated PDFs from reMarkable tablets.
- [rMsync](https://github.com/lschwetlick/rMsync) - Synchronisation script with a local dedicated "library" folder.
- [rmTabletDriver](https://github.com/LinusCDE/rmTabletDriver) - Application that allows you to simulate/clone rM input on your computer.
- [rmWacomToMouse](https://github.com/LinusCDE/rmWacomToMouse) - Use the wacom pen as a mouse to draw on your pc.
- [rmWebUiTools](https://github.com/LinusCDE/rmWebUiTools) - View a file tree, see statistics and export/backup all files with some simple scripts utilizing the web ui.


## Screen Sharing/Streaming

- [pipes and paper](https://gitlab.com/afandian/pipes-and-paper) - Stream pen strokes to browser canvas via websockets ([blog post](https://blog.afandian.com/2020/10/pipes-and-paper-remarkable/)). Uses Python and SSH, nothing to compile or install on the reMarkable device.
- [pipes and rust](https://github.com/AnyTimeTraveler/pipes-and-rust) - (Made for rM2) Stream pen strokes to browser. A single executable on the reMarkable that hosts a tiny webserver in the local WLAN.
- [reStream](https://github.com/rien/reStream) - Stream your reMarkable screen over SSH.
- [rMview](https://github.com/bordaigorl/rmview) - A fast GUI to stream your reMarkable screen over vanilla-SSH or VNC.
- [rM-vnc-server](https://github.com/peter-sa/rM-vnc-server) - A fast & efficient damage-tracking (sending only updated regions) VNC server for streaming the reMarkable's screen.
- [srvfb](https://github.com/merovius/srvfb) - Alternative screen-streaming software. Written in Go.
- [VNSee](https://github.com/matteodelabre/vnsee) - VNC client for the reMarkable tablet allowing you to use the device as a second screen.
- [goMarkableStream](https://github.com/owulveryck/goMarkableStream) - Stream the screen of the reMarkable 2 (FW 2.5) easily (client/server in Go with no installation)

## Custom Templates
- [reMarkable-bujo](https://github.com/vonneudeck/remarkable-bujo) - "Bullet Journal" templates.
- [remarkable-engineering](https://gitlab.com/asciiphil/remarkable-engineering) - Engineering-style grid templates.
- [reMarkable-gtd-templates](https://github.com/BartKeulen/remarkable-gtd-templates) - "Getting Things Done" templates.
- [reMarkable Templates](https://rm.ezb.io/) - A website to host and view community-built templates.
- [reMarkable-Templates](https://github.com/newtonhonk/reMarkable-Templates) - To Do templates with lines, checkboxes or text blocks.
- [reMarkable_templates](https://github.com/steka/reMarkable_templates) - White lines/squares on gray background.
- [reMarkabletemplates](https://github.com/equivocates/remarkabletemplates/) - Planner per 1 or 3 weeks.
- [rM2Mods templates](https://github.com/DanielRunningen/rM2Mods/tree/main/assests/templates) - Collection of different templates. E.g., micro dots/grids, checklists, budgeting,  boxes.
