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

'**Retro**' is a great collection of retro effects, simple to use and with many configuration options. It consists of the following effects:

* [VHS](#vhs), mimic VHS as true as possible.
* [Old Films](#oldfilms), the best way to replicate the look of old movies.
* [CRT TV](#crttv), the most configurable old TV effect you'll ever find.
* [Old Computers](#oldcomputers), emulates the color palettes of old 8-bit and 16-bit computers.
* [ASCII](#ascii), the old-school ASCII effect with steroids.
* [Spectrum](#spectrum), mimics the legendary ZX Spectrum 8-bits computer from 1982.
* [Vintage Filters](#vintagefilters), a great collection of vintage filters inspired by Instagram effects.
* [Handheld 8-Bit](#handheld8bit), imitates the graphics of the 8-bit handheld consoles of the late 1980s.

{{< alert color="light" >}}
You can obtain each effect separately (**for only $8!**), but if you want multiple effects, you might be interested in **'[RETRO BUNDLE](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-bundle-245493?aid=1101l9zFC&utm_source=aff)'** where you can find them all at a special price!
{{< /alert >}}

## Requirements

All '**Retro**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP), which means they will **not work** with Built-In, or HDRP.

You will need to have URP version **12.1.15** or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Retro**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< image src="editor_0.jpg" wrapper="col-6 mx-auto">}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< image src="editor_1.jpg" wrapper="col-6 mx-auto">}}

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
Spectrum.Settings settings = Spectrum.GetSettings();

settings.intensity = 0.5f;
```

If you are using an effect other than '**Spectrum**' just change it to its name. Check the source code comments for more information.

{{< alert color="warning" icon="fas triangle-exclamation" >}}
Do not use the code of the demos in your projects, they are only there to show you the use of the effect through code.
{{< /alert >}}

#
---
## VHS {#vhs}
{{< asset-header youtube="LH9KDnOq0dg" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-vhs-244944" demo="https://fronkongames.github.io/demos-retro/vhs/" demo2="https://fronkongames.github.io/demos-retro/vhs_material/">}}

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

You can also apply the effect on objects in the scene using the material found in '**Fronkon Games/Retro/VHS**'.

{{< image src="vhs_1.jpg" wrapper="col-6 mx-auto">}}

Simply create a '**Fronkon Games/Retro/VHS**' material and apply it to the object you want.

{{< video src="vhs_2.mp4" loop="true" autoplay="true">}}

Remember that the object to which you apply the material **must have UV coordinates**. In the example they are like this:

{{< image src="tv_uv.jpg" wrapper="col-6 mx-auto">}}

You have an example in the scene '**FronkonGames/Retro/VHS/Demo/VHS_Material_Demo**'.

---
## Old Films {#oldfilms}
{{< asset-header youtube="zBwXR_i6_gw" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-old-films-241298" demo="https://fronkongames.github.io/demos-retro/oldfilms/" >}}

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
{{< asset-header youtube="UFFvtpXdUBc" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-crt-tv-241411" demo="https://fronkongames.github.io/demos-retro/crttv/" demo2="https://fronkongames.github.io/demos-retro/crttv_material/">}}

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

You can also apply the effect on objects in the scene using the material found in '**Fronkon Games/Retro/CRT TV**'.

{{< image src="crttv_2.jpg" wrapper="col-6 mx-auto">}}

Simply create a '**Fronkon Games/Retro/CRT TV**' material and apply it to the object you want.

{{< video src="/store/retro/crttv_3.mp4" loop="true" autoplay="true" >}}

Remember that the object to which you apply the material **must have UV coordinates**. In the example they are like this:

{{< image src="tv_uv.jpg" wrapper="col-6 mx-auto">}}

You have an example in the scene '**FronkonGames/Retro/CRTTV/Demo/CRTTV_Material_Demo**'.

---
## Old Computers {#oldcomputers}
{{< asset-header youtube="_gADYOdLbL4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-old-computers-243911" demo="https://fronkongames.github.io/demos-retro/oldcomputers/" >}}

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
{{< asset-header youtube="shQxDDe8Aw4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-ascii-241924" demo="https://fronkongames.github.io/demos-retro/ascii/" >}}

The ASCII render was an effect you could see in old [demoscene](https://en.wikipedia.org/wiki/Demoscene). It consists of replacing blocks of pixels with [ASCII](https://en.wikipedia.org/wiki/ASCII) characters according to their luminosity. The higher the luminosity, the 'denser' the character it was replaced with. Now it's back on steroids!

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< image src="ascii_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

'**ASCII**' needs a texture with characters from a [monospaced font](https://en.wikipedia.org/wiki/Monospaced_font). To create one use the '**ASCII Charset Tool**' (by clicking on _9_ or in the menu _Window > Fronkon Games > Retro > ASCII > ASCII Charset Tool_). With this tool you can create the necessary file to set it to '**Charset**' (_2_).

{{< image src="ascii_1.jpg" wrapper="col-6 mx-auto">}}

This tool will show you all the monospaced fonts you have on your system. If you don't have any, install one and click on '**Refresh**'. In addition to selecting the size of the characters in '**Size**', you can select the pattern to be used. As I mentioned before, this effect replaces blocks of pixels with characters according to their luminosity. The brighter the blocks, the more pixels the characters will be. The most common patterns are included in the tool, but you can use your own by selecting '_Custom_'.

{{< alert type="info" >}}
All patterns start from the lowest luminosity, or density, to the highest. For example, a 10-character pattern represents 10 levels of brightness: " .:-=++*#%@".
{{< /alert >}}

Once you have created the charsets you want and have it set in '**Charsets**' (_2_) we can continue with the following parameters. With '**Zoom**' (_3_) you can change the scale of each text block, the more you zoom the bigger the characters will appear.

You can multiply with '**Boost**' (_4_) the brightness that is calculated to use one character or another. With very high values, you will see more characters from the end of the pattern used.

If '**Block colour**' (_5_) is active, each block of each character will have a unique colour (result of pixelating that area). If it is not active, the original colours will be respected. This makes the shapes of the original image more distinguishable.

{{< image src="ascii_2.png" >}}

With '**Font**' (_6_) you can change how the color of each character is _mixed_ with the original pixels. These operations are very similar to the one you can find in _Photoshop_. You can also change their color. The same can be done with the background (_7_).

{{< alert type="info">}}
As this effect can generate a lot of black pixels, the final image can be darker than the original. Turn up the brightness of the "**Background**" color (_7_) a bit to avoid this.
{{< /alert >}}

By default, there is no color gradient for the final image, but you can select several in '**Color gradient**' (_8_).

---
## Spectrum {#spectrum}
{{< asset-header youtube="d66etIztDjs" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-spectrum-239827" demo="https://fronkongames.github.io/demos-retro/spectrum/" >}}

'**Spectrum**' simulates the graphical style of old games of the mythical 8-bit microcomputer [Sinclair ZX Spectrum](https://en.wikipedia.org/wiki/ZX_Spectrum) from 1982.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="spectrum_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

**Simulation**' (_2_) allows you to use two simulation modes. The first, 'Simple' (default), only simulates the color palette. The second, 'Full', also emulates the screen resolution.

{{< image src="spectrum_1.jpg" wrapper="col-6 mx-auto">}}

To change the pixel size, use '**Pixel size**' (_3_) and to adjust the pattern size use '**Dither**' (_4_).

**Spectrum**' uses the image brightness for many calculations, if your scene is too dark (or too bright), you can adjust the brightness range used in '**Brightness levels**' (_5_). You can also modify the initial gamma with '**Adjust gamma**' (_7_).

---
## Vintage Filters {#vintagefilters}
{{< asset-header youtube="YXMNQn7cu8I" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/retro-vintage-filters-242600" demo="https://fronkongames.github.io/demos-retro/vintagefilters/" >}}

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

All '**Spice Up**' effects have a panel, '**Color**', in which you can modify the final color of the effect.

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
