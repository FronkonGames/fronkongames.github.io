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
-->

* [Fire Tunnel](#firetunnel), a mesmerizing fire tunnel screen-space effect.
* [Extruder](#extruder), pixelated voxel effect with customizable camera, lighting.

<!--
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

If you are using an effect other than '**FireTunnel**' just change it to its name. Check the source code comments for more information.

#
---
## 🔥 Fire Tunnel {#firetunnel}
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

---
## 🔲 Extruder {#extruder}
{{< asset-header youtube="4ueppnM4m-A" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/weird-extruder-343886" demo="https://fronkongames.github.io/demos-weird/extruder/" warn="assets used in video and demo are not included">}}

Transform your rendered scene into a stunning **3D voxel-extruded world**! This postprocess effect uses advanced raymarching techniques to convert your screen into an artistic grid of height-mapped blocks, creating a unique retro-futuristic aesthetic reminiscent of classic voxel graphics.

Perfect for artistic visualizations, music videos, stylized game cinematics, or adding that extra "weird" factor to your Unity projects!

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="ExtruderInspector.png" wrapper="col-8 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

#### Extruder

- **Scale** [1-20]: Controls the size of individual voxel blocks. Smaller values create larger, more visible blocks. Default: 3.
- **Height**: Method for calculating voxel height. Options:
  - **Grayscale** (default): Uses image luminance to determine height
  - **Depth**: Uses the depth buffer for 3D-aware height mapping
- **Depth Scale** [0.1-10]: Amplifies depth differences for height calculation. Only used with Depth mode. Higher values create more dramatic height variations. Default: 1.0.
- **Depth Remap Min** [0-1]: Minimum depth value to remap. Only used with Depth mode. Depth values below this become zero height. Default: 0.0.
- **Depth Remap Max** [0-1]: Maximum depth value to remap. Only used with Depth mode. Depth values above this become maximum height. Default: 1.0.
- **Luminosity Remap Min** [0-1]: Minimum luminosity value to remap. Only used with Grayscale mode. Luminosity values below this become zero height. Default: 0.0.
- **Luminosity Remap Max** [0-1]: Maximum luminosity value to remap. Only used with Grayscale mode. Luminosity values above this become maximum height. Default: 1.0.
- **Blend**: Blend mode for colors (Solid, Additive, Multiply, Overlay, Screen, etc.). Default: Solid. See ColorBlends enum for all available modes.
- **Rotation** [0-360]: Camera rotation in degrees (X, Y axes). Default: (0, 0).

#### Camera & Lighting

- **Distance** [-5 to -0.5]: Distance of the virtual camera from the extruded scene. Closer values give more dramatic perspective. Default: -2.
- **Light Position** [-3 to 3]: 3D position of the light source (X, Y, Z). Default: (1.5, 2.0, -1.0).
- **Light Color**: Color and intensity of the light source (RGBA). The alpha channel controls light intensity. Default: (0.25, 0.5, 1.0, 0.3).
- **Specular Color**: Color of specular highlights. Default: (1.0, 0.5, 0.2).
- **Fresnel Intensity** [0-128]: Intensity of the fresnel effect (edge lighting). Default: 16.

#### Raymarching

- **Max Ray Distance** [1-50]: Maximum distance rays can travel. Lower values improve performance but may clip distant elements. Default: 20.
- **Raymarching Steps** [4-128]: Number of steps per ray. Higher values = more accurate but slower. Default: 32.
- **Step Multiplier** [0.1-1]: Controls raymarching precision. Lower values = more accurate but slower. Higher values = faster but may miss details. Default: 0.7.
- **Shadow Softness** [1-16]: Controls how soft or hard shadows appear. Higher values create softer, more diffused shadows. Default: 8.
- **Shadow Iterations** [0-32]: Number of shadow ray iterations. Higher values = more accurate shadows but slower. Set to 0 to disable shadows completely. Default: 8.
- **Ambient Occlusion Iterations** [0-32]: Number of ambient occlusion iterations. Higher values = more accurate AO but slower. Set to 0 to disable AO completely. Default: 5.

#### Floor Settings

- **Floor Color**: Color of the floor/background plane. Default: Black (0, 0, 0, 1).
- **Floor Color Blend**: Blend mode for the floor color (same options as Color Blend). Default: Solid.

#### Height Methods

The `Height` setting determines how voxel heights are calculated:

##### **Grayscale**
- Uses image luminance (brightness) to determine extrusion height.
- Brighter areas = taller blocks, darker areas = shorter blocks.
- Works with any content (2D, 3D, stylized, or realistic).
- Not depth-aware, purely based on pixel brightness.
- **Advanced**: Use `Luminosity Remap` to focus on specific brightness ranges:
  - Set `Min = 0.5, Max = 1.0` to only extrude bright areas (highlights).
  - Set `Min = 0.0, Max = 0.4` to only extrude dark areas (shadows).
  - Set `Min = 0.3, Max = 0.7` to focus on mid-tones only.

#### **Depth** (Default)
- Uses the camera's depth buffer to determine extrusion height.
- Closer objects = taller blocks, farther objects = shorter blocks.
- Depth-aware and respects 3D scene geometry.
- Requires a 3D scene with proper depth information.
- Use `Scale` to amplify height differences (values like 2-5 often work well for dramatic effects).
- **Advanced**: Use `Depth Remap` to focus on specific depth ranges:
  - Set `Min = 0.0, Max = 0.4` to only extrude foreground objects (closest 40%).
  - Set `Min = 0.3, Max = 0.7` to focus on mid-range objects only.
  - Set `Min = 0.7, Max = 1.0` to only extrude background objects (farthest 30%).

{{< image src="extruder_1.jpg" wrapper="col-8 mx-auto">}}

This method requires you to activate `Depth Texture` in your URP settings.

**When to use each:**
- **Grayscale**: Best for stylized looks, 2D content, UI effects, or when you want creative control over height based on brightness.
- **Depth**: Best for 3D scenes where you want accurate spatial representation and realistic depth-based extrusion.

#### Basic Code Usage

```csharp
// Add the namespace
using FronkonGames.Weird.Extruder;

// Safe to use?
if (Extruder.IsInRenderFeatures() == false)
  return;

// Access the settings (after ensuring Extruder is added as a Render Feature)
Extruder.Settings settings = Extruder.Instance.settings;

// Enable the effect
settings.intensity = 1.0f;

// Disable it
settings.intensity = 0.0f;
```

Reset everything to defaults:

```csharp
Extruder.Instance.settings.ResetDefaultValues();
```

Every parameter is at your fingertips:

```csharp
var settings = Extruder.Instance.settings;

// Core effect
settings.intensity = 1.0f;                    // [0, 1] - Master intensity

// Extruder settings
settings.gridScale = 3.0f;                    // [1, 20] - Block size (smaller = larger blocks)
settings.heightMethod = HeightMethod.Grayscale; // Height calculation method (Grayscale or Depth)
settings.depthScale = 1.0f;                   // [0.1, 10] - Depth amplification (only for Depth mode)
settings.depthRemapMin = 0.0f;                // [0, 1] - Minimum depth to remap (only for Depth mode)
settings.depthRemapMax = 1.0f;                // [0, 1] - Maximum depth to remap (only for Depth mode)
settings.luminosityRemapMin = 0.0f;           // [0, 1] - Minimum luminosity to remap (only for Grayscale mode)
settings.luminosityRemapMax = 1.0f;           // [0, 1] - Maximum luminosity to remap (only for Grayscale mode)
settings.colorBlend = ColorBlends.Solid;      // Color blend mode (Solid, Additive, Multiply, etc.)
settings.rotation = new Vector2(0f, 0f);      // [0, 360] - Camera rotation (X, Y)

// Camera & lighting
settings.cameraDistance = -2.0f;              // [-5, -0.5] - Camera distance from scene
settings.lightPosition = new Vector3(1.5f, 2.0f, -1.0f);  // [-3, 3] - Light position (X, Y, Z)
settings.lightColor = new Color(0.25f, 0.5f, 1.0f, 0.3f); // Light color and intensity (RGBA)
settings.specularColor = new Color(1.0f, 0.5f, 0.2f);     // Specular highlight color
settings.fresnelIntensity = 16.0f;            // [0, 128] - Fresnel effect intensity

// Raymarching (performance & quality)
settings.maxRayDistance = 20.0f;              // [1, 50] - Maximum ray distance
settings.raymarchingSteps = 32;               // [4, 128] - Number of steps per ray
settings.stepMultiplier = 0.7f;               // [0.1, 1] - Raymarching step size
settings.shadowSoftness = 8.0f;               // [1, 16] - Shadow softness
settings.shadowIterations = 8;                // [0, 32] - Shadow ray iterations (0 = no shadows)
settings.ambientOcclusionIterations = 5;      // [0, 32] - AO iterations (0 = no AO)

// Floor settings
settings.floorColor = Color.black;            // Floor/background color
settings.floorColorBlend = ColorBlends.Solid; // Floor color blend mode

// Color adjustments
settings.brightness = 0.0f;                   // [-1, 1] - Brightness adjustment
settings.contrast = 1.0f;                     // [0, 10] - Contrast
settings.gamma = 1.0f;                        // [0.1, 10] - Gamma correction
settings.hue = 0.0f;                          // [0, 1] - Hue shift
settings.saturation = 1.0f;                   // [0, 2] - Color saturation

// Advanced settings
settings.affectSceneView = false;             // Affect Scene View?
settings.whenToInsert = RenderPassEvent.BeforeRenderingPostProcessing;  // Render pass injection point
```

#### Scene Recommendations

- ✅ **Best**: High-contrast scenes with varied lighting and textures.
- ✅ **Good**: Outdoor scenes, cityscapes, character models with good lighting.
- ⚠️ **Challenging**: Very dark scenes (consider increasing brightness), flat-lit environments.
- ❌ **Avoid**: Completely uniform colors or same depth (nothing to extrude!).

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
