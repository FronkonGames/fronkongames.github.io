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
* [Distortions](#distortions), distortions effects to increase the awesomeness of your games.
* [Cheap Camera](#cheap-camera), emulates the defects of cheap cameras with poor quality digital sensors.
* [Bad GPU](#bad-gpu), simulates the effects of a broken GPU.

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

---
## Distortions {#distortions}
{{< asset-header youtube="ydWFcmFnSaU" demo="https://fronkongames.github.io/demos-glitches/distortions/">}}

This asset includes several distortion-based effects. You should include them individually.

### Gravity {#gravity}

{{< video src="/store/glitches/distortions/gravity.mp4" loop="true" autoplay="true">}}

A black hole on tour screen. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="gravity.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Center**' (_2_): the position of the effect, where (0.5, 0.5) is the center of the screen.

'**Radius**' (_3_): size of the effect.

'**Strength**' (_4_): intensity of the deformation effect.

'**Corona**' (_5_): Outer corona tint, strength and color mixing operation.

'**Core**' (_6_): Tint of the inner zone and color mixing operation.

### Water 2D {#water2D}

{{< video src="/store/glitches/distortions/water2D.mp4" loop="true" autoplay="true">}}

Perfect water for platform games. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="water2D.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Height**' (_2_): vertical water height.

'**Strength**' (_3_): wave strength.

'**Frequency**' (_4_): wave frequency.

'**Angle**' (_5_): angle of reflection.

'**Tint**' (_6_): effect tint.

'**Blend**' (_7_): color operation used.

### Under Water {#under-water}

{{< video src="/store/glitches/distortions/underwater.mp4" loop="true" autoplay="true">}}

Simulates that you are underwater in a simple way. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="underwater.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Strength**' (_2_): effect strength on each axis.

'**Speed**' (_3_): speed of ripples on each axis.

'**Amplitude**' (_4_): wave amplitude.

'**Blend**' (_5_): color operation used to blend effect with original image.

'**Use depth**' (_6_): Activates the tinting depending on the pixel depth. You can change the color of the near and far zones. You can also adjust the depth modulation.

{{< alert color="info" icon="fas triangle-exclamation" >}}
If you activate '**Use depth**' (_6_), '**Depth Texture**' of the Universal Render Pipeline file must be enabled.
{{< /alert >}}

### Raining {#raining}

{{< video src="/store/glitches/distortions/raining.mp4" loop="true" autoplay="true">}}

Blurred vision when coming out of the water. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="raining.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Strength**' (_2_): strength of effect.

'**Speed**' (_3_): movement speed.

'**Density**' (_4_): effect density.

'**Tint**' (_5_): effect tint.

'**Blend**' (_6_): color mixing operation used.

### Magnifying {#magnifying}

{{< video src="/store/glitches/distortions/magnifying.mp4" loop="true" autoplay="true">}}

A magnifying glass to investigate details. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="magnifying.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Center**' (_2_): the center of the effect, being the center (0.5, 0.5).

'**Radius**' (_3_): lens radius.

'**Magnification**' (_4_): zoom level.

{{< alert color="info" icon="fas triangle-exclamation" >}}
High values of '**Magnification**' (_4_) can show very pixelated images.
{{< /alert >}}

'**Tint**' (_5_): lens border color.

'**Distortion**' (_6_): color aberration and power in each channel.

'**Border**' (_7_): color aberration power and tint.

### Swirl {#swirl}

{{< video src="/store/glitches/distortions/swirl.mp4" loop="true" autoplay="true">}}

Twist the screen mercilessly! Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="swirl.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Angle**' (_2_): torsion angle.

'**Radius**' (_3_): effect radius.

'**Center**' (_4_): the center of the effect, being the center.

'**Threshold**' (_5_): smoothness of the effect limit.

'**Blend**' (_6_): color operation used to blend effect with original image.

'**Tint**' (_7_): color tint.

### Tremors {#tremors}

{{< video src="/store/glitches/distortions/tremors.mp4" loop="true" autoplay="true">}}

Shakes like in a earthquake! Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="tremors.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Strength**' (_2_): effect strength on each axis.

'**Speed**' (_3_): speed on each axis.

'**Amplitude**' (_4_): wave amplitude.

'**Frequency**' (_5_): wave frequency.

'**Blend**' (_6_): color operation used to blend effect with original image.

'**Samples**' (_7_): samples used to calculate blur.

{{< alert color="danger" icon="fas triangle-exclamation" >}}
The higher the value, the better the blur quality and the lower the performance.
{{< /alert >}}

'**Tint**' (_8_): color tint.

### Scope {#scope}

{{< video src="/store/glitches/distortions/scope.mp4" loop="true" autoplay="true">}}

The sight of a sniper. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="scope.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Center**' (_2_): the center of the effect, being the center (0.5, 0.5).

'**Radius**' (_3_): effect radius.

'**Vignette**' (_4_): vignette strength.

'**Tint**' (_5_): effect tint.

'**Radial distortion**' (_6_): lens distortion [formula](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html#:%7E:text=The%20next%20figures,monotonically%20increasing).

'**Dispersion**' (_7_): size of the distortion zone.

### Inflate {#inflate}

{{< video src="/store/glitches/distortions/inflate.mp4" loop="true" autoplay="true">}}

Swells (or deflates) areas of the screen. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="inflate.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Strength**' (_2_): values above 0 for a inflate effect, below 0 for deflate.

'**Radius**' (_3_): effect radius.

'**Center**' (_4_): the center of the effect, being the center (0.5, 0.5).

### Fisheye {#fisheye}

{{< video src="/store/glitches/distortions/fisheye.mp4" loop="true" autoplay="true">}}

Fisheye / anti-fisheye effect. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="fisheye.jpg" wrapper="col-6 mx-auto">}}

'**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.

'**Strength**' (_2_): values above 0 for a fisheye effect, below 0 for anti-fisheye.

'**Center**' (_3_): the center of the effect, being the center (0.5, 0.5).

'**Blend**' (_4_): color operation used to blend effect with original image.

'**Tint**' (_5_): color tint.

---
## Cheap Camera {#cheap-camera}

{{< asset-header youtube="GJZYzdBmruM" demo="https://fronkongames.github.io/demos-glitches/cheap-camera/">}}

Emulates the defects of cheap cameras with poor quality digital sensors. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="cheapcamera_0.jpg" wrapper="col-6 mx-auto">}}

* '**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.
* '****' (__): .

---
## Bap GPU {#bad-gpu}
{{< asset-header youtube="Q86NARQPUJk" demo="https://fronkongames.github.io/demos-glitches/bad-gpu/">}}

Simulates the effects of a broken GPU. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="badgpu_0.jpg" wrapper="col-6 mx-auto">}}

* '**Intensity**' (_1_): intensity of the effect. If it is 0, the effect will not be active.
* '****' (__): .

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
