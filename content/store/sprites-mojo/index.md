---
author: Martin Bustos
title: Sprites Mojo
showTitle: false
date: 6
description: A collection of 2D effects to add more juice to your games
tags: ["unity", "store", "2D", "sprites"]
metadata: none
showImage: false
thumbnail:
  url: img/sprites-mojo.jpg
---

{{< asset-header youtube="4eyGdIvJxko" store="https://assetstore.unity.com/packages/vfx/shaders/sprites-mojo-214468" demo="https://fronkongames.github.io/demos-artistic/sprites-mojo/" >}}

## Editor

From the editor you can create '**Sprites Mojo**' effects in two different ways: creating sprites and creating materials.

To create a sprite that uses one of the '**Sprites Mojo**' effects, right click on the '_Hierarchy_' window and select an effect from the list that will appear under '_2D Object > Sprites Mojo_'.

{{< image src="editor_0.jpg" wrapper="col-6 mx-auto">}}

This will create an empty sprite with a '**Sprites Mojo**' material. When you assign a sprite (__1__) you will see the effect. '**Sprites Mojo**' is material based, so you will have to display its material (__2__) to see its parameters.

{{< image src="editor_1.jpg" wrapper="col-6 mx-auto">}}

All effects have a layout similar to the example above. A first part (__3__) with the effect parameters. Another part that you can activate to adjust the color (__4__) and another part where you can adjust sprite values (__5__).

Finally, by clicking on '[doc]' (__6__) you can access the online documentation and by clicking on the '_Reset_' button (__7__) you will set all the parameters to their original values.

This is the easiest way to create sprites using '**Sprites Mojo**', but you must keep in mind that it will create a new material for each sprite you create. If your sprites do not share textures between them, no problem. If your sprites share the same texture, the second way is more optimal: creating materials.

To create a material that uses a '**Sprites Mojo**' effect, just right click on the '_Project_' window and select one of the '_Create > Sprites Mojo_' effects. Once the material is created, you only have to assign it to the sprites you want to use it.

{{< rawhtml >}}<center>{{< /rawhtml >}}
![](editor.gif)
{{< rawhtml >}}</center>{{< /rawhtml >}}

## Code

All the code is inside the _namespace_ '__FronkonGames.SpritesMojo__'. The first thing to do is to import the _namespace_:

```csharp
 using FronkonGames.SpritesMojo;
```

You can create sprites that use the effects of '**Sprites Mojo**' as follows (in this example '__Retro__'):

```csharp
GameObject gameObject = Retro.CreateSprite();
```

Remember that each sprite will have a new material. If you want several sprites to use the same material with an effect, you can create it that way and then assign it to the sprites you want:

```csharp
Material material = Retro.CreateMaterial();
```

Each effect has those two functions (_CreateSprite()_ and _CreateMaterial()_) to create its own sprites and materials. You can find them all in the '_Fronkon Games/SpritesMojo/Runtime_' folder.

Continuing with the previous example, if you wanted to modify or query any parameter of the '__Retro__' effect, you can do it like this:

```csharp
SpriteRenderer sprite = gameObject.GetComponent<SpriteRenderer>();

// Changes the sprite emulation mode.
Retro.Mode.Set(sprite, Retro.Emulations.Gameboy);

// Check pixelation.
int pixelation = Retro.Pixelation.Get(sprite);

// You can also do it with the material.
Retro.Mode.Set(material, Retro.Emulations.Gameboy);
float luminance = Retro.Luminance.Get(material);
```

In addition, all effects have some common parameters that you can access through the '_SpritesMojo_' class that you can find in '_Fronkon Games/Sprites Mojo/Runtime_'. For example, let's enable '_ColorAdjust_' if it is disabled and modify some of its parameters:

```csharp
if (SpriteMojo.ColorAdjust.Get(sprite) == false)
{
  SpriteMojo.ColorAdjust.Set(sprite, true);

  SpriteMojo.Gamma.Set(sprite, 1.2f);
  SpriteMojo.Hue.Set(sprite, 0.25f);
}
```

All effect variables of type _IntVariable_, _FloatVariable_, _ColorVariable_ and _VectorVariable_ can be set to a value and you can specify how long (in seconds) you want the transition to last from the current value to the one you have set. For example, if you want to transition to a pixel size of 8 in 2 seconds:

```
Retro.Pixelation.Set(sprite, 8, 2.0f);
```

Check the class comments for more information.

---
#
## Effects

### Black and White

Desaturates the image by selecting the intensity for each color channel, the amount of light and the smoothness of the color change.

{{< image src="blackandwhite.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/BlackAndWhite.mp4" loop="true" autoplay="true">}}

### Black Hole

Create a '_black hole_' inside the sprite. Use the alpha channel of '_Color_' to modify the transparency of the effect.

