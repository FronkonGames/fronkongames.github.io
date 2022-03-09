---
title: "Sprites Mojo"
date: 2022-02-23T12:23:10+06:00
image: /store/store-todo.jpg
description: "A collection of 2D effects to add more juice to your games."
type: "store"
---

{{< rawhtml >}}
<!--
    <div align="right">
      <a href="https://nephasto-git.gitlab.io/work/unity-store/sprite-fx" class="button">🕹️ Demo</a>&nbsp;
      <a href="https://assetstore.unity.com/packages/slug/213504?aid=1101l9zFC&utm_source=aff" class="button">🛒 Store</a>
    </div>
-->
<br>
{{< /rawhtml >}}

## Editor

From the editor you can create '__Sprites Mojo__' effects in two different ways: creating sprites and creating materials.

To create a sprite that uses one of the '__Sprites Mojo__' effects, right click on the '_Hierarchy_' window and select an effect from the list that will appear under '_2D Object > Sprites Mojo_'.

{{< imagecenter src="sprite-fx/editor_0.jpg" >}}

This will create an empty sprite with a '__Sprites Mojo__' material. When you assign a sprite (__1__) you will see the effect. '__Sprites Mojo__' is material based, so you will have to display its material (__2__) to see its parameters.

{{< imagecenter src="sprite-fx/editor_1.jpg" >}}

All effects have a layout similar to the example above. A first part (__3__) with the effect parameters. Another part that you can activate to adjust the color (__4__) and another part where you can adjust sprite values (__5__).

Finally, by clicking on '[doc]' (__6__) you can access the online documentation and by clicking on the '_Reset_' button (__7__) you will set all the parameters to their original values.

This is the easiest way to create sprites using '__Sprites Mojo__', but you must keep in mind that it will create a new material for each sprite you create. If your sprites do not share textures between them, no problem. If your sprites share the same texture, the second way is more optimal: creating materials.

To create a material that uses a '__Sprites Mojo__' effect, just right click on the '_Project_' window and select one of the '_Create > Fronkon Games > Sprite FX_' effects. Once the material is created, you only have to assign it to the sprites you want to use it.

{{< imagecenter src="sprite-fx/editor.gif" >}}

## Effects

<br><br>

### Black and White

Desaturates the image by selecting the intensity for each color channel, the amount of light and the smoothness of the color change.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/blackandwhite.jpg" >}} | {{< video src="sprite-fx/BlackAndWhite.mp4">}} |

### Black Hole

Create a '_black hole_' inside the sprite. Use the alpha channel of '_Color_' to modify the transparency of the effect.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/blackhole.jpg" >}} | {{< video src="sprite-fx/BlackHole.mp4">}} |

