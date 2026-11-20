# Miyu package template

A template repository for writing [Miyu](https://github.com/miyu-agent/miyu) packages: the manifest, release workflow, license and examples are ready, so click **Use this template** on GitHub and start writing. 中文：[README.md](README.md).

## What's inside

```text
├── my-package/                 # the package itself: the folder name is the package id, change it to yours
│   ├── package.toml            # manifest
│   └── scripts/
│       └── my-package-hello.py # a script, installed as a tool
├── examples/                   # examples to copy from, not released
│   ├── meeting-notes/          # skill package: skills/meeting-notes/SKILL.md
│   └── lighthouse/             # knowledge base package: kb/lighthouse/kb.toml and two documents
├── .github/workflows/release.yml  # pushing a v* tag packs the package and uploads it to the release
├── LICENSE                     # MIT, put your own name as the copyright holder
└── .gitignore
```

## How to use it

### 1. Create the repository

On this repository's page, click **Use this template → Create a new repository**. Name it as you like; `miyu-<id>` is common. A repository created from a template is not a fork, so the package source collects it as usual (forks are skipped).

### 2. Pick an id, replace the placeholders

The **id** is the package's name in the package source and what people type to install it (`miyu pkg install <id>`): it starts with a lowercase letter, uses only lowercase letters, digits, `-` and `_`, at most 64 characters. Pick a short name that says what it is: no `miyu-`, no kind of package (`scripts-`, `skills-` and the like), and don't start with `base-` (that's for packages shipped with Miyu). Ids in the package source are first come, first served, so run `miyu pkg search <word>` before picking one.

What to change (searching the repository for `my-package` finds them all):

1. Rename the folder `my-package/` to your id: `git mv my-package <id>`. **The folder name is the id**: local packing and installing go by it.
2. In `.github/workflows/release.yml`, set both `package:` and `folder:` to your id.
3. In `<id>/package.toml`: `name`, `summary`, `author`, `upstream`, `license`.
4. The script `scripts/my-package-hello.py`: the tool is named after the file, so prefix it with your id to avoid clashing with other packages; delete it if you don't need the example.
5. The copyright holder in `LICENSE`. If you pick another license, change `license` in the manifest to match (an [SPDX](https://spdx.org/licenses/) expression such as `MIT`, `Apache-2.0`, `CC-BY-SA-4.0`).

### 3. Write the content

A package can bring any mix of the following. The file-based kinds go into the package folder by convention, with nothing in the manifest:

| To do | Put | Example |
|---|---|---|
| Give the AI a small tool | `scripts/<name>.py` (or any executable) | `my-package/scripts/` |
| Teach the AI a way of doing something | `skills/<name>/SKILL.md` | `examples/meeting-notes/` |
| A set of material for the AI to look up | `kb/<id>/`: `kb.toml` and documents | `examples/lighthouse/` |
| A slash command | `commands/<name>.md` | see the author guides |
| Personas, presets | `personas/<id>/`, `presets/<id>.toml` | see the author guides |
| An MCP server, a long-running extension, a settings page | `[[mcp]]`, `[process]`, `[page]` in the manifest | see the author guides |
| A few settings for people to fill in | `[settings.<name>]` in the manifest; scripts read them from the `MIYU_SETTINGS_JSON` environment variable | see the author guides |
| A model provider | `[providers.<id>]` in the manifest | see the author guides |
| A look, the mascot on the terminal's home screen | `[theme]`, `[mascot]` in the manifest | see the author guides |
| Methods other packages call, content for another package | `[export]`, `[content.<package id>]` in the manifest | see the author guides |

To use an example: copy its `skills/` or `kb/` into your package folder; to take a whole example, copy its folder to the repository root, rename it to your id and update `release.yml`.

Tool and skill descriptions (`Description`, `description`) are for the model and go out with every request: write short English sentences, at most three per tool. Names and descriptions for people have their own places (`Display name`, `显示名称`, `display_name`, `summary` and their `_zh`/`_ja` variants).

How to write each one: the [author guides](https://github.com/miyu-agent/miyu/tree/main/docs/en/dev), in particular [Things that work as files](https://github.com/miyu-agent/miyu/blob/main/docs/en/dev/scripts-skills.md) (scripts, skills, command templates, knowledge bases, personas), [the manifest](https://github.com/miyu-agent/miyu/blob/main/docs/en/dev/manifest.md), [MCP servers](https://github.com/miyu-agent/miyu/blob/main/docs/en/dev/mcp.md) and [extensions](https://github.com/miyu-agent/miyu/blob/main/docs/en/dev/extensions.md).

### 4. Try it locally

Replace `<id>` with your id and run these from the repository root. Try in a separate data directory so your everyday Miyu is untouched: prefix commands with `MIYU_HOME=/tmp/miyu-try` (bash, zsh and fish all accept it; in PowerShell run `$env:MIYU_HOME = "$env:TEMP\miyu-try"` first).

```sh
MIYU_HOME=/tmp/miyu-try miyu pkg info ./<id>    # checks the manifest the way installing does and lists what it brings, installs nothing; errors name the line
miyu pkg pack ./<id> -o dist                    # writes dist/<id>-<version>.miyu, prints SHA-256 and size (no core needed)
MIYU_HOME=/tmp/miyu-try miyu pkg install ./dist/<id>-0.1.0.miyu
MIYU_HOME=/tmp/miyu-try miyu pkg info <id>      # name, version, what it provides, license
MIYU_HOME=/tmp/miyu-try miyu pkg list           # what's installed
MIYU_HOME=/tmp/miyu-try miyu check              # says why a script or skill was skipped
MIYU_HOME=/tmp/miyu-try miyu kb list            # with a knowledge base: shows "from <package name>"; try miyu kb search <word>
MIYU_HOME=/tmp/miyu-try miyu core stop          # stop that core when done, then delete /tmp/miyu-try
```

- A script whose first line is a `#!` line needs no executable bit. One without it does on Linux and macOS: `chmod +x <id>/scripts/<file>`, and git keeps it.
- Installing again after a change is an upgrade. Installed skills show up when you type `$` in `miyu`'s input box; script tools show up in the preset settings, where each can be switched on or off.
- Packing leaves out `.git`, `.github`, `__pycache__`, `.DS_Store` and `*.pyc`. Everything else goes in, so keep what you don't want packed out of the package folder.

### 5. Release

1. Bump `version` in the manifest following semver (`0.1.0` → `0.1.1`): the package source only goes by version, so re-releasing the same version is not an update.
2. Commit, push, then tag: the tag is `v` followed by `version`.

   ```sh
   git tag v0.1.0
   git push origin v0.1.0
   ```

3. `release.yml` calls the official packing workflow ([miyu-agent/packages](https://github.com/miyu-agent/packages)), which checks the manifest the way installing does, packs a `.miyu` and uploads it to that tag's release. A tag that doesn't match `version` fails right there.
4. To try packing without releasing: run release by hand from the repository's Actions tab; the package lands in that run's artifacts.

### 6. Get collected as a community package

Add the topic `miyu-package` to the repository (the gear next to About on the repository page). The package source collects once a day (around 03:17 UTC), looking only at each repository's latest full release (drafts and pre-releases don't count), takes the `.miyu` files in it and marks them as community: expect up to a day after you release.

- Ids are first come, first served: the first repository collected under an id keeps it, and other repositories using that id are skipped. Renaming means a new id.
- To check: `miyu pkg update`, then `miyu pkg search <id>`. If it isn't there, the summary of the latest collect run in the [package source repository](https://github.com/miyu-agent/packages)'s Actions gives one line per skipped repository with the reason.
- Forks and archived repositories are not collected; if one `.miyu` in the release can't be read, the whole repository is skipped that round.

## Common errors

| You see | What to do |
|---|---|
| The packed file is called `my-package-…` or something else | The folder name is the id: rename the package folder |
| Cannot pack: the manifest has no version | Write `version = "0.1.0"` in `[package]` |
| `Unknown key package.license`, or `package.license is not a known key` when packing | The running Miyu predates the `license` field: update Miyu, or remove the `license` line |
| `tag … does not match version …` in Actions | The tag without `v` must equal `version` in the manifest |
| `package_conflict` | A tool, skill or knowledge base name clashes with another installed package: rename and install again |
| A script or skill doesn't show up | `miyu check` says which one and why it was skipped |

For other errors see [Common errors](https://github.com/miyu-agent/miyu/blob/main/docs/en/dev/packages.md#common-errors) in the author guides.

## License

`LICENSE` is an MIT template for your package: put your own name as the copyright holder, or switch to the license you want and change `license` in the manifest to match.

The text and examples in this template are dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/): copy, change and publish them without credit, and you can drop this paragraph.
