---
title: "Retro"
date: 2022-11-23T12:23:10+06:00
image: /store/retro/mini.png
logo: /store/retro/logo.png
#demo: https://fronkongames.github.io/store/demos/one-bit/
#store: https://assetstore.unity.com/packages/slug/216000
#youtube: https://www.youtube.com/watch?v=WY10wS39GDw
description: "A collection of retro effects for your games"
type: "store"
---

'**Retro**' is a great collection of retro effects, simple to use and with many configuration options. It consists of the following effects:

* [Spectrum](#spectrum), mimics the legendary ZX Spectrum 8-bits computer from 1982.
* [Handheld 8-Bit](#handheld8bit), imitates the graphics of the 8-bit handheld consoles of the late 1980s.
* [Old Films](#oldfilms), the best way to replicate the look of old movies.
* [CRT TV](#crttv), the most configurable old TV effect you'll ever find.
* [ASCII](#ascii), the old-school ASCII effect with steroids.
* [Vintage Filters](#vintagefilters), a great collection of vintage filters inspired by Instagram effects.
* [Old Computers](#oldcomputers), emulates the color palettes of old 8-bit and 16-bit computers.

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Requirements

All '**Retro**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP)', which means they will **not work** with Built-In, or HDRP.

You will need to have URP version 12.1 or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Retro**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< imagecenter src="/store/retro/editor_0.jpg" >}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< imagecenter src="/store/retro/editor_1.jpg" >}}

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Using them in code

You can also handle '**Retro**' effects by code. The first thing you will have to do is to add the namespace of the effect you want to use.

They are all of the style 'FronkonGames.Retro.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**Spectrum**' the code would be:

{{< highlight csharp "linenos=false" >}}
using FronkonGames.Retro.Spectrum;
{{< /highlight >}}
</br>

And with this code you could check if the effect is added, and if it is not, add it.

{{< highlight csharp "linenos=false" >}}
if (Spectrum.IsInRenderFeatures() == false)
    Spectrum.AddRenderFeature();
{{< /highlight >}}
</br>

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

{{< highlight csharp "linenos=false" >}}
 Spectrum.Settings settings = Spectrum.GetSettings();

 settings.intensity = 0.5f;
 {{< /highlight >}}
</br>

If you are using an effect other than '**Spectrum**' just change it to its name. Check the source code comments for more information.

# {#spectrum}
{{< rawhtml >}}</br></br></br>{{< /rawhtml >}}

{{< imagecenter src="/store/retro/spectrum.jpg" >}}

{{< rawhtml >}}
<div class="text-center">
    <a href="https://fronkongames.github.io/store/demos/spectrum/" class="btn btn-default">🕹️ Demo</a>
    <a href="https://assetstore.unity.com/packages/slug/239827" class="btn btn-default">🛒 Store</a>
</div>
</br>
{{< /rawhtml >}}

'**Spectrum**' simulates the graphical style of old games of the mythical 8-bit microcomputer [Sinclair ZX Spectrum](https://en.wikipedia.org/wiki/ZX_Spectrum) from 1982.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/retro/spectrum_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

**Simulation**' (_2_) allows you to use two simulation modes. The first, 'Simple' (default), only simulates the color palette. The second, 'Full', also emulates the screen resolution.

{{< imagecenter src="/store/retro/spectrum_1.jpg" >}}

To change the pixel size, use '**Pixel size**' (_3_) and to adjust the pattern size use '**Dither**' (_4_).

**Spectrum**' uses the image brightness for many calculations, if your scene is too dark (or too bright), you can adjust the brightness range used in '**Brightness levels**' (_5_). You can also modify the initial gamma with '**Adjust gamma**' (_7_).

Finally, if you click on '**documentation**' (_7_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_8_). If you need to reset all the effect values, click on '**Reset**' (_9_).

# {#handheld8bit}
{{< rawhtml >}}</br></br></br>{{< /rawhtml >}}

{{< imagecenter src="/store/retro/handheld8bit.jpg" >}}

{{< rawhtml >}}
<div class="text-center">
    <a href="https://fronkongames.github.io/store/demos/handheld8bit/" class="btn btn-default">🕹️ Demo</a>
    <a href="https://assetstore.unity.com/packages/slug/239924" class="btn btn-default">🛒 Store</a>
</div>
</br>
{{< /rawhtml >}}

With '**Handheld 8-Bit**' you will get the look of the famous handheld console [Nintendo Game Boy](https://en.wikipedia.org/wiki/Game_Boy), introduced in Japan in 1989 and a year later in the rest of the world.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/retro/handheld8bit_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

**Simulation**' (_2_) allows you to use two simulation modes. The first, '**Full**' (default), emulates the complete look. The second, '**Simple**', uses a dither algorithm to obtain a simplified (but faster than the first) version of the console look.

{{< imagecenter src="/store/retro/handheld8bit_1.jpg" >}}

To change the pixel size, use '**Pixel size**' (_3_) and to adjust the luminosity use '**Luminosity**' (_4_). You can also adjust the brightness balance with '**Threshold**' (_5_).

Although the color palette used by the effect is perfect to emulate the console, you may want to change some (or all) colors. You can do this in '**Palette colors**' (_6_). Note that they should be sorted by luminance, with the darkest colors first and the lightest at the end.

In '**Full**' simulation mode, you can also adjust the grid color with '**Grid color**' (_7_). Use the alpha channel of the color to modulate its intensity.

Finally, if you click on '**documentation**' (_8_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_9_). If you need to reset all the effect values, click on '**Reset**' (_10_).

# {#oldfilms}
{{< rawhtml >}}</br></br></br>{{< /rawhtml >}}

{{< imagecenter src="/store/retro/oldfilms.jpg" >}}

{{< rawhtml >}}
<div class="text-center">
    <a href="https://fronkongames.github.io/store/demos/oldfilms/" class="btn btn-default">🕹️ Demo</a>
    <a href="https://assetstore.unity.com/packages/slug/241298" class="btn btn-default">🛒 Store</a>
</div>
</br>
{{< /rawhtml >}}

'**Old Films**' is the best way to simulate the look of any old movie.

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< imagecenter src="/store/retro/oldfilms_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

'**Old Films**' mimics a multitude of film manufacturers used in old films, such as Kodak, Agfa or Polaroid. To do this, it use '[Color Decision List](https://en.wikipedia.org/wiki/ASC_CDL)'. You can select the manufacturer using '**Manufacturer**' (_2_).

'**Vignette**' (_3_) adds some shadows on the edges of the screen. **Sepia**' (_4_) imitates the color that certain chemical reactions may produce over time in films and photographs. By default it is disabled.

**Grain**' (_5_) adds noise to the screen, simulating the small metallic particles that occur in films that have received a lot of light.

The following parameters cause the frame to appear to move. The first, '**Jump frame**' (_6_), causes small random instantaneous jumps. The second, '**Movement**' (_6_) causes it to move constantly.

You can also cause the brightness of the film to change with '**Blink strength**' (_7_).

The next parameter, '**Blotches**' (_8_), simulates spots on the film that are usually caused by dirt.

Something you can also see in old films are small scratches. You can simulate them with '**Scratches**' (_9_). Something similar happens with '**Lines**' (_10_).

Finally, if you click on '**documentation**' (_11_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_12_). If you need to reset all the effect values, click on '**Reset**' (_13_).

# {#crttv}
{{< rawhtml >}}</br></br></br>{{< /rawhtml >}}

{{< imagecenter src="/store/retro/crttv.jpg" >}}

{{< rawhtml >}}
<div class="text-center">
    <a href="https://fronkongames.github.io/store/demos/crttv/" class="btn btn-default">🕹️ Demo</a>
    <a href="https://assetstore.unity.com/packages/slug/241411" class="btn btn-default">🛒 Store</a>
</div>
</br>
{{< /rawhtml >}}

'**CRT TV**' makes your game look like on an old television, those with the [glass tube](https://en.wikipedia.org/wiki/Cathode-ray_tube). With more than 40 parameters, it is possibly the most configurable effect in the store.

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< imagecenter src="/store/retro/crttv_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

One of the technologies used by the old cathode-ray tube ('_Cathode-ray tube_' or [CRT](https://en.wikipedia.org/wiki/Cathode-ray_tube)) televisions to produce color images uses a metal plate with tiny holes through which rays pass and which, upon impacting a phosphor surface, produce a color. The rays were fired in threes to hit three areas to produce red, green and blue colors. In the distance you would see the mixture of all, giving rise to a 'pixel', but up close you could see something like this:

{{< imagecenter src="/store/retro/crttv_1.jpg" >}}

This technique is known as '[Shadow mask](https://en.wikipedia.org/wiki/Shadow_mask)' and you can control its intensity with '**Shadowmask**' (_2_). By generating black areas, the final image will be darker than the original. You can adjust with '**Luminosity**'. You can also change the grid scale using '**Scale**'.

Although it doesn't affect the final result of the image too much, you can change the order of the red, green and blue channels of each grid cell. In '**Color offset**' you can move each channel. You can also vary the hardness of the horizontal and vertical spacing of each cell with '**Horizontal hardness**' and '**Vertical hardness**' respectively.

Due to the curvature of the glass screen, the image on older televisions was distorted. In '**Fisheye**' (_3_) you can simulate this effect. Due to the geometry of the tube, the corners of the image are rounded. With '**Vignette smoothness**' (_4_) you can adjust the image deformation.

> With '**Zoom**' you can simulate the switching on and off of the TV.

The reflection on the glass screen can be controlled with '**Shine**' (_5_).

To tint the final image, you can use '**Gamma color**' (_6_) and '**Color curves**' (_7_). The first one enhances the brightest areas, while the second one is applied to the whole image. You can use the _alpha_ channel to modulate the intensity.

Another common effect on TVs is the offset of the color channels, using '**RGB offset**' (_8_) you can adjust it. Another similar effect is '**Color bleeding**' (_9_).

By using a horizontally moving ray to draw the image, a line-like pattern is produced on the screen. With '**Scanlines**' (_10_) you can configure them.

With '**Signal interference**' (_11_) you can adjust the interference that often occurs at the bottom of old TV sets.

It was also frequent to find 'jumps' in the picture on old TV sets, due to defects in the ray tracer circuitry. With '**Frame shaking**' (_12_) and '**Frame movement**' (_13_) you can simulate them.

The signal coming to the recorder was analog and could incorporate noise depending on many factors (signal quality, antenna, weather, etc.). The result was an image with '**Grain**' (_14_) and '**Static noise**' (_15_). Some circuit failures used to produce some bands that moved vertically. You can control them in '**Bar effect**' (_16_).

In '**Flicker**' (_17_) you can adjust another very common defect in TV sets which is the fluctuation of the screen brightness.

Finally, if you click on '**documentation**' (_20_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_21_). If you need to reset all the effect values, click on '**Reset**' (_22_).

# {#ascii}
{{< rawhtml >}}</br></br></br>{{< /rawhtml >}}

{{< imagecenter src="/store/retro/ascii.jpg" >}}

{{< rawhtml >}}
<div class="text-center">
    <a href="https://fronkongames.github.io/store/demos/ascii/" class="btn btn-default">🕹️ Demo</a>
    <a href="https://assetstore.unity.com/packages/slug/241924" class="btn btn-default">🛒 Store</a>
</div>
</br>
{{< /rawhtml >}}

The ASCII render was an effect you could see in old [demoscene](https://en.wikipedia.org/wiki/Demoscene). It consists of replacing blocks of pixels with [ASCII](https://en.wikipedia.org/wiki/ASCII) characters according to their luminosity. The higher the luminosity, the 'denser' the character it was replaced with. Now it's back on steroids!

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< imagecenter src="/store/retro/ascii_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

'**ASCII**' needs a texture with characters from a [monospaced font](https://en.wikipedia.org/wiki/Monospaced_font). To create one use the '**ASCII Charset Tool**' (by clicking on _9_ or in the menu _Window > Fronkon Games > Retro > ASCII > ASCII Charset Tool_). With this tool you can create the necessary file to set it to '**Charset**' (_2_).

{{< imagecenter src="/store/retro/ascii_1.jpg" >}}

This tool will show you all the monospaced fonts you have on your system. If you don't have any, install one and click on '**Refresh**'. In addition to selecting the size of the characters in '**Size**', you can select the pattern to be used. As I mentioned before, this effect replaces blocks of pixels with characters according to their luminosity. The brighter the blocks, the more pixels the characters will be. The most common patterns are included in the tool, but you can use your own by selecting '_Custom_'.

> All patterns start from the lowest luminosity, or density, to the highest. For example, a 10-character pattern represents 10 levels of brightness: " .:-=++*#%@".

Once you have created the charsets you want and have it set in '**Charsets**' (_2_) we can continue with the following parameters. With '**Zoom**' (_3_) you can change the scale of each text block, the more you zoom the bigger the characters will appear.

You can multiply with '**Boost**' (_4_) the brightness that is calculated to use one character or another. With very high values, you will see more characters from the end of the pattern used.

If '**Block colour**' (_5_) is active, each block of each character will have a unique colour (result of pixelating that area). If it is not active, the original colours will be respected. This makes the shapes of the original image more distinguishable.

{{< imagecenter src="/store/retro/ascii_2.png" >}}

With '**Font**' (_6_) you can change how the color of each character is _mixed_ with the original pixels. These operations are very similar to the one you can find in _Photoshop_. You can also change their color. The same can be done with the background (_7_).

> As this effect can generate a lot of black pixels, the final image can be darker than the original. Turn up the brightness of the "**Background**" color (_7_) a bit to avoid this.

By default, there is no color gradient for the final image, but you can select several in '**Color gradient**' (_8_).

Finally, if you click on '**documentation**' (_10_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_11_). If you need to reset all the effect values, click on '**Reset**' (_12_).

# {#vintagefilters}
{{< rawhtml >}}</br></br></br>{{< /rawhtml >}}

{{< imagecenter src="/store/retro/vintagefilters.jpg" >}}

{{< rawhtml >}}
<div class="text-center">
    <a href="https://fronkongames.github.io/store/demos/vintagefilters/" class="btn btn-default">🕹️ Demo</a>
    <a href="https://assetstore.unity.com/packages/slug/242600" class="btn btn-default">🛒 Store</a>
</div>
</br>
{{< /rawhtml >}}

A great collection of vintage filters inspired by photo Instagram effects. Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< imagecenter src="/store/retro/vintagefilters_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

**Vintage Filters**', is very easy to use. Simply select the filter you want to use in '**Filter**' (_2_). Although most of them do not have them, in some filters you will see some options (_3_). In _4_ you will see a brief description of the selected filter.

The filters '_70s_', '_Aden_', '_Crema_', '_Juno_', '_Kings_' and '_Slumber_' use [LUT](https://en.wikipedia.org/wiki/Lookup_table) 3D textures. If the device does not support 3D textures, a simplified 2D version is used automatically. **If you don't want to use 3D textures**, disable the '**Use 3D textures**' option in '**Advanced**'.

{{< imagecenter src="/store/retro/vintagefilters_1.jpg" >}}

Finally, if you click on '**documentation**' (_5_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_6_). If you need to reset all the effect values, click on '**Reset**' (_7_).

# {#oldcomputers}
{{< rawhtml >}}</br></br></br>{{< /rawhtml >}}

{{< imagecenter src="/store/retro/oldcomputers.jpg" >}}

{{< rawhtml >}}
<div class="text-center">
    <a href="https://fronkongames.github.io/store/demos/oldcomputers/" class="btn btn-default">🕹️ Demo</a>
    <a href="https://assetstore.unity.com/packages/slug/243911" class="btn btn-default">🛒 Store</a>
</div>
</br>
{{< /rawhtml >}}

Emulates the color palettes of old 8-bit and 16-bit computers. You can emulate all of these systems:

* Apple ][: the first series of mass-produced microcomputers made by Apple (1977).
* CGA: Color Graphics Adapter, marketed in 1981, was IBM's first color graphics card.
* BBC Micro: affectionately known as the Beeb, was one of the first home computers in the UK (1981).
* Commodore 64: an 8-bit home computer developed by Commodore in August 1982.
* MSX: an 8-bit home microcomputer standard marketed during the 1980s.
* Aquarius: a home computer released by Mattel Electronics in 1983.
* Amstrad CPC: a series of 8-bit personal computers produced by Amstrad during the 1980s.
* Atari ST: a line of home computers introduced by the Atari company, successor to the Atari 8-bit family.
* EGA: stands for Enhanced Graphics Adapter, the IBM PC standard specification for graphics display (1987).
* Mac II: a computer model of the Apple Macintosh series that appeared in 1987.
* Game Boy: is a handheld game console developed Nintendo, first released in Japan and USA in 1989.

You can also define the color palette you want to emulate!

Once installed, when you select your ‘Universal Renderer Data’, you will see something like this:

{{< imagecenter src="/store/retro/oldcomputers_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

**Old Computers**', is very easy to use. Simply select the computer you want to emulate in '**Computer**' (_2_). Some systems have several modes of operation.

By changing '**Pixelation**' (_3_) you can adjust the pixel size and with '**Dithering**' (_4_) you can change the intensity of the '_Bayer 2x2_' pattern used for color dithering.

Finally, if you click on '**documentation**' (_5_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_6_). If you need to reset all the effect values, click on '**Reset**' (_7_).

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Misc

All '**Retro**' effects have a panel, '**Color**', in which you can modify the final color of the effect.

{{< imagecenter src="/store/retro/color.jpg" >}}

They also have an '**Advanced**' panel with these options:

{{< imagecenter src="/store/retro/advanced.jpg" >}}

Activate '**Affect the Scene View?**' (_1_) if you want the effect to be applied also in the '_Scene_' window of the Editor. With '**Filter mode**' (_2_) you can change the type of filter used.

Although it is not recommended to change it, with '**RenderPass event**' (_3_) you can modify at which point in the render pipeline the effect is applied. Finally, activate '**Enable profiling**' (_4_) to show in the '_Profiling_' window the metrics of the effect.

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Support

Do you have any problem or any suggestions? Click on "**support**" or send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

Remember that if you want to inform me of an error, it would help me if you sent to me the [log file](https://docs.unity3d.com/Manual/LogFiles.html).

If you are happy with this asset, **please consider leaving a positive review** in the store, it would really help me, **thanks**!