{{% notice info %}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'. This effect does not support [Sprite Atlas](https://docs.unity3d.com/Manual/class-SpriteAtlas.html).
{{% /notice %}}

### Blend

Use some of Photoshop's 25 blending modes.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/blend.jpg" >}} | {{< video src="sprite-fx/Blend.mp4">}} |

{{% notice info %}}
Since URP does not support '[Grab Pass](https://docs.unity3d.com/Manual/SL-GrabPass.html)' at the moment, this effect is only available for the Built-in Render Pipeline.
{{% /notice %}}

### Dissolve

'_Dissolve_' the sprite using a gradient texture as a pattern. Change the mode to '_Color_' to make a border appear with the color of your choice, or use '_Texture_' to make it a texture.

This effect has a large list of built-in patterns you can use, but if you want to use your own, select '_Custom_' under '_Shape_'. This way you can specify the texture you want to use.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/dissolve.jpg" >}} | {{< video src="sprite-fx/Dissolve.mp4">}} |

{{% notice info %}}
This effect does not support [Sprite Atlas](https://docs.unity3d.com/Manual/class-SpriteAtlas.html).
{{% /notice %}}

### Dither

Applies various algorithms to reduce the amount of colors. It also pixelizes the sprite.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/dither.jpg" >}} | {{< video src="sprite-fx/Dither.mp4">}} |

### Duo Tone

It uses a two-color gradient based on the sprite's luminance. To adjust the brightness ranges it uses, you can press the '_Auto_' button or adjust it manually in 'Luminance'.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/duotone.jpg" >}} | {{< video src="sprite-fx/DuoTone.mp4">}} |

### Edge

Highlight sprite edges using different modes and algorithms.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/edge.jpg" >}} | {{< video src="sprite-fx/Edge.mp4">}} |

### Glass

Simulates a glass material, deforming the background.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/glass.jpg" >}} | {{< video src="sprite-fx/Glass.mp4">}} |

{{% notice info %}}
Since URP does not support '[Grab Pass](https://docs.unity3d.com/Manual/SL-GrabPass.html)' at the moment, this effect is only available for the Built-in Render Pipeline.
{{% /notice %}}

### Hologram

It simulates a hologram or projection.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/hologram.jpg" >}} | {{< video src="sprite-fx/Hologram.mp4">}} |

### Instagram

Apply one of the 15 most used filters on Instagram.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/instagram.jpg" >}} | {{< video src="sprite-fx/Instagram.mp4">}} |

### Masks

Applies blending effects, colors and textures to areas of a sprite defined by a mask. The mask is a texture in which you can define up to 3 zones, one for each color channel.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/masks.jpg" >}} | {{< video src="sprite-fx/Masks.mp4">}} |

{{% notice info %}}
This effect does not support [Sprite Atlas](https://docs.unity3d.com/Manual/class-SpriteAtlas.html).
{{% /notice %}}

### Negative

Change each color by its opposite. You can define how each color channel is affected.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/negative.jpg" >}} | {{< video src="sprite-fx/Negative.mp4">}} |

### Outline

Creates a border around the sprite outline.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/outline.jpg" >}} | {{< video src="sprite-fx/Outline.mp4">}} |

### Pinch

Clamp the sprite in a certain area.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/pinch.jpg" >}} | {{< video src="sprite-fx/Pinch.mp4">}} |

{{% notice info %}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{% /notice %}}

### Ramp

Replaces the sprite colors with a gradient of 5 colors based on luminance. To adjust the luminance ranges it uses, you can click the 'Auto' button or adjust it manually in 'Luminance'.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/ramp.jpg" >}} | {{< video src="sprite-fx/Ramp.mp4">}} |

To easily find a gradient, click on '__search__' (__1__), to open the gradient search tool (internet connection required), or click on '__random__' (__2__) to get a random one.

{{< imagecenter src="sprite-fx/ramptool.jpg" >}}

Clicking on '__sort__' (__3__) will sort the gradient colors from the darkest (in '_Color 1_') to the brightest (in '_Color 5_'). You can also '__copy__' '__paste__' (__4__) between sprites with the '__Ramp__' effect.

### Retro

Emulates old devices such as: Gameboy, Commodore 64, ZX Spectrum, etc.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/retro.jpg" >}} | {{< video src="sprite-fx/Retro.mp4">}} |

### RGB Glitch

Simulates a failure in the RGB color channels.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/rgbglitch.jpg" >}} | {{< video src="sprite-fx/RGBGlitch.mp4">}} |

{{% notice info %}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{% /notice %}}

### Shake

Shake the sprite.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/shake.jpg" >}} | {{< video src="sprite-fx/Shake.mp4">}} |

{{% notice info %}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{% /notice %}}

### Shift

Shitfs the RGB color channels linearly or radially. Enable '__Noise__' to add noise to the scroll.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/shift.jpg" >}} | {{< video src="sprite-fx/Shift.mp4">}} |

{{% notice info %}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{% /notice %}}

### Swirl

Twist a certain area of the sprite.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/swirl.jpg" >}} | {{< video src="sprite-fx/Swirl.mp4">}} |

{{% notice info %}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'. This effect does not support [Sprite Atlas](https://docs.unity3d.com/Manual/class-SpriteAtlas.html).
{{% /notice %}}

### Tremor

Causes tremors in the sprite.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/tremor.jpg" >}} | {{< video src="sprite-fx/Tremor.mp4">}} |

{{% notice info %}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{% /notice %}}

### Trio Tone

It uses a three-color gradient based on the sprite's luminance. To adjust the luminance ranges it uses, you can click the '_Auto_' button or adjust it manually in 'Luminance'.

| | |
| -: | :- |
| {{< imagecenter src="sprite-fx/triotone.jpg" >}} | {{< video src="sprite-fx/TrioTone.mp4">}} |

<br>

## Code

All the code is inside the _namespace_ '__FronkonGames.SpritesMojo__'. The first thing to do is to import the _namespace_:

```cs {linenos=true}
 using FronkonGames.SpritesMojo;
```
&nbsp;

You can create sprites that use the effects of '__Sprites Mojo__' as follows (in this example '__Retro__'):

```cs {linenos=true}
 GameObject gameObject = Retro.CreateSprite();
```
&nbsp;

Remember that each sprite will have a new material. If you want several sprites to use the same material with an effect, you can create it that way and then assign it to the sprites you want:

```cs {linenos=true}
 Material material = Retro.CreateMaterial();
```
&nbsp;

Each effect has those two functions (_CreateSprite()_ and _CreateMaterial()_) to create its own sprites and materials. You can find them all in the '_Fronkon Games/SpriteFX/Runtime/FX_' folder.

Continuing with the previous example, if you wanted to modify or query any parameter of the '__Retro__' effect, you can do it like this:

```cs {linenos=true}
 SpriteRenderer sprite = gameObject.GetComponent<SpriteRenderer>();

 // Changes the sprite emulation mode.
 Retro.Mode.Set(sprite, Retro.Emulations.Gameboy);
 
 // Check pixelation.
 int pixelation = Retro.Pixelation.Get(sprite);

 // You can also do it with the material.
 Retro.Mode.Set(material, Retro.Emulations.Gameboy);
 float luminance = Retro.Luminance.Get(material);
```
&nbsp;

In addition, all effects have some common parameters that you can access through the '_SpritesMojo_' class that you can find in '_Fronkon Games/Sprites Mojo/Runtime_'. For example, let's enable '_ColorAdjust_' if it is disabled and modify some of its parameters:

```cs {linenos=true}
  if (SpriteFX.ColorAdjust.Get(sprite) == false)
  {
    SpriteFX.ColorAdjust.Set(sprite, true);

    SpriteFX.Gamma.Set(sprite, 1.2f);
    SpriteFX.Hue.Set(sprite, 0.25f);
  }
```
&nbsp;

All effect variables of type _IntVariable_, _FloatVariable_, _ColorVariable_ and _VectorVariable_ can be set to a value and you can specify how long (in seconds) you want the transition to last from the current value to the one you have set. For example, if you want to transition to a pixel size of 8 in 2 seconds:

```cs {linenos=true}--
  Retro.Pixelation.Set(sprite, 8, 2.0f);
```
&nbsp;

Check the class comments for more information.