{{< image src="blackhole.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/BlackHole.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'. This effect does not support [Sprite Atlas](https://docs.unity3d.com/Manual/class-SpriteAtlas.html).
{{< /alert >}}

### Blend

Use some of Photoshop's 25 blending modes.

{{< image src="blend.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Blend.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
Since URP does not support '[Grab Pass](https://docs.unity3d.com/Manual/SL-GrabPass.html)' at the moment, this effect is only available for the Built-in Render Pipeline.
{{< /alert >}}

### Dissolve

'_Dissolve_' the sprite using a gradient texture as a pattern. Change the mode to '_Color_' to make a border appear with the color of your choice, or use '_Texture_' to make it a texture.

This effect has a large list of built-in patterns you can use, but if you want to use your own, select '_Custom_' under '_Shape_'. This way you can specify the texture you want to use.

{{< image src="dissolve.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Dissolve.mp4">}}

{{< alert type="info">}}
This effect does not support [Sprite Atlas](https://docs.unity3d.com/Manual/class-SpriteAtlas.html).
{{< /alert >}}

### Dither

Applies various algorithms to reduce the amount of colors. It also pixelizes the sprite.

{{< image src="dither.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Dither.mp4" loop="true" autoplay="true">}}

### Duo Tone

It uses a two-color gradient based on the sprite's luminance. To adjust the brightness ranges it uses, you can press the '_Auto_' button or adjust it manually in 'Luminance'.

{{< image src="duotone.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/DuoTone.mp4" loop="true" autoplay="true">}}

### Edge

Highlight sprite edges using different modes and algorithms.

{{< image src="edge.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Edge.mp4" loop="true" autoplay="true">}}

### Glass

Simulates a glass material, deforming the background.

{{< image src="glass.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Glass.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
Since URP does not support '[Grab Pass](https://docs.unity3d.com/Manual/SL-GrabPass.html)' at the moment, this effect is only available for the Built-in Render Pipeline.
{{< /alert >}}

### Hologram

It simulates a hologram or projection.

{{< image src="hologram.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Hologram.mp4" loop="true" autoplay="true">}}

### Instagram

Apply one of the 15 most used filters on Instagram.

{{< image src="instagram.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Instagram.mp4" loop="true" autoplay="true">}}

### Masks

Applies blending effects, colors and textures to areas of a sprite defined by a mask. The mask is a texture in which you can define up to 3 zones, one for each color channel.

{{< image src="masks.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Masks.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
This effect does not support [Sprite Atlas](https://docs.unity3d.com/Manual/class-SpriteAtlas.html).
{{< /alert >}}

### Negative

Change each color by its opposite. You can define how each color channel is affected.

{{< image src="negative.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Negative.mp4" loop="true" autoplay="true">}}

### Outline

Creates a border around the sprite outline.

{{< image src="outline.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Outline.mp4" loop="true" autoplay="true">}}

### Pinch

Clamp the sprite in a certain area.

{{< image src="pinch.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Pinch.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{< /alert >}}

### Ramp

Replaces the sprite colors with a gradient of 5 colors based on luminance. To adjust the luminance ranges it uses, you can click the 'Auto' button or adjust it manually in 'Luminance'.

{{< image src="ramp.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Ramp.mp4" loop="true" autoplay="true">}}

To easily find a gradient, click on '__search__' (__1__), to open the gradient search tool (internet connection required), or click on '__random__' (__2__) to get a random one.

{{< image src="ramptool.jpg" wrapper="col-6 mx-auto">}}

Clicking on '__sort__' (__3__) will sort the gradient colors from the darkest (in '_Color 1_') to the brightest (in '_Color 5_'). You can also '__copy__' '__paste__' (__4__) between sprites with the '__Ramp__' effect.

### Retro

Emulates old devices such as: Gameboy, Commodore 64, ZX Spectrum, etc.

{{< image src="retro.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Retro.mp4" loop="true" autoplay="true">}}

### RGB Glitch

Simulates a failure in the RGB color channels.

{{< image src="rgbglitch.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/RGBGlitch.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{< /alert >}}

### Shake

Shake the sprite.

{{< image src="shake.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Shake.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{< /alert >}}

### Shift

Shitfs the RGB color channels linearly or radially. Enable '__Noise__' to add noise to the scroll.

{{< image src="shift.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Shift.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{< /alert >}}

### Swirl

Twist a certain area of the sprite.

{{< image src="swirl.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Swirl.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'. This effect does not support [Sprite Atlas](https://docs.unity3d.com/Manual/class-SpriteAtlas.html).
{{< /alert >}}

### Tremor

Causes tremors in the sprite.

{{< image src="tremor.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/Tremor.mp4" loop="true" autoplay="true">}}

{{< alert type="info">}}
This effect modifies the outline of the sprite, in some cases you may notice some bugs in the edges. To fix it, make sure that in the sprite import options '__Mesh Type__' is set to '__Full Rect__'.
{{< /alert >}}

### Trio Tone

It uses a three-color gradient based on the sprite's luminance. To adjust the luminance ranges it uses, you can click the '_Auto_' button or adjust it manually in 'Luminance'.

{{< image src="triotone.jpg" wrapper="col-6 mx-auto">}}

{{< video src="/store/sprites-mojo/TrioTone.mp4" loop="true" autoplay="true">}}

---
#
## Support

Do you have any problem or any suggestions? Send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

Remember that if you want to inform me of an error, it would help me if you sent to me the [log file](https://docs.unity3d.com/Manual/LogFiles.html).

{{< rawhtml >}}
<br><center><h4>
{{< /rawhtml >}}

{{< alert color="warning" >}}
If you are happy with this asset, consider write a review in the store

❤️ thanks! ❤️
{{< /alert >}}

{{< rawhtml >}}
</center></h4>
{{< /rawhtml >}}
