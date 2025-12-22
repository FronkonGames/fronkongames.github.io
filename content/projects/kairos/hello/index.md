---
author: Martin Bustos
title: Hello Everybody! 🧟
showTitle: true
date: 0
description: This is a devblog about a game of cards and zombies
tags: ["devblog", "gamedev", "game development"]
giscus: true
showImage: true
metadata: none
thumbnail:
  url: img/kairos/kairos_hello.jpg
  ratio: "4x3"
---

## Hello Everybody! 🧟 {#hello_everybody}

Hi I'm **Martin Bustos** and I've been developing games for more than two decades for PC, consoles, online, etc (you can check the list in my [GitHub](https://github.com/FronkonGames) profile). I've worked in several videogame companies and even co-founded two of them.

I recently decided to leave the corporate environment and dedicate myself to making games that I feel like making and playing! Here I will be recording the progress of my first game as an indie developer: '**Kairos**' (_codename_).

The game engine will be [Unity](https://unity.com/) and I will build a modular framework to use it in future projects. This framework, which I've called '**Game:Work**', is available on my [GitHub](https://github.com/FronkonGames) under [MIT License](https://github.com/FronkonGames/GameWork-Core/blob/main/LICENSE.md).

{{< image src="img/kairos/gamework_logo.png" wrapper="col-8 mx-auto">}}

The pilars of '**Game:Work**' is formed by two parts, the first '[Foundation](https://github.com/FronkonGames/GameWork-Foundation)' is a set of utilities and code extensions useful for game development. It has no architecture, so it can be used on any project. All its functions are supported by [Unit Tests](https://docs.unity3d.com/Manual/testing-editortestsrunner.html).

On top of this is '[Core](https://github.com/FronkonGames/GameWork-Core)' which is where the architecture of '**Game:Work**' is implemented, building on modularity, events and dependency injection.

With modules you can add functionality to '**Game:Work**'. Some of the ones I am developing are:

* [Scene](https://github.com/FronkonGames/GameWork-Scene): async scene loading.
* [Local Data](https://github.com/FronkonGames/GameWork-Local-Data): async load / save local data with compression, encryption and integrity check.
* [Tween](https://github.com/FronkonGames/GameWork-Tween): tween / easing.

A big part of the project I hope to separate it into modules and those that are useful for further development I will publish them with the same framework license.

Until next time... {{< badge title="stay gamedev, stay awesome!" >}}
{.h4}
