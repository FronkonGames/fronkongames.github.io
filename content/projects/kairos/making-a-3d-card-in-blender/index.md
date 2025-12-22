---
author: Martin Bustos
title: Making A 3D Card In Blender 🃏
showTitle: true
date: 1
description: The first thing a card game needs is... cards
tags: ["devblog", "kairos"]
metadata: none
showImage: true
giscus: true
parent: kairos
thumbnail:
  url: img/kairos/kairos_3d_card.png
  ratio: "4x3"
---

The first thing a card game needs is... cards.

And why in 3D? It would be _easier_ to do it in 2D, but to have more options in terms of effects and also to differentiate from the rest I decided that my card game would be 3D.

I was going to need a 3D editor, and in my modest opinion [Blender](https://www.blender.org/) is unbeatable in quality / price.

{{< image src="blender.jpg" wrapper="col-10 mx-auto">}}

Once installed, in an empty scene, I added a plane using the menu '**Add > Mesh > Plane**'.
To make it easier to handle, I set the top camera by pressing '**7**' on the numeric pad.

{{< image src="plane.jpg" wrapper="col-10 mx-auto">}}

There is no standard size for a card. A Bridge card measures 57.15 x 88.9 mm, while a Poker card measures 62 x 88 mm. This size is known as [B8 in ISO 216](https://formaty.info/en/B8/). Since it is the best known, it is the size I will use.

{{< image src="b8.jpg" wrapper="col-6 mx-auto">}}

However, I am not really interested in the size itself, but in the ratio between width and height or _aspect ratio_. In the case case of a Poker card is **0.7** (62 / 88).

To achieve that _aspect ratio_, with the plane selected, press '**S**' and then '**X**', and typing '**0.7**' (62 / 88) will get the _aspect ratio_ I'm looking for.

{{< image src="plane_07.jpg" wrapper="col-8 mx-auto">}}

To round corners I use the '**Bevel**' modifier.

{{< image src="card_bevel.jpg" wrapper="col-8 mx-auto">}}

And to give it a little thickness the modifier '**Solidify**'.

{{< image src="card_solidify.jpg" wrapper="col-8 mx-auto">}}

Now I applied all the transformations pressing '**Ctrl+A**', so that the scale of the final geometry is 1.

{{< image src="transform.jpg" wrapper="col-8 mx-auto">}}

And the modifiers.

{{< image src="apply.jpg" wrapper="col-8 mx-auto">}}

It was time for the materials. But first I created some UV coordinates in the '**UV Editing**' tab and selecting a _cube projection_.

{{< image src="uv.jpg" wrapper="col-8 mx-auto">}}

As its name indicates, this tool creates the coordinates by projecting a cube on the model.

{{< image src="cube_uv.png" wrapper="col-10 mx-auto">}}

It may not be the best option for rounded edges, but it is the easiest one. You can adjust the coordinates by hand using the window on the left.

In the '**Shading**' tab, I created three materials: 'FrontFace', 'BackFace' and 'Border'. I selected the front face and the 'FrontFace
the 'FrontFace' material, and clicked the '**Assign**' button to associate them.

With '**CONTROL + 7**' I switched to the back view and performed a similar operation.

To assign the border material, select the two faces and invert the selection.

{{< image src="assign.jpg" wrapper="col-8 mx-auto">}}

Now it was only left to export to FBX to the Unity project.

The only change I made in the export options was in '**Apply Scalings**', which I set to '**FBX Units Scale**' so that in Unity would export the scale correctly.

{{< image src="export.jpg" wrapper="col-6 mx-auto">}}


Until next time... {{< badge title="stay gamedev, stay awesome!" >}}
{.h4}

{{< icon fas download >}}[Blender scene](card.blend)
{.h4}