---
author: Martin Bustos
title: Glitches
showTitle: false
date: 4
description: Add digital and analog glitches to increase the realism of your games
tags: ["unity", "store", "glitch", "hack"]
metadata: none
showImage: true
thumbnail:
  url: img/glitches.jpg
---

'**Glitches**' contains the following assets:

* [Color Blindness](#colorblindness), simulates the most common vision defects.
* [Corrupt Memory](#corruptmemory), a cyber attack? no, it's just corrupted memory.
* [Interferences](#interferences), something is interfering with the signal...
* [VHS](#vhs), the beauty of analog.

## Requirements

All '**Glitches**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP), which means they will **not work** with Built-In, or HDRP.

You will need to have URP version 12.1 or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Glitches**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< image src="editor_0.jpg" wrapper="col-6 mx-auto">}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< image src="editor_1.jpg" wrapper="col-6 mx-auto">}}

## VR

To increase compatibility with VR devices, I recommend that you select '**Stereo Rendering Mode**' in '**Multi Pass**' mode:

{{< image src="vr.jpg" wrapper="col-6 mx-auto">}}

## Using them in code

You can also handle '**Glitches**' effects by code. The first thing you will have to do is to add the namespace of the effect you want to use.

They are all of the style 'FronkonGames.Glitches.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**Color Blindness**' the code would be:

```csharp
using FronkonGames.Glitches.ColorBlindness;
```

And with this code you could check if the effect is added, and if it is not, add it.

```csharp
if (ColorBlindness.IsInRenderFeatures() == false)
    ColorBlindness.AddRenderFeature();
```

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

```csharp
ColorBlindness.Settings settings = ColorBlindness.GetSettings();

settings.intensity = 0.5f;
```

If you are using an effect other than '**Color Blindness**' just change it to its name. Check the source code comments for more information.

{{< alert color="warning" icon="fas triangle-exclamation" >}}
Do not use the code of the demos in your projects, they are only there to show you the use of the effect through code.
{{< /alert >}}

#

---
## Color Blindness {#colorblindness}
{{< asset-header youtube="f5CiPt9bzBE" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/glitches-color-blindness-273126" demo="https://fronkongames.github.io/demos-glitches/colorblindness/">}}

'**Color Blindness**' simulates the most common vision defects.

{{< alert color="danger" icon="fas triangle-exclamation" >}}
This asset **simulates** a series of vision defects, **NOT** corrects them.
{{< /alert >}}

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="colorblindness_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

Select the type of deficiency you want to simulate with '**Deficiency**' (_2_):

* **Protanomaly**: red-green vision deficiency, 1% of males, 0.03% of females.
* **Deuteranomaly**: red-green color blindness, 6% of males, 0.4% of females.
* **Tritanomaly**: blue-yellow color blindness, 0.01% for males and females.
* **Protanopia**: reds are greatly reduced, 1% of males, 0.02% of females.
* **Deuteranopia**: greens are greatly reduced, 1% of males.
* **Tritanopia**: blues are greatly reduced, 0.003% population.
* **Achromatopsia**: total color blindness, 0.001% population.
* **Achromatomaly**: partial color blindness, 0.00001% population.

In order to compare the result with a normal view, move '**Comparator**'.

---
## Corrupt Memory {#corruptmemory}
{{< asset-header youtube="F4ubH6fGgcA" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/glitches-corrupt-memory-274730" demo="https://fronkongames.github.io/demos-glitches/corruptmemory/">}}

'**Corrupt Memory**' emulates malfunctioning memory.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="corruptmemory_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The effect generates a pattern of overlapping rectangles that change dimensions and position randomly. The first parameters (from _2_ to _6_), modify this pattern. If you want to see it better, activate '**Debug view**' (_10_).

The first thing you can adjust is the complexity (_2_) of the pattern and the density (_3_) of the rectangles. Then the speed (_4_) with which they vary and their displacement (_5_) on the screen. Finally you can also change their magnification (_6_).

The pattern is used to define the zones where three effects will be applied. The first one is a pixelation effect (_7_), then a chromatic aberration effect (_8_) and finally an image displacement effect (_9_).

In all of them you can adjust the limit at which it is activated ('_Threshold_'). With a very high limit, it will use very few rectangles of the pattern. With a very low limit, many.

---
## Interferences {#interferences}
{{< asset-header youtube="lYrj9jj3U8Y" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/glitches-interferences-281861" demo="https://fronkongames.github.io/demos-glitches/interferences/">}}

With '**Interferences**' you can simulate video transmission failures.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="interferences_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Blend**' (_2_) modify the color operation used to blend the original pixel with the effect pixel.

'**Offset**' (_3_) amplifies the strength of the effect.

From the distortion effect (_4_) you can control different variables such as speed, density, amplitude and frequency.

The second effect applied is scanlines (_5_) and you can adjust its density and opacity.

---
## VHS {#vhs}
{{< asset-header youtube="f3W4_dPwZK0" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/glitches-vhs-282181" demo="https://fronkongames.github.io/demos-glitches/vhs/">}}

Accurately emulates an old VHS tape. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="vhs_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

**VHS**' consists of two very typical effects of the old VHS tapes: the noise and the pause.

The first one can be controlled using '**Noise**' (_2_) and its parameters. The second with '**Pause**' (_3_) and '**Pause Band**' (_4_).

If you want to use only the noise, set '**Pause**' (_3_) and '**Pause Band**' (_4_) to zero. If you only want to use the pause effect, set '**Noise**' (_2_) to zero.

#
---
## Misc

All '**Spice Up**' effects have a panel, '**Color**', in which you can modify the final color of the effect.

{{< image src="color.jpg" wrapper="col-6 mx-auto">}}

They also have an '**Advanced**' panel with these options:

{{< image src="advanced.jpg" wrapper="col-6 mx-auto">}}

Activate '**Affect the Scene View?**' (_1_) if you want the effect to be applied also in the '_Scene_' window of the Editor. With '**Filter mode**' (_2_) you can change the type of filter used.

Although it is not recommended to change it, with '**RenderPass event**' (_3_) you can modify at which point in the render pipeline the effect is applied. Finally, activate '**Enable profiling**' (_4_) to show in the '_Profiling_' window the metrics of the effect.

---
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
