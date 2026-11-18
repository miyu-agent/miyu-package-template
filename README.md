# Miyu 软件包模板

写 [Miyu](https://github.com/miyu-agent/miyu) 软件包用的模板仓库：清单、发版工作流、许可证、例子都备好了，点 GitHub 上的 **Use this template** 就能开写。English: [README.en.md](README.en.md)。

## 里面有什么

```text
├── my-package/                 # 包本身：文件夹名就是包的编号，改成你的
│   ├── package.toml            # 清单
│   └── scripts/
│       └── my-package-hello.py # 一个脚本，装上就是一件工具
├── examples/                   # 可以拷过去的例子，不发版
│   ├── meeting-notes/          # 技能包：skills/meeting-notes/SKILL.md
│   └── lighthouse/             # 知识库包：kb/lighthouse/kb.toml 和两篇文档
├── .github/workflows/release.yml  # 推 v* 标签就打包、传进 Release
├── LICENSE                     # MIT，版权人改成你自己
└── .gitignore
```

## 怎么用

### 1. 建仓库

在这个仓库页面点 **Use this template → Create a new repository**。仓库名随意，常见的是 `miyu-<编号>`。用模板建出来的不是分叉，软件源照常收录（分叉的不收）。

### 2. 起编号，改掉占位

**编号**是包在软件源里的名字，装的时候敲的就是它（`miyu pkg install <编号>`）：小写字母开头，只用小写字母、数字、`-`、`_`，最多 64 个。起个短的、说得出它是什么的名字：不用带 `miyu-`，也不用带包的种类（`scripts-`、`skills-` 这些），别用 `base-` 打头（那是随 Miyu 出厂的包）。软件源的编号先到先得，起名前先 `miyu pkg search <词>` 看占没占。

要改的地方（全仓库搜 `my-package` 能找全）：

1. 文件夹 `my-package/` 改成你的编号：`git mv my-package <编号>`。**文件夹名就是编号**，本地打包、安装都照它。
2. `.github/workflows/release.yml` 里 `package:` 和 `folder:` 两处，都写你的编号。
3. `<编号>/package.toml`：`name`、`summary`、`author`、`upstream`、`license`。
4. 脚本 `scripts/my-package-hello.py`：工具名照文件名，带上编号做前缀免得和别的包撞；不要这个例子的就删掉。
5. `LICENSE` 的版权人；换别的许可证的，清单的 `license` 跟着改（照 [SPDX](https://spdx.org/licenses/) 写，例如 `MIT`、`Apache-2.0`、`CC-BY-SA-4.0`）。

### 3. 写内容

一个包能带下面几样，几样混着带也行。放文件就能用的这几样照约定放在包文件夹里，清单不用写：

| 想做的 | 放什么 | 例子 |
|---|---|---|
| 给 AI 一件小工具 | `scripts/<名字>.py`（或别的可执行文件） | `my-package/scripts/` |
| 教 AI 一套做事的办法 | `skills/<名字>/SKILL.md` | `examples/meeting-notes/` |
| 一套给她查的资料 | `kb/<编号>/`：`kb.toml` 和文档 | `examples/lighthouse/` |
| 一条斜杠命令 | `commands/<名字>.md` | 见作者文档 |
| 人格、预设 | `personas/<编号>/`、`presets/<编号>.toml` | 见作者文档 |
| 接 MCP 服务、常驻的扩展程序、后台页 | 清单里写 `[[mcp]]`、`[process]`、`[page]` | 见作者文档 |

用例子：把例子里的 `skills/`、`kb/` 拷进你的包文件夹；整包照搬的，把例子文件夹拷到仓库根目录、改名成你的编号，再改 `release.yml`。

清单里多写几张表，还能带下面这些：

| 还能带什么 | 清单里写 | 一句话 |
|---|---|---|
| 配置项 | [`[settings.<名字>]`](https://github.com/miyu-agent/miyu/blob/main/docs/authors/manifest.md#settings名字) | 人在设置的「软件包」页填；扩展握手时拿到，包里的脚本从环境变量 [`MIYU_SETTINGS_JSON`](https://github.com/miyu-agent/miyu/blob/main/docs/authors/scripts-skills.md#脚本) 读 |
| 预设里的开关 | [`[features.<编号>]`](https://github.com/miyu-agent/miyu/blob/main/docs/authors/manifest.md#features编号) | 一个开关管一组工具；不写的整个包一个开关 |
| 模型供应商 | [`[providers.<编号>]`](https://github.com/miyu-agent/miyu/blob/main/docs/authors/manifest.md#providers编号) | 装上就出现在供应商列表里，直接切到它的模型 |
| 总线上的名字 | [`[export]`](https://github.com/miyu-agent/miyu/blob/main/docs/authors/manifest.md#export) | 别的包经总线照名字（例如 `stt`）调你的方法 |
| 给别的包带内容 | [`[content.<包的编号>]`](https://github.com/miyu-agent/miyu/blob/main/docs/authors/manifest.md#content包的编号) | 给另一个包带一个目录的内容，例如表情包的内容包 |
| 终端、网页上的一块 | [`[[widget]]`](https://github.com/miyu-agent/miyu/blob/main/docs/authors/manifest.md#widget) | 扩展往终端、网页上放自己的一块内容 |
| 吉祥物 | [`[mascot]`](https://github.com/miyu-agent/miyu/blob/main/docs/authors/manifest.md#mascot) | 终端首页的吉祥物，做成一个包 |
| 外观 | [`[theme.tui]`、`[theme.web]`](https://github.com/miyu-agent/miyu/blob/main/docs/authors/manifest.md#theme) | 终端主题、网页主题；外观包只带这一样 |

工具、技能的说明（`Description`、`description`）是给模型看的，每一轮跟着请求发：写英文短句，一件工具最多三句。给人看的名字、说明另有地方写（`显示名称`、`描述`、`display_name_zh`、`summary_zh`）。

每一样怎么写：[作者文档](https://github.com/miyu-agent/miyu/tree/main/docs/authors)，其中 [放文件就能用的](https://github.com/miyu-agent/miyu/blob/main/docs/authors/scripts-skills.md)（脚本、技能、命令模板、知识库、人格）、[清单](https://github.com/miyu-agent/miyu/blob/main/docs/authors/manifest.md)、[接 MCP 服务](https://github.com/miyu-agent/miyu/blob/main/docs/authors/mcp.md)、[写扩展](https://github.com/miyu-agent/miyu/blob/main/docs/authors/extensions.md)。

### 4. 本地试

下面的 `<编号>` 换成你的编号，在仓库根目录跑。先在一份单独的数据里试，不碰自己平常用的 Miyu：命令前面加上 `MIYU_HOME=/tmp/miyu-try`（bash、zsh、fish 都认；PowerShell 先 `$env:MIYU_HOME = "$env:TEMP\miyu-try"`）。

```sh
MIYU_HOME=/tmp/miyu-try miyu pkg info ./<编号>  # 照装的那一套查清单，列出带了什么，什么都不装；写错的说第几行
miyu pkg pack ./<编号> -o dist                  # 打成 dist/<编号>-<版本>.miyu，印 SHA-256 和大小（不连核心）
MIYU_HOME=/tmp/miyu-try miyu pkg install ./dist/<编号>-0.1.0.miyu
MIYU_HOME=/tmp/miyu-try miyu pkg info <编号>    # 名称、版本、提供了什么、许可证
MIYU_HOME=/tmp/miyu-try miyu pkg list           # 装了哪些
MIYU_HOME=/tmp/miyu-try miyu check              # 脚本、技能写错的在这里说为什么跳过
MIYU_HOME=/tmp/miyu-try miyu kb list            # 带了知识库的：写着「来自 <包名>」，miyu kb search <词> 试搜
MIYU_HOME=/tmp/miyu-try miyu core stop          # 试完停掉这一份的核心，再删 /tmp/miyu-try
```

- 脚本第一行写了 `#!`（像模板里的例子）就不用 `chmod +x`：Miyu 起的是解释器，脚本文件当参数交给它。没写 `#!` 的脚本，Linux、macOS 上要 `chmod +x`，git 会记住它。
- 改了再装一次就是升级。技能装上以后，在 `miyu` 的输入框敲 `$` 能看到；脚本工具在设置的预设里能看到、能开关。
- 打包不打进去的：`.git`、`.github`、`__pycache__`、`.DS_Store`、`*.pyc`。别的都进，不想打进去的别放在包文件夹里。

### 5. 发版

1. 清单的 `version` 照 semver 加一次（`0.1.0` → `0.1.1`）：软件源只认版本，同一个版本重发不算更新。
2. 提交、推上去，再打标签：标签是 `v` 加上 `version`。

   ```sh
   git tag v0.1.0
   git push origin v0.1.0
   ```

3. `release.yml` 调官方的打包模板（[miyu-agent/packages](https://github.com/miyu-agent/packages)），照 Miyu 装包的那一套查清单、打成 `.miyu`、传进这个标签的 Release。标签和 `version` 对不上的当场报错。
4. 想先试打不发版：在仓库的 Actions 页手动跑 release，打出来的包在这一趟的产物里。

### 6. 进社区收录

给仓库加上话题（topic）`miyu-package`（仓库首页右边 About 的齿轮里）。软件源每天收一次（UTC 03:17 前后），每个仓库只看最新的那个正式 Release（草稿、预发布的不算），收里面的 `.miyu`，标「社区」：发了以后最多等一天。

- 编号先到先得：第一个收录了这个编号的仓库一直占着它，别的仓库再用这个编号的不收。改名就是换一个新编号。
- 查收没收进来：`miyu pkg update`，再 `miyu pkg search <编号>`。没有的，看 [软件源仓库](https://github.com/miyu-agent/packages) Actions 里最近一趟 collect 的摘要，每个没收的仓库一行原因。
- 分叉出来的、存档了的仓库不收；Release 里有一个 `.miyu` 读不成的，这个仓库这一趟整个不收。

## 常见报错

| 看到的 | 怎么办 |
|---|---|
| 打出来的包叫 `my-package-…` 或别的名字 | 文件夹名就是编号：改包文件夹的名字 |
| 无法打包：清单没有写版本 | `[package]` 里写 `version = "0.1.0"` |
| `package.license is not a known key` | 正在跑的 Miyu 比 `license` 这一格旧：更新 Miyu，或者删掉清单里 `license` 那一行 |
| Actions 里 `tag … does not match version …` | 标签去掉 `v` 要和清单的 `version` 一样 |
| `package_conflict` | 工具、技能、知识库的名字和装着的别的包撞了：改名再装 |
| 脚本、技能没出现 | `miyu check` 说哪一个、为什么跳过 |

别的报错见作者文档的 [常见报错](https://github.com/miyu-agent/miyu/blob/main/docs/authors/README.md#常见报错)。

## 许可证

`LICENSE` 是给你的包用的 MIT 模板：把版权人改成你自己，或者换成你要的许可证，清单的 `license` 跟着改。

这个模板仓库自己的文字和例子以 [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.zh-hans) 放弃版权：照抄、改、发都不用署名，也不用保留这一段。
