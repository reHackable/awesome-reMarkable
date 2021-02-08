# Awesome reMarkable [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)


# [<img src="Awesome.png"></p>](https://github.com/sindresorhus/awesome)

The [reMarkable](https://www.remarkable.com) is a paper tablet for those who prefer writing on paper, rather than keyboards. Its remarkably fast paper-white display, Linux based operating system and awesome community make it highly attractive amongst hackers and developers.

*Contributions are welcome as long as they follow the [guidelines](CONTRIBUTING.md).*

## reMarkable 2 disclaimer

Take special care if you are using a reMarkable 2:
- There is no tool for system recovery. If you lose ssh access you lose access to the device. Write down your password.
- The screen on rm2 and rm1 are different. ~~No application drawing into rm2 screen works yet.~~ Check [remarkable2-framebuffer repo](https://github.com/ddvk/remarkable2-framebuffer) and [#14](https://github.com/ddvk/remarkable2-framebuffer/issues/14)


## Contents

- [APIs](#apis)
- [Applications](#applications)
  - [Games](#games)
  - [Launchers](#launchers)
- [Cloud Tools](#cloud-tools)
- [Device Tools](#device-tools)
- [GUI Clients](#gui-clients)
- [Other](#other)
- [Screen Sharing/Streaming](#screen-sharingstreaming)
- [Custom Templates](#custom-templates)

## APIs

- [google-drive-remarkable-sync](https://github.com/bsdz/google-drive-remarkable-sync) - Apps Script API for reMarkable Cloud. Includes Synchronizer capability to automate mirroring of documents from Google Drive to reMarkable Cloud.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/bsdz/google-drive-remarkable-sync?style=social)
  ![Languages](https://shields.io/github/languages/top/bsdz/google-drive-remarkable-sync)
  ![License](https://shields.io/github/license/bsdz/google-drive-remarkable-sync)
  ![Last commit](https://shields.io/github/last-commit/bsdz/google-drive-remarkable-sync)
  ![Issues](https://shields.io/github/issues/bsdz/google-drive-remarkable-sync)
  <!-- /shields -->
- [jrmapi](https://github.com/jlarriba/jrmapi) - A Java API for the reMarkable Cloud.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/jlarriba/jrmapi?style=social)
  ![Languages](https://shields.io/github/languages/top/jlarriba/jrmapi)
  ![License](https://shields.io/github/license/jlarriba/jrmapi)
  ![Last commit](https://shields.io/github/last-commit/jlarriba/jrmapi)
  ![Issues](https://shields.io/github/issues/jlarriba/jrmapi)
  <!-- /shields -->
- [libreMarkable](https://github.com/canselcik/libremarkable) - A framework for developing applications with native refresh support for reMarkable Tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/canselcik/libremarkable?style=social)
  ![Languages](https://shields.io/github/languages/top/canselcik/libremarkable)
  ![License](https://shields.io/github/license/canselcik/libremarkable)
  ![Last commit](https://shields.io/github/last-commit/canselcik/libremarkable)
  ![Issues](https://shields.io/github/issues/canselcik/libremarkable)
  <!-- /shields -->
- [lines-are-beautiful](https://github.com/ax3l/lines-are-beautiful) - C++ File API for the reMarkable tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/ax3l/lines-are-beautiful?style=social)
  ![Languages](https://shields.io/github/languages/top/ax3l/lines-are-beautiful)
  ![License](https://shields.io/github/license/ax3l/lines-are-beautiful)
  ![Last commit](https://shields.io/github/last-commit/ax3l/lines-are-beautiful)
  ![Issues](https://shields.io/github/issues/ax3l/lines-are-beautiful)
  <!-- /shields -->
- [lines-are-rusty](https://github.com/ax3l/lines-are-rusty) - Rust File API for the reMarkable tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/ax3l/lines-are-rusty?style=social)
  ![Languages](https://shields.io/github/languages/top/ax3l/lines-are-rusty)
  ![License](https://shields.io/github/license/ax3l/lines-are-rusty)
  ![Last commit](https://shields.io/github/last-commit/ax3l/lines-are-rusty)
  ![Issues](https://shields.io/github/issues/ax3l/lines-are-rusty)
  <!-- /shields -->
- [reMarkableAPI](https://github.com/splitbrain/ReMarkableAPI) - Docs and implementation of the reMarkable file sync API.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/splitbrain/ReMarkableAPI?style=social)
  ![Languages](https://shields.io/github/languages/top/splitbrain/ReMarkableAPI)
  ![License](https://shields.io/github/license/splitbrain/ReMarkableAPI)
  ![Last commit](https://shields.io/github/last-commit/splitbrain/ReMarkableAPI)
  ![Issues](https://shields.io/github/issues/splitbrain/ReMarkableAPI)
  <!-- /shields -->
- [reMarkable-layers](https://github.com/bsdz/remarkable-layers) - Python API for reading & writing reMarkable Lines format. Supports very basic conversion of PDFs and SVGs to Lines format.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/bsdz/remarkable-layers?style=social)
  ![Languages](https://shields.io/github/languages/top/bsdz/remarkable-layers)
  ![License](https://shields.io/github/license/bsdz/remarkable-layers)
  ![Last commit](https://shields.io/github/last-commit/bsdz/remarkable-layers)
  ![Issues](https://shields.io/github/issues/bsdz/remarkable-layers)
  <!-- /shields -->
- [reMarkable-typescript](https://github.com/Ogdentrod/reMarkable-typescript) - TypeScript API for reMarkable Cloud.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/Ogdentrod/reMarkable-typescript?style=social)
  ![Languages](https://shields.io/github/languages/top/Ogdentrod/reMarkable-typescript)
  ![License](https://shields.io/github/license/Ogdentrod/reMarkable-typescript)
  ![Last commit](https://shields.io/github/last-commit/Ogdentrod/reMarkable-typescript)
  ![Issues](https://shields.io/github/issues/Ogdentrod/reMarkable-typescript)
  <!-- /shields -->
- [rMAPI](https://github.com/juruen/rmapi) - ReMarkable Cloud Go API.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/juruen/rmapi?style=social)
  ![Languages](https://shields.io/github/languages/top/juruen/rmapi)
  ![License](https://shields.io/github/license/juruen/rmapi)
  ![Last commit](https://shields.io/github/last-commit/juruen/rmapi)
  ![Issues](https://shields.io/github/issues/juruen/rmapi)
  <!-- /shields -->
- [rmapy](https://github.com/subutux/rmapy) - ReMarkable Cloud Python API.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/subutux/rmapy?style=social)
  ![Languages](https://shields.io/github/languages/top/subutux/rmapy)
  ![License](https://shields.io/github/license/subutux/rmapy)
  ![Last commit](https://shields.io/github/last-commit/subutux/rmapy)
  ![Issues](https://shields.io/github/issues/subutux/rmapy)
  <!-- /shields -->
- [rmfakecloud](https://github.com/ddvk/rmfakecloud) - Fake Cloud Sync, server implementation of the Cloud API.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/ddvk/rmfakecloud?style=social)
  ![Languages](https://shields.io/github/languages/top/ddvk/rmfakecloud)
  ![License](https://shields.io/github/license/ddvk/rmfakecloud)
  ![Last commit](https://shields.io/github/last-commit/ddvk/rmfakecloud)
  ![Issues](https://shields.io/github/issues/ddvk/rmfakecloud)
  <!-- /shields -->

## Applications

- [harmony](https://rmkit.dev/apps/harmony) - a low latency sketching app with procedural brushes.
- [KOReader](https://github.com/koreader/koreader) - An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/koreader/koreader?style=social)
  ![Languages](https://shields.io/github/languages/top/koreader/koreader)
  ![License](https://shields.io/github/license/koreader/koreader)
  ![Last commit](https://shields.io/github/last-commit/koreader/koreader)
  ![Issues](https://shields.io/github/issues/koreader/koreader)
  <!-- /shields -->
- [darvin/plato](https://github.com/darvin/plato) [LinusCDE/plato](https://github.com/LinusCDE/plato) - Plato reader port. Supports pdfs, epubs, many other formats.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/darvin/plato?style=social)
  ![Languages](https://shields.io/github/languages/top/darvin/plato)
  ![License](https://shields.io/github/license/darvin/plato)
  ![Last commit](https://shields.io/github/last-commit/darvin/plato)
  ![Issues](https://shields.io/github/issues/darvin/plato)
  <!-- /shields -->
- [reMarkable keywriter](https://github.com/dps/remarkable-keywriter) - A distraction free keyboard notes app.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/dps/remarkable-keywriter?style=social)
  ![Languages](https://shields.io/github/languages/top/dps/remarkable-keywriter)
  ![License](https://shields.io/github/license/dps/remarkable-keywriter)
  ![Last commit](https://shields.io/github/last-commit/dps/remarkable-keywriter)
  ![Issues](https://shields.io/github/issues/dps/remarkable-keywriter)
  <!-- /shields -->
- [reMarkable wikipedia](https://github.com/dps/remarkable-wikipedia) - Offline wikipedia reader for reMarkable.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/dps/remarkable-wikipedia?style=social)
  ![Languages](https://shields.io/github/languages/top/dps/remarkable-wikipedia)
  ![License](https://shields.io/github/license/dps/remarkable-wikipedia)
  ![Last commit](https://shields.io/github/last-commit/dps/remarkable-wikipedia)
  ![Issues](https://shields.io/github/issues/dps/remarkable-wikipedia)
  <!-- /shields -->

### Games

- [chessMarkable](https://github.com/LinusCDE/chessmarkable) - Play chess against a bot or a friend.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/LinusCDE/chessmarkable?style=social)
  ![Languages](https://shields.io/github/languages/top/LinusCDE/chessmarkable)
  ![License](https://shields.io/github/license/LinusCDE/chessmarkable)
  ![Last commit](https://shields.io/github/last-commit/LinusCDE/chessmarkable)
  ![Issues](https://shields.io/github/issues/LinusCDE/chessmarkable)
  <!-- /shields -->
- [minesweeper](https://rmkit.dev/apps/minesweeper) - A mine detection game.
- [retris](https://github.com/LinusCDE/retris) - Play a clone of the popular block stacking game with either buttons or swipe guestures.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/LinusCDE/retris?style=social)
  ![Languages](https://shields.io/github/languages/top/LinusCDE/retris)
  ![License](https://shields.io/github/license/LinusCDE/retris)
  ![Last commit](https://shields.io/github/last-commit/LinusCDE/retris)
  ![Issues](https://shields.io/github/issues/LinusCDE/retris)
  <!-- /shields -->

### Launchers

- [draft-reMarkable](https://github.com/dixonary/draft-reMarkable) - A launcher for the reMarkable tablet, which wraps around the standard interface.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/dixonary/draft-reMarkable?style=social)
  ![Languages](https://shields.io/github/languages/top/dixonary/draft-reMarkable)
  ![License](https://shields.io/github/license/dixonary/draft-reMarkable)
  ![Last commit](https://shields.io/github/last-commit/dixonary/draft-reMarkable)
  ![Issues](https://shields.io/github/issues/dixonary/draft-reMarkable)
  <!-- /shields -->
- [oxide](https://github.com/Eeems/oxide/releases) - A launcher application for the reMarkable tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/Eeems/oxide?style=social)
  ![Languages](https://shields.io/github/languages/top/Eeems/oxide)
  ![License](https://shields.io/github/license/Eeems/oxide)
  ![Last commit](https://shields.io/github/last-commit/Eeems/oxide)
  ![Issues](https://shields.io/github/issues/Eeems/oxide)
  <!-- /shields -->
- [remux](https://rmkit.dev/apps/remux) - A multi-tasking launcher for the reMarkable tablet.


## Cloud Tools

- [CUPS Printing](https://ofosos.org/2018/10/22/printing-to-remarkable-cloud-from-cups/) - Script to print directly to reMarkable Cloud from CUPS using rMAPI.
- [rM-sync](https://github.com/simonschllng/rm-sync) - Sync script for reMarkable paper tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/simonschllng/rm-sync?style=social)
  ![Languages](https://shields.io/github/languages/top/simonschllng/rm-sync)
  ![License](https://shields.io/github/license/simonschllng/rm-sync)
  ![Last commit](https://shields.io/github/last-commit/simonschllng/rm-sync)
  ![Issues](https://shields.io/github/issues/simonschllng/rm-sync)
  <!-- /shields -->
- [reMarkable_syncthing](http://github.com/evidlo/remarkable_syncthing) - Syncthing on reMarkable.
- [zotero-reMarkable](https://github.com/michaelmior/zotero-remarkable) - Script to sync PDFs from the [Zotero](https://www.zotero.org/) reference manager.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/michaelmior/zotero-remarkable?style=social)
  ![Languages](https://shields.io/github/languages/top/michaelmior/zotero-remarkable)
  ![License](https://shields.io/github/license/michaelmior/zotero-remarkable)
  ![Last commit](https://shields.io/github/last-commit/michaelmior/zotero-remarkable)
  ![Issues](https://shields.io/github/issues/michaelmior/zotero-remarkable)
  <!-- /shields -->
- [sync_zotero_remarkable](https://github.com/danijoo/sync_zotero_remarkable) - Sync PDFs from Zotero to Remarkable.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/danijoo/sync_zotero_remarkable?style=social)
  ![Languages](https://shields.io/github/languages/top/danijoo/sync_zotero_remarkable)
  ![License](https://shields.io/github/license/danijoo/sync_zotero_remarkable)
  ![Last commit](https://shields.io/github/last-commit/danijoo/sync_zotero_remarkable)
  ![Issues](https://shields.io/github/issues/danijoo/sync_zotero_remarkable)
  <!-- /shields -->

## Device Tools
- [ReCept](https://github.com/funkey/recept/) - Fix for the rM2 jagged line issue.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/funkey/recept?style=social)
  ![Languages](https://shields.io/github/languages/top/funkey/recept)
  ![License](https://shields.io/github/license/funkey/recept)
  ![Last commit](https://shields.io/github/last-commit/funkey/recept)
  ![Issues](https://shields.io/github/issues/funkey/recept)
  <!-- /shields -->

## GUI Clients

- [asTounding](https://github.com/jlarriba/astounding) -  A multiplatform GUI application for the reMarkable cloud, including Linux.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/jlarriba/astounding?style=social)
  ![Languages](https://shields.io/github/languages/top/jlarriba/astounding)
  ![License](https://shields.io/github/license/jlarriba/astounding)
  ![Last commit](https://shields.io/github/last-commit/jlarriba/astounding)
  ![Issues](https://shields.io/github/issues/jlarriba/astounding)
  <!-- /shields -->
- [RemaDroid](https://play.google.com/store/apps/details?id=org.remadroid) - An alternative Android app to upload documents, webpages or images to the reMarkable tablet.
- [RemaPy](https://github.com/peerdavid/remapy) - GUI to browse, download/upload files and backup the tablet (also on Linux) using the cloud.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/peerdavid/remapy?style=social)
  ![Languages](https://shields.io/github/languages/top/peerdavid/remapy)
  ![License](https://shields.io/github/license/peerdavid/remapy)
  ![Last commit](https://shields.io/github/last-commit/peerdavid/remapy)
  ![Issues](https://shields.io/github/issues/peerdavid/remapy)
  <!-- /shields -->
- [reMarkable-assistant](https://github.com/richeymichael/remarkable-assistant) - Manage templates, splash screens, and settings on your reMarkable tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/richeymichael/remarkable-assistant?style=social)
  ![Languages](https://shields.io/github/languages/top/richeymichael/remarkable-assistant)
  ![License](https://shields.io/github/license/richeymichael/remarkable-assistant)
  ![Last commit](https://shields.io/github/last-commit/richeymichael/remarkable-assistant)
  ![Issues](https://shields.io/github/issues/richeymichael/remarkable-assistant)
  <!-- /shields -->
- [reMarkable Connection Utility (RCU)](http://www.davisr.me/projects/rcu/) - A cross-platform client for offline management of backups, screenshots, notebooks, templates, wallpaper, and third-party software.
- [reMarkable-hyutilities](https://github.com/moovida/remarkable-hyutilities) - A GUI written in java to backup your device, upload templates and modify splash screens.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/moovida/remarkable-hyutilities?style=social)
  ![Languages](https://shields.io/github/languages/top/moovida/remarkable-hyutilities)
  ![License](https://shields.io/github/license/moovida/remarkable-hyutilities)
  ![Last commit](https://shields.io/github/last-commit/moovida/remarkable-hyutilities)
  ![Issues](https://shields.io/github/issues/moovida/remarkable-hyutilities)
  <!-- /shields -->
- [ReMy](https://github.com/bordaigorl/remy) - A GUI to browse, preview documents, export documents with custom settings, all via SSH (no cloud needed); works from local raw backups too.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/bordaigorl/remy?style=social)
  ![Languages](https://shields.io/github/languages/top/bordaigorl/remy)
  ![License](https://shields.io/github/license/bordaigorl/remy)
  ![Last commit](https://shields.io/github/last-commit/bordaigorl/remy)
  ![Issues](https://shields.io/github/issues/bordaigorl/remy)
  <!-- /shields -->
- [rMExplorer](https://github.com/bruot/pyrmexplorer/wiki) - GUI to browse, download/upload files and backup the tablet without using the cloud.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/bruot/pyrmexplorer?style=social)
  ![Languages](https://shields.io/github/languages/top/bruot/pyrmexplorer)
  ![License](https://shields.io/github/license/bruot/pyrmexplorer)
  ![Last commit](https://shields.io/github/last-commit/bruot/pyrmexplorer)
  ![Issues](https://shields.io/github/issues/bruot/pyrmexplorer)
  <!-- /shields -->
- [rmUploader](https://github.com/lobre/rmuploader) - Simple web app to upload epub or pdf files to the reMarkable tablet via drag and drop.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/lobre/rmuploader?style=social)
  ![Languages](https://shields.io/github/languages/top/lobre/rmuploader)
  ![License](https://shields.io/github/license/lobre/rmuploader)
  ![Last commit](https://shields.io/github/last-commit/lobre/rmuploader)
  ![Issues](https://shields.io/github/issues/lobre/rmuploader)
  <!-- /shields -->

## Other

- [Crazy Cow](https://github.com/machinelevel/sp425-crazy-cow) - Typewriter input from USB keyboard directly into reMarkable interface.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/machinelevel/sp425-crazy-cow?style=social)
  ![Languages](https://shields.io/github/languages/top/machinelevel/sp425-crazy-cow)
  ![License](https://shields.io/github/license/machinelevel/sp425-crazy-cow)
  ![Last commit](https://shields.io/github/last-commit/machinelevel/sp425-crazy-cow)
  ![Issues](https://shields.io/github/issues/machinelevel/sp425-crazy-cow)
  <!-- /shields -->
- [Funcky reMarkable Exporter](https://github.com/simonbaudart/Funcky.Remarkable.Exporter) - Export notes from a reMarkable Tablet to File System and External Services.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/simonbaudart/Funcky.Remarkable.Exporter?style=social)
  ![Languages](https://shields.io/github/languages/top/simonbaudart/Funcky.Remarkable.Exporter)
  ![License](https://shields.io/github/license/simonbaudart/Funcky.Remarkable.Exporter)
  ![Last commit](https://shields.io/github/last-commit/simonbaudart/Funcky.Remarkable.Exporter)
  ![Issues](https://shields.io/github/issues/simonbaudart/Funcky.Remarkable.Exporter)
  <!-- /shields -->
- [Goosepaper](https://github.com/j6k4m8/goosepaper): Deliver prettily-formatted RSS feeds, news articles, Wikipedia articles-of-the-day, and more to your reMarkable tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/j6k4m8/goosepaper?style=social)
  ![Languages](https://shields.io/github/languages/top/j6k4m8/goosepaper)
  ![License](https://shields.io/github/license/j6k4m8/goosepaper)
  ![Last commit](https://shields.io/github/last-commit/j6k4m8/goosepaper)
  ![Issues](https://shields.io/github/issues/j6k4m8/goosepaper)
  <!-- /shields -->
- [instapaper-as-pdf-to-reMarkable](https://github.com/fabianmu/instapaper-as-pdf-to-remarkable) - Export Instapaper-Articles to PDF and send them to a connected rM tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/fabianmu/instapaper-as-pdf-to-remarkable?style=social)
  ![Languages](https://shields.io/github/languages/top/fabianmu/instapaper-as-pdf-to-remarkable)
  ![License](https://shields.io/github/license/fabianmu/instapaper-as-pdf-to-remarkable)
  ![Last commit](https://shields.io/github/last-commit/fabianmu/instapaper-as-pdf-to-remarkable)
  ![Issues](https://shields.io/github/issues/fabianmu/instapaper-as-pdf-to-remarkable)
  <!-- /shields -->
- [morningpaper2reMarkable](https://github.com/jessfraz/morningpaper2remarkable) - A bot to sync the morning paper to a remarkable tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/jessfraz/morningpaper2remarkable?style=social)
  ![Languages](https://shields.io/github/languages/top/jessfraz/morningpaper2remarkable)
  ![License](https://shields.io/github/license/jessfraz/morningpaper2remarkable)
  ![Last commit](https://shields.io/github/last-commit/jessfraz/morningpaper2remarkable)
  ![Issues](https://shields.io/github/issues/jessfraz/morningpaper2remarkable)
  <!-- /shields -->
- [paper2reMarkable](https://github.com/GjjvdBurg/paper2remarkable) - Download an academic paper or HTML article, crop it, and send it to the reMarkable with a single command.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/GjjvdBurg/paper2remarkable?style=social)
  ![Languages](https://shields.io/github/languages/top/GjjvdBurg/paper2remarkable)
  ![License](https://shields.io/github/license/GjjvdBurg/paper2remarkable)
  ![Last commit](https://shields.io/github/last-commit/GjjvdBurg/paper2remarkable)
  ![Issues](https://shields.io/github/issues/GjjvdBurg/paper2remarkable)
  <!-- /shields -->
- [Parabola-rM](http://www.davisr.me/projects/parabola-rm/) - A Desktop GNU/Linux-libre replacement OS with fast partial refreshing and USB OTG.
- [pocket2rm](https://github.com/glidergeek/pocket2rm) - Synchronize articles from read-later platform pocket in PDF and epub.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/glidergeek/pocket2rm?style=social)
  ![Languages](https://shields.io/github/languages/top/glidergeek/pocket2rm)
  ![License](https://shields.io/github/license/glidergeek/pocket2rm)
  ![Last commit](https://shields.io/github/last-commit/glidergeek/pocket2rm)
  ![Issues](https://shields.io/github/issues/glidergeek/pocket2rm)
  <!-- /shields -->
- [remailable](https://github.com/j6k4m8/remailable) - Email PDFs directly to your reMarkable. ([Free publicly-hosted version available](https://remailable.getneutrality.org/)).
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/j6k4m8/remailable?style=social)
  ![Languages](https://shields.io/github/languages/top/j6k4m8/remailable)
  ![License](https://shields.io/github/license/j6k4m8/remailable)
  ![Last commit](https://shields.io/github/last-commit/j6k4m8/remailable)
  ![Issues](https://shields.io/github/issues/j6k4m8/remailable)
  <!-- /shields -->
- [reHackable/maxio](https://github.com/reHackable/maxio) - Companion daemon for the reMarkable paper tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/reHackable/maxio?style=social)
  ![Languages](https://shields.io/github/languages/top/reHackable/maxio)
  ![License](https://shields.io/github/license/reHackable/maxio)
  ![Last commit](https://shields.io/github/last-commit/reHackable/maxio)
  ![Issues](https://shields.io/github/issues/reHackable/maxio)
  <!-- /shields -->
- [reHackable/scripts](https://github.com/reHackable/scripts) - A set of bash scripts that may enhance your reMarkable experience.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/reHackable/scripts?style=social)
  ![Languages](https://shields.io/github/languages/top/reHackable/scripts)
  ![License](https://shields.io/github/license/reHackable/scripts)
  ![Last commit](https://shields.io/github/last-commit/reHackable/scripts)
  ![Issues](https://shields.io/github/issues/reHackable/scripts)
  <!-- /shields -->
- [reMarkable_entware](http://github.com/evidlo/remarkable_entware) - Package manager for reMarkable.  Install common Unix utilities through the command line.
- [reMarkable_keyboard](https://github.com/Evidlo/remarkable_keyboard) - Software to use rM as wireless keyboard/mouse.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/Evidlo/remarkable_keyboard?style=social)
  ![Languages](https://shields.io/github/languages/top/Evidlo/remarkable_keyboard)
  ![License](https://shields.io/github/license/Evidlo/remarkable_keyboard)
  ![Last commit](https://shields.io/github/last-commit/Evidlo/remarkable_keyboard)
  ![Issues](https://shields.io/github/issues/Evidlo/remarkable_keyboard)
  <!-- /shields -->
- [reMarkable_mouse](https://github.com/evidlo/remarkable_mouse) - Use your reMarkable as a graphics tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/evidlo/remarkable_mouse?style=social)
  ![Languages](https://shields.io/github/languages/top/evidlo/remarkable_mouse)
  ![License](https://shields.io/github/license/evidlo/remarkable_mouse)
  ![Last commit](https://shields.io/github/last-commit/evidlo/remarkable_mouse)
  ![Issues](https://shields.io/github/issues/evidlo/remarkable_mouse)
  <!-- /shields -->
- [remarkable_news](https://github.com/evidlo/remarkable_news) - Use daily news/comics/images as the suspend screen.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/evidlo/remarkable_news?style=social)
  ![Languages](https://shields.io/github/languages/top/evidlo/remarkable_news)
  ![License](https://shields.io/github/license/evidlo/remarkable_news)
  ![Last commit](https://shields.io/github/last-commit/evidlo/remarkable_news)
  ![Issues](https://shields.io/github/issues/evidlo/remarkable_news)
  <!-- /shields -->
- [reMarkable_pdflets](https://github.com/evidlo/remarkable_pdflets) - Dynamically updating PDFs.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/evidlo/remarkable_pdflets?style=social)
  ![Languages](https://shields.io/github/languages/top/evidlo/remarkable_pdflets)
  ![License](https://shields.io/github/license/evidlo/remarkable_pdflets)
  ![Last commit](https://shields.io/github/last-commit/evidlo/remarkable_pdflets)
  ![Issues](https://shields.io/github/issues/evidlo/remarkable_pdflets)
  <!-- /shields -->
- [remarkable_printer](https://github.com/Evidlo/remarkable_printer) - Print from any device to reMarkable without browser extensions or reMarkable cloud.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/Evidlo/remarkable_printer?style=social)
  ![Languages](https://shields.io/github/languages/top/Evidlo/remarkable_printer)
  ![License](https://shields.io/github/license/Evidlo/remarkable_printer)
  ![Last commit](https://shields.io/github/last-commit/Evidlo/remarkable_printer)
  ![Issues](https://shields.io/github/issues/Evidlo/remarkable_printer)
  <!-- /shields -->
- [reMarkable-fs](https://github.com/nick8325/remarkable-fs) - A FUSE filesystem wrapper for the reMarkable tablet.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/nick8325/remarkable-fs?style=social)
  ![Languages](https://shields.io/github/languages/top/nick8325/remarkable-fs)
  ![License](https://shields.io/github/license/nick8325/remarkable-fs)
  ![Last commit](https://shields.io/github/last-commit/nick8325/remarkable-fs)
  ![Issues](https://shields.io/github/issues/nick8325/remarkable-fs)
  <!-- /shields -->
- [reMarkable-random-screens](https://github.com/Neurone/reMarkable) - Change your poweroff and suspend screens every 5 minutes with random images of your choice
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/Neurone/reMarkable?style=social)
  ![Languages](https://shields.io/github/languages/top/Neurone/reMarkable)
  ![License](https://shields.io/github/license/Neurone/reMarkable)
  ![Last commit](https://shields.io/github/last-commit/Neurone/reMarkable)
  ![Issues](https://shields.io/github/issues/Neurone/reMarkable)
  <!-- /shields -->
- [reMarkable-touchgestures](https://github.com/ddvk/remarkable-touchgestures) - Touch gestures (swipe/touch) for easy page navigation.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/ddvk/remarkable-touchgestures?style=social)
  ![Languages](https://shields.io/github/languages/top/ddvk/remarkable-touchgestures)
  ![License](https://shields.io/github/license/ddvk/remarkable-touchgestures)
  ![Last commit](https://shields.io/github/last-commit/ddvk/remarkable-touchgestures)
  ![Issues](https://shields.io/github/issues/ddvk/remarkable-touchgestures)
  <!-- /shields -->
- [reMarkable-tweak](https://github.com/morngrar/remarkable-tweak) - Tweak tool for the reMarkable paper tablet. Lets you organize your templates with no fuss.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/morngrar/remarkable-tweak?style=social)
  ![Languages](https://shields.io/github/languages/top/morngrar/remarkable-tweak)
  ![License](https://shields.io/github/license/morngrar/remarkable-tweak)
  ![Last commit](https://shields.io/github/last-commit/morngrar/remarkable-tweak)
  ![Issues](https://shields.io/github/issues/morngrar/remarkable-tweak)
  <!-- /shields -->
- [remarks](https://github.com/lucasrla/remarks) - Extract highlights, scribbles, and annotations from PDFs. Export to Markdown, PNG, and SVG.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/lucasrla/remarks?style=social)
  ![Languages](https://shields.io/github/languages/top/lucasrla/remarks)
  ![License](https://shields.io/github/license/lucasrla/remarks)
  ![Last commit](https://shields.io/github/last-commit/lucasrla/remarks)
  ![Issues](https://shields.io/github/issues/lucasrla/remarks)
  <!-- /shields -->
- [remt](https://gitlab.com/wrobell/remt) - reMarkable tablet command-line tools.
- [rM-dl-annotated](https://github.com/jmptable/rm-dl-annotated) - Export annotated PDFs from reMarkable tablets.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/jmptable/rm-dl-annotated?style=social)
  ![Languages](https://shields.io/github/languages/top/jmptable/rm-dl-annotated)
  ![License](https://shields.io/github/license/jmptable/rm-dl-annotated)
  ![Last commit](https://shields.io/github/last-commit/jmptable/rm-dl-annotated)
  ![Issues](https://shields.io/github/issues/jmptable/rm-dl-annotated)
  <!-- /shields -->
- [rMsync](https://github.com/lschwetlick/rMsync) - Synchronisation script with a local dedicated "library" folder.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/lschwetlick/rMsync?style=social)
  ![Languages](https://shields.io/github/languages/top/lschwetlick/rMsync)
  ![License](https://shields.io/github/license/lschwetlick/rMsync)
  ![Last commit](https://shields.io/github/last-commit/lschwetlick/rMsync)
  ![Issues](https://shields.io/github/issues/lschwetlick/rMsync)
  <!-- /shields -->
- [rmTabletDriver](https://github.com/LinusCDE/rmTabletDriver) - Application that allows you to simulate/clone rM input on your computer.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/LinusCDE/rmTabletDriver?style=social)
  ![Languages](https://shields.io/github/languages/top/LinusCDE/rmTabletDriver)
  ![License](https://shields.io/github/license/LinusCDE/rmTabletDriver)
  ![Last commit](https://shields.io/github/last-commit/LinusCDE/rmTabletDriver)
  ![Issues](https://shields.io/github/issues/LinusCDE/rmTabletDriver)
  <!-- /shields -->
- [rmWacomToMouse](https://github.com/LinusCDE/rmWacomToMouse) - Use the wacom pen as a mouse to draw on your pc.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/LinusCDE/rmWacomToMouse?style=social)
  ![Languages](https://shields.io/github/languages/top/LinusCDE/rmWacomToMouse)
  ![License](https://shields.io/github/license/LinusCDE/rmWacomToMouse)
  ![Last commit](https://shields.io/github/last-commit/LinusCDE/rmWacomToMouse)
  ![Issues](https://shields.io/github/issues/LinusCDE/rmWacomToMouse)
  <!-- /shields -->
- [rmWebUiTools](https://github.com/LinusCDE/rmWebUiTools) - View a file tree, see statistics and export/backup all files with some simple scripts utilizing the web ui.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/LinusCDE/rmWebUiTools?style=social)
  ![Languages](https://shields.io/github/languages/top/LinusCDE/rmWebUiTools)
  ![License](https://shields.io/github/license/LinusCDE/rmWebUiTools)
  ![Last commit](https://shields.io/github/last-commit/LinusCDE/rmWebUiTools)
  ![Issues](https://shields.io/github/issues/LinusCDE/rmWebUiTools)
  <!-- /shields -->


## Screen Sharing/Streaming

- [pipes and paper](https://gitlab.com/afandian/pipes-and-paper) - Stream pen strokes to browser canvas via websockets ([blog post](https://blog.afandian.com/2020/10/pipes-and-paper-remarkable/)). Uses Python and SSH, nothing to compile or install on the reMarkable device.
- [pipes and rust](https://github.com/AnyTimeTraveler/pipes-and-rust) - (Made for rM2) Stream pen strokes to browser. A single executable on the reMarkable that hosts a tiny webserver in the local WLAN.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/AnyTimeTraveler/pipes-and-rust?style=social)
  ![Languages](https://shields.io/github/languages/top/AnyTimeTraveler/pipes-and-rust)
  ![License](https://shields.io/github/license/AnyTimeTraveler/pipes-and-rust)
  ![Last commit](https://shields.io/github/last-commit/AnyTimeTraveler/pipes-and-rust)
  ![Issues](https://shields.io/github/issues/AnyTimeTraveler/pipes-and-rust)
  <!-- /shields -->
- [reStream](https://github.com/rien/reStream) - Stream your reMarkable screen over SSH.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/rien/reStream?style=social)
  ![Languages](https://shields.io/github/languages/top/rien/reStream)
  ![License](https://shields.io/github/license/rien/reStream)
  ![Last commit](https://shields.io/github/last-commit/rien/reStream)
  ![Issues](https://shields.io/github/issues/rien/reStream)
  <!-- /shields -->
- [rMview](https://github.com/bordaigorl/rmview) - A fast GUI to stream your reMarkable screen over vanilla-SSH or VNC.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/bordaigorl/rmview?style=social)
  ![Languages](https://shields.io/github/languages/top/bordaigorl/rmview)
  ![License](https://shields.io/github/license/bordaigorl/rmview)
  ![Last commit](https://shields.io/github/last-commit/bordaigorl/rmview)
  ![Issues](https://shields.io/github/issues/bordaigorl/rmview)
  <!-- /shields -->
- [rM-vnc-server](https://github.com/peter-sa/rM-vnc-server) - A fast & efficient damage-tracking (sending only updated regions) VNC server for streaming the reMarkable's screen.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/peter-sa/rM-vnc-server?style=social)
  ![Languages](https://shields.io/github/languages/top/peter-sa/rM-vnc-server)
  ![License](https://shields.io/github/license/peter-sa/rM-vnc-server)
  ![Last commit](https://shields.io/github/last-commit/peter-sa/rM-vnc-server)
  ![Issues](https://shields.io/github/issues/peter-sa/rM-vnc-server)
  <!-- /shields -->
- [srvfb](https://github.com/merovius/srvfb) - Alternative screen-streaming software. Written in Go.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/merovius/srvfb?style=social)
  ![Languages](https://shields.io/github/languages/top/merovius/srvfb)
  ![License](https://shields.io/github/license/merovius/srvfb)
  ![Last commit](https://shields.io/github/last-commit/merovius/srvfb)
  ![Issues](https://shields.io/github/issues/merovius/srvfb)
  <!-- /shields -->
- [VNSee](https://github.com/matteodelabre/vnsee) - VNC client for the reMarkable tablet allowing you to use the device as a second screen.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/matteodelabre/vnsee?style=social)
  ![Languages](https://shields.io/github/languages/top/matteodelabre/vnsee)
  ![License](https://shields.io/github/license/matteodelabre/vnsee)
  ![Last commit](https://shields.io/github/last-commit/matteodelabre/vnsee)
  ![Issues](https://shields.io/github/issues/matteodelabre/vnsee)
  <!-- /shields -->


## Custom Templates
- [reMarkable-bujo](https://github.com/vonneudeck/remarkable-bujo) - "Bullet Journal" templates.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/vonneudeck/remarkable-bujo?style=social)
  ![Languages](https://shields.io/github/languages/top/vonneudeck/remarkable-bujo)
  ![License](https://shields.io/github/license/vonneudeck/remarkable-bujo)
  ![Last commit](https://shields.io/github/last-commit/vonneudeck/remarkable-bujo)
  ![Issues](https://shields.io/github/issues/vonneudeck/remarkable-bujo)
  <!-- /shields -->
- [reMarkable-gtd-templates](https://github.com/BartKeulen/remarkable-gtd-templates) - "Getting Things Done" templates.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/BartKeulen/remarkable-gtd-templates?style=social)
  ![Languages](https://shields.io/github/languages/top/BartKeulen/remarkable-gtd-templates)
  ![License](https://shields.io/github/license/BartKeulen/remarkable-gtd-templates)
  ![Last commit](https://shields.io/github/last-commit/BartKeulen/remarkable-gtd-templates)
  ![Issues](https://shields.io/github/issues/BartKeulen/remarkable-gtd-templates)
  <!-- /shields -->
- [reMarkable-Templates](https://github.com/newtonhonk/reMarkable-Templates) - To Do templates with lines, checkboxes or text blocks.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/newtonhonk/reMarkable-Templates?style=social)
  ![Languages](https://shields.io/github/languages/top/newtonhonk/reMarkable-Templates)
  ![License](https://shields.io/github/license/newtonhonk/reMarkable-Templates)
  ![Last commit](https://shields.io/github/last-commit/newtonhonk/reMarkable-Templates)
  ![Issues](https://shields.io/github/issues/newtonhonk/reMarkable-Templates)
  <!-- /shields -->
- [reMarkable_templates](https://github.com/steka/reMarkable_templates) - White lines/squares on gray background.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/steka/reMarkable_templates?style=social)
  ![Languages](https://shields.io/github/languages/top/steka/reMarkable_templates)
  ![License](https://shields.io/github/license/steka/reMarkable_templates)
  ![Last commit](https://shields.io/github/last-commit/steka/reMarkable_templates)
  ![Issues](https://shields.io/github/issues/steka/reMarkable_templates)
  <!-- /shields -->
- [reMarkabletemplates](https://github.com/equivocates/remarkabletemplates/) - Planner per 1 or 3 weeks.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/equivocates/remarkabletemplates?style=social)
  ![Languages](https://shields.io/github/languages/top/equivocates/remarkabletemplates)
  ![License](https://shields.io/github/license/equivocates/remarkabletemplates)
  ![Last commit](https://shields.io/github/last-commit/equivocates/remarkabletemplates)
  ![Issues](https://shields.io/github/issues/equivocates/remarkabletemplates)
  <!-- /shields -->
- [rM2Mods templates](https://github.com/DanielRunningen/rM2Mods/tree/main/assests/templates) - Collection of different templates. E.g., micro dots/grids, checklists, budgeting,  boxes.
  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/DanielRunningen/rM2Mods?style=social)
  ![Languages](https://shields.io/github/languages/top/DanielRunningen/rM2Mods)
  ![License](https://shields.io/github/license/DanielRunningen/rM2Mods)
  ![Last commit](https://shields.io/github/last-commit/DanielRunningen/rM2Mods)
  ![Issues](https://shields.io/github/issues/DanielRunningen/rM2Mods)
  <!-- /shields -->
