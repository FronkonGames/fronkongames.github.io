---
title: "Introduction to Go"
description: "The oldest board game still played today"
date: 2022-28-01
image: blog/go-weiqi-igo-baduk/banner.jpg
featured: blog/go-weiqi-igo-baduk/featured.jpg
type: "blog"
---

[Go](https://en.wikipedia.org/wiki/Go_(game)) is a very old strategy game that consists of capturing pieces and winning territories. It is about 2,500 years old and was invented in China, although the exact location is unknown.

## What is Go?

{{< image src="go-weiqi-igo-baduk/sato.jpg" alt="" align="right">}}

It is very popular in China, Japan, and Korea (known as __weiqi__, __igo__, and __baduk__ respectively). So popular that it is taught in schools, it has its own TV channels and even has its own [anime](https://en.wikipedia.org/wiki/Hikaru_no_Go).

Although little known in the West, it is the most played board game in the world (ahead of chess). Only in Japan 10 million people practice it, and I don't want to imagine how many millions in China.

{{< rawhtml >}}<br><br>{{< /rawhtml >}}

## Introduction

__Go__ perfectly fulfills the maxim of the founder of [Atari](https://en.wikipedia.org/wiki/Atari), [Nolan Bushnell](https://en.wikipedia.org/wiki/Nolan_Bushnell), on the games:

> '...the best games are those easy to learn and difficult to master.'

__Bushnell__ is a big fan of this game, so much so that the name of his company, '__Atari__', is a term used in __Go__.

__Go__ is played on a board like this:

{{< imagecenter src="go-weiqi-igo-baduk/go_board.png" alt="Go board" >}}

Its rules are very simple and have hardly changed since it was invented:

- Both players (one with white stones and the other with black stones) play in turns, putting a single stone on the board each time (it starts empty).
- The stones must be placed on the intersection between the vertical lines and the horizontal lines, including the edges.
- Once a stone is placed, it cannot be withdrawn unless it loses all its __liberties__.

It is so easy to learn that the recommended age to start playing is only 5 years old. It is also proven that it is a very healthy mental exercise. There are [studies](https://www.nejm.org/doi/full/10.1056/NEJMoa022252) on its positive effects against senile dementia and Alzheimer's in adults. At an early age its benefits in the development of intelligence and concentration are demonstrated.

But it is so complex that it was not until 2016 that an AI managed to beat a great master (something that happened in chess 20 years earlier). If you are interested in learning more about this topic, I recommend you watch the great documentary '[AlphaGo - The Movie](https://www.youtube.com/watch?v=WXuK6gekU1Y)'.

I finish this brief introduction with an old tale that illustrates very well what it is to play __Go__ and tells how...

{{< image src="go-weiqi-igo-baduk/devil11.jpg" alt="" align="right">}}

> the young and robust Chih ventured into the mountains to find the best wood for his ax. He went so deep into the forest that he ended up getting lost.
> 
> He wander for some time and end up discovering two strange men, very old, who were playing Go. Chih was fascinated. He put his ax aside and began to look closely. So much he got into the game that he lost track of time.
>
> When he woke up from the deep trance, he realized that the elders had disappeared. Picking up his ax, the handle fell apart in his hands. He had grown a long white beard. Upon returning to his village his family had disappeared and no one remembered his name ...

{{< rawhtml >}}<br><br>{{< /rawhtml >}}

## Basic rules

The official board is 19×19 positions (between 20 and 40 minutes of play), although beginners usually use boards smaller like 13×13 (between about 15 minutes of play) or 9×9 (no more than 10 minutes). To teach you the basic rules I will use a 5×5 board like this:

{{< imagecenter src="go-weiqi-igo-baduk/board.png" alt="Go board" >}}

The stones will be placed in turns, at the intersections of the black lines (including the edges). Black usually starts, so a first move could be **B4**:

{{< imagecenter src="go-weiqi-igo-baduk/board01.png" alt="Go board" >}}

We already have our first __group__ done, although for now it only has one stone. Now it would be White's turn and they could move, for example in **D2** and the board would look like this:

{{< imagecenter src="go-weiqi-igo-baduk/board02.png" alt="Go board" >}}

A __group__ are stones of the same color that are joined at the top, bottom, left, or right. **Never** diagonally. Let's see a board with only black stones and count the groups we have:

{{< imagecenter src="go-weiqi-igo-baduk/board03.png" alt="Go board" >}}

We can count three different groups. Note that the stones in **C4** and **D3** **do not touch**, they belong to two different groups. There is never diagonal contact.

I said at the beginning that one of the rules is that you cannot remove a token (or group) unless they lose their __liberties__. The __liberty__ of a group is the number of free spaces around it. Consider these examples:

{{< rawhtml >}}<br>{{< /rawhtml >}}

|     |     |     |     |
| :-: | :-: | :-: | :-: |
| {{< imagecenter src="go-weiqi-igo-baduk/board04.png" >}} | {{< imagecenter src="go-weiqi-igo-baduk/board05.png" >}} | {{< imagecenter src="go-weiqi-igo-baduk/board06.png" >}} | {{< imagecenter src="go-weiqi-igo-baduk/board07.png" >}} |
|  **A**  |  **B**  |  **C**  |  **D**  |

{{< rawhtml >}}<br><br>{{< /rawhtml >}}

On the board **A**, we have a group consisting of a single stone. All of your neighbors are empty (red squares), so we have **four liberties**. In **B** we only have two neighbors and they are empty, so we have **two liberties**.

On the board **C** we already have a group of more than one token, and logically we have more __liberties__, we have **eight**. In **D** we see how White has taken away **two liberties**, so that group only has **five liberties**.

What happens to groups with only one __liberty__? These groups are said to be in '__Atari__', in danger. Let's see an example:

{{< imagecenter src="go-weiqi-igo-baduk/board08.png" alt="Go board" >}}

This group of stones only has **one liberty**, its survival is in danger. As I said at the beginning, a group without liberties is withdrawn, or captured, by the enemy. If it was White's turn now, the logical move would be to move on **B3**, which is the only liberty left for that group of Black:

{{< imagecenter src="go-weiqi-igo-baduk/board09.png" alt="Go board" >}}

Running out of __liberties__, White removes those stones earning one point for each stone captured. The board would look like this:

{{< imagecenter src="go-weiqi-igo-baduk/board10.png" alt="Go board" >}}

In case you're wondering, suicide is not allowed in Go. I mean, you can't put a stone that takes away the liberties of a group (and give them points to the enemy). You will see it clearly with the following example:

{{< imagecenter src="go-weiqi-igo-baduk/board11.png" alt="Go board" >}}

If you could put a black stone on **B1**, you would form a group without liberties, which would be a kind of suicide. In this example, if it is Black's turn, **B1** is a **forbidden move**.

There is another **forbidden movement**, the '__Ko__'. It is used to prevent two players from repeating identical plays over and over again without stopping, something that would not make much sense either. Let's see a very simple example with these boards:

{{< rawhtml >}}<center><br>{{< /rawhtml >}}

|     |     |     |
| :-: | :-: | :-: |
| {{< imagecenter src="go-weiqi-igo-baduk/board12.png" >}} | {{< imagecenter src="go-weiqi-igo-baduk/board13.png" >}} | {{< imagecenter src="go-weiqi-igo-baduk/board12.png" >}} |
|  **A**  |  **B**  |  **C**  |

{{< rawhtml >}}</center><br><br>{{< /rawhtml >}}

If White's turn start on the board **A**, they could remove the black stone at **D3** since he only has one liberty at **C3** (so he is at __Atari__). That brings us to the board **B** and the turn goes to Black. Thinking of avenging their stone, they will want to eliminate the white token at **C3**, which is now at __Atari__. This brings us to the **C** board.

Board **C** is the same as board **A**, so this loop could be repeated forever (Ko or 劫 means eternal in Japanese). Basically, the '__Ko__' rule tells us that we cannot make a move that recreates a board as in the previous move. In the example above:

{{< rawhtml >}}<center><br>{{< /rawhtml >}}

|     |     |     |
| :-: | :-: | :-: |
| {{< imagecenter src="go-weiqi-igo-baduk/board12.png" >}} | {{< imagecenter src="go-weiqi-igo-baduk/board13.png" >}} | {{< imagecenter src="go-weiqi-igo-baduk/board14.png" >}} |
|  **A**  |  **B**  |  **C**  |

{{< rawhtml >}}</center><br><br>{{< /rawhtml >}}

Black, on the board **C**, could put anywhere, except for **D3**, which would cause a '__Ko__'. On the next move, it could be used again.

These are the basic rules, it only remains to know when a game ends and how to know who wins.

A game ends when **both players decide to pass their turn**. A player may do so at any time during the game. Do not put any stone and pass the turn to your opponent. Normally only a turn is passed when a player considers that it is not worth putting more stones on the board. And it is that, as we will see shortly, when you think you have all your safe territories, putting superfluous stones takes away points.

When both players pass, the game is over and it's time to count points. Let's see a finished board and how we would count the points of both players to know who is the winner:

{{< rawhtml >}}<br>{{< /rawhtml >}}

{{< imagecenter src="go-weiqi-igo-baduk/board15.png" alt="Go board" >}}

As I said at the beginning, the purpose of this game is to have more territory and capture stones from your opponent. Suppose the black player has captured **6 white stones** and the white player has another **6 black stones** as well. Let's count how much land each player has totally encompassed:

{{< rawhtml >}}<center><br>{{< /rawhtml >}}

|     |     |
| :-: | :-: |
| {{< imagecenter src="go-weiqi-igo-baduk/board17.png" >}} | {{< imagecenter src="go-weiqi-igo-baduk/board19.png" >}} |
|  **Black: 7 points**  |  **White: 5 points**  |

{{< rawhtml >}}</center><br><br>{{< /rawhtml >}}

Black would add **6 points** for captured stones and **7 points** for territory won, in total **13 points**. Note that **D3** does not count as won territory for anyone because it is not **fully encompassed** by stones of one color.

White adds **6 points** for captured pieces and **5 for territory**, in total **11 points**. Black has won the game because they have conquered more territory than white.

Can a tie occur? The points of both players could be identical and to solve this (and another problem) the '__Komi__' was created. This is one of the few variations that the original game rules have suffered since it was invented.

Back in 1930, the great masters of the time realized that there was an advantage to moving first (traditionally black). To fix it, they gave White an initial score to make up for that disadvantage, the '__Komi__'. Its value has varied greatly over time. In current tournaments it is set between **5.5** and **6.5**. In __amateur__ games, where players don't know how to take advantage of that advantage, **0.5** is usually used.

Why are decimals used? Because by the way, thanks to '__Komi__' games can never end in a draw. In the case of the example, a '__Komi__' of **0.5** should be added to White's score. The end result would be black **13 points**, white **11.5 points**, so black would continue to win.

{{< rawhtml >}}<br>{{< /rawhtml >}}

## Lets play!

You already know the basics of Go and **you can start playing**! If you play online, you will be interested to know that there is a way to know how good a player is. Each player has a rank according to the games he wins. When you start you don't have any rank (normally it will tell you that you have a rank '__?__'). Until you play your first rated game (on 19×19 boards) you will not be assigned one.

Amateur players usually start with __30 kyu__ (Japanese system). The better you are, the less __kyu__ you will have. When you have __1 kyu__ you can go to the next category and be __1 dan__. Here are the best players. The better you play, the more you will have. It usually goes from __1 dan__ to __9 dan__. The winning teacher of the most prestigious Go tournament, is usually called __Judan__, which means __10 dan__.

To play online the best __IMHO__ site is [online-go](https://online-go.com).

{{< rawhtml >}}<br><br>{{< /rawhtml >}}
