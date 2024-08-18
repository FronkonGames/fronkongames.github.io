---
author: Martin Bustos
title: Spice Up
showTitle: false
date: 2
description: A large selection of assets to give juice to your FPS / VR games
tags: ["unity", "store"]
metadata: none
showImage: true
thumbnail:
  url: img/spiceup.jpg
---

'**Spice Up**' is a large selection of effects to give juice to your FPS / VR games. It consists of the following effects:

* [Damage](#damage), a visual indicator of health and damage received.
* [Drunk](#drunk), simulates the effects of alcohol on the player.
* [Stoned](#stoned), imitates the symptoms of feeling high or intoxicated.
* [Frozen](#frozen), experience a realistic and immersive freezing effect.
* [Speed Lines](#speedlines), anime speed lines.
* [Blurry](#blurry), blurred vision based on previous frames.
* [Double Vision](#doublevision), dual vision effect with steroids.
* [Rain](#rain), simulates the raindrops on the screen.
* [Ghost Vision](#ghostvision), the vision of strange creatures.
* [Scanner](#scanner), cameras, monitors and robots.
* [Death Screeen](#deathscreen), the last screen.
* [Purkinje](#purkinje), human eye perception under dim light condition.
* [Broken Screen](#brokenscreen), simulated...
* [Pulse](#pulse), focus on one point on the screen.
* [Shake](#shake), like in an earthquake!
* [Night Vision](#nightvision), the most versatile solution for night vision.
* [BodyCam](#bodycam), body camera (BWC) or wearable camera.
* [Lens Flare](#lensflare), a.k.a. JJ Abrams' illumination.

{{< alert color="light" >}}
You can obtain each effect separately (**for only $8!**), but if you want multiple effects, you might be interested in **'[SPICE UP BUNDLE](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-bundle-262333?aid=1101l9zFC&utm_source=aff)'** where you can find them all at a special price!
{{< /alert >}}

## Requirements

All '**Spice Up**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP), which means they will **not work** with Built-In, or HDRP.

You will need to have URP version **12.1.11** or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Spice Up**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< image src="editor_0.jpg" wrapper="col-6 mx-auto">}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< image src="editor_1.jpg" wrapper="col-6 mx-auto">}}

## VR

To increase compatibility with VR devices, I recommend that you select '**Stereo Rendering Mode**' in '**Multi Pass**' mode:

{{< image src="vr.jpg" wrapper="col-6 mx-auto">}}

## Using them in code

Once you have added the effect in the Editor, you can also handle '**Spice Up**' effects by code. 

First you must add the corresponding namespace. They are all of the style 'FronkonGames.SpiceUp.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**Damage**' the code would be:

```csharp
using FronkonGames.SpiceUp.Damage;
```

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

```csharp
Damage.Settings settings = Damage.GetSettings();

settings.intensity = 0.5f;
```

If you are using an effect other than '**Damage**' just change it to its name. Check the source code comments for more information.

{{< alert color="warning" icon="fas triangle-exclamation" >}}
Do not use the code of the demos in your projects, they are only there to show you the use of the effect through code.
{{< /alert >}}

#
---
## Damage {#damage}
{{< asset-header youtube="rChUFliVX_E" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-damage-247019" demo="https://fronkongames.github.io/demos-spiceup/damage/" >}}

'**Damage**' is a visual indicator of the damage suffered by the player. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="damage_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The damage must be **normalized**, or in other words between 0 and 1 (inclusive). Being 0 a perfectly healthy player and 1 a perfectly dead one. You can adjust its value with '**Damage**' (_1_), although most commonly you will modify it via code.

Let's say that '_DamageMax_' is a constant that indicates the maximum amount of damage the player can receive and '_damage_' is the variable with the damage received:

```csharp
Damage.GetSettings().damage = damage / DamageMax;
```

It can also be calculated from health:

```csharp
Damage.GetSettings().damage = 1.0f - (health / HealthMax);
```

Visually the damage is represented by three effects: _Liquid_, _Veins_ and _Drops_. You can configure how much they affect the final result using their sliders.

{{< carousel class="col-sm-12 col-lg-8 mx-auto" >}}
  {{< img src="img/damage/slide1.jpg" caption="Liquid">}}
  {{< img src="img/damage/slide2.jpg" caption="Veins">}}
  {{< img src="img/damage/slide3.jpg" caption="Drops">}}
{{< /carousel >}}

* Liquid: is the liquid that expands from the edges of the screen.
* Veins: simulates the capillary vessels of the human eye and add an extra 'gore'.
* Drops: adds dynamic liquid drops. '_Range_' is the number of droplet layers, with each layer having droplets of similar sizes. With '_Scale_' you control their size and with '_Speed_' the speed at which they disappear.

To indicate impacts, and the direction they come from, you can use '**Impact strength**' (_3_). These impacts will be displayed on the edges of the screen and will indicate the direction from which the impact is coming, the top part being a frontal impact, and the bottom part a rear impact.

{{< image src="damage_2.jpg" wrapper="col-6 mx-auto">}}

The time it stays on screen can be configured with: '_Rise time_', '_Wait time_' and '_Fall time_'. You can also adjust its thickness and the smoothness of the edges.

To get an idea of the effect, you can do it with '**Simulate impact**' (_13_).

{{< image src="damage_1.jpg" wrapper="col-6 mx-auto">}}

And how do I do it in the game? Very simple, 'Damage' takes care of everything. First it sets the target of the hits. The most typical case would be on the player. If 'player' is a GameObject that represents the player, it would be like this:

```csharp
Damage.Target = player.transform;
```

Now you will only have to call the 'Impact' function every time the unfortunate player receives an impact. If you do not specify the origin of the hit, a flash effect (general damage) will be created. If you specify who caused the damage, an impact with direction will be created.

```csharp
// Flash effect.
Damage.Impact(0.25f);

// Impact with direction.
Damage.Impact(0.5f, zombie.transform);
```

{{< alert type="info" >}}
* Damage must be **normalized**, i.e. from 0 to 1.
* The maximum number of hits with direction on the screen is **4**.
* The plane in which the direction is calculated is the XZ.
{{< /alert >}}

You can change the color in '**Color gradient**'. From the gradient used (_4_), through the color and ending with how the effect blends with the screen.

{{< alert type="info" >}}
If the final result is too dark, or too bright, try one of the many Blend operations included.
{{< /alert >}}

To modify the definition of the edges, change '**Definition**' (_5_). The final brightness of the effect can be set with '**Brightness**' (_6_).

To simulate a _more organic_ substance, a Vonoroi type noise can be applied to distort the effect. You can adjust its parameters in '**Noise**' (_7_).

With '**Distortion**' (_9_) you can modify how much the effect distorts the screen.

In some games you may have seen how they apply a _black and white_ effect as the player loses life. You can recreate it with '**Desaturation**' (_9_). This parameter is not modified according to '**Damage**' (_2_), so you will have to modify it manually.

To simulate some _volume_ to the liquid, a slight shimmer effect is applied to the top edges. Modify this effect in '**Edge**' (_10_).

Another effect you may have seen in other games, is how the player blinks, or loses peripheral vision. This effect can be adjusted with '**Blink**' (_11_). Like '**Desaturation**' (_9_), this effect must be adjusted manually.

{{< alert type="danger" >}}
Very high values of '_Speed_' can create a **stroboscopic** effect that **may affect some users**.
{{< /alert >}}

Do values close to 1 of '**Damage**' (_2_) make the effect too intense? Adjust the range with '**Remap damage**' (_12_). By lowering the upper range somewhat, you will make very high values lower.

---
## Drunk {#drunk}
{{< asset-header youtube="L7agg4NP7XU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-drunk-247929" demo="https://fronkongames.github.io/demos-spiceup/drunk/" >}}

With '**Drunk**' you can let players know that they are drinking too much.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="drunk_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Drunkenness**' (_2_) you control the overall intensity of the effect. The higher the value, the more intense the result. You can also adjust the speed of the oscillations and their amplitude.

{{< alert type="danger" >}}
High values of this effect may cause dizziness. Use with caution.
{{< /alert >}}

'**Swinging**' (_3_) causes the camera to swing. In addition to the intensity, you can control its speed.

With '**Distortion**' you can modify how the image is distorted, you can also control the speed and frequency of the distortion. You can also add to the image distortion, a displacement of the color channels (RGB) with '**Aberration**' (_5_).

'**Blink**' (_6_) adds to the effect a blinking of the eyes. You can also control with '**Eye**' (_7_) the point of the vision, being (0.5, 0.5) the center of the screen.

Do values close to 1 of '**Drunkenness**' (_2_) make the effect too intense? Adjust the range with '**Remap damage**' (_8_). By lowering the upper range somewhat, you will make very high values lower.

---
## Stoned {#stoned}
{{< asset-header youtube="5f_TMTkHXM0" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-stoned-248596" demo="https://fronkongames.github.io/demos-spiceup/stoned/" >}}

Too many potions? With '**Stoned**' you can simulate the effect of drinking too many.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="stoned_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Stoned**' (_2_) you control the overall intensity of the effect. The higher the value, the more intense the result.

The first thing you can adjust is the speed of the effect with '**Speed**' (_3_). You can add some volume with '**Definition**' (_4_).

With '**Displacement**' (_5_) you can adjust the screen deformation. You can increase the granularity with '**Noise**' (_6_).

With '**Hue**' (_7_) you can shift the final color of the effect (is not the same control as the one in 'Color').

{{< alert type="info" >}}
If you cycle from 0 to 1 and back again, you can add extra psychedelia to the effect.
{{< /alert >}}

Adjust the strength of each color channel with '**Channel**' (_8_).

Internally, the effect uses the YIQ color space (used by the analog NTSC TV). In '**Luma info**' you can adjust its parameters. See more information about the [YIQ color space here](https://en.wikipedia.org/wiki/YIQ).

**Lines** (_10_) transforms the clouds of the effect into lines of intense color.

{{< alert type="info" >}}
If you use lines and add ['Bloom' postprocessing](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/post-processing-bloom.html), you can get a very interesting effect. Adjust the intensity of 'Bloom' well to avoid annoying flares.
{{< /alert >}}

With '**Tint**' (_11_) you can color the final result with the color of your choice. In '**Blend**' (_12_) you can select from a large list of color mixing functions. The selected function will be the one that blends the effect with the screen.

---
## Frozen {#frozen}
{{< asset-header youtube="FPn7dk3fkG4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-frozen-249207" demo="https://fronkongames.github.io/demos-spiceup/frozen/" >}}

Experience a realistic and immersive freezing effect. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="frozen_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Frozen**' (_2_) you control the overall intensity of the effect. The higher the value, the more intense the result.

The effect is created with two layers, you can configure them in '**Blend Layers**' (_3_). The first thing is how they are blended, if you have the slider set to 0 or 1, only one layer will be used ('**Layer 0**' or '**Layer 1**' respectively). If you leave it in the middle, both layers will be blended equally. You can also choose how the color of each layer is blended with the screen.

To increase detail, or decrease smoothing, use '**Sharpness**' (_4_). You can also increase the granularity effect with '**Bump**' (_5_) and '**Volume**' (_6_).

Modify the distortion that the effect produces on the screen with '**Distortion**' (_7_).

With '**Vision tint**' (_8_) you can modify the color of the effect.

---
## Speed Lines {#speedlines}
{{< asset-header youtube="KfDiwLYM6xw" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-speed-lines-250408" demo="https://fronkongames.github.io/demos-spiceup/speedlines/" >}}

Anime speed lines. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="speedlines_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Strength**' (_2_) you control the intensity of its parameters.

The radius, or amplitude, of the effect can be modified with '**Radius**' (_3_), as well as the length of the _arrows_ with '**Length**' (_4_).

The speed with which they move on the screen can be adjusted with '**Speed**' (_5_). You can also change how many arrows are displayed on the screen with '**Frequency**' (_6_), as well as the softness of the edges with '**Softness**' (_7_).

With '**Noise**' (_8_) you can modify how different some _arrows_ are from others.

The color of the effect can be adjusted in '**Color blend**' (_9_). From the type of operation used to blend with the background of the screen, to brightness, colors, etc.

If you check '**Aspect ratio**' (_10_), the effect will not conform to the screen and will form a circle inside the screen instead of conforming to the edges of the screen.

---
## Blurry {#blurry}
{{< asset-header youtube="izte-BmU-nw" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-blurry-251642" demo="https://fronkongames.github.io/demos-spiceup/blurry/" >}}

Blurred vision based on previous frames. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="blurry_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Strength**' (_2_) you control the intensity of its parameters.

The number of frames the effect will use can be set in '**Frames**' (_3_). The more frames, the more blurriness you will get. You can also set in '**Step**' (_4_) if you want to skip frames.

By default the frames used will have the same resolution as the screen. You can change this with '**Resolution**' (_5_) to make them smaller. This not only improves the performance of the effect, but also makes the image more blurred.

---
## Double Vision {#doublevision}
{{< asset-header youtube="FPELiWUmtw4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-double-vision-252006" demo="https://fronkongames.github.io/demos-spiceup/doublevision/" >}}

Dual vision effect with steroids. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="doublevision_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Strength**' (_2_) you control the intensity of its parameters. Adjust the intensity of the effect on each axis with '**X**' and '**Y**'. You can also control the speed of the effect with '**Speed**' (_3_), and its axes.

You can also add a _color channel phase effect_ (_4_) and adjust its intensity on each color channel.

With '**Blend strength**' (_5_) you can configure how the effect mixes with the screen and which operation is used to mix them.

---
## Rain {#rain}
{{< asset-header youtube="DKMAa_LY7yU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-rain-252460" demo="https://fronkongames.github.io/demos-spiceup/rain/" >}}

Simulates the raindrops on the screen. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="rain_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

In the '**Droplets**' (_2_) section you can configure how the drops are: the amount, the size, their speed, their angle and finally how much they distort the background color.

In the next section, '**Color**' (_3_) you can change its color. If you activate '**Tint trails**', the drops will also have a trail.

With '**Layers**' (_4_) you can configure the drop layers. Three layers are available. The first, '**Static**', are droplets that do not move on the screen. The next two correspond to drops that do scroll on the screen.

---
## Ghost Vision {#ghostvision}
{{< asset-header youtube="NyqkpzdqkNU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-ghost-vision-252730" demo="https://fronkongames.github.io/demos-spiceup/ghostvision/" >}}

The vision of strange creatures. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="ghostvision_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

'**Quality**' (_2_) can select different quality levels of the noise used to generate the effect. A '_Custom_' mode is also included in which you can manually adjust the octaves of the noise.

'**Strength**' (_3_) modulates the intensity of the rest of the parameters.

By default the focus of the vision is positioned in the center of the screen (at 0, 0), if you want to modify it, you can use '**Focus**' (_3_). You can also modify its aperture (_5_) and zoom (_6_).

{{< alert type="info" >}}
Activate '**Debug view**' (_11_) to see the area where the effect is most applied with a red tint.
{{< /alert >}}

With '**Speed**' (_7_) you can change the speed of the effect and by activating '**Aspect ratio**' (_8_) it will be adjusted to the resolution of the monitor.

You can also modify the color of the central viewing area, '**Inner color**' (_9_), and the outer area, '**Outer color**' (_10_).

---
## Scanner {#scanner}
{{< asset-header youtube="cudFCcHb_HY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-scanner-253706" demo="https://fronkongames.github.io/demos-spiceup/scanner/" >}}

Cameras, Monitors and Robots. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="scanner_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active. '**Strength**' (_2_) modulates the intensity of the rest of the parameters.

{{< alert type="info" >}}
'**Intensity**' and '**Strength**' must be greater than 0 to activate the effect.
{{< /alert >}}

With '**Lines**' (_3_) you can adjust the number of lines, their color and how the line blends with the background color. In the spaces between lines you can also modify its color, '**Background**' (_4_) and the function used to mix its color.

'**Scanline**' (_5_) is one line in a raster scanning pattern, such as a line of video on a cathode ray tube (CRT). Band noise' (_6_) is another similar effect that can also be found on older TV sets.

The frame jumps, can be adjusted with '**Frame noise**' (_7_), the higher the values, the more the frame jumps. You can also add more noise to the signal with '**Signal noise**' (_8_), '**Interlace noise**' (_9_) and '**Bad signal**' (_10_).

You can simulate the typical curvature of old monitors with '**Barrel**' (_11_). The higher your values, the more curved the image will appear. You can also change the color and size.

To add a shadow effect on the edges you can use '**Vignette**' (_12_).

---
## Death Screen {#deathscreen}
{{< asset-header youtube="ewXstV38FWc" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-death-screen-254360" demo="https://fronkongames.github.io/demos-spiceup/deathscreen/" >}}

The last screen. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="deathscreen_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

To move the effect, use '**Progress**' (_2_). If its value is 0, you will not see any effect. As it reaches 1, it will scroll across the screen.

To adjust the color, use '**Blood**' (_3_). You can also change the formula used to blend the effect with the background (_4_) and the glow effect on the edges (_5_). To change the shape of the border use '**Wave seed**' (_6_).

If you want to modify the color of the areas where the effect does not act, use '**Not blood**' (_7_).

---
## Purkinje {#purkinje}
{{< asset-header youtube="FGC6LDY1RGg" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-purkinje-255525" demo="https://fronkongames.github.io/demos-spiceup/purkinje/" >}}

When the level of luminance drops below a certain threshold, the stimuli from rod cells supersedes that of cone cells. Due to the rod cells' minimal sensitivity to red light and heightened sensitivity to blue-green light, it leads to the perception of blue images during nighttime. This asset attempts to correct colour by simulating the above effect. 

{{< image src="purkinje_1.jpg" wrapper="col-6 mx-auto">}}

With '[Purkinje](https://en.wikipedia.org/wiki/Purkinje_cell)' you can create night scenes that really feel nocturnal, not just darker.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="purkinje_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

You can modify the hue with '**Tint**' (_2_) and adjust the darkness of the image with '**Darkness**' (_3_).

---
## Broken Screen {#brokenscreen}
{{< asset-header youtube="eqaPjR1KYPg" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-broken-screen-256124" demo="https://fronkongames.github.io/demos-spiceup/brokenscreen/" >}}

Real-time glass fractures. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="brokenscreen_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

Adjust the fracture center with '**Impact**' (_2_), the number of branches with '**Splits**' (_3_) and its thickness with '**Width**' (_4_).

The operation used to blend the color of the fracture with the background can be modified with '**Blend**' (_5_), as well as its tint with '**Color**' (_6_). Modify '**Threashold**' (_7_) to limit the zones where color operations are applied.

Add distortion effects to the background image and its colors with '**Distortion**' (_8_) and '**Aberration**' (_9_).

With '**Seed**' (_10_) you can change the random seed used to generate the fractures. The same random seed will generate the same shapes in the fractures.

---
## Pulse {#pulse}
{{< asset-header youtube="63-RWxded2A" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-pulse-257920" demo="https://fronkongames.github.io/demos-spiceup/pulse/" >}}

Focus on one point on the screen. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="pulse_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

Set the origin of the pulse with '**Center**' (_2_), the coordinates (0.5, 0.5) being the center of the screen. With '**Duration**' (_3_) you can set the duration of the pulse.

Each pulse is created with one frame scaling from a center. '**Alpha**' (_4_) is the transparency of that frame. With '**Scale**' (_5_) you control how much the frame is scaled.

You can change the color with '**Tint**' (_6_) and the operation that will be used to mix the frame color with the background color (_7_).

To see the result in the editor, press '**Test**' (_8_).

Creating a new pulse with code is very simple. As always the first thing to do is to include the namespace:

```csharp
using FronkonGames.SpiceUp.Pulse;
```

Now, when you want to create a new pulse, simply do:

```csharp
Pulse.Start();
```

---
## Shake {#shake}
{{< asset-header youtube="5Zc_0_BYOVw" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-shake-258721" demo="https://fronkongames.github.io/demos-spiceup/shake/" >}}

Shakes like in an earthquake! Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="shake_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The direction of the impact can be controlled using '**Direction**' (_2_), the default value (0, 1) being an impact at the top center of the screen. The duration of the effect can be adjusted with '**Duration**' (_3_).

For small impacts use a small '**Zoom**' (_4_) value. As you increase this value, the feeling will be of stronger jolts. Something similar happens with '**Shake**' (_5_). You can also set the frequency of the shaking with '**Frequency**'. It adds an extra to the shaking sensation by adding image distortion and chromatic aberration.

To add even more chaos, if you want, '**Noise**' (_6_) adds some noise to all the above values.

To check the results in the Editor, you can use the '**Test**' button (_7_).

Creating a new shake with code is very simple. As always the first thing to do is to include the namespace:

```csharp
using FronkonGames.SpiceUp.Shake;
```

Now, when you want to create a new shake, simply do:

```csharp
Shake.Start();
```

---
## Night Vision {#nightvision}
{{< asset-header youtube="7Dam3W04TzU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-night-vision-259563" demo="https://fronkongames.github.io/demos-spiceup/nightvision/" >}}

The most versatile solution for night vision. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="nightvision_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

You can decrease the resolution with '**Resolution**' (_2_). Doing this will make the effect faster and the image blurred. You can also do this by modifying '**Blur**' (_3_) and add a '**Glow**' effect (_4_).

You can select a wide variety of color gradients. First set the gradient strength (_5_) and then select one of those shown in '**Tint**'. You can use your own gradient if you select '_Custom_'.

Gradients work by calculating the brightness of the original pixel and replacing it with the corresponding color in the gradient. If the scale is too dark (or too bright), you can modify the brightness range in '**Luminance**'.

'**Exposure**' (_6_), '**Brightness**' (_7_), '**Contrast**' (_9_) and '**Saturation**' (_10_) change the **original** color, **do not** confuse them with the controls in the 'Color' section that modify the **final** color.

With '**RGB offset**' (_10_) you can shift the black and white range.

You can add an effect that defines the edges with '**Edge**' (_11_), add noises (_12_ and _14_). With '**Distortion**' (_13_) you can curve the image and add chromatic aberration.

'**UI**' (_16_) adds some interface elements such as a grid of points, crosses, etc.

With '**Vignette**' (_17_) you can select a shading on the edges of the screen, binoculars or monoculars.

{{< image src="nightvision_1.jpg" wrapper="col-6 mx-auto">}}

To create a convincing night vision effect, a light is usually added in the direction of the camera. This is not done by the effect and you can do it on your own, but I have added the '**Night Vision Manager**' component to make this task easier for you.

Add it to the camera you are going to use. Set the on (_1_) and off (_2_) time of the effect.

{{< alert type="info" >}}
If you are going to use sounds, it is a good idea to match the time to the length of the audios.
{{< /alert >}}

In '**Light intensity**' (_3_) you can configure the light that will be added to the camera.

If you want the other lights in the scene to be automatically turned off when the effect is activated, activate '**Light management**'. You can add to the '**Light to ignore**' list the lights you want to be ignored.

To turn the effect on and off using '**Night Vision Manager**' just do this:

```csharp
// Turn on.
nightVisionManager.On = true;

// Turn off.
nightVisionManager.On = false;
```

---
## Body Cam {#bodycam}
{{< asset-header youtube="pBp_WXNzlTY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-bodycam-260035" demo="https://fronkongames.github.io/demos-spiceup/bodycam/" >}}

Body camera (BWC) or wearable camera. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="bodycam_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Fish Eye**' (_2_) you can control the deformation typical of cameras with small lenses or a very large focus. Softness**' and 'Abberation**' are effects that define the edge of the camera.

Add a '**Blur**' effect (_3_), setting its quality with '**Samples**'. Remember that the higher the number of samples, the higher the quality of the effect, but the worse the performance.

You can simulate a reflection of a light with '**Flare**' (_4_). You can manually change its '**Angle**', or you can synchronize it with the Y axis of your character's rotation:

```csharp
settings.flareAngle = this.transform.eulerAngles.y;
```

With '**Chroma band**' (_5_) and '**Luma band**' (_6_) you can simulate the defects that some poor quality cameras have. Add some '**Noise**' (_8_) for extra reality.

By default dark colors tend to a blue, change it in '**Shadow tint**' (_7_) and adjust its White / Black balance.

If you look at the demo, and the video, the center of the effect seems to move with some inertia depending on the rotation of the player. This can be easily achieved by adding the '**Body Cam Roll**' component to the camera.

{{< image src="bodycam_1.jpg" wrapper="col-6 mx-auto">}}

In this simple component you can adjust the '**Strength**' (_1_) and '**Speed**' (_2_) of the inertia.

Note that this component is designed for objects that move in the XZ plane, and therefore rotate on the Y axis (as in the vast majority of FPS). If in your game the displacement planes are different, you will have to modify the code.

---
## Lens Flare {#lensflare}
{{< asset-header youtube="9Z6wVV6XXPk" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-lens-flare-261769" demo="https://fronkongames.github.io/demos-spiceup/lensflare/" >}}

Lens flare effect, intended for scenes with high brightness contrast (e.g. night scenes with lights). Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="lensflare_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The number of '**Iterations**' (_2_) will define the quality of the effect. Note that the higher the number, the better the effect but the worse the performance. You can achieve a good balance by adjusting '**Scale**' (_3_) to reduce the number of iterations.

With '**Threshold**' (_4_) you can filter the brightness threshold used to calculate the flares.

Add a cinematic touch with '**ACES**' (_5_), a tonemapper widely used in the film industry, '**Grain**' (_6_) and '**Bands**' (_8_).

You can change the operation used to blend the color of the flares with the original image with '**Blend**' (_7_), as well as their color and gamma.

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

{{< alert color="warning" icon="fas triangle-exclamation" >}}
Note that when you make this change, the coordinates of your UI will be in camera space, so you will have to change them.
{{< /alert >}}
<br>

##### _When Bloom is added, its intensity is too low or the effect stops working._

Bloom's URP Unity effect is not compatible with postprocessing effects based on [ScriptableRendererFeature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html?q=ScriptableRendererFeature) (like this one).

You will have to add your own one based on ScriptableRendererFeature or you can use [this one at no cost](https://github.com/FronkonGames/ScriptableRenderBloom) ;)

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
