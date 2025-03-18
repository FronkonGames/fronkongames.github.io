---
author: Martin Bustos
title: Artistic
showTitle: false
date: 1
description: Enhance your creativity and get a unique style with this effects bundle
tags: ["unity", "store"]
metadata: none
showImage: true
thumbnail:
  url: img/artistic.jpg
---

All the effects of '**[Artistic](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-bundle-272266?aid=1101l9zFC&utm_source=aff)**' will help you to achieve a unique look for your games. It consists of the following effects:

* [One Bit](#onebit), a hipster, original and versatile look using a dithering with blue noise.
* [Oil Paint](#oilpaint), transform your games into pieces of art.
* [Tilt Shift](#tiltshift), used to simulate a miniature scene.
* [Color Isolation](#colorisolation), isolates areas by color and applies effects.
* [Sharpen](#sharpen), enhances image details.
* [Tonemapper](#tonemapper), maps HDR into LDR using different algorithms.
* [Comic](#comic), simulates the printing technique used in comics and newspapers.
* [Neon](#neon), synth-wave effect.
* [Spark](#spark), adds bloom and ray-of-light effects.
* [Radial Blur](#radialblur), the need for the speed.

{{< alert color="dark" >}}
You can obtain each effect separately, but if you want multiple effects, you might be interested in **'[ARTISTIC BUNDLE](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-bundle-272266?aid=1101l9zFC&utm_source=aff)'** where you can find them all at a special price!
{{< /alert >}}

## Requirements

All '**Artistic**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP), which means they will **not work** with Built-In, or HDRP.

#### Unity 6 or higher

All effects are compatible with **Unity 6**. Most of them do it natively when using [Render Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html).
You will need to have URP version *17.0.2* or higher installed. In the [official documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html) you can find the steps to install it correctly.

Make sure that the '_Compatibility Mode_' is **disabled** (_Project Settings > Graphics > Render Graph_).

{{< image src="compatibility_mode.jpg" wrapper="col-6 mx-auto">}}

#### Unity 2022.3 or higher

You will need to have URP version *12.1.15* or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Artistic**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< image src="editor_0.jpg" wrapper="col-6 mx-auto">}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< image src="editor_1.jpg" wrapper="col-6 mx-auto">}}

## VR

To increase compatibility with VR devices, I recommend that you select '**Stereo Rendering Mode**' in '**Multi Pass**' mode:

{{< image src="vr.jpg" wrapper="col-6 mx-auto">}}


## Using them in code

Once you have added the effect in the Editor, you can also handle '**Artistic**' effects by code. 

First you must add the corresponding namespace. They are all of the style 'FronkonGames.Artistic.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**One Bit**' the code would be:

```csharp
using FronkonGames.Artistic.OneBit;
```

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

```csharp
OneBit.Settings settings = OneBit.GetSettings();

settings.intensity = 0.5f;
```

If you are using an effect other than '**OneBit**' just change it to its name. Check the source code comments for more information.

#
---
## One Bit {#onebit}
{{< asset-header youtube="Yz9j7iXuDhY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/one-bit-216000" demo="https://fronkongames.github.io/demos-artistic/onebit/" >}}

Get a distinctive look with '**One Bit**', an original and versatile effect that uses a special type of dithering algorithm based on Blue Noise, similar to that used at the award-winning '_Return of the Obra Dinn_'.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="onebit_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

'**Edges**' (_2_) makes it remarked more the edges and '**Noise**' (_2_) affects the amount of noise that will appear on the screen. You can change the random seed used to generate the noise with '**Seed**'.

'**Blend**' (_4_), specifies the formula used to mix the original color of the screen with the effect. They are very similar to those you can find in '_Photoshop_'. With '**Color**' you can change the way a color (or several) effects the final result. The simplest is '**Solid**' and its '**Color**' parameter tints the image. Other modes are '**Horizontal**', '**Vertical**' and '**Circular**' and use two colors in a gradient in different directions.

{{< image src="onebit_1.jpg" wrapper="col-6 mx-auto">}}

'**Gradient**' is another mode that uses the brightness of the original pixel to replace it in a color gradient. So the leftmost colors of the gradient would be used for the darker areas of the image and the rightmost colors would be used for the brighter areas. Click on the gradient to modify it to your liking. If the gradient you use does not have dark colors, the result may be too bright, and vice versa. You can modify the brightness range used with '**Luminance**'.

Click on '**search**' to open the color palette search tool.

{{< image src="onebit_2.jpg" wrapper="col-6 mx-auto">}}

Just find a palette you like and click the '**Use**' button.

{{< alert color="success" icon="fas circle-info" >}}
This tool requires an Internet connection.
{{< /alert >}}

In _6_, _7_ and _8_ you can modify the color range in each channel. Small values in these fields can create a '_retro_' effect.

When '**Invert**' (_9_) is activated, the color is inverted.

---
## Oil Paint {#oilpaint}
{{< asset-header youtube="A9jtFpXo02Q" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-oil-paint-264134" demo="https://fronkongames.github.io/demos-artistic/oilpaint/" >}}

Transform your games into pieces of art in a very easy way. Once installed, when you select your '_Universal Renderer Data_', you will have the following [Renderer Features](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@10.1/manual/urp-renderer-feature-how-to-add.html) to choose from:

* **Kuwahara Basic**: the simplest and fastest based on the algorithm created by [Michiyoshi Kuwahara](https://en.wikipedia.org/wiki/Kuwahara_filter).
* **Kuwahara Generalized**: a version that fixes some problems of the previous one, based on the work of [Acerola](https://www.youtube.com/@Acerola_t).
* **Kuwahara Directional**: a Sobel filter is added to improve the denoising process.
* **Kuwahara Anisotropic**: improves the quality in the smallest details, based on the paper '[Image and Video Abstraction by Anisotropic Kuwahara Filtering](https://www.researchgate.net/publication/220507613_Image_and_Video_Abstraction_by_Anisotropic_Kuwahara_Filtering)'.
* **Tomita-Tsuji**: a steroid version of Kuwahara's algorithm, with the best visual results but with a performance decrease.
* **Symmetric Nearest Neighbour**: another smoothing algorithm designed to preserve image edges. Much more efficient than the previous ones.

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

Depending on the selected algorithm, you will see different parameters although all of them have '**Passes**'. This parameter specifies the number of passes of the algorithm to be performed. If it is 1, the algorithm will only run once per pixel.

If you increase the value, the effect will be greatly enhanced but you will multiply the cost of the effect. I only recommend that the value be greater than 1 if you are going to use it on powerful hardware (consoles and PC).

You can add an extra algorithm to better define details with '**Improve details**': Emboss and Sharpen. Note that adding this algorithm creates an additional pass and therefore lower performance.

Still not enough? Raise the value of '**Water Color**' to add an water color paint effect to the image.

If you need more control, activate '**Process depth**'.

{{< image src="oilpaint_1.jpg" wrapper="col-6 mx-auto">}}

With '**Depth curve**' (__1__) you can adjust the intensity of the effect depending on the depth. In the values of the example you can see that the effect would have the maximum intensity except in the farthest areas it would tend to 0. With this you can avoid that small details in the background of the scene disappear because of the effect. You can also adjust the intensity of the curve with '**Depth power**' (__2__).

Adjusting these two parameters can be complicated by not being able to see clearly how the curve varies. Activate '**View depth curve**' (__4__) and you will see that the areas with the most intense effect are warmer and the areas with the least are cooler.

{{< video src="oilpaint_2.mp4" loop="true" autoplay="true" >}}

Don't want the effect to be applied to the sky? Disable '**Sample sky**' (__3__).

{{< alert color="success" icon="fas circle-info" >}}
In order to use this feature, you must enable '**Depth Texture**' in your camera or pipeline settings.
{{< /alert >}}

---
## Tilt Shift {#tiltshift}
{{< asset-header youtube="ixqjMNnUSus" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-tilt-shift-265465" demo="https://fronkongames.github.io/demos-artistic/tiltshift/" >}}

Used to simulate a miniature scene, something very used in cinema as in the [race scene](https://www.youtube.com/watch?v=QetnuKbo1XI) of '_The Social Network_'. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="tiltshift_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

You can modify the angle (_2_), aperture (_3_) and offset (_4_) of the effect. Also the blur intensity (_5_) and distortion (_6_).

You can also modify certain color parameters in the 'focused' (_7_) area (where the effect is not applied) and in the 'unfocus' (_8_) area.

{{< image src="tiltshift_1.jpg" wrapper="col-6 mx-auto" >}}

In order to better adjust these parameters, you can activate '**Debug**' (_9_) to better see how the effect is applied. With this parameter activated, the areas with more intensity of the effect will be tinted red, and those with less intensity will be tinted blue.

---
## Color Isolation {#colorisolation}
{{< asset-header youtube="XfHdKU1qTF4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-color-isolation-266086" demo="https://fronkongames.github.io/demos-artistic/colorisolation/" >}}

Isolates areas by color and applies effects. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="colorisolation_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The first thing to do is to set the color you want to isolate, using '_Isolated color_' (_2_). You can adjust the sensitivity with '**Threshold**', to be more or less strict when filtering colors.

'**Color Isolation**' translates the image into the [CIELAB color space](https://en.wikipedia.org/wiki/CIELAB_color_space), in order to more accurately differentiate colors. You can adjust the parameters that are used:

* L*: luminosity.
* a*: green-magenta axis.
* b*: blue-yellow axis.

Once you have isolated the color you want, you can apply different effects to both the '**Isolated zone**' (_3_) and the '**Not isolated zone**' (_4_).

---
## Sharpen {#sharpen}
{{< asset-header youtube="Xjax-orCmVY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-sharpen-266728" demo="https://fronkongames.github.io/demos-artistic/sharpen/" >}}

Enhances image details using different algorithms. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="sharpen_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The first thing is to select the algorithm (_2_) that gives you the best result. They are as follows:

* **Luma**, it applies a blurring effect to the original pixel by incorporating the neighboring pixels, and subsequently, it subtracts this blur to enhance the image's sharpness. Is similar to using Unsharp Mask in Photoshop.
* **Contrast Adaptive**, dynamically regulates the sharpening intensity on a per-pixel basis to achieve a uniform level of sharpness throughout the entire image.

From the first algorithm, '**Luma**', you can choose between different patterns:

* **Fast**, only two texture fetches. Faster but slightly lower quality.
* **Normal**, four texture fetches.
* **Wider**, four texture fetches, less sensitive to noise but also to fine details.
* **Pyramid**, four texture fetches, diamond-shaped. A slightly more aggresive look

Once you have chosen the algorithm that best suits your needs, you can adjust the intensity of the effect with '**Sharpeness**' (_3_) and the radius of each sample pattern (_4_).

You can also increase the contrast of the colors with '**Vibrance**' (_5_).

To view in which areas of the image the effect is applied, activate '**Debug view**' (_6_).

---
## Tonemapper {#tonemapper}
{{< asset-header youtube="XcLXlvqG5yU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-tonemapper-267617" demo="https://fronkongames.github.io/demos-artistic/tonemapper/" >}}

Maps wide range colors (HDR) into low dynamic range (LDR) using different algorithms. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="tonemapper_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active. These are the operators (_2_) included:

* **Linear**: Good old linear.
* **Logarithmic**: logarithmic mapping
* **Exponential**: exponential mapping.
* **Simple Reinhard**: simple and fast Reinhard.
* **Luma Reinhard**: Reinhard based on luminance from "Photographic Tone Reproduction for Digital Images".
* **Luma Inverted Reinhard**: Reinhard based on inverted luminance, by Brian Karis.
* **White Luma Reinhard**: Reinhard based on luminance, but white preserving.
* **Hejl 2015**: ACES-liked, by Jim Hejl.
* **Filmic**: filmic tonemapping.
* **Filmic Aldridge**: variation of the Hejl and Burgess-Dawson filmic curve by Graham Aldridge.
* **ACES**: From 'ACES Filmic Tone Mapping Curve' by Narkowicz.
* **ACES Oscars**: Pastel hue function, designed to provide a pleasing albedo.
* **ACES Hill**: ACES curve fit by Stephen Hill (@self_shadow).
* **Lottes**: From "Advanced Techniques and Optimization of HDR Color Pipelines" by Timothy Lottes.
* **Uchimura**: Used in Gran Turismo. From "HDR theory and practice" by Uchimura.
* **Unreal**: Adapted to be close to ACES curve by Romain Guy. Used in Unreal Engine 3 up to 4.14.
* **Uncharted 2**: Created by John Hable for 'Uncharted 2' (based on Haarm-Pieter Duiker's works in 2006 for EA).
* **Watch Dogs**: Used in 'Watch Dogs' by Ubisoft.
* **Piece-Wise**: 'Piece-Wise Power Curve' by John Hable at Epic Games.
* **RomBin Da House**: By tech art Roman Galashov (@RomanGalashov).
* **Oklab**: Oklab-based.
* **Clamping**: Clamps everything above a given luminance threshold to 1, by Schlick.
* **Max 3**: From 'Optimized Reversible Tonemapper for Resolve', by Timothy Lottes.
* **Max 3 Inverted**: Inverted luminance.

Each operator can also have some extra parameters that will appear under it.

You can also modify the final color with the parameters offered by '**Color filter**' (_3_) and its '**Lift**' (_4_), '**Midtones**' (_5_) and '**Gain**' (_6_).

---
## Comic {#comic}
{{< asset-header youtube="W4t0Cnk1Q0U" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-comic-269586" demo="https://fronkongames.github.io/demos-artistic/comic/" >}}

Simulates the printing technique used in comics and newspapers: [halftone](https://en.wikipedia.org/wiki/Halftone). Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="comic_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The scale of the points can be modified with '**Scale**' (_2_). The operation used to blend the color of these points with the original image can be adjusted with '**Color blend**' (_3_).

To increase the feeling of seeing a comic book, you can add a stroke effect with '**Edge**' (_4_).

If you want to finely adjust the angle of each color point, you can modify it with '**CMYK pattern**' (_5_).

---
## Neon {#neon}
{{< asset-header youtube="nNVYDesYfF8" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-neon-270269" demo="https://fronkongames.github.io/demos-artistic/neon/" >}}

Neon synthwave effect highlighting the edges of the image with cycling colors. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="neon_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active. You can control the edge strength with '**Strength**' (_2_). The thickness can be adjusted with '**Radius**' (_3_).

With '**Blend**' (_4_) you can change how the original image and the effect are blended, using formulas very similar to those used by _Photoshop_.

Additionally you can apply a deformation to the effect with '**Fisheye**' (_5_). If the value is positive a _fisheye_ effect will be applied and if negative an _anti-fisheye_ effect will be applied.

You may want the effect to become less intense as you move away from the camera. Activate '**Process depth**' (_7_) and adjust '**Depth power**' to achieve this. If you also want it to affect the sky, turn on '**Sample sky**'.

{{< alert color="success" icon="fas circle-info" >}}
In order to use this feature, you must enable '**Depth Texture**' in your camera or pipeline settings.
{{< /alert >}}

---
## Spark {#spark}
{{< asset-header youtube="kgwMRlHzGxs" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-spark-270898" demo="https://fronkongames.github.io/demos-artistic/spark/" >}}

Adds bloom and ray-of-light effects to the brightest areas. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="spark_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

In the '**Rays**' section (_2_) you can adjust everything related to the rays generated by the effect. From their size, intensity, color and angle, to the operation used to blend them with the original image.

{{< alert color="success" icon="fas circle-info" >}}
By default the rays do not rotate, but you can do it easily by moving '**Spin**'. If you want to do it via script, you have an example in the demo code.
{{< /alert >}}

In '**Barrel**' (_3_) you can control the deformation of the rays and with '**Dispersion**' (_4_) you can simulate a chromatic shift of their colors.

Add more smoothness to the shape of the rays with '**Blur**' (_5_), but remember that very high values may affect performance. You can also add some noise with '**Dirt**' (_6_).

If you want to better adjust at what brightness level rays start to be generated, use '**Threshold**' (_7_).

Although it will decrease the quality of the effect, you can increase the performance of the effect by choosing other values for '**Down sample**' (_8_). This may generate some annoying glitches in the brightness, you can mitigate them by using '**Artifacts**' (_9_).

{{< alert type="info" >}}
You don't want the effect to be generated on your particles? You can change when it is applied by going to '**Advanced** > **RenderPass event**' and setting it to '**After Rendering Transparents**'.
{{< /alert >}}

---
## Radial Blur {#radialblur}
{{< asset-header youtube="rSE8fjbire4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-radial-blur-271547" demo="https://fronkongames.github.io/demos-artistic/radialblur/" >}}

Increases the feeling of speed and adrenaline! Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="radialblur_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

Change the origin of the effect with '**Center**' (_2_), where (0, 0) is the center of the screen.

The quality depends directly on the number of '**Samples**' (_3_) you use. The higher the number, the better the quality, the lower the number, the better the performance. By adjusting the '**Density**' (_4_) and '**Falloff**' (_5_) values correctly you can lower the number of samples.

In addition to the radial blur effect, another chromatic aberration effect (also radial) is used. Adjust how it affects each color channel with '**Offset**' (_6_).

A screen warping effect is also added with '**Fisheye**' (_7_). With negative values the deformation will be inward and with positive values outward.

You can also apply color effects to the inner zone, '**Inner**' (_10_), where less effect is applied and to the outer zone, '**Outer**' (_11_), where more effect is applied. The zones can be modified with '**Gradient power**' (_8_) and '**Range**' (_9_).

#
---
<br>

## Misc

All effects have a panel, '**Color**', in which you can modify the final color of the effect.

{{< image src="color.jpg" wrapper="col-6 mx-auto">}}

They also have an '**Advanced**' panel with these options:

{{< image src="advanced.jpg" wrapper="col-6 mx-auto">}}

Activate '**Affect the Scene View?**' (_1_) if you want the effect to be applied also in the '_Scene_' window of the Editor. With '**Filter mode**' (_2_) you can change the type of filter used.

Although it is not recommended to change it, with '**RenderPass event**' (_3_) you can modify at which point in the render pipeline the effect is applied. Finally, activate '**Enable profiling**' (_4_) to show in the '_Profiling_' window the metrics of the effect.

---
## F.A.Q.

##### _How to make the effect also affect the UI?_

In order for the UI not to be affected by the effect, you should set the 'Render Mode' of your canvas from 'Screen Space - Overlay' to 'Screen Space - Camera' and dragging your camera with to 'Render Camera'.

{{< image src="ui.jpg" wrapper="col-6 mx-auto">}}

Note that when you make this change, the coordinates of your UI will be in camera space, so you will have to change them.
<br>

##### _When Bloom is added, its intensity is too low or the effect stops working._

Bloom's URP Unity effect is not compatible with postprocessing effects based on [ScriptableRendererFeature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html?q=ScriptableRendererFeature) (like this one).

You will have to add your own one based on ScriptableRendererFeature or you can use [this one at no cost](https://github.com/FronkonGames/ScriptableRenderBloom) ;)
<br>

##### _Can I use it in a material?_

Yes! Any effect can easily be used on a material. Just follow these steps:

* In the '**Project**' window, open the '**Create**' menu with the right mouse button and select '**Create > Render Texture**'.
* Create a new camera and in '**Output Texture**' select the Render Texture previously created. Remember to activate '**Post Processing**' and select in '**Renderer**' where you have the effect added.
* In the material you want to use, select in '**Base Map**' the Render Texture.
<br>

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
