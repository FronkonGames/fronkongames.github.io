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
* [Crystal](#crystal), crystalline patterns and dynamic light effects.
* [Bubbles](#bubbles), pop your games with funky bubbles!
* [Pinch](#pinch), a raymarching-based dynamic pinch distortion.
* [Doodle](#doodle), a hand-drawn doodle effect.
* [Kaleidoscope](#kaleidoscope), a symmetrical, rotating patterns.
* [Spiral](#spiral), a hypnotic droste effect.

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

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

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

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

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

---
## 🔮 Crystal {#crystal}
{{< asset-header youtube="jlNRgLQmGoE" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/weird-crystal-344468" demo="https://fronkongames.github.io/demos-weird/crystal/" warn="assets used in video and demo are not included">}}

Transform your games with mesmerizing crystalline patterns and dynamic light effects! This post-processing effect creates stunning visual distortions reminiscent of looking through a kaleidoscopic crystal, enhanced with flowing particle-like lights.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="CrystalInspector.png" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

#### Crystal Effect

- **Crystal** [0-1]: Controls the intensity of the crystalline pattern overlay. Default: 1.0
- **Blend**: Color blend operation for the crystal effect. Default: Additive
- **Color**: RGB color tint for the crystal pattern. Default: (0.3, 0.8, 1.2) - cyan/blue tint
- **Gain** [0-2]: Amplification of the crystal pattern. Higher values create more pronounced patterns. Default: 0.45
- **Scale** [0.1-10]: Size of the crystal patterns. Larger values create smaller, more detailed patterns. Default: 2.2
- **Speed** [0-2]: Animation speed of the crystal effect. Default: 0.5
- **Power** [0.1-20]: Exponential power applied to the crystal pattern, affecting contrast and sharpness. Default: 5.0
- **Rotation #0** [0-180]: Primary rotation angle for the crystal pattern (degrees). Default: 30.0
- **Rotation #1** [0-180]: Secondary rotation angle for layered complexity (degrees). Default: 5.0
- **Reflection** [0-1]: Amount of reflection/mirroring in the crystal effect. Default: 0.1
  - **Refraction** [0-10]: Strength of refraction (distortion and scale) when reflection is active. Default: 1.0

#### Lights Effect

- **Lights** [0-1]: Intensity of the flowing particle-like lights effect. Default: 0.1
- **Blend**: Color blend operation for the lights. Default: Screen
- **Speed** [0-2]: Animation speed of the light particles. Default: 0.5
- **Iterations** [5-30]: Number of iterations for detail and complexity. Higher values create richer effects but are more expensive. Default: 19
- **Color Offset**: RGB values that shift the color spectrum of the lights. Default: (1, 2, 3)
- **Complexity** [0.01-0.1]: Growth rate per iteration, controls how patterns evolve. Default: 0.03
- **Distortion** [1-15]: Spatial warping intensity of the light patterns. Default: 7.0
- **Spread** [1-10]: How much the light patterns disperse across the screen. Default: 5.0
- **Rotation Speed** [0-0.1]: Speed of rotation animation for the light patterns. Default: 0.02
- **Turbulence** [10-100]: Intensity of chaotic motion in the lights. Default: 40.0
- **Detail** [0.5-3.0]: Level of fine detail in the light patterns. Default: 1.5
- **Warp** [3-15]: Amount of spatial warping applied to the coordinate space. Default: 9.0
- **Brightness** [5-50]: Overall brightness multiplier for the lights. Default: 25.6
- **Contrast** [5-30]: Contrast level and clipping threshold. Default: 13.0
- **Power** [1-10]: Final exponential curve applied to the lights for intensity control. Default: 5.0

#### Use in Code

Want to control the crystalline effects programmatically? It's easier than you think:

```csharp
// Add the namespace
using FronkonGames.Weird.Crystal;

// Is it added as a Renderer Feature?
if (Crystal.IsInRenderFeatures() == false)
    return;

// Access the effect instance
Crystal.Settings settings = Crystal.Instance.settings;
settings.intensity = 1.0f;

// Control crystal effect
settings.crystalIntensity = 1.0f;
settings.crystalColor = new Vector3(0.3f, 0.8f, 1.2f);
settings.crystalSpeed = 0.5f;

// Control lights effect
settings.lightsIntensity = 0.5f;
settings.lightsSpeed = 1.0f;
settings.lightsIterations = 25;
```

Animate effects at runtime:

```csharp
// Smoothly fade in the crystal effect
Crystal.Instance.settings.crystalIntensity = Mathf.Lerp(
    Crystal.Instance.settings.crystalIntensity, 
    1.0f, 
    Time.deltaTime * 2.0f);

// Dynamically adjust light turbulence based on game events
Crystal.Instance.settings.lightsTurbulence = 40.0f + Random.Range(-10.0f, 30.0f);

// Shift colors over time
float hueShift = (Time.time * 0.1f) % 1.0f;
Crystal.Instance.settings.hue = hueShift;
```

Every parameter is at your fingertips:

```csharp
Crystal.Settings settings = Crystal.Instance.settings;

// Crystal parameters
settings.crystalColorBlend = ColorBlends.Screen;
settings.crystalGain = 0.45f;
settings.crystalScale = 2.2f;
settings.crystalPower = 5.0f;
settings.crystalRotation0 = 30.0f;
settings.crystalRotation1 = 5.0f;
settings.crystalReflection = 0.1f;
settings.crystalRefraction = 1.0f;

// Lights parameters
settings.lightsColorBlend = ColorBlends.Additive;
settings.lightsColorOffset = new Vector3(1.0f, 2.0f, 3.0f);
settings.lightsComplexity = 0.03f;
settings.lightsDistortion = 7.0f;
settings.lightsSpread = 5.0f;
settings.lightsRotationSpeed = 0.02f;
settings.lightsTurbulence = 40.0f;
settings.lightsDetail = 1.5f;
settings.lightsWarp = 9.0f;
settings.lightsBrightness = 25.6f;
settings.lightsContrast = 13.0f;
settings.lightsPower = 5.0f;

// Color adjustments
settings.brightness = 0.0f;
settings.contrast = 1.0f;
settings.gamma = 1.0f;
settings.saturation = 1.0f;
```

Check if the effect is ready:

```csharp
if (Crystal.IsInRenderFeatures() == true)
{
    // Safe to use!
}
```

Reset everything to defaults:

```csharp
Crystal.Instance.settings.ResetDefaultValues();
```

---
## 🫧 Bubbles {#bubbles}
{{< asset-header youtube="EuXGj0qHLAQ" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/weird-bubbles-344944" demo="https://fronkongames.github.io/demos-weird/bubbles/" warn="assets used in video and demo are not included">}}

Transform your games into a stunning bubble-like effect with customizable lighting, shapes, and colors. Create stunning visual effects with circular or square bubbles, adjustable bevels, and full 3D light control.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="BubblesInspector.png" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

#### Bubbles

- **Bubbles**: Main bubble color. Default: white.
- **Blend**: Bubble color blend mode with the original color. Options: Solid, Multiply, Screen, Overlay, etc. Default: Solid.
- **Roundness** [0-1]: Bubble shape roundness. 0 = perfect squares, 1 = perfect circles. Default: 1.
- **Size** [10-100]: Bubble size in pixels. Default: 40.
- **Bevel** [0.05-1]: Bevel depth of the bubbles. Higher values create more pronounced 3D effect. Default: 0.4.
- **Spacing** [0-1]: Spacing between bubbles. Lower values create tighter grids. Default: 0.1.

#### Lighting

- **Lighting** [0-2]: Specular intensity of the lighting. Controls how shiny the bubbles appear. Default: 0.45.
- **Color**: Light color. Default: white.
- **Power** [1-200]: Specular power/sharpness. Higher values create sharper highlights. Default: 70.
- **Angle** [0-360]: Light orientation angle (azimuth). Rotates the light direction around the bubbles. Default: 45.
- **Elevation** [0-90]: Light elevation angle. 0 = horizontal (side lighting), 90 = vertical (top-down lighting). Default: 46.

#### Background

- **Background**: Background color between bubbles. Default: white.
- **Blend**: Background blend mode with the original color. Default: Solid.
- **Blur** [0-20]: Background blur radius in pixels. Set to 0 to disable blur. Default: 8.
- **Exposure** [-2-2]: Background exposure adjustment. Negative values darken, positive values brighten. Default: -0.6.

#### Use in Code

Basic usage:

```csharp
// Add the namespace
using FronkonGames.Weird.Bubbles;

// Safe to use?
if (Bubbles.IsInRenderFeatures() == false)
  return;

// Access the settings (after ensuring Bubbles is added as a Render Feature)
Bubbles.Settings settings = Bubbles.Instance.settings;

// Enable the effect
settings.intensity = 1.0f;

// Disable it
settings.intensity = 0.0f;
```

Every parameter is at your fingertips:

```csharp
var settings = Bubbles.Instance.settings;

// Core effect
settings.intensity = 1.0f;                        // [0, 1] - Master intensity

// Bubbles settings
settings.bubbleColor = Color.white;               // Bubble color
settings.bubbleColorBlend = ColorBlends.Solid;    // Bubble blend mode
settings.bubbleRoundness = 1.0f;                  // [0, 1] - Shape: 0=square, 1=circle
settings.bubbleSize = 40.0f;                      // [10, 100] - Bubble size
settings.bubbleBevel = 0.4f;                      // [0.05, 1] - Bevel depth
settings.bubbleSpacing = 0.1f;                    // [0, 1] - Spacing between bubbles

// Lighting settings
settings.lightSpecular = 0.45f;                   // [0, 2] - Specular intensity
settings.lightColor = Color.white;                // Light color
settings.lightSpecularPower = 70.0f;              // [1, 200] - Specular power
settings.lightAngle = 45.0f;                      // [0, 360] - Light azimuth angle
settings.lightElevation = 46.0f;                  // [0, 90] - Light elevation angle

// Background settings
settings.backgroundColor = Color.white;            // Background color
settings.backgroundBlend = ColorBlends.Solid;      // Background blend mode
settings.backgroundBlur = 8.0f;                    // [0, 20] - Blur radius
settings.backgroundExposure = -0.6f;               // [-2, 2] - Exposure adjustment
```

Check if the effect is ready:

```csharp
if (Bubbles.IsInRenderFeatures() == true)
{
    // Safe to use!
}
```

Reset everything to defaults:

```csharp
Bubbles.Instance.settings.ResetDefaultValues();
```

---
## 🤏 Pinch {#pinch}
{{< asset-header youtube="3z-9r5hjPVM" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/weird-pinch-345684" demo="https://fronkongames.github.io/demos-weird/pinch/" warn="assets used in video and demo are not included">}}

A raymarching-based post-processing effect that creates a dynamic pinch distortion on the screen. Click and drag to create a conical extrusion effect that follows your pointer, with configurable start and end areas, roundness, and Lambert lighting.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="PinchInspector.png" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

#### Pinch

- **Start** [0-1]: Center/start position of the pinch effect in normalized screen coordinates. Default (0.5, 0.5).
- **End** [0-1]: End/target position for the pinch distortion, relative to start. Default (-0.2, 0.2).
- **Start Radius** [0-1]: Size of the pinch effect at the start position. Higher values create a wider base. Default 0.
- **End Radius** [0-1]: Size of the pinch effect at the end position. Lower values create sharper pinches. Default 0.1.
- **Roundness** [0-1]: Controls how sharp or soft the pinch appears. Higher values create softer, more rounded transitions. Default 0.1.

#### Lighting

- **Light Intensity** [0-1]: Controls how much Lambert lighting affects the result. 0 = no lighting, 1 = full lighting. Default 0.5.
- **Light Direction** [0-1]: Direction vector for the light source. Should be normalized. Default (0.577, 0.577, 0.577) - diagonal.

#### Raymarching

- **Steps** [1-100]: Number of raymarching iterations. Higher values = better quality but slower performance. Default 100.
- **Max Distance** [0.1-10]: Maximum raymarching distance. Controls how far the effect extends. Default 1.0.

#### Use in Code

Create a Pinch using a coroutine and tween:

```csharp
using FronkonGames.Weird.Pinch;
using UnityEngine;
using System.Collections;

public class PinchController : MonoBehaviour
{
  private Pinch.Settings settings;
  
  void Start()
  {
    // Check if Pinch is available
    if (Pinch.IsInRenderFeatures() == false)
    {
      Debug.LogWarning("Pinch effect not found in Render Features!");
      this.enabled = false;
      return;
    }
    
    // Access the settings
    settings = Pinch.Instance.settings;
    settings.intensity = 1.0f; // Enable the effect
  }
  
  // Create a pinch effect at a specific position
  void CreatePinch(Vector2 screenPosition)
  {
    // Convert screen position to normalized coordinates [0, 1]
    Vector2 startPoint = new Vector2(
      screenPosition.x / Screen.width,
      screenPosition.y / Screen.height
    );
    
    // Set the start point (center of the effect)
    settings.start = startPoint;
    
    // Set the end point offset (creates the pinch direction)
    settings.end = new Vector2(0.3f, 0.2f); // Pinch points to the right and up
  }
  
  // Release the pinch - smoothly animate end back to start
  void ReleasePinch() => StartCoroutine(TweenPinchRelease());
  
  IEnumerator TweenPinchRelease()
  {
    Vector2 startEnd = settings.end;
    float duration = 0.5f;
    float elapsed = 0f;
    
    while (elapsed < duration)
    {
      elapsed += Time.deltaTime;
      float t = elapsed / duration;
      
      // Smooth easing (you can use any easing function)
      t = t * t * (3f - 2f * t); // Smoothstep
      
      // Interpolate end point back to start (Vector2.zero)
      settings.end = Vector2.Lerp(startEnd, Vector2.zero, t);
      yield return null;
    }
    
    // Ensure it's exactly at start (no pinch)
    settings.end = Vector2.zero;
  }
  
  // Example: Mouse interaction
  void Update()
  {
    if (Input.GetMouseButtonDown(0))
      // Create pinch at mouse position
      CreatePinch(Input.mousePosition);
    else if (Input.GetMouseButtonUp(0))
      // Release the pinch
      ReleasePinch();
  }
}
```

#### All the Knobs and Dials

Every parameter is at your fingertips:

```csharp
// Pinch configuration
settings.start = new Vector2(0.5f, 0.5f);        // Start position
settings.end = new Vector2(-0.2f, 0.2f);         // End position (relative to start)
settings.startRadius = 0.0f;                     // Start area size
settings.endRadius = 0.1f;                       // End area size
settings.roundness = 0.1f;                       // Pinch roundness

// Lighting
settings.lightDirection = new Vector3(0.577f, 0.577f, 0.577f);  // Light direction
settings.lightIntensity = 0.5f;                  // Light intensity

// Raymarching quality
settings.raymarchSteps = 100.0f;                 // Number of steps
settings.maxDistance = 1.0f;                      // Max distance

// Color adjustments
settings.brightness = 0.0f;                      // Brightness
settings.contrast = 1.0f;                        // Contrast
settings.gamma = 1.0f;                           // Gamma
settings.hue = 0.0f;                             // Hue shift
settings.saturation = 1.0f;                      // Saturation
```

---
## ✏️ Doodle {#doodle}
{{< asset-header youtube="6lrL4Ma1hVg" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/weird-doodle-346038" demo="https://fronkongames.github.io/demos-weird/doodle/" warn="assets used in video and demo are not included">}}

A hand-drawn doodle effect. It applies a noise-based distortion to simulate a wobbly, sketched look, combined with posterization and edge detection for a complete artistic style.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="DoodleInspector.png" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

#### Doodle

Uses a noise-based displacement map to simulate the natural jitter and imperfection of hand-drawn animation. By animating this noise over time at a reduced frame rate, it creates a convincing "boiling lines" effect.

- **Doodle** [0-10]: Controls the strength of the distortion.
- **Scale** [Vector2]: Scale of the noise texture used for distortion.
- **Frame Rate** [0-60]: Speed of the doodle animation (frames per second). Lower values (e.g., 6-12) look more like traditional animation.
- **Blend** [Enum]: Color blend mode.

#### Paper

Simulates drawing on paper by blending a paper texture over the image.

- **Paper** [0-1]: Intensity of the paper texture.
- **Blend** [Enum]: Blend mode for the paper texture.
- **Scale** [Vector2]: Scale of the paper texture.
- **Doodle** [0-1]: Controls how much the paper texture distorts with the doodle effect.
- **Tint** [Color]: Tint color for the paper.

#### Grid

Adds a grid overlay, useful for graph paper or technical drawing effects.

- **Grid** [0-1]: Intensity of the grid effect.
- **Line Blend** [Enum]: Blend mode for the grid lines.
- **Size** [1-32]: Size of the grid cells.
- **Width** [0-5]: Width of the grid lines.
- **Color** [Color]: Color of the grid lines.

#### Sketch

Adds procedural hatching or sketch lines to shading.

- **Sketch** [0-1]: Intensity of the sketch effect.
- **Mode** [Enum]: Sketch mode (Simple, Cross, Animated).
- **Scale** [0.1-10]: Scale of the hatch pattern.
- **Speed** [0-10]: Animation speed for the hatch pattern.
- **Angle** [0-360]: Angle of the hatch lines.
- **Color** [Color]: Color of the sketch lines.
- **Blend** [Enum]: Blend mode for the sketch lines.

#### Sobel

Calculates the image gradient to detect edges. By applying this after the doodle distortion, the outlines wiggle and vibrate along with the drawing, reinforcing the hand-sketched aesthetic.

- **Sobel** [0-1]: Master intensity of the Sobel edge detection. Set to 0 to disable.
- **Strength** [0-10]: Thickness/sensitivity of the edge detection.
- **Tint** [Color]: Color of the edges. Alpha controls the tint strength.
- **Blend** [Enum]: Blend mode for the edges (Solid, Add, Multiply, Screen, Overlay, etc.).

#### Posterize

Reduces the tonal resolution of the image, banding continuous gradients into fewer steps of color. Lower values create a more stylized, comic-book or retro-digital appearance.

- **Posterize** [2-256]: Controls color quantization. Lower values reduce the number of colors. Set to 256 to disable.

#### Color Remapping

Applies various color presets to the final image.

- **Remapping** [Enum]: Selects the color remapping mode (None, Blueprint, Sepia, Grayscale, Invert, Cyberpunk, Gameboy, Thermal, CGA, RedScale, Matrix, Technicolor, Vintage).

#### Use in Code

```csharp
// Add the namespace
using FronkonGames.Weird.Doodle;

// Safe to use?
if (Doodle.IsInRenderFeatures() == false)
  return;

// Access the settings (after ensuring Doodle is added as a Render Feature)
Doodle.Settings settings = Doodle.Instance.settings;

// Enable the effect
settings.intensity = 1.0f;

// Disable it
settings.intensity = 0.0f;
```

Every parameter is at your fingertips:

```csharp
var settings = Doodle.Instance.settings;

// Core effect
settings.intensity = 1.0f;                    // [0, 1] - Master intensity

// Doodle settings
settings.strength = 1.0f;                     // [0, 10] - Distortion strength
settings.scale = Vector2.one;                 // Noise scale
settings.frameRate = 12.0f;                   // Animation FPS
settings.blend = ColorBlends.Solid;           // Blend mode

// Paper settings
settings.paperIntensity = 0.5f;               // [0, 1] - Paper intensity
settings.paperBlend = ColorBlends.Multiply;   // Paper blend mode
settings.paperScale = Vector2.one;            // Paper scale
settings.paperDoodleIntensity = 0.5f;         // [0, 1] - Doodle influence
settings.paperTint = Color.white;             // Paper tint

// Grid settings
settings.gridIntensity = 1.0f;                // [0, 1] - Grid intensity
settings.gridLineBlend = ColorBlends.Solid;   // Grid blend mode
settings.gridSize = 9;                        // [1, 32] - Grid size
settings.gridLineWidth = 1.0f;                // [0, 5] - Grid line width
settings.gridLineColor = new Color(0.35f, 0.65f, 1.0f); // Grid color

// Sketch settings
settings.sketchIntensity = 1.0f;              // [0, 1] - Sketch intensity
settings.sketchMode = SketchModes.Simple;     // Sketch mode
settings.sketchScale = 5.0f;                  // [0.1, 10] - Sketch scale
settings.sketchSpeed = 0.0f;                  // [0, 10] - Sketch speed
settings.sketchAngle = 45.0f;                 // [0, 360] - Sketch angle
settings.sketchColor = Color.black;           // Sketch color
settings.sketchBlend = ColorBlends.Multiply;  // Sketch blend mode

// Sobel settings
settings.sobelIntensity = 1.0f;               // [0, 1] - Sobel master intensity
settings.sobelStrength = 1.0f;                // [0, 10] - Edge detection strength
settings.sobelTint = Color.black;             // Edge color
settings.sobelBlend = ColorBlends.Multiply;   // Edge blend mode

// Posterize
settings.posterize = 8;                       // [2, 256] - Color levels

// Color remapping
settings.colorRemapping = ColorRemapping.Blueprint;

// Color adjustments
settings.brightness = 0.0f;
settings.contrast = 1.1f;
```

---
## 🌈 Kaleidoscope {#kaleidoscope}
{{< asset-header youtube="qpNbKw2UQqA" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/weird-kaleidoscope-346522" demo="https://fronkongames.github.io/demos-weird/kaleidoscope/" warn="assets used in video and demo are not included">}}

A kaleidoscope effect for Unity. It creates a symmetrical, rotating pattern from the screen content.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="KaleidoscopeInspector.png" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

#### Kaleidoscope

Controls the core kaleidoscope pattern generation. These parameters define how the symmetrical tunnel pattern is created and animated. Adjust the center position to shift the effect's focal point, use iterations to control pattern complexity, and the strength curve to create radial falloff effects.

- **Center** [0-1, 0-1]: Center position of the effect in normalized screen coordinates. Default: (0.5, 0.5).
- **Iterations** [1-10]: Number of pattern iterations. Higher values create more complex patterns. Default: 6.
- **Strength**: AnimationCurve that controls effect strength based on distance from center. X-axis: 0 = edge of screen, 1 = center. Y-axis: strength value.
- **Speed** [-10-10]: Speed of the animation. Negative values reverse the direction. Default: 1.
- **Scale** [0.1-10]: Scale of the effect. Higher values create tighter patterns. Default: 1.
- **Aspect Ratio**: When enabled, the effect maintains circular symmetry regardless of screen aspect ratio. When disabled, the effect stretches with the screen. Default: false.

#### Offset UV

Creates a chromatic aberration effect by offsetting the UV coordinates of each RGB channel independently. This produces color fringing and separation effects similar to lens distortion. The offset is based on the kaleidoscope pattern, creating dynamic color separation that follows the tunnel's structure. Use this to add depth and visual interest to the effect.

- **Offset UV** [0-1]: Intensity of UV offset effect. Creates chromatic aberration-style separation. Default: 0.
  - **Red**: Offset scale for red channel. Default: (10.0, 10.0).
  - **Green**: Offset scale for green channel. Default: (-10.0, 10.0).
  - **Blue**: Offset scale for blue channel. Default: (10.0, -10.0).
  - **Scale** [0-10]: Overall scale multiplier for offset distances. Default: 1.

#### Color

Controls the color appearance of the kaleidoscope pattern. Choose from 10 predefined color palettes to instantly change the aesthetic, or use the color adjustments to fine-tune brightness, contrast, gamma, hue, and saturation. The blend mode determines how the kaleidoscope colors combine with the original image.

- **Color** [0-1]: Intensity of the kaleidoscope color pattern. Default: 1.
  - **Palette**: Color palette preset. Options: Original, Rainbow, BlackAndWhite, Neon, Pastel, Fire, Ocean, Sunset, Monochrome, Cyberpunk. Default: Original.
  - **Blend**: Blend mode for combining kaleidoscope colors with the source image. Default: Additive.
- **Brightness** [-1-1]: Adjusts the overall luminosity of the effect. Default: 0.
- **Contrast** [0-10]: Controls the difference between light and dark areas. Default: 1.
- **Gamma** [0.1-10]: Fine-tunes the brightness curve of the effect. Default: 1.
- **Hue** [0-1]: Shifts the color wheel of the entire effect. Default: 0.
- **Saturation** [0-2]: Controls the intensity of the colors. Lower values make it more grayscale. Default: 1.

#### Segment

Renders geometric segment lines that outline the kaleidoscope pattern boundaries. These lines add structure and definition to the effect, creating a more stylized, geometric appearance. Adjust the width to control line thickness, set the color to match your aesthetic, and use blend modes to control how segments interact with the underlying image.

- **Segment** [0-1]: Intensity of segment lines rendering. Default: 1.
  - **Blend**: Blend mode for segment lines. Default: Solid.
  - **Color**: Color of the segment lines. Default: Black.
  - **Width** [0-1]: Width/thickness of segment lines. Lower values = thicker lines. Default: 0.25.

#### Use in Code

Basic Usage

```csharp
// Add the namespace
using FronkonGames.Weird.Kaleidoscope;

// Safe to use?
if (Kaleidoscope.IsInRenderFeatures() == false)
  return;

// Access the settings (after ensuring Kaleidoscope is added as a Render Feature)
Kaleidoscope.Settings settings = Kaleidoscope.Instance.settings;

// Enable the effect
settings.intensity = 1.0f;

// Disable it
settings.intensity = 0.0f;
```

Every parameter is at your fingertips:

```csharp
var settings = Kaleidoscope.Instance.settings;

// Core effect
settings.intensity = 1.0f;                    // [0, 1] - Master intensity

// Kaleidoscope settings
settings.center = new Vector2(0.5f, 0.5f);    // Center position [0-1, 0-1]
settings.iterationCount = 6;                  // [1-10] - Pattern complexity
settings.strength = new AnimationCurve(...);  // Radial strength curve
settings.speed = 1.0f;                        // [-10, 10] - Animation speed
settings.scale = 1.0f;                        // [0.1, 10] - Effect scale
settings.keepAspectRatio = false;             // Keep circular symmetry (true) or stretch with screen (false)

// Offset UV
settings.offsetIntensity = 0.5f;              // [0, 1] - UV offset intensity
settings.offsetRedScale = new Vector2(10f, 10f);
settings.offsetGreenScale = new Vector2(-10f, 10f);
settings.offsetBlueScale = new Vector2(10f, -10f);
settings.offsetScale = 1.0f;                  // [0, 10] - Offset scale multiplier

// Color
settings.colorIntensity = 1.0f;               // [0, 1] - Color pattern intensity
settings.colorPalette = ColorPalettes.Rainbow; // Color palette preset
settings.blend = ColorBlends.Additive;        // Blend mode

// Color adjustments
settings.brightness = 0.0f;                   // [-1, 1]
settings.contrast = 1.0f;                     // [0, 10]
settings.gamma = 1.0f;                        // [0.1, 10]
settings.hue = 0.0f;                          // [0, 1]
settings.saturation = 1.0f;                   // [0, 2]

// Segments
settings.segmentIntensity = 1.0f;              // [0, 1] - Segment line intensity
settings.segmentColor = Color.black;          // Segment line color
settings.segmentBlend = ColorBlends.Solid;    // Segment blend mode
settings.segmentWidth = 0.25f;                // [0, 1] - Segment width
```

---
## 🌀 Spiral {#spiral}
{{< asset-header youtube="yHp39rLtd9E" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/weird-kaleidoscope-346522" demo="https://fronkongames.github.io/demos-weird/spiral/" warn="assets used in video and demo are not included">}}

A mesmerizing Droste effect that warps image-space to recursively appear within itself, creating infinite spiral tunnels and recursive patterns.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="SpiralInspector.png" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the intensity of the effect. If it is 0, the effect will not be active.

#### Wrap

The Droste effect works by mapping the screen into a logarithmic spiral, creating the illusion that the image contains smaller copies of itself that spiral infinitely inward.

- **Wrap** [0-1]: Controls the geometric transition between the original flat image and the warped droste effect. At 0, you see the unmodified image. At 1, full droste warping is applied. Animating this creates a mesmerizing "folding into itself" morphing effect - much more interesting than a simple opacity fade.

- **Shape**: Determines the geometric boundary of each recursion layer:
  - *Circular*: Classic round droste spiral (respects screen aspect ratio)
  - *Rectangular*: Square/rectangular layers (stretches to fill)
  - *Triangular*: 3-sided polygon layers
  - *Pentagonal*: 5-sided polygon layers  
  - *Hexagonal*: 6-sided polygon layers (honeycomb-like)

- **Center** [-0.5, 0.5]: Moves the focal point of the spiral. At (0,0) the spiral centers on screen. Offset values shift where the infinite recursion point appears. Keep near zero for best results.

- **Spiral Amount** [0-1]: The "twist" factor. At 0, you get pure concentric rings/shapes with no spiral twist - the image just repeats in shrinking layers. At 1, full logarithmic spiral warping creates the classic Escher-like twisted tunnel effect.

- **Rotation** [0-360]: Rotates the entire effect statically. Useful for orienting polygon shapes or adjusting the spiral's starting angle.

- **Rotation Speed** [-2, 2]: Continuously animates rotation over time. Positive values spin clockwise, negative counter-clockwise. Combined with Zoom Speed, creates hypnotic spinning tunnel effects.

- **Outer Ring Size** [0-1]: Controls how much of the screen edge is used as the "source" texture that gets repeated inward. Lower values create tighter, more compressed recursions. At 1.0, the full screen edge is used.

- **Zoom Speed** [-2, 2]: The tunnel travel animation. Positive values make you appear to fly *into* the spiral (zooming inward). Negative values make you appear to fly *out* (zooming outward). This animates which recursion layer is displayed, creating seamless infinite travel.

- **Frequency** [0.1-5]: How many recursion layers fit in the visible area. Higher values pack more smaller copies together (denser recursion). Lower values create fewer, larger layers. This directly affects how "deep" the spiral appears.

- **Edge Mode**: When the warped UVs sample outside the original image bounds:
  - *Clamp*: Stretches edge pixels (can show seams)
  - *Mirror*: Reflects the image at boundaries (seamless, default)
  - *Repeat*: Tiles the image (can create interesting patterns)

#### Outer Tint

Applies a color effect to the outer recursion layers (the larger, edge copies). Use this to add atmosphere, highlight the "entrance" of the spiral, or create color gradients from outside to inside.

- **Outer Tint** [0-1]: How strongly the tint is applied. At 0, no tint. At 1, full tint color applied to outer layers.
- **Blend**: How the tint color combines with the image. *Solid* replaces colors, *Additive* brightens, *Multiply* darkens, *Screen* lightens, *Overlay* increases contrast, etc.
- **Color**: The tint color to apply.
- **Softness** [0.1-5]: Controls the falloff curve. Values < 1 concentrate the tint at the very outer edge. Value of 1 is linear falloff. Values > 1 spread the tint further inward.

#### Shadow

Applies darkening to the inner recursion layers (the smaller, center copies). Creates a sense of depth as if looking down a tunnel that gets darker. Complements Outer Tint - together they give full control over the depth gradient.

- **Shadow** [0-1]: How dark the inner layers become. At 0, no shadow. Higher values create stronger darkening toward the center.
- **Blend**: How the shadow combines with the image. *Multiply* is classic darkening. *Burn* creates more intense shadows. Other modes create artistic effects.
- **Color**: The shadow color (usually black, but colored shadows create interesting effects).
- **Softness** [0.1-5]: Controls the falloff curve. Values < 1 concentrate shadows at the very center. Value of 1 is linear. Values > 1 spread shadows outward.
- **Offset** [-1, 1]: Shifts where shadows begin. Negative values push shadows toward outer layers. Positive values delay shadows until deeper in.

#### Line

Draws lines at the boundaries between recursion layers - where one copy of the image meets the next smaller copy. These lines trace the spiral shape and can create neon outlines, subtle separations, or bold graphic effects.

- **Line** [0-1]: Line thickness. At 0, no lines drawn. Higher values create thicker lines. The width is resolution-independent.
- **Blend**: How line color combines with the image. *Solid* for opaque lines. *Additive* or *Screen* for glowing neon effects. *Multiply* for subtle dark outlines.
- **Color**: The line color.
- **Softness** [0.01-1]: Edge falloff of the lines. Low values (0.01-0.2) create hard, crisp edges. High values (0.5-1.0) create soft, blurred, glowing edges.
- **Count** [1-10]: Number of evenly-spaced lines per recursion interval. At 1, one line per layer boundary. Higher values subdivide each layer with additional lines.

#### Use in Code

Basic usage:

```csharp
// Add the namespace
using FronkonGames.Weird.Spiral;

// Safe to use?
if (Spiral.IsInRenderFeatures() == false)
  return;

// Access the settings
Spiral.Settings settings = Spiral.Instance.settings;

// Enable the effect
settings.intensity = 1.0f;

// Disable it
settings.intensity = 0.0f;
```

Every parameter is at your fingertips:

```csharp
var settings = Spiral.Instance.settings;

// Core effect
settings.intensity = 1.0f;                              // [0, 1] - Master intensity

// Spiral settings
settings.wrap = 1.0f;                                   // [0, 1] - Wrap/unwrap transition
settings.shape = ShapeType.Circular;                    // Shape type
settings.center = Vector2.zero;                         // [-0.5, 0.5] - Center position
settings.spiralAmount = 1.0f;                           // [0, 1] - Spiral twist amount
settings.rotation = 0.0f;                               // [0, 360] - Static rotation
settings.rotationSpeed = 0.0f;                          // [-2, 2] - Rotation animation speed
settings.outerRing = 1.0f;                              // [0, 1] - Outer ring size
settings.zoomSpeed = 0.5f;                              // [-2, 2] - Zoom animation speed
settings.frequency = 1.0f;                              // [0.1, 5] - Recursion frequency
settings.edgeMode = Spiral.Settings.EdgeMode.Mirror;   // Edge handling mode

// Outer tint (affects outer layers)
settings.outerTintIntensity = 0.3f;                     // [0, 1] - Tint intensity
settings.outerTintColorBlend = ColorBlends.Solid;       // Blend mode
settings.outerTintColor = Color.cyan;                   // Tint color
settings.outerTintSoftness = 1.0f;                      // [0.1, 5] - Falloff

// Shadow (affects inner layers)
settings.shadowIntensity = 0.2f;                        // [0, 1] - Shadow intensity
settings.shadowColorBlend = ColorBlends.Multiply;       // Blend mode
settings.shadowColor = Color.black;                     // Shadow color
settings.shadowSoftness = 1.0f;                         // [0.1, 5] - Falloff
settings.shadowOffset = 0.0f;                           // [-1, 1] - Offset

// Line at recursion boundaries
settings.lineWidth = 0.05f;                             // [0, 1] - Line width
settings.lineColorBlend = ColorBlends.Solid;            // Blend mode
settings.lineColor = Color.white;                       // Line color
settings.lineSoftness = 0.5f;                           // [0.01, 1] - Edge softness
settings.lineCount = 1;                                 // [1, 10] - Number of lines

// Color adjustments
settings.brightness = 0.0f;                             // [-1, 1]
settings.contrast = 1.0f;                               // [0, 10]
settings.gamma = 1.0f;                                  // [0.1, 10]
settings.hue = 0.0f;                                    // [0, 1]
settings.saturation = 1.0f;                             // [0, 2]
```

Create a tunnel travel effect:

```csharp
settings.zoomSpeed = 0.5f;  // Continuous inward travel
settings.rotationSpeed = 0.1f;  // Slow rotation
```

Animate the wrap for a morphing transition:

```csharp
// Gradually wrap into the effect
settings.wrap = Mathf.Lerp(0f, 1f, t);
```

Check if the effect is ready:

```csharp
if (Spiral.IsInRenderFeatures() == true)
{
    // Safe to use!
}
```

Reset everything to defaults:

```csharp
Spiral.Instance.settings.ResetDefaultValues();
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
