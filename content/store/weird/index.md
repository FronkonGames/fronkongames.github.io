---
author: Martin Bustos
title: Weird
showTitle: false
date: 4
description: Embrace the weirdness and make your games truly unique
tags: ["unity", "store"]
metadata: none
showImage: true
thumbnail:
  url: img/weird.jpg
---

**Embrace the weirdness** and make your games truly unique. From hypnotic fire tunnels to reality-warping distortions and ethereal auras, give your projects that extra edge in horror, magic, and psychedelic experiences.

High-performance, fully customizable, and designed specifically for game developers!

<!--
All the effects of '**[Weird](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/Weird-bundle-272266?aid=1101l9zFC&utm_source=aff)**' will help you to achieve a unique look for your games. It consists of the following effects:

* [Fire Tunnel](#firetunnel), a mesmerizing fire tunnel screen-space effect.
{{< alert color="dark" >}}
You can obtain each effect separately, but if you want multiple effects, you might be interested in **'[Weird BUNDLE](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/Weird-bundle-272266?aid=1101l9zFC&utm_source=aff)'** where you can find them all at a special price!
{{< /alert >}}
-->
## Requirements

All '**Weird**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP), which means they will **not work** with Built-In, or HDRP.

#### Unity 6

All effects are compatible with **Unity 6**, and use [Render Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html). You will need to have URP version *17.0.2* or higher installed. In the [official documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html) you can find the steps to install it correctly.

Make sure that the '_Compatibility Mode_' is **disabled** (_Project Settings > Graphics > Render Graph_).

{{< image src="compatibility_mode.jpg" wrapper="col-8 mx-auto">}}

## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Weird**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< image src="editor_0.jpg" wrapper="col-4 mx-auto">}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< image src="editor_1.jpg" wrapper="col-6 mx-auto">}}

{{< alert color="info" >}}
'_Quality_' levels (_Project Settings > Quality_) can have their own active '_Render Pipeline Asset_'.

If so, whatever you assign in '_Scriptable Render Pipeline Settings_' in '_Graphics_' will be ignored.

**Remember to add the effect to the quality levels you want to use.**
{{< /alert >}}

## VR

To increase compatibility with VR devices, I recommend that you select '**Stereo Rendering Mode**' in '**Multi Pass**' mode:

{{< image src="vr.jpg" wrapper="col-8 mx-auto">}}


## Using them in code

Once you have added the effect in the Editor, you can also handle '**Weird**' effects by code. 

First you must add the corresponding namespace. They are all of the style 'FronkonGames.Weird.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**Fire Tunnel**' the code would be:

```csharp
using FronkonGames.Weird.FireTunnel;
```

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

```csharp
FireTunnel.Settings settings = FireTunnel.Instance.settings;

settings.intensity = 0.5f;
```

And how can I activate and deactivate the effect? It's as easy as that:

```csharp
FireTunnel fireTunnel = FireTunnel.Instance;

// Switch between active and inactive.
if (fireTunnel.isActive == true)
  fireTunnel.SetActive(false);
else
  fireTunnel.SetActive(true);
```

{{< alert color="warning" icon="fas triangle-exclamation" >}}
The Instance function uses [Reflection](https://learn.microsoft.com/en-us/dotnet/fundamentals/reflection/reflection), and is therefore expensive. I recommend that you save the Instance value to use it without affecting performance.
{{< /alert >}}

If you are using an effect other than '**OneBit**' just change it to its name. Check the source code comments for more information.

#
---
## Fire Tunnel {#firetunnel}
{{< asset-header youtube="t63DSqXg250" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/weird-fire-tunnel-342436" demo="https://fronkongames.github.io/demos-weird/firetunnel/" warn="assets used in video and demo are not included">}}

Transform your game into a hypnotic journey through flames with **Fire Tunnel**, a mesmerizing post-processing effect that creates a swirling vortex of fire that engulfs the screen. Perfect for dramatic transitions, hellish portals, or just making your players feel like they're diving into the heart of an inferno. 

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="firetunnel_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

#### Tunnel
- **Center** (X,Y): Position of the tunnel's center point on screen. (0,0) is center, (-1,-1) bottom-left, (1,1) top-right.
- **Radius** [0-10]: Controls how wide the tunnel appears. Higher values create a larger tunnel opening.
- **Turbulence** [0-1]: Amount of chaos in the fire movement. Higher values create more erratic patterns.

#### Animation
- **Speed** [0-10]: How fast the fire effect moves and churns.
- **Rotation** [0-10]: Speed at which the tunnel rotates around its center.

#### Color
- **Color Blend**: How the fire effect blends with the scene.
- **Intensity** [0-10]: Adjusts the strength and brightness of the fire effect.
- **Fire Color**: Base color of the flames (RGB values from 0-10). Default is (5, 2, 1) for a natural fire look.

#### Quality
- **Steps** [1-200]: Number of steps in the raymarching calculation. Higher values mean better quality but lower performance.
- **Noise Scale** [0-10]: Controls the size and detail of the fire patterns. Lower values create finer detail.

#### Use in Code

Want to summon the flames programmatically? It's easier than you think:

```csharp
// Add the namespace
using FronkonGames.Weird.FireTunnel;

// Safe to use?
if (FireTunnel.IsInRenderFeatures() == false)
  return;

// Access the settings (after ensuring FireTunnel is added as a Render Feature)
FireTunnel.Settings settings = FireTunnel.Instance.settings;

// Open the portal!
settings.intensity = 1.0f;
settings.tunnelRadius = 4.0f;

// Close it
settings.intensity = 0.0f;
```

Want a smooth, dramatic reveal? Here's how to animate the tunnel opening:

```csharp
IEnumerator OpenFireTunnel()
{
  var settings = FireTunnel.Instance.settings;
  settings.intensity = 1.0f;
    
  float duration = 3.0f;
  float elapsed = 0.0f;
    
  while (elapsed < duration)
  {
    settings.tunnelRadius = Mathf.Lerp(0.0f, 4.0f, elapsed / duration);
    elapsed += Time.deltaTime;
    yield return null;
  }
    
  settings.tunnelRadius = 4.0f;
}

// Start the animation
StartCoroutine(OpenFireTunnel());
```

Here's the fade-out version:

```csharp
IEnumerator CloseFireTunnel()
{
  var settings = FireTunnel.Instance.settings;
  settings.intensity = 1.0f;
    
  float duration = 3.0f;
  float elapsed = 0.0f;
    
  while (elapsed < duration)
  {
    settings.tunnelRadius = Mathf.Lerp(4.0f, 0.0f, elapsed / duration);
    elapsed += Time.deltaTime;
    yield return null;
  }
    
  settings.tunnelRadius = 0.0f;
}

// Start the animation
StartCoroutine(CloseFireTunnel());
```

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
