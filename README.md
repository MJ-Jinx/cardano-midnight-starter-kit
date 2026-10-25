[![Cardano & Midnight Starter Kit](og-image.png)](https://mj-jinx.github.io/cardano-midnight-starter-kit/)

# Cardano & Midnight Starter Kit

Skills, plugins, MCP servers and repos for building on Cardano and Midnight, plus a step-by-step setup guide for Claude Code in VS Code.

**Read it here: https://mj-jinx.github.io/cardano-midnight-starter-kit/**

## What's inside

- A setup guide for Windows (WSL) as well as macOS and Linux. It covers VS Code extensions, Node, the Compact toolchain, the proof server, Aiken, Claude Code plugins and skills, MCP servers, wallets, faucets and first builds.
- Claude Code skills and plugins for Midnight and Cardano.
- MCP servers.
- Official and community repos and docs for both chains.
- Watch-outs: archived repos, version pinning, and skills to install with care.

## Updating

The whole site is one file, `index.html`. Edit it on GitHub with the pencil icon or locally, then commit to `main`. GitHub Pages republishes in a minute or two.

The banner (`og-image.png`) is the preview image shown when the link is shared. Its source is `assets/banner-source.html`. To change it, edit that file and take a 1200×630 screenshot, for example with headless Edge or Chrome:

```bash
msedge --headless=new --hide-scrollbars --window-size=1200,630 --virtual-time-budget=8000 --screenshot=og-image.png file:///full/path/to/assets/banner-source.html
```

Social sites cache previews, so a changed banner can take a while to show up where the link was already shared.

## Link checks

A GitHub Action (`.github/workflows/link-check.yml`) checks every link once a week and on every push to `main`. When a link breaks, it opens an issue listing the broken links. You can also run it by hand from the **Actions** tab.

## Suggest a fix

If a link is broken or a version is out of date, please open an issue or a pull request.
