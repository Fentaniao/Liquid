# Liquid Theme的开发文档

## 目录结构

### Release

```bash
│  liquid-dark.css
│  liquid-ink-dark.css
│  liquid-ink.css
│  liquid.css
│  Demo.md
│  Document.md
│
└─liquid # 使用到的字体文件
```

### 源代码

```bash
├─.github
│  └─workflows
├─dist # 组装好的CSS文件
├─font # 所有的字体文件
├─media # picture of Liquid Theme
└─src # 有多么
   ├─Deploy # 用于构建发布的Python脚本
   └─liquid # CSS组件
```



## 用法

### 添加自定义CSS（推荐）

这是最简单的方法。

查看https://support.typora.io/Add-Custom-CSS/以了解如何使用。

### 修改发布的CSS文件

首先将Liquid Theme安装到PC上，然后直接修改Liquid Theme的`xxxxx.css`文件.

### 修改项目的源代码

从[Releases](https://github.com/Fentaniao/Liquid/releases)页面下载`Source code (zip)`，然后修改`scr`目录下的CSS文件。
