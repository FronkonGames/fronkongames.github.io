---
author: Martin Bustos
title: Retro
showTitle: false
date: 3
description: A great collection of retro effects, simple to use and with many configuration options
tags: ["unity", "store", "retro"]
metadata: none
showImage: true
thumbnail:
  url: img/retro.jpg
---

'**[Retro](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-bundle-245493?aid=1101l9zFC&utm_source=aff)**' is a great collection of retro effects, simple to use and with many configuration options. It consists of the following effects:

* [VHS](#vhs), mimic VHS as true as possible.
* [Pixelator](#pixelator), unleash stunning retro visuals!
* [Old Films](#oldfilms), the best way to replicate the look of old movies.
* [CRT TV](#crttv), the most configurable old TV effect you'll ever find.
* [Lo-Fi](#lofi), stunning retro-style visuals.
* [NTSC](#ntsc), simulates the analog video artifacts characteristic of the NTSC.
* [Noir](#noir), a classic, stylized film noir aesthetic.
* [Old Computers](#oldcomputers), emulates the color palettes of old 8-bit and 16-bit computers.
* [ASCII](#ascii), the old-school ASCII effect with steroids.
* [Spectrum](#spectrum), mimics the legendary ZX Spectrum 8-bits computer from 1982.
* [LCD](#lcd), simulates the visual characteristics of a Liquid Crystal Display (LCD).
* [Vintage Filters](#vintagefilters), a great collection of vintage filters inspired by Instagram effects.
* [Handheld 8-Bit](#handheld8bit), imitates the graphics of the 8-bit handheld consoles of the late 1980s.

{{< alert color="light" >}}
You can obtain each effect separately, but if you want multiple effects, you might be interested in **'[RETRO BUNDLE](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-bundle-245493?aid=1101l9zFC&utm_source=aff)'** where you can find them all at a special price!
{{< /alert >}}

## Requirements

All '**Retro**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP), which means they will **not work** with Built-In, or HDRP.

#### Unity 6 or higher

All effects are compatible with **Unity 6**, and use the new [Render Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html). You will need to have URP version *17.0.2* or higher installed. In the [official documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html) you can find the steps to install it correctly.

Make sure that the '_Compatibility Mode_' is **disabled** (_Project Settings > Graphics > Render Graph_).

{{< image src="compatibility_mode.jpg" wrapper="col-6 mx-auto">}}

#### Unity 2022.3 or higher

You will need to have URP version *12.1.15* or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Retro**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< image src="editor_0.jpg" wrapper="col-6 mx-auto">}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< image src="editor_1.jpg" wrapper="col-6 mx-auto">}}

{{< alert color="info" >}}
'_Quality_' levels (_Project Settings > Quality_) can have their own active '_Render Pipeline Asset_'.

If so, whatever you assign in '_Scriptable Render Pipeline Settings_' in '_Graphics_' will be ignored.

**Remember to add the effect to the quality levels you want to use.**
{{< /alert >}}

## VR

To increase compatibility with VR devices, I recommend that you select '**Stereo Rendering Mode**' in '**Multi Pass**' mode:

{{< image src="vr.jpg" wrapper="col-6 mx-auto">}}

## Using them in code

Once you have added the effect in the Editor, you can also handle '**Retro**' effects by code. 

First you must add the corresponding namespace. They are all of the style 'FronkonGames.Retro.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**Spectrum**' the code would be:

```csharp
using FronkonGames.Retro.Spectrum;
```

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

```csharp
Spectrum.Settings settings = Spectrum.Instance.settings;

settings.intensity = 0.5f;
```

And how can I activate and deactivate the effect? It's as easy as that:

```csharp
Spectrum spectrum = Spectrum.Instance;

// Switch between active and inactive.
if (spectrum.isActive == true)
  spectrum.SetActive(false);
else
  spectrum.SetActive(true);
```

{{< alert color="warning" icon="fas triangle-exclamation" >}}
The Instance function uses [Reflection](https://learn.microsoft.com/en-us/dotnet/fundamentals/reflection/reflection), and is therefore expensive. I recommend that you save the Instance value to use it without affecting performance.
{{< /alert >}}

If you are using an effect other than '**Spectrum**' just change it to its name. Check the source code comments for more information.

#
---
## VHS {#vhs}
{{< asset-header youtube="LH9KDnOq0dg" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-vhs-244944" demo="https://fronkongames.github.io/demos-retro/vhs/" warn="assets used in video and demo are not included">}}

'**VHS**' mimic as true as possible. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="vhs_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The best quality of the effect is obtained with '**Quality**' (_2_) set to '**High Fidelity**', however on older mobile devices the performance may not be optimal. In that case you can select the '**Performant**' mode which is more suitable for older hardware. In the '**High Fidelity**' mode you can adjust the number of '**Samples**' that are used, the lower the number of samples the more optimal.

A VHS/VHS-C tape has a resolution of 240 vertical lines. You can reduce the resolution with '**Resolution**' (_3_). Select '**Same**' to not reduce it.

Internally, a VHS tape runs in [YIQ color space](https://en.wikipedia.org/wiki/YIQ), in '**YIQ color space**' (_4_) you can modify its components: _luma_, _in-phase_ and _quadrature_.

Due to the chemical components of the ribbons, over time the dark colors could change and tend to purple. With '**Shadow tint**' (_5_) you can simulate this. You can also select the brightness range with '**Color levels**'.

As a result of mechanical failures in the heads, some noise bands could appear and also modify the color. This effect can be controlled in '**Tape crease**' (_6_) and its parameters.

**Color noise**' (_7_) adds a general noise to the color of the image.

The information for color and luminance on a VHS tape was limited. With '**Chroma band**' (_8_) and '**Luma band**' (_9_) you can emulate this effect.

With '**Tape noise high**' (_10_) you can add high frequency noise to the image (and with '**Low**' add low frequency noise).

Another very common effect due to head alignment failures was bands that modified the brightness of the image. This effect can be emulated with '**AC beat**' (_11_).

With '**Bottom warp**' (_12_) you can simulate the noise in the signal that was produced in the lower part of the image due to head tracking failures.

Thanks to '**Vignette**' (_13_) you can adjust the shading effect on old CRT monitors.
<!--
You can also apply the effect on objects in the scene using the material found in '**Fronkon Games/Retro/VHS**'.

{{< image src="vhs_1.jpg" wrapper="col-6 mx-auto">}}

Simply create a '**Fronkon Games/Retro/VHS**' material and apply it to the object you want.

{{< video src="vhs_2.mp4" loop="true" autoplay="true">}}

Remember that the object to which you apply the material **must have UV coordinates**. In the example they are like this:

{{< image src="tv_uv.jpg" wrapper="col-6 mx-auto">}}

You have an example in the scene '**FronkonGames/Retro/VHS/Demo/VHS_Material_Demo**'.
-->

---
## Pixelator {#pixelator}
{{< asset-header youtube="lLxdmqDiQec" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-pixelator-292731" demo="https://fronkongames.github.io/demos-retro/pixelator/" warn="assets used in video and demo are not included">}}

'**Pixelator**' allows you to create a wide variety of retro-inspired visuals. It offers highly customizable pixelation, advanced color manipulation including posterization and dithering, unique visual effects like beveling and chromatic aberration, and a suite of color filters.

{{< image src="pixelator_0.jpg" wrapper="col-6 mx-auto">}}

#### Main control

*   **Intensity**: `float` (Range: 0.0 to 1.0, Default: 1.0)
    Controls the overall intensity of all combined Pixelator effects. An intensity of 0 means the effect is not applied.

#### Pixelation

*   **Pixelation Mode**: `enum` (Default: Rectangle)
    Determines the shape and algorithm used for pixelation.
    Available modes:
    *   `Rectangle`: Classic square/rectangular pixelation.
    *   `Circle`: Pixels are represented as circles.
    *   `Triangle`: Pixels are represented as triangles.
    *   `Diamond`: Pixels are represented as diamonds.
    *   `Hexagon`: Pixels are represented as hexagons.
    *   `Leaf`: A leaf-like pattern for pixel cells.
    *   `LED`: Simulates an LED screen display.
    *   `Knitted`: Simulates a knitted or cross-stitch pattern.

*   **Pixel Size**: `float` (Range: 0.0 to 1.0, Default: 0.75)
    Controls the perceived size of the pixels. The exact interpretation can vary slightly per mode.

##### Mode-Specific Pixelation Parameters:

*   **For `Rectangle`, `Triangle`, `Hexagon`, `Leaf` modes:**
    *   **Screen Aspect Ratio**: `bool` (Default: true)
        If true, uses the screen's aspect ratio to calculate pixel scaling. If false, `Custom Aspect Ratio` is used.
    *   **Custom Aspect Ratio**: `float` (Range: 0.2 to 5.0, Default: 1.0)
        Only used if `Screen Aspect Ratio` is false. Defines a custom aspect ratio for pixel scaling.
    *   **Pixel Scale**: `Vector2` (Default: (1,1))
        Allows non-uniform scaling of pixels along X and Y axes.

*   **For `Circle`, `LED` modes:**
    *   **Radius**: `float` (Range: 0.0 to 1.0, Default: 0.5)
        Controls the radius of the circular or LED elements within each pixel cell.
    *   **Background**: `Color` (Default: Black)
        The color shown in the gaps between circular/LED elements if their radius doesn't fill the cell.

*   **For `Knitted` mode:**
    *   **Threads**: `int` (Range: 1 to 8, Default: 3)
        Simulates the number of threads in the knitted pattern.
    *   **Pixel Scale**: `Vector2` (Default: (1,1))
        Controls the scale of the knitted pattern.

#### Gradient Mapping

Maps the screen colors to a custom gradient texture.

*   **Gradient Intensity**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    The intensity of the gradient mapping effect. 0 means disabled.
*   **Gradient**: `UnityEngine.Gradient` (Default: Grayscale gradient)
    The gradient to use for color mapping. This is baked into a texture at runtime.
*   **Luminance Min**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    The minimum input luminance that maps to the start of the gradient (for Luminance mode).
*   **Luminance Max**: `float` (Range: 0.0 to 1.0, Default: 1.0)
    The maximum input luminance that maps to the end of the gradient (for Luminance mode).
*   **Mapping Mode**: `enum` (Default: CIELAB)
    Determines how colors are mapped to the gradient.
    *   `Luminance`: Maps based on the input pixel's luminance.
    *   `CIELAB`: Maps based on perceptual color similarity in the CIELAB color space, finding the closest color in the gradient.
*   **CIELAB Samples**: `int` (Range: 2 to 64, Default: 16)
    Number of samples taken along the gradient texture when `Mapping Mode` is `CIELAB`. Higher values are more accurate but slower.
*   **Apply Luminance**: `bool` (Default: true)
    If true, the luminance of the original pixel (or mapped luminance for Luminance mode) is multiplied with the final mapped gradient color. This can preserve some of the original brightness characteristics.

'**Pixelator**' brings a tool to search through more than 6,000 palettes created by artists. Simply click on the `magnifying glass icon`.

{{< image src="pixelator_1.jpg" wrapper="col-6 mx-auto">}}

Select or use the search to find the palette you want to use and click on its name to apply it automatically.

{{< image src="pixelator_2.jpg" wrapper="col-6 mx-auto">}}

#### Dithering

Simulates colors by using patterns of a limited color palette.

*   **Dither Intensity**: `float` (Range: 0.0 to 1.0, Default: 0.5)
    The strength of the dithering effect.
*   **Pattern Scale**: `int` (Options: 2, 4, 8, Default: 4)
    The size of the Bayer matrix used for ordered dithering (2x2, 4x4, or 8x8).
*   **Threshold Scale**: `float` (Range: 0.0 to 1.0, Default: 0.75)
    Adjusts the influence of the dither pattern.
*   **Color Steps**: `int` (Range: 2 to 16, Default: 8)
    The number of discrete color steps per channel that the dithering will attempt to simulate.

#### Posterization

Reduces the number of distinct colors in the image.

*   **Posterize Intensity**: `float` (Range: 0.0 to 1.0, Default: 0.5)
    The overall strength of the posterization effect. 0 effectively disables it.
*   **RGB Steps**: `Vector3Int` (Range: 2 to 256 per channel, Default: (24,24,24))
    Number of color steps for Red, Green, and Blue channels respectively when RGB posterization is active.
*   **Luminance Steps**: `int` (Range: 2 to 256, Default: 24)
    Number of steps for the luminance channel when Luminance posterization is active.
*   **HSV Steps**: `Vector3Int` (Range H: 2-64, S: 2-32, V: 2-32, Default: (24,24,24))
    Number of color steps for Hue, Saturation, and Value channels respectively when HSV posterization is active.
*   **Gamma**: `float` (Range: 0.1 to 3.0, Default: 1.0)
    Applies gamma correction before posterization and de-correction after. Values other than 1.0 can change perceived brightness and color relationships.

#### Bevel Effect

Adds a pseudo-3D bevel based on color differences, giving a chiseled look.

*   **Bevel**: `float` (Range: 0.0 to 10.0, Default: 1.0)
    The strength and depth of the bevel effect.

#### Chromatic Aberration

Simulates lens distortion by offsetting color channels.

*   **Chromatic Aberration Intensity**: `float` (Range: 0.0 to 10.0, Default: 1.0)
    The overall strength of the chromatic aberration effect.
*   **Offset**: `Vector3` (Default: (1.0, 2.0, -1.0))
    The amount by which the Red, Green, and Blue channels are shifted, respectively.

#### Color Filters

Applies various stylistic color filters.

*   **Filters Intensity**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    The global intensity for all active color filters. Lerps between the original color and the filtered color.

*   **Sepia**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of the sepia tone filter.
*   **Cool Blue**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a cool blue tint filter.
*   **Warm**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a warm orange/yellow tint filter.
*   **Invert Color**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of the color inversion filter.
*   **Hudson**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a filter emulating the Hudson Instagram effect (cool, vignetted).
*   **Hefe**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a filter emulating the Hefe Instagram effect (high contrast, warm, vignetted).
*   **X-Pro**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a filter emulating the X-Pro II Instagram effect (high contrast, saturated, warm cast, vignette).
*   **Rise**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a filter emulating the Rise Instagram effect (soft, warm, desaturated).
*   **Toaster**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a filter emulating the Toaster Instagram effect (strong vignette, warm center, burnt edges).
*   **Infrared**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of an infrared photography simulation filter.
*   **Thermal**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a thermal camera/heat map style filter.
*   **Duotone**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of the duotone filter, which maps image luminance between two chosen colors.
    *   **Color A**: `Color` (Default: Dark Blue)
        The first color for the duotone effect (typically for darker areas).
    *   **Color B**: `Color` (Default: Bright Yellow)
        The second color for the duotone effect (typically for lighter areas).
*   **Night Vision**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a night vision goggle simulation filter.
*   **Pop Art**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a Pop Art style filter using a limited, vibrant color palette.
*   **Blueprint**: `float` (Range: 0.0 to 1.0, Default: 0.0)
    Intensity of a blueprint-style filter with edge detection.
    *   **Edge Color**: `Color` (Default: Light Blue)
        The color for detected edges in blueprint mode.
    *   **Background Color**: `Color` (Default: Dark Blue)
        The background color for blueprint mode.
    *   **Edge Threshold**: `float` (Range: 0.05 to 0.5, Default: 0.1)
        The threshold for edge detection in blueprint mode.


---
## Old Films {#oldfilms}
{{< asset-header youtube="zBwXR_i6_gw" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-old-films-241298" demo="https://fronkongames.github.io/demos-retro/oldfilms/" warn="assets used in video and demo are not included">}}

'**Old Films**' is the best way to simulate the look of any old movie.

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< image src="oldfilms_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

'**Old Films**' mimics a multitude of film manufacturers used in old films, such as Kodak, Agfa or Polaroid. To do this, it use '[Color Decision List](https://en.wikipedia.org/wiki/ASC_CDL)'. You can select the manufacturer using '**Manufacturer**' (_2_).

'**Vignette**' (_3_) adds some shadows on the edges of the screen. **Sepia**' (_4_) imitates the color that certain chemical reactions may produce over time in films and photographs. By default it is disabled.

**Grain**' (_5_) adds noise to the screen, simulating the small metallic particles that occur in films that have received a lot of light.

The following parameters cause the frame to appear to move. The first, '**Jump frame**' (_6_), causes small random instantaneous jumps. The second, '**Movement**' (_6_) causes it to move constantly.

You can also cause the brightness of the film to change with '**Blink strength**' (_7_).

The next parameter, '**Blotches**' (_8_), simulates spots on the film that are usually caused by dirt.

Something you can also see in old films are small scratches. You can simulate them with '**Scratches**' (_9_). Something similar happens with '**Lines**' (_10_).

---
## CRT TV {#crttv}
{{< asset-header youtube="UFFvtpXdUBc" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-crt-tv-241411" demo="https://fronkongames.github.io/demos-retro/crttv/" warn="assets used in video and demo are not included">}}

'**CRT TV**' makes your game look like on an old television, those with the [glass tube](https://en.wikipedia.org/wiki/Cathode-ray_tube). With more than 40 parameters, it is possibly the most configurable effect in the store.

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< image src="crttv_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

One of the technologies used by the old cathode-ray tube ('_Cathode-ray tube_' or [CRT](https://en.wikipedia.org/wiki/Cathode-ray_tube)) televisions to produce color images uses a metal plate with tiny holes through which rays pass and which, upon impacting a phosphor surface, produce a color. The rays were fired in threes to hit three areas to produce red, green and blue colors. In the distance you would see the mixture of all, giving rise to a 'pixel', but up close you could see something like this:

{{< image src="crttv_1.jpg" wrapper="col-6 mx-auto">}}

This technique is known as '[Shadow mask](https://en.wikipedia.org/wiki/Shadow_mask)' and you can control its intensity with '**Shadowmask**' (_2_). By generating black areas, the final image will be darker than the original. You can adjust with '**Luminosity**'. You can also change the grid scale using '**Scale**'.

Although it doesn't affect the final result of the image too much, you can change the order of the red, green and blue channels of each grid cell. In '**Color offset**' you can move each channel. You can also vary the hardness of the horizontal and vertical spacing of each cell with '**Horizontal hardness**' and '**Vertical hardness**' respectively.

Due to the curvature of the glass screen, the image on older televisions was distorted. In '**Fisheye**' (_3_) you can simulate this effect. Due to the geometry of the tube, the corners of the image are rounded. With '**Vignette smoothness**' (_4_) you can adjust the image deformation. If you want to adjust the borders of the screen, you can do it with '**Borders**' (one for each axis).

With '**Zoom**' you can adjust the screen size on each axis. By changing the values of '**Zoom**' with Tween functions, you can simulate the switching on and off of the TV.

The reflection on the glass screen can be controlled with '**Shine**' (_5_).

To tint the final image, you can use '**Gamma color**' (_6_) and '**Color curves**' (_7_). The first one enhances the brightest areas, while the second one is applied to the whole image. You can use the _alpha_ channel to modulate the intensity.

Another common effect on TVs is the offset of the color channels, using '**RGB offset**' (_8_) you can adjust it. Another similar effect is '**Color bleeding**' (_9_).

By using a horizontally moving ray to draw the image, a line-like pattern is produced on the screen. With '**Scanlines**' (_10_) you can configure them.

With '**Signal interference**' (_11_) you can adjust the interference that often occurs at the bottom of old TV sets.

It was also frequent to find 'jumps' in the picture on old TV sets, due to defects in the ray tracer circuitry. With '**Frame shaking**' (_12_) and '**Frame movement**' (_13_) you can simulate them.

The signal coming to the recorder was analog and could incorporate noise depending on many factors (signal quality, antenna, weather, etc.). The result was an image with '**Grain**' (_14_) and '**Static noise**' (_15_). Some circuit failures used to produce some bands that moved vertically. You can control them in '**Bar effect**' (_16_).

In '**Flicker**' (_17_) you can adjust another very common defect in TV sets which is the fluctuation of the screen brightness.
<!--
You can also apply the effect on objects in the scene using the material found in '**Fronkon Games/Retro/CRT TV**'.

{{< image src="crttv_2.jpg" wrapper="col-6 mx-auto">}}

Simply create a '**Fronkon Games/Retro/CRT TV**' material and apply it to the object you want.

{{< video src="/store/retro/crttv_3.mp4" loop="true" autoplay="true" >}}

Remember that the object to which you apply the material **must have UV coordinates**. In the example they are like this:

{{< image src="tv_uv.jpg" wrapper="col-6 mx-auto">}}

You have an example in the scene '**FronkonGames/Retro/CRTTV/Demo/CRTTV_Material_Demo**'.
-->

---
## Lo-Fi {#lofi}
{{< asset-header youtube="51rAf7z0Plg" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-lo-fi-297300" demo="https://fronkongames.github.io/demos-retro/lofi/" warn="assets used in video and demo are not included">}}

Create stunning retro-style visuals with '**Lo-Fi**'. Craft the perfect nostalgic look for your project.

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< image src="lofi_0.jpg" wrapper="col-6 mx-auto">}}

#### Master Control

*   **Intensity:** Think of this as the main volume knob for the entire effect. Slide it down towards zero to gently blend the retro vibe with your original visuals, or push it up to one for the full, unfiltered Lo-Fi experience. If you set it to zero, the effect won't run at all.

#### Palette: The Heart of Retro Color

Enable this section to transform your scene's colors using classic, limited palettes.

*   **Enable Palette:** Toggle this on to activate the color conversion process.
*   **Profile:** This is where you choose your retro color scheme. Click the search icon to open the Palette Browser and select a pre-made profile (like those mimicking old consoles or computers) or even one you've created yourself. Changing the profile tells the effect which specific set of colors to use.
*   **Mode:** How should the colors in the palette blend?
    *   `Blend`: Creates smooth transitions between the colors in the palette, like a gradient.
    *   `Fixed`: Results in sharp, distinct boundaries between colors, closer to how some very old hardware displayed graphics.
*   **Sample Method:** This determines *how* the effect decides which palette color to use for each pixel in your original scene. Different methods produce distinct looks:
    *   `Luminance`: Matches colors based purely on the brightness (luminance) of the original pixel. Good for simple, brightness-based color swaps.
        *   *Luminance Power:* Adjusts the contrast when using the Luminance method. Higher values make the brightness differences more dramatic in the final palette.
        *   *Remap Luminance:* Fine-tune which brightness range in the original image gets mapped to the palette. Drag the sliders to focus the effect on shadows, highlights, or mid-tones.
        *   *Invert:* Flips the palette order, useful for creating negative or unique film-like effects.
    *   `Distance`: Finds the palette color that is mathematically closest to the original pixel's color in standard RGB space (with perceptual weighting). A good all-around choice.
    *   `HSV`: Compares colors based on Hue, Saturation, and Value. Can be good at preserving the general *feel* of colors even when the palette is very different.
    *   `Similarity (CIELab)`: Uses a more advanced, perceptually accurate color comparison (CIELab) to find the closest match. Often gives the most visually pleasing results but is slightly more performance-intensive.
    *   `Dominant`: Looks at a small area around each pixel, finds the most prominent color, and then maps *that* color to the palette. Can create a slightly chunkier, posterized look.
*   **Color Threshold (for non-Luminance methods):** How strictly should the effect stick to the palette? Lower values mean the chosen palette color must be very close to the original; higher values allow for looser matches.
*   **Resolution:** Controls the detail level of the internal texture generated from your chosen palette profile. Higher resolutions mean smoother gradients (in `Blend` mode) and potentially more accurate color matching, but use slightly more memory. You'll see a preview of the generated palette texture below if you have a Profile selected.

#### Pixelate: Embrace the Blocks

Turn this on to give your scene that classic, low-resolution pixelated appearance.

*   **Enable Pixelate:** Activate the pixelation effect.
*   **Size:** Determines how big the pixel blocks are. Larger values mean chunkier, more abstract pixels, like zooming in on an old game sprite. The value snaps to even numbers.
*   **Blend:** How does the pixelated image combine with the original? `Solid` replaces the original, while other modes like `Multiply` or `Additive` can create interesting overlay effects.
*   **Tint:** Apply a color wash over the pixelated result. Use white for no tint, or pick a color to create monochrome or duotone styles. The alpha channel controls the tint's strength.
*   **Sobel:** Adds an edge-detection effect to the pixel blocks, giving them a subtle, pseudo-3D look.
    *   *Sobel Power:* Controls the strength of the edge effect.
    *   *Sobel Light Angle:* Sets the direction the 'light' seems to be coming from for the edge effect, influencing where highlights and shadows appear on the pixel edges.
    *   *Sobel Light Intensity:* How bright is the light source for the Sobel effect? Affects the contrast of the edges.
    *   *Sobel Ambient:* Sets a base light level, preventing the shadowed parts of the Sobel effect from becoming completely black.
*   **Round:** Smooths the corners of the pixel blocks. At 0, they are perfect squares; slide towards 1 to make them increasingly circular.
    *   *Bevel:* When `Round` is greater than zero, this adds a 3D-like bevel to the rounded pixel edges, enhancing the sense of depth.
*   **Samples:** Improves the quality of the pixelation by taking multiple samples within each original pixel area before creating the final block color. Higher values give smoother results (less jaggedness) but cost more performance. A value of 1 is the fastest but can look more aliased.

#### Scanline: CRT Monitor Vibes

*   **Scanline Intensity:** Adds horizontal lines across the screen, mimicking the look of old CRT monitors. Slide from 0 (no lines) up to 1 (strong lines).
*   **Count:** How many scanlines should appear vertically? More lines mean finer, denser scanlines.
*   **Speed:** Makes the scanlines gently scroll up or down the screen. Use negative values for upward movement, positive for downward. Zero keeps them static.

#### Screen Effects

*   **Vignette:** Darkens the corners and edges of the screen, simulating the natural light falloff on CRT displays. Higher values create a stronger, more focused center.
*   **Quantization:** Reduces the number of distinct colors visible on screen *after* other effects are applied, forcing the image into a more limited color range for an extra retro feel.
    *   *Colors:* Sets the target number of colors for the quantization process. Lower values (like 8, 16, or 32) create more noticeable color banding.
*   **Chromatic Aberration:** Introduces color fringing, especially towards the edges of the screen. This simulates the lens distortions or signal imperfections common in older display technologies.
*   **Glass Shine:** Adds a subtle, broad highlight, like light reflecting off the curved glass surface of a CRT monitor.
    *   *Shine Size:* Controls how large and diffuse the glass shine effect is.
*   **Aperture:** Simulates the physical mask or grille inside a CRT, slightly darkening the edges and creating a softer frame within the screen area. Lower values make the effect more pronounced.
*   **Curvature:** Bends the entire image outwards, mimicking the physically curved screens of old CRT monitors. Higher values create a more noticeable bulge.

#### Border: Frame Your View

*   **Enable Border:** Adds a solid border around the screen, simulating the plastic bezel of a vintage monitor or TV.
*   **Color:** Choose the color for the border. The default is a classic beige.
*   **Smooth:** Controls how soft the transition is between the screen image and the border. Higher values create a more feathered edge.
*   **Noise:** Adds a subtle noise texture to the border, giving it a slightly aged or textured look.
*   **Margins:** Adjust the thickness of the border horizontally (x) and vertically (y).

#### Using the Palette Browser

{{< image src="lofi_1.jpg" wrapper="col-6 mx-auto">}}

The Palette Browser is a handy tool designed to help you discover, manage, and apply **+6000** palettes for the Retro Lo-Fi effect directly within the Unity editor.

##### Opening the Browser

You can typically access the Palette Browser by clicking the small search icon next to the **Profile** field in the Lo-Fi effect settings in the Inspector.

##### Exploring Palettes

Once opened, the Palette Browser presents you with a list of available `LoFiProfile` assets found in your project.

###### Finding Your Palette

*   **Search Bar:** At the top right, use the search bar to quickly find palettes by typing parts of their **name** or any associated **tags**. Hit Enter or wait a moment for the list to filter. Click "Clear" to remove the search term.
*   **Sorting:** Next to the search bar, you can choose how to sort the palettes:
    *   By **Name** (A-Z or Z-A)
    *   By **Likes** (Most popular first or least popular first - *Note: 'Likes' seem to be a predefined value in the profile asset*)
    *   By **Color Count** (Fewest colors first or most colors first)
    Click "Apply Sort" after selecting your preferred order.
*   **Tag Filters:** Click the "Show Tag Filters" button to reveal a list of tags associated with the palettes. Tags are sorted by how many palettes use them.
    *   Click on one or more tags to filter the list, showing only palettes that contain *all* the selected tags.
    *   The button for a selected tag will appear highlighted. Click it again to deselect it.
    *   Click "Clear All" in the tag filter section to remove all tag selections.

###### Palette List

The main area displays the filtered and sorted palettes. Each palette entry shows:

*   **Title:** The name of the palette profile.
*   **Likes:** A small heart icon followed by a number, indicating its popularity score.
*   **Color Preview:** A horizontal strip showcasing the first 16 colors contained within the palette.
*   **Use Button:** Click this button to instantly apply the selected palette profile to the active Lo-Fi effect settings in your scene's rendering pipeline.

###### Navigation

If there are more palettes than can fit on one screen (typically 5 per page), pagination controls will appear at the bottom:

*   Use the **"◄ Previous"** and **"Next ►"** buttons to navigate between pages.
*   The text in the middle shows your current page number and the total number of pages.

##### Applying a Palette

When you find a palette you like, simply click the **"Use"** button on its entry. The browser will attempt to find the Lo-Fi effect settings in your project's Universal Render Pipeline asset and update the **Profile** field automatically.

{{< alert type="info" >}}
This requires the Lo-Fi effect to be added as a Renderer Feature in your active URP Renderer Data asset. If the effect isn't found, you'll receive a notification.
{{< /alert >}}

The Palette Browser makes it easy to experiment with different color schemes and find the perfect retro look for your project!

---
## NTSC {#ntsc}
{{< asset-header youtube="MXQ5qz31Cos" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-ntsc-321946" demo="https://fronkongames.github.io/demos-retro/ntsc/" warn="assets used in video and demo are not included">}}

This effect simulates the analog video artifacts characteristic of the [NTSC](https://en.wikipedia.org/wiki/NTSC) (National Television System Committee) broadcast standard, commonly associated with older televisions and VHS tapes in North America and Japan.

It aims to replicate visual imperfections such as color bleeding, dot crawl, scanlines (though not explicitly a parameter, it's an emergent property of NTSC emulation), phase errors, and signal noise to achieve a retro aesthetic.

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< image src="ntsc_0.jpg" wrapper="col-6 mx-auto">}}

#### NTSC Settings

*   **Intensity**: `float` [0, 1], Default: 1
    *   Controls the overall strength of the NTSC effect. A value of 0 will bypass the effect.
*   **Window Radius**: `int` [1, 64], Default: 20
    *   Controls the size of the sinc filter window used in NTSC signal processing passes. Larger values use more samples, which can improve quality by reducing aliasing and ringing artifacts but will increase computational cost.
*   **NTSC Scale**: `float` [0.1, 5.0], Default: 1.0
    *   An overall scaling factor for NTSC artifacts related to the width of pixels. This can affect the prominence of artifacts like color fringing and dot crawl.
*   **Phase Alternation**: `float` [0.0, ~PI], Default: 0.0
    *   Simulates the phase alteration per scanline, a characteristic of NTSC signals that can cause hues to shift on alternate lines. A value of 0.0 disables this, while a value close to PI (3.1415927) enables it. This is often related to the "Never The Same Color" moniker of NTSC.
*   **Noise**: `float` [0.0, 1.0], Default: 0.1
    *   Controls the amount of random TV static or signal noise added to the image.
*   **Window Bias**: `float` [-1.0, 1.0], Default: 0.0
    *   Offsets the shape of the sinc filter window. This can cause artifacts to smear or trail more to one side than the other, affecting the appearance of ringing and other signal-related distortions.

#### Encoder

These settings control the simulation of the NTSC encoding process, where the original RGB signal is converted into Luminance (Y) and Chrominance (I, Q) components and modulated onto a carrier wave.

*   **AM Carrier**: `float` [0.5, 10.0], Default: 2.0
    *   Wavelength of the Amplitude Modulation (AM) carrier signal used in the NTSC encoding pass. This influences how the luma and chroma information is combined.
*   **Wavelengths Low-Pass**:
    *   **Y LowPass**: `float` [0.1, 10.0], Default: 1.0
        *   Wavelength for the low-pass filter applied to the luminance (Y) component before encoding. Lower values retain more high-frequency detail in luminance, while higher values soften it. This affects the sharpness and can interact with color fringing.
    *   **I LowPass**: `float` [1.0, 20.0], Default: 8.0
        *   Wavelength for the low-pass filter applied to the I (in-phase) chrominance component. NTSC allocates less bandwidth to chroma, so I and Q are typically blurred. Higher values increase color smearing and reduce chroma resolution for the I component (orange-cyan axis).
    *   **Q LowPass**: `float` [1.0, 20.0], Default: 11.0
        *   Wavelength for the low-pass filter applied to the Q (quadrature) chrominance component. Similar to I LowPass, but for the Q component (green-magenta axis), which typically has even less bandwidth. Higher values increase color smearing.
*   **Colorburst**: `float` [1.0, 10.0], Default: 3.0
    *   Wavelength of the colorburst signal for the NTSC encoder pass. The colorburst is a reference signal used by the decoder to correctly interpret hues.

#### Decoder

These settings control the simulation of the NTSC decoding process, where the modulated NTSC signal is converted back into a viewable image, introducing further artifacts.

*   **AM Demodulate**: `float` [0.5, 10.0], Default: 2.0
    *   Wavelength used for AM signal demodulation in the NTSC decoding pass. This is part of separating the luma and chroma information.
*   **AM Decode HiPass**: `float` [0.5, 10.0], Default: 2.0
    *   Wavelength for the high-pass filter used during AM decoding. This helps separate the chroma information from the luma.
*   **Colorburst**: `float` [1.0, 10.0], Default: 3.0
    *   Wavelength of the colorburst signal used by the NTSC decoder pass to correctly align and interpret the chrominance information. Mismatches with the encoder can lead to color errors.
*   **Decode LowPass**: `float` [1.0, 10.0], Default: 4.5
    *   Wavelength for the low-pass filter applied during the final NTSC decoding stage. This affects the overall blurriness of the decoded signal and can reduce dot crawl and other high-frequency artifacts.

---
## Noir {#noir}
{{< asset-header youtube="U3wnxAc5Cww" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-noir-322864" demo="https://fronkongames.github.io/demos-retro/noir/" warn="assets used in video and demo are not included">}}

A comprehensive post-processing solution designed to give your projects a classic, stylized film noir aesthetic. It combines several configurable visual elements to achieve a range of looks, from subtle desaturation and mood lighting to more pronounced vintage film appearances.

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< image src="noir_0.jpg" wrapper="col-6 mx-auto">}}

#### Noir

The `Noir` parameter transforms the scene into a black and white image, offering four distinct artistic methods to simulate classic printing and display techniques. Each method provides a unique visual style, from granular dithering to structured lines and patterns.

{{< image src="noir_1.png" wrapper="col-6 mx-auto">}}

- **Dither**: This method uses an 8x8 Bayer matrix to create a dithered black and white image, simulating the look of early digital displays.
  - `Spread`: Controls the spread of the dither pattern.
  - `Density`: Adjusts the density of the dither effect.
  - `Color Blend`: Determines how the dithered pattern blends with the original image.

{{< image src="noir_2.png" wrapper="col-6 mx-auto">}}

- **Dot Screen**: Simulates the dot matrix printing technique, creating a grid of dots of varying sizes to represent shades of gray.
  - `Grid Size`: Sets the size of the dot screen grid.
  - `Luminance Gain`: Adjusts the luminance gain, affecting the size of the dots.
  - `Color Blend`: Specifies the blending mode for the dot screen effect.

{{< image src="noir_3.png" wrapper="col-6 mx-auto">}}

- **Halftone**: Mimics the halftone printing process, using dots of varying sizes and angles to create tonal variations.
  - `Size`: Controls the size of the halftone dots.
  - `Angle`: Sets the angle of the halftone pattern.
  - `Threshold`: Defines the threshold for the halftone effect.
  - `Color Blend`: Determines how the halftone pattern is blended.

{{< image src="noir_4.png" wrapper="col-6 mx-auto">}}

- **Lines**: This method uses parallel lines of varying thickness to create the black and white image, similar to an engraved or etched illustration.
  - `Count`: Sets the number of lines.
  - `Granularity`: Adjusts the granularity of the lines.
  - `Threshold`: Defines the threshold for line visibility.
  - `Color Blend`: Specifies the blending mode for the lines.

#### Duo Tone

The Duo Tone effect remaps the image's tones to a gradient between two specified colors, creating a stylized, two-color look. This is often used for dramatic and artistic visuals.

- `Intensity`: Controls the overall intensity of the Duo Tone effect.
- `Brightness Color`: Sets the color for the brighter parts of the image.
- `Darkness Color`: Sets the color for the darker parts of theimage.
- `Threshold`: Defines the midpoint between the brightness and darkness colors.
- `Luminance Min Range`: Sets the minimum luminance range for the effect.
- `Luminance Max Range`: Sets the maximum luminance range for the effect.
- `Softness`: Controls the smoothness of the transition between the two colors.
- `Exposure`: Adjusts the overall exposure of the image.
- `Emboss Dark`: Adds an embossing effect to the dark areas.
- `Color Blend`: Determines how the duo tone colors blend with the scene.

#### Sepia

The Sepia effect applies a brownish tint to the image, simulating the look of aged photographs from the early days of photography.

- `Intensity`: Controls the strength of the Sepia toning. A value of 0 means no effect, while 1 applies the full effect.

#### Chromatic Aberration

Chromatic Aberration simulates the lens artifact where different color channels are not perfectly aligned, resulting in color fringing, especially at the edges of the frame. This can add to the vintage or lo-fi feel of the image.

- `Intensity`: Adjusts the amount of color separation. Higher values increase the distance between the color channels.

#### Film Grain

This effect adds a layer of simulated film grain to the image, mimicking the texture of traditional photographic film. It can enhance the vintage look and help to reduce color banding.

- `Intensity`: Controls the visibility of the film grain.
- `Speed`: Adjusts the animation speed of the grain, creating a dynamic, flickering effect.

#### Vignette

The Vignette effect darkens the corners and edges of the screen, drawing focus to the center of the image. It's a common technique in photography and cinematography to create mood and frame the subject.

- `Intensity`: Controls the overall strength of the vignette.
- `Size`: Adjusts the size of the clear, unaffected central area.
- `Color`: Sets the color of the vignette. While typically black, other colors can be used for stylistic purposes.
- `Smoothness`: Controls the softness of the vignette's falloff, from a hard edge to a smooth gradient.
- `Time Variation`: Introduces a subtle, time-based fluctuation to the vignette's intensity, adding a dynamic quality.

#### Blotches

This effect simulates the appearance of film damage or aging by overlaying animated blotches onto the image. This can significantly enhance the retro and worn-out feel of the visuals.

- `Intensity`: Controls the visibility of the blotches.
- `Speed`: Adjusts the speed at which the blotches animate and change.

#### Scratches

The Scratches effect simulates vertical scratches on the film, another common artifact of old or damaged film reels. It adds to the authenticity of a vintage film look.

- `Intensity`: Controls the visibility and frequency of the scratches.
- `Speed`: Adjusts the animation speed of the scratches, making them flicker and move.


---
## Old Computers {#oldcomputers}
{{< asset-header youtube="_gADYOdLbL4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-old-computers-243911" demo="https://fronkongames.github.io/demos-retro/oldcomputers/" warn="assets used in video and demo are not included">}}

Emulates the color palettes of old 8-bit and 16-bit computers. You can emulate all of these systems:

* **Apple** ][: the first series of mass-produced microcomputers made by Apple (1977).
* **CGA**: Color Graphics Adapter, marketed in 1981, was IBM's first color graphics card.
* **BBC** Micro: affectionately known as the Beeb, was one of the first home computers in the UK (1981).
* **Commodore** 64: an 8-bit home computer developed by Commodore in August 1982.
* **MSX**: an 8-bit home microcomputer standard marketed during the 1980s.
* **Aquarius**: a home computer released by Mattel Electronics in 1983.
* **Amstrad CPC**: a series of 8-bit personal computers produced by Amstrad during the 1980s.
* **Atari ST**: a line of home computers introduced by the Atari company, successor to the Atari 8-bit family.
* **EGA**: stands for Enhanced Graphics Adapter, the IBM PC standard specification for graphics display (1987).
* **Mac II**: a computer model of the Apple Macintosh series that appeared in 1987.
* **Game Boy**: is a handheld game console developed Nintendo, first released in Japan and USA in 1989.

You can also define the color palette you want to emulate!

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< image src="oldcomputers_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

'**Old Computers**', is very easy to use. Simply select the computer you want to emulate in '**Computer**' (_2_). Some systems have several modes of operation.

If you want to use your own color palette, select '**Custom**'.

{{< image src="oldcomputers_1.jpg" wrapper="col-6 mx-auto">}}

You can vary the number of colors you want to use with '**Colors**' (up to a maximum of 16). It doesn't matter in which order you put them, since the algorithm used selects the color in the palette based on the _distance_ from the original color. In this way, and with the default colors, all red tones would be replaced by color number 3.

By changing '**Pixelation**' (_3_) you can adjust the pixel size and with '**Dithering**' (_4_) you can change the intensity of the '_Bayer 2x2_' pattern used for color dithering.

Some palettes may have very dark colors that cause the final result to have too many black areas. You can correct the color range used with '**Remap colors**' (_5_). By discarding the lower parts, you would ignore the darker areas. With the upper part you would discard the brighter ones. 

{{< image src="oldcomputers_2.jpg" wrapper="col-6 mx-auto">}}

Discarding the darker range:

{{< image src="oldcomputers_3.jpg" wrapper="col-6 mx-auto">}}

---
## ASCII {#ascii}
{{< asset-header youtube="shQxDDe8Aw4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-ascii-241924" demo="https://fronkongames.github.io/demos-retro/ascii/" warn="assets used in video and demo are not included">}}

The ASCII render was an effect you could see in old [demoscene](https://en.wikipedia.org/wiki/Demoscene). It consists of replacing blocks of pixels with [ASCII](https://en.wikipedia.org/wiki/ASCII) characters according to their luminosity. The higher the luminosity, the 'denser' the character it was replaced with. Now it's back on steroids!

Once installed, when you select your 'Universal Renderer Data', you will see something like this:

{{< image src="ascii_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

'**ASCII**' needs a texture with characters from a [monospaced font](https://en.wikipedia.org/wiki/Monospaced_font). To create one use the '**ASCII Charset Tool**' (or menu _Window > Fronkon Games > Retro > ASCII > ASCII Charset Tool_). With this tool you can create the necessary file to set it to '**Charset**'.

{{< image src="ascii_1.jpg" wrapper="col-8 mx-auto">}}

This tool will show you all the monospaced fonts you have on your system. If you don't have any, install one and click on '**Refresh**'. In addition to selecting the size of the characters in '**Size**', you can select the pattern to be used. As I mentioned before, this effect replaces blocks of pixels with characters according to their luminosity. The brighter the blocks, the more pixels the characters will be. The most common patterns are included in the tool, but you can use your own by selecting '_Custom_'.

{{< alert type="info" >}}
All patterns start from the lowest luminosity, or density, to the highest. For example, a 10-character pattern represents 10 levels of brightness: " .:-=++*#%@".
{{< /alert >}}

#### Selection Mode

'**Selection mode**' determines how characters are chosen for each cell:

- **Luminance** (default): The classic method. Characters are selected based solely on the average brightness of each cell. Fast and compatible with all charsets.

{{< image src="ascii_luminance.jpg" wrapper="col-8 mx-auto">}}

- **Shape Aware**: A revolutionary approach that considers the *spatial distribution* of brightness within each cell, not just overall luminance. Each cell is divided into a 2×3 grid, and the algorithm finds characters whose shape best matches the image content. This produces dramatically sharper edges and better detail preservation.

{{< image src="ascii_shape_aware.jpg" wrapper="col-8 mx-auto">}}

{{< alert color="warning" >}}
'Shape Aware' mode requires charsets generated with version 3.0 or later. Older charsets will need to be regenerated using the ASCII Charset Tool.
{{< /alert >}}

When using ShapeAware mode:
- **Shape weight** [0-1]: Balance between shape matching and density. Higher values (default 0.7) prioritize shape matching for sharper results.

#### Edge Detection

Enable '**Edge detection**' to apply Sobel edge detection for sharper character boundaries. This feature works in both Luminance and ShapeAware modes.

- **Sensitivity** [0-2]: How easily edges are detected. Higher values detect more subtle edges.
- **Contrast** [0-2]: Edge contrast enhancement strength. Higher values create more dramatic edge enhancement.

{{< image src="ascii_edge_detection.jpg" wrapper="col-8 mx-auto">}}

#### Supersampling

Enable '**Supersampling**' for smoother anti-aliased edges. Instead of taking a single sample per cell, this takes multiple samples and averages them.

- **Quality** [2-4]: The supersampling level:
  - 2 = 2×2 grid (4 samples per cell)
  - 3 = 3×3 grid (9 samples per cell)
  - 4 = 4×4 grid (16 samples per cell)

{{< image src="ascii_super_sampling.jpg" wrapper="col-8 mx-auto">}}

{{< alert type="info" >}}
Higher supersampling quality produces smoother results but requires more processing power. Level 2 offers a good balance between quality and performance.
{{< /alert >}}

#### Basic Settings

Once you have created the charsets you want and have it set in '**Charsets**' we can continue with the following parameters. With '**Zoom**' you can change the scale of each text block, the more you zoom the bigger the characters will appear.

You can multiply with '**Boost**' the brightness that is calculated to use one character or another. With very high values, you will see more characters from the end of the pattern used.

If '**Block colour**' is active, each block of each character will have a unique colour (result of pixelating that area). If it is not active, the original colours will be respected. This makes the shapes of the original image more distinguishable.

{{< image src="ascii_2.png" >}}

With '**Font**' you can change how the color of each character is _mixed_ with the original pixels. These operations are very similar to the one you can find in _Photoshop_. You can also change their color. The same can be done with the background.

{{< alert type="info">}}
As this effect can generate a lot of black pixels, the final image can be darker than the original. Turn up the brightness of the "**Background**" color a bit to avoid this.
{{< /alert >}}

By default, there is no color gradient for the final image, but you can select several in '**Color gradient**'.

---
## Spectrum {#spectrum}
{{< asset-header youtube="d66etIztDjs" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-spectrum-239827" demo="https://fronkongames.github.io/demos-retro/spectrum/" warn="assets used in video and demo are not included">}}

'**Spectrum**' simulates the graphical style of old games of the mythical 8-bit microcomputer [Sinclair ZX Spectrum](https://en.wikipedia.org/wiki/ZX_Spectrum) from 1982.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="spectrum_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

**Simulation**' (_2_) allows you to use two simulation modes. The first, 'Simple' (default), only simulates the color palette. The second, 'Full', also emulates the screen resolution.

{{< image src="spectrum_1.jpg" wrapper="col-6 mx-auto">}}

To change the pixel size, use '**Pixel size**' (_3_) and to adjust the pattern size use '**Dither**' (_4_).

**Spectrum**' uses the image brightness for many calculations, if your scene is too dark (or too bright), you can adjust the brightness range used in '**Brightness levels**' (_5_). You can also modify the initial gamma with '**Adjust gamma**' (_7_).

---
## LCD {#lcd}
{{< asset-header youtube="huKT3CiRfRA" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-spectrum-239827" demo="https://fronkongames.github.io/demos-retro/lcd/" warn="assets used in video and demo are not included">}}

Simulates the distinct visual characteristics of a [Liquid Crystal Display](https://en.wikipedia.org/wiki/Liquid-crystal_display) (LCD), such as those found on older handheld games, digital watches, or early portable computers.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="lcd_0.jpg" wrapper="col-6 mx-auto">}}

#### General Settings

* **Intensity**: `float` [0, 1], Default: 1.0. Controls the overall strength of the entire LCD effect. A value of 0 will effectively bypass the effect.

#### Grid Settings

* **Grid Intensity**: `float` [0, 1], Default: 0.9. Controls the visibility of the pixel grid.
* **Grid Color**: `Color`, Default: Black. The RGB color of the physical grid structure. Alpha is not typically used.
* **Grid Size**: `float` [1, 4], Default: 2.0. The size of the pixels, acting as grid line thickness.
* **Grid Bevel**: `float` [0, 2], Default: 0.5. Controls the softness of the subpixel dot edges. Higher values create softer, wider transitions, affecting the perceived bevel of the grid.
* **Subpixel Layout**: `enum` { RGB, BGR }, Default: RGB. The ordering of color components within each pixel: RGB (standard) or BGR (swapped red and blue).
* **Subpixel Tiling Factor**: `Vector2`, Default: (3.0, 1.0). Controls the horizontal and vertical tiling of subpixels.
* **Jitter Intensity**: `float` [0, 2], Default: 0.0. Intensity of UV jitter to reduce moiré patterns, may introduce noise.

#### Blacklight Settings

* **Bleed Intensity**: `float` [0, 1], Default: 0.0. Overall strength of the backlight bleed effect.
* **Bleed Focus**: `float` [0, 1], Default: 0.5. Controls concentration of the bleed: 0 for edges, 1 for center, 0.5 for even.
* **Bleed Color**: `Color`, Default: (0.1, 0.1, 0.1, 0.0) (Subtle Gray). Color of the backlight bleed.

#### Dead pixels Settings

* **Dead Subpixel Density**: `float` [0, 1], Default: 0.0. Density of dead subpixels (0 = none, 1 = very high).
* **Dead Subpixel Seed**: `int`, Default: 0. Seed for the dead subpixel pattern.
* **Dead Subpixel Color**: `Color`, Default: Black. Color of a dead subpixel.

#### Misc Settings

* **Color Correction Intensity**: `float` [0, 1], Default: 1.0. Intensity of the color correction effect.
* **Color Bands Intensity**: `float` [0, 1], Default: 0.5. Intensity of the color bands effect.
* **Color Bands Brightness**: `float` [0, 10], Default: 4.0. Brightness of the color bands effect.

---
## Vintage Filters {#vintagefilters}
{{< asset-header youtube="YXMNQn7cu8I" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-vintage-filters-242600" demo="https://fronkongames.github.io/demos-retro/vintagefilters/" warn="assets used in video and demo are not included">}}

A great collection of vintage filters inspired by photo Instagram effects:

* **70s**: looks like it's on a old 70's TV.
* **Aden**: makes games look pastel shades.
* **Amaro**: adds more light to the centre of the screen and darkens around the edges.
* **Brannan**: this low-key effect brings out the grays and greens in your game.
* **Crema**: makes games look creamy and smooth.
* **Earlybird**: a retro 'Polaroid' feel with soft faded colors and a hint of yellow.
* **Hefe**: slightly increases saturation and gives a warm fuzzy tone to your game.
* **Hudson**: emphasizes light and gives your game a bluish, colder feel.
* **Inkwell**: adds high contrast and also makes black and white.
* **Juno**: it tints cool tones green, amps up warm tones, and makes whites glow.
* **Lomofi**: a dreamy, blurry effect and saturated colors.
* **LordKevin**: a retro look by boosting the earth tones green, brown and orange and adds brightness.
* **Nashville**: a warm retro fell and adds a soft purple-pink hue.
* **Reyes**: desaturates your game, brightens it up, and gives it an old-time feel.
* **Rise**: a nice glow and warmth by adding yellow tones.
* **Sierra**: makes the game appear softer by adding bluish tones while emphasizing darks and yellows.
* **Slumber**: desaturate the game and makes them hazy and dreamy look.
* **Sutro**: gives you Sepia-like tones, with an emphasis on purple and brown.
* **Toaster**: a burnt, aged look. It also adds a slight texture plus vignetting.
* **Valencia**: a slight faded, 1980’s touch by adding a light brown and gray tint.
* **Walden**: washed-out, bluish colors and adds a slight corner vignetting.
* **XProII**: a warm vintage feeling and saturated tones.

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< image src="vintagefilters_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

**Vintage Filters**', is very easy to use. Simply select the filter you want to use in '**Filter**' (_2_). Although most of them do not have them, in some filters you will see some options (_3_). In _4_ you will see a brief description of the selected filter.

The filters '_70s_', '_Aden_', '_Crema_', '_Juno_', '_Kings_' and '_Slumber_' use [LUT](https://en.wikipedia.org/wiki/Lookup_table) 3D textures. If the device does not support 3D textures, a simplified 2D version is used automatically. **If you don't want to use 3D textures**, disable the '**Use 3D textures**' option in '**Advanced**'.

{{< image src="vintagefilters_1.jpg" wrapper="col-6 mx-auto">}}

---
## Handheld 8-bit {#handheld8bit}
{{< asset-header youtube="muFs-_hRCVc" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-handheld-8-bit-239924" demo="https://fronkongames.github.io/demos-retro/handheld8bit/" >}}

With '**Handheld 8-Bit**' you will get the look of the famous handheld console [Nintendo Game Boy](https://en.wikipedia.org/wiki/Game_Boy), introduced in Japan in 1989 and a year later in the rest of the world.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="handheld8bit_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

**Simulation**' (_2_) allows you to use two simulation modes. The first, '**Full**' (default), emulates the complete look. The second, '**Simple**', uses a dither algorithm to obtain a simplified (but faster than the first) version of the console look.

{{< image src="handheld8bit_1.jpg" wrapper="col-6 mx-auto">}}

To change the pixel size, use '**Pixel size**' (_3_) and to adjust the luminosity use '**Luminosity**' (_4_). You can also adjust the brightness balance with '**Threshold**' (_5_).

Although the color palette used by the effect is perfect to emulate the console, you may want to change some (or all) colors. You can do this in '**Palette colors**' (_6_). Note that they should be sorted by luminance, with the darkest colors first and the lightest at the end.

In '**Full**' simulation mode, you can also adjust the grid color with '**Grid color**' (_7_). Use the alpha channel of the color to modulate its intensity.

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
