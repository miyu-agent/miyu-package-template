<p align="center">
  <a href="README.md">English</a> | 简体中文
</p>

# Miyu 软件包模板

> <sub>本文档由 Anthropic 的 Claude Fable 5.2 生成。</sub>

这是一个用来编写 [Miyu](https://github.com/miyu-agent/miyu) 软件包的模板仓库。清单、发布用的工作流、许可证和例子都已经准备好，在 GitHub 上点击 `Use this template` 按钮，就可以开始编写你的软件包。

## 仓库里有什么

模板仓库的目录结构如下：

```text
├── my-package/                 # 软件包本身：文件夹名就是软件包的编号，改成你的编号
│   ├── package.toml            # 清单
│   └── scripts/
│       └── my-package-hello.py # 一个脚本，安装以后就是一个工具
├── examples/                   # 可以复制过去使用的例子，不发布
│   ├── meeting-notes/          # 技能包：skills/meeting-notes/SKILL.md
│   └── lighthouse/             # 知识库包：kb/lighthouse/kb.toml 和两篇文档
├── .github/workflows/release.yml  # 推送 v* 标签时打包，并上传到发行版
├── LICENSE                     # MIT 许可证，把版权人改成你自己
└── .gitignore
```

## 使用方法

从建立仓库到被软件源收录，一共分为下面六步。

### 1. 建立仓库

在这个仓库的页面上点击 `Use this template → Create a new repository`。仓库名可以随意取，常见的写法是 `miyu-<编号>`。用模板建立的仓库不是分叉（fork），所以软件源会正常收录（分叉出来的仓库不会被收录）。

### 2. 取编号，替换占位

**编号**是软件包在软件源里的名字，安装时输入的就是它（`miyu pkg install <编号>`）。编号以小写字母开头，只能使用小写字母、数字、`-` 和 `_`，最多 64 个字符。请取一个简短、能说明软件包用途的名字：不需要带 `miyu-`，也不需要带软件包的种类（`scripts-`、`skills-` 这类前缀），不要用 `base-` 开头（这个前缀留给随 Miyu 一起提供的软件包）。软件源里的编号先到先得，所以取名之前先运行 `miyu pkg search <词>`，确认这个编号还没有被占用。

需要修改的地方如下（在整个仓库里搜索 `my-package` 就能全部找到）：

1. 把文件夹 `my-package/` 改成你的编号：`git mv my-package <编号>`。**文件夹名就是编号**，本地打包和安装都以文件夹名为准。
2. `.github/workflows/release.yml` 里的 `package:` 和 `folder:` 两处都要写成你的编号。
3. `<编号>/package.toml` 里的 `name`、`summary`、`author`、`upstream`、`license`。
4. 脚本 `scripts/my-package-hello.py`：工具名取自文件名，所以文件名要带上编号作为前缀，以免和其他软件包重名；如果不需要这个例子，就把它删掉。
5. `LICENSE` 里的版权人。如果换用其他许可证，清单里的 `license` 也要跟着修改（按 [SPDX](https://spdx.org/licenses/) 的写法填写，例如 `MIT`、`Apache-2.0`、`CC-BY-SA-4.0`）。

### 3. 编写内容

一个软件包可以带下面这几类内容，也可以混合带上几类。其中放入文件就能使用的几类，按约定放在软件包文件夹里即可，不需要写进清单：

| 想做的事 | 放什么 | 例子 |
|---|---|---|
| 给 AI 一个小工具 | `scripts/<名字>.py`（或者其他可执行文件） | `my-package/scripts/` |
| 教 AI 一套做事的方法 | `skills/<名字>/SKILL.md` | `examples/meeting-notes/` |
| 一套供 AI 查阅的资料 | `kb/<编号>/`：`kb.toml` 和文档 | `examples/lighthouse/` |
| 一条斜杠命令 | `commands/<名字>.md` | 见作者文档 |
| 人格、预设 | `personas/<编号>/`、`presets/<编号>.toml` | 见作者文档 |
| 接入 MCP 服务、常驻的扩展程序、后台页 | 在清单里写 `[[mcp]]`、`[process]`、`[page]` | 见作者文档 |
| 让人在设置页里填写的几项设置 | 在清单里写 `[settings.<名字>]`；脚本从环境变量 `MIYU_SETTINGS_JSON` 读取 | 见作者文档 |
| 一家模型供应商 | 在清单里写 `[providers.<编号>]` | 见作者文档 |
| 外观、终端界面首页的吉祥物 | 在清单里写 `[theme]`、`[mascot]` | 见作者文档 |
| 供其他软件包调用的方法、带给其他软件包的内容 | 在清单里写 `[export]`、`[content.<包的编号>]` | 见作者文档 |

使用例子的方法：把例子里的 `skills/`、`kb/` 复制到你的软件包文件夹里；如果要整个照搬一个例子，就把例子文件夹复制到仓库根目录，改名成你的编号，再修改 `release.yml`。

工具和技能的说明（`Description`、`description`）是写给模型看的内容，每一轮都会随请求一起发送，所以要写成英文短句，一个工具最多三句。给人看的名字和说明写在另外的地方（`显示名称`、`描述`、`display_name_zh`、`summary_zh`）。

每一类内容的写法见[作者文档](https://github.com/miyu-agent/miyu/tree/main/docs/zh/dev)，其中包括[放入文件就能使用的内容](https://github.com/miyu-agent/miyu/blob/main/docs/zh/dev/scripts-skills.md)（脚本、技能、命令模板、知识库、人格）、[清单](https://github.com/miyu-agent/miyu/blob/main/docs/zh/dev/manifest.md)、[接入 MCP 服务](https://github.com/miyu-agent/miyu/blob/main/docs/zh/dev/mcp.md)和[编写扩展](https://github.com/miyu-agent/miyu/blob/main/docs/zh/dev/extensions.md)。

### 4. 在本地试用

把下面命令里的 `<编号>` 换成你的编号，然后在仓库根目录运行。先在一份单独的数据目录里试用，这样不会影响你平常使用的 Miyu：在命令前面加上 `MIYU_HOME=/tmp/miyu-try`（bash、zsh、fish 都支持这种写法；在 PowerShell 里，先运行 `$env:MIYU_HOME = "$env:TEMP\miyu-try"`）。

```sh
MIYU_HOME=/tmp/miyu-try miyu pkg info ./<编号>  # 按安装时的规则检查清单，列出带了哪些内容，不安装任何东西；写错时会指出第几行
miyu pkg pack ./<编号> -o dist                  # 打包成 dist/<编号>-<版本>.miyu，输出 SHA-256 和大小（不连接核心）
MIYU_HOME=/tmp/miyu-try miyu pkg install ./dist/<编号>-0.1.0.miyu
MIYU_HOME=/tmp/miyu-try miyu pkg info <编号>    # 名称、版本、提供了什么、许可证
MIYU_HOME=/tmp/miyu-try miyu pkg list           # 已经安装了哪些软件包
MIYU_HOME=/tmp/miyu-try miyu check              # 脚本、技能写错时，这里会说明跳过的原因
MIYU_HOME=/tmp/miyu-try miyu kb list            # 带了知识库时会显示「来自 <包名>」，可以用 miyu kb search <词> 试着搜索
MIYU_HOME=/tmp/miyu-try miyu core stop          # 试用完以后停止这一份数据的核心，再删除 /tmp/miyu-try
```

- 第一行写了 `#!` 的脚本不需要可执行权限。第一行没有写 `#!` 的脚本在 Linux、macOS 上需要可执行权限：运行 `chmod +x <编号>/scripts/<文件>`，Git 会记住这个权限。
- 修改以后再安装一次就是升级。技能安装以后，在 `miyu` 的输入框里输入 `$` 就能看到；脚本工具可以在设置的预设里看到，并且可以单独开关。
- 打包时不会打进去的文件有：`.git`、`.github`、`__pycache__`、`.DS_Store`、`*.pyc`。其他文件都会打进去，所以不想打进去的文件不要放在软件包文件夹里。

### 5. 发布

发布新版本的步骤如下：

1. 按语义化版本（semver）的规则把清单里的 `version` 加一（`0.1.0` → `0.1.1`）：软件源只看版本号，同一个版本重新发布不算更新。
2. 提交并推送，然后打标签：标签是 `v` 加上 `version`。

   ```sh
   git tag v0.1.0
   git push origin v0.1.0
   ```

3. `release.yml` 会调用官方的打包模板（[miyu-agent/packages](https://github.com/miyu-agent/packages)），按 Miyu 安装软件包时的规则检查清单，打包成 `.miyu`，并上传到这个标签的发行版。如果标签和 `version` 对不上，工作流会立即报错。
4. 如果想先试着打包而不发布：在仓库的 `Actions` 页面手动运行 `release`，打出来的软件包在这次运行的产物（artifacts）里。

### 6. 加入社区收录

给仓库加上话题（topic）`miyu-package`（在仓库首页右侧 `About` 旁边的齿轮里设置）。软件源每天收录一次（UTC 03:17 前后），每个仓库只看最新的那个正式发行版（草稿和预发布版不算），收录其中的 `.miyu` 文件，并标为“社区”：发布以后最多需要等待一天。

- 编号先到先得：第一个以这个编号被收录的仓库会一直占用这个编号，其他仓库再使用这个编号时不会被收录。改名就等于换一个新编号。
- 确认是否已经收录：先运行 `miyu pkg update`，再运行 `miyu pkg search <编号>`。如果搜不到，可以看[软件源仓库](https://github.com/miyu-agent/packages)的 `Actions` 里最近一次 `collect` 运行的摘要，每个没有被收录的仓库占一行，写明原因。
- 分叉出来的仓库和已经存档的仓库不会被收录；如果发行版里有一个 `.miyu` 文件无法读取，这一次就不会收录这个仓库的任何内容。

## 常见报错

下表列出常见的报错和解决方法：

| 看到的现象 | 解决方法 |
|---|---|
| 打出来的软件包叫 `my-package-…` 或者其他名字 | 文件夹名就是编号：修改软件包文件夹的名字 |
| 无法打包：清单没有写版本 | 在 `[package]` 里写上 `version = "0.1.0"` |
| `未知的键：package.license` | 正在运行的 Miyu 版本比 `license` 这一项旧：更新 Miyu，或者删掉清单里 `license` 那一行 |
| `Actions` 里出现 `tag … does not match version …` | 标签去掉 `v` 以后要和清单里的 `version` 相同 |
| `package_conflict` | 工具、技能、知识库的名字和已经安装的其他软件包重名：改名后再安装 |
| 脚本、技能没有出现 | 运行 `miyu check`，它会说明是哪一个、为什么被跳过 |

其他报错见作者文档里的[常见报错](https://github.com/miyu-agent/miyu/blob/main/docs/zh/dev/packages.md#常见报错)。

## 许可证

`LICENSE` 是给你的软件包使用的 MIT 许可证模板：把版权人改成你自己，或者换成你想用的许可证，清单里的 `license` 也要跟着修改。

这个模板仓库本身的文字和例子以 [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.zh-hans) 放弃版权：复制、修改、发布都不需要署名，也不需要保留这一段。
