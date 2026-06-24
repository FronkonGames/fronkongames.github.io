---
author: Martin Bustos
title: Spice Up
showTitle: false
date: 2
description: A large collection of first-person and VR fullscreen effects for Unity 6 and URP
tags: ["unity", "store"]
metadata: none
showImage: true
thumbnail:
  url: img/spiceup.jpg
---

'**[Spice Up](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-bundle-262333?aid=1101l9zFC&utm_source=aff)**' is a collection of **fullscreen post-processing effects** designed to add impact, distortion, feedback, and stylized camera treatment to first-person and VR games. Each effect can be used as a standalone package, but inside the bundle they share the same URP workflow, volume-driven runtime model, and editor conventions.

It consists of the following effects:

* [🩸 Damage](#damage), a health and hit feedback system with directional indicators.
* [🍺 Drunk](#drunk), unstable vision with oscillation, blinking, and chromatic distortion.
* [🌈 Stoned](#stoned), psychedelic color deformation with YIQ-based controls.
* [🧊 Frozen](#frozen), layered frost, distortion, and cold-screen tinting.
* [⚔️ Slash](#slash), a cinematic screen-split with glow, smoke, and distortion.
* [💨 Speed Lines](#speedlines), anime-inspired radial velocity streaks.
* [👀 Double Vision](#doublevision), oscillating image separation and color offsets.
* [🌧️ Rain](#rain), animated droplets, trails, and layered wet-screen effects.
* [👻 Ghost Vision](#ghostvision), creature-like tunnel vision with animated noise.
* [📺 Scanner](#scanner), CCTV, monitor, and robotic-display artifacts.
* [☠️ Death Screen](#deathscreen), a blood wipe for death or defeat states.
* [🌙 Purkinje](#purkinje), low-light adaptation inspired by human night perception.
* [💥 Broken Screen](#brokenscreen), procedural fractures and impact distortion.
* [💓 Pulse](#pulse), expanding pulses driven by timed progress.
* [🌪️ Shake](#shake), screen shake with zoom, distortion, and aberration.
* [🟢 Night Vision](#nightvision), a rich night vision system with gradients and UI overlays.
* [🎥 BodyCam](#bodycam), body camera optics with blur, flare, and sensor artifacts.
* [✨ Lens Flare](#lensflare), cinematic flare generation for bright scenes.
* [🌫️ Blurry](#blurry), blurred vision built from frame history.

{{< badge title="You can obtain each effect separately, but if you want more effects, you might be interested in **'[SPICE UP BUNDLE](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-bundle-262333?aid=1101l9zFC&utm_source=aff)'** where you can find them all at a special price!" color="secondary">}}
{.h3}

## Bundle Requirements

All '**Spice Up**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-introduction.html)' (URP), which means they do **not** work with Built-In or HDRP.

#### Unity 6 or Higher

The current bundle is centered on **Unity 6** and the **URP Render Graph** workflow. You will need **URP 17.0.3** or higher installed. If you need help with setup, follow the [official URP installation guide](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html).

Make sure that '_Compatibility Mode_' is **disabled** in '_Project Settings > Graphics > Render Graph_'.

{{< image src="compatibility_mode.jpg" wrapper="col-8 mx-auto">}}

## Installation

#### Step 1: Add Renderer Feature

The effects must be registered in your project's [URP configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html):

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select the desired distortion from **Fronkon Games > Retro**.

Once installed, you have to add the effect you want to use from '**Retro**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< image src="editor_camera.jpg" wrapper="col-8 mx-auto">}}

{{< alert color="info" >}}
'_Quality_' levels (_Project Settings > Quality_) can have their own active '_Render Pipeline Asset_'.

If so, whatever you assign in '_Scriptable Render Pipeline Settings_' in '_Graphics_' will be ignored.

**Remember to add the effect to the quality levels you want to use.**
{{< /alert >}}

#### Step 2: Configure The Volume

To apply the effects to your scene:

1. Create a **Volume** component (Global or Local) or select one that has already been created.
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select the desired distortion from **Fronkon Games > Retro**.
4. Enable the '**Intensity**' parameter (and any others you wish to modify).

{{< alert color="info" >}}
Remember that for a parameter to take effect, you must activate it. Click on '**ALL**' to activate them all.
{{< /alert >}}

#### VR

To increase compatibility with VR devices, I recommend that you select '**Stereo Rendering Mode**' in '**Multi Pass**' mode:

{{< image src="vr.jpg" wrapper="col-8 mx-auto">}}

#
---
## 🩸 Damage {#damage}
{{< asset-header youtube="rChUFliVX_E" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-damage-247019" demo="https://fronkongames.github.io/demos-spiceup/damage/" warn="assets used in video and demo are not included">}}

'**Damage**' is a complete hit-feedback effect for health loss, impacts, and low-health stress. It combines continuous injured-eye visuals with optional directional hit indicators and flash feedback.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

The effect must be registered in your project's URP configuration:

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Damage**.

##### Step 2: Configure the Volume

To apply the effect to your scene:

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Damage**.
4. Enable the '**Intensity**' parameter and the damage-related fields you want to control.

#### Parameter Configuration

{{< image src="damage_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Damage

The main '**Damage**' block in the custom inspector defines the continuous injury state, including the nested `Liquid`, `Veins`, and `Drops` controls shown under it.

{{< rawhtml >}}<br>{{< /rawhtml >}}
|                                                          |                                                          |                                                          |
| :------------------------------------------------------: | :------------------------------------------------------: | :------------------------------------------------------: |
| {{< image src="slide1.jpg" >}} | {{< image src="slide2.jpg" >}} | {{< image src="slide3.jpg" >}} |
|                          **Liquiq**                           |                          **Veins**                           |                          **Drops**                           |
{{< rawhtml >}}<br>{{< /rawhtml >}}

The base damage look is controlled by normalized health feedback and three layered visual systems.

{{< table >}}
| | |
|---|---|
| **Damage** | Normalized damage value [0, 1] that drives the core effect |
| **Liquid** | Main injured-eye liquid layer |
| **Veins** | Capillary/vein overlay contribution |
| **Drops** | Dynamic droplets over the image |
| **Drops Range / Scale / Speed** | Layer count, droplet size, and disappearance speed |
{{< /table >}}

##### Impacts Strength

{{< image src="damage_2.jpg" wrapper="col-8 mx-auto">}}

In the custom inspector, the '**Impacts Strength**' block controls the strength, timing, thickness, and softness of flash hits and directional indicators.

{{< table >}}
| | |
|---|---|
| **Impacts Strength** | Global strength of flash and directional indicators |
| **Time** | Rise, hold, and fall timing of hits |
| **Thickness** | Width of directional hit markers |
| **Feather** | Softness of indicator edges |
{{< /table >}}

##### Color Gradient

This '**Color Gradient**' section in the custom inspector controls how the damage overlay is tinted and blended, including the conditional tint slots shown for multi-color gradients.

{{< table >}}
| | |
|---|---|
| **Color Gradient** | Selects the gradient mode used by the effect |
| **Tint / Tint #0 / Tint #1** | Available color fields depending on the selected gradient mode |
| **Color blend** | Blend mode used to composite the damage color |
{{< /table >}}

##### Definition

This standalone '**Definition**' control appears next in the custom inspector and adjusts the border definition of the liquid layer.

{{< table >}}
| | |
|---|---|
| **Definition** | Border definition of the liquid |
{{< /table >}}

##### Brightness

This standalone '**Brightness**' control appears after `Definition` in the custom inspector and adjusts the brightness of the liquid effect itself.

{{< table >}}
| | |
|---|---|
| **Brightness** | Brightness of the liquid effect |
{{< /table >}}

##### Noise

The custom inspector groups these controls under '**Noise**', where they define the animated Voronoi breakup applied over the damage effect.

{{< table >}}
| | |
|---|---|
| **Noise** | Strength of the animated breakup |
| **Scale** | Noise scale |
| **Velocity** | Noise movement direction and speed |
{{< /table >}}

##### Distortion

This standalone '**Distortion**' control appears after `Noise` in the custom inspector and determines how much the damage refracts the background image.

{{< table >}}
| | |
|---|---|
| **Distortion** | Refraction applied to the background image |
{{< /table >}}

##### Desaturation

This standalone '**Desaturation**' control appears after `Distortion` in the custom inspector and drains color from unaffected areas as damage increases.

{{< table >}}
| | |
|---|---|
| **Desaturation** | Drains color from unaffected areas |
{{< /table >}}

##### Edge

Under '**Edge**' in the custom inspector, these controls shape the outer contour of the effect.

{{< table >}}
| | |
|---|---|
| **Edge** | Extra border shaping and edge emphasis |
| **Damage** | Additional damage emphasis inside the edge block |
{{< /table >}}

##### Blink

The '**Blink**' block in the custom inspector controls eyelid-style vision closure plus the visible eye position.

{{< table >}}
| | |
|---|---|
| **Blink** | Eyelid-style interruption of vision |
| **Speed** | Blink speed |
| **Eye** | Focus point of the blink effect |
{{< /table >}}

##### Remap Range

This final control matches the '**Remap Range**' slider shown at the bottom of the custom inspector and lets you compress or expand the damage response curve.

{{< table >}}
| | |
|---|---|
| **Remap Range** | Compress or expand the response curve |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Damage;

[SerializeField] private VolumeProfile volumeProfile;

private void ApplyDamage(float normalizedDamage)
{
  if (volumeProfile.TryGet(out DamageVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.damage.overrideState = true;
    volume.desaturation.overrideState = true;

    volume.intensity.value = 1.0f;
    volume.damage.value = Mathf.Clamp01(normalizedDamage);
    volume.desaturation.value = normalizedDamage > 0.5f ? 0.25f : 0.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Impacts Manager

`ImpactsManager` is an optional runtime helper for flash hits and directional indicators. It reads the active `DamageVolume`, animates hit timing automatically, and can show up to **4** simultaneous directional indicators.

* **Target**: usually the damaged actor or player transform.
* **Hit(float damage, Transform damager)**: main runtime entry point. `damage` should be normalized to `[0, 1]`.
* **Stop()**: resets current flash and indicator state.

If `Target` and `damager` are both valid, the helper computes the hit direction relative to the target. If `damager` is `null`, it falls back to a centered flash-only response.

##### Performance Characteristics

The effect executes in a single full-screen render pass, but visual complexity varies with the enabled layers.

* Pass Count: 1 blit pass.
* Texture Samples: Moderate and dependent on enabled layers such as drops and noise.
* Complexity: O(1) per pixel with extra branch cost for layered damage features.

##### Usage Patterns and Presets

###### Survival Horror

For slow-building stress and heavy low-health pressure:
* Damage: 0.6 - 1.0
* Liquid: 1.0
* Veins: 0.3 - 0.6
* Desaturation: 0.3 - 0.7
* Blink: 0.2 - 0.5

###### Shooter Hit Feedback

For punchy directional impacts with less permanent obstruction:
* Damage: 0.15 - 0.4
* Impacts Strength: 1.0 - 2.5
* Time: fast rise, short hold
* Liquid: 0.5 - 0.8
* Distortion: 0.05 - 0.15

---
## 🍺 Drunk {#drunk}
{{< asset-header youtube="L7agg4NP7XU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-drunk-247929" demo="https://fronkongames.github.io/demos-spiceup/drunk/" warn="assets used in video and demo are not included">}}

'**Drunk**' simulates alcohol-induced instability with oscillation, head sway, distortion, blinking, and chromatic aberration.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Drunk**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Drunk**.
4. Enable '**Intensity**' and the drunkenness-related parameters you want to animate.

#### Parameter Configuration

{{< image src="drunk_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Drunkenness

The custom inspector starts this group with '**Drunkenness**', which defines the main alcohol-induced wobble and its nested `Speed` and `Amplitude` controls.

{{< table >}}
| | |
|---|---|
| **Drunkenness** | Main normalized strength of the effect |
| **Speed** | Speed of the core oscillation |
| **Amplitude** | Amplitude of the overall wobble |
{{< /table >}}

{{< alert type="danger" >}}
High values of **Drunkenness** may cause dizziness. Use with caution.
{{< /alert >}}

##### Swinging

Here the custom inspector switches to the '**Swinging**' block, which controls the slower head sway layered on top of the base drunken wobble.

{{< table >}}
| | |
|---|---|
| **Swinging** | Head sway strength |
| **Speed** | Head sway speed |
{{< /table >}}

##### Distortion

The '**Distortion**' block in the custom inspector is where the animated screen warping is configured.

{{< table >}}
| | |
|---|---|
| **Distortion** | Animated image warping |
| **Speed** | Distortion animation speed |
| **Frequency** | Distortion wave frequency |
{{< /table >}}

##### Aberration

Inside the custom inspector, '**Aberration**' defines how strongly the color channels separate over time.

{{< table >}}
| | |
|---|---|
| **Aberration** | Chromatic offset and channel separation |
| **Speed** | Aberration animation speed |
{{< /table >}}

##### Blink

This '**Blink**' block in the custom inspector controls the eyelid-style interruption of vision.

{{< table >}}
| | |
|---|---|
| **Blink** | Eyelid-style interruption of vision |
| **Speed** | Blink speed |
{{< /table >}}

##### Eye

This standalone '**Eye**' control appears after `Blink` in the custom inspector and sets the focus point used by the blink effect.

{{< table >}}
| | |
|---|---|
| **Eye** | Focus point of the blink effect |
{{< /table >}}

##### Remap Range

This final control matches the '**Remap Range**' slider shown at the bottom of the custom inspector and lets you tame or exaggerate high drunkenness values.

{{< table >}}
| | |
|---|---|
| **Remap Range** | Remap extreme values into a more usable range |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Drunk;

[SerializeField] private VolumeProfile volumeProfile;

private void SetDrunkLevel(float value)
{
  if (volumeProfile.TryGet(out DrunkVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.drunkenness.overrideState = true;
    volume.drunkenness.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect executes in a single pass and remains lightweight unless multiple distortions are pushed to high values.

* Pass Count: 1 blit pass.
* Texture Samples: Low to moderate.
* Complexity: O(1) per pixel with animated trigonometric distortion.

##### Usage Patterns and Presets

###### Slight Intoxication

For a readable but impaired screen:
* Drunkenness: 0.2 - 0.4
* Swinging: 0.1 - 0.2
* Distortion: 0.15 - 0.3
* Aberration: 1.0 - 3.0

###### Severe Drunkenness

For near-loss-of-control presentation:
* Drunkenness: 0.7 - 1.0
* Amplitude: 0.75 - 1.0
* Distortion: 0.4 - 0.8
* Blink: 1.0 - 1.8

---
## 🌈 Stoned {#stoned}
{{< asset-header youtube="5f_TMTkHXM0" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-stoned-248596" demo="https://fronkongames.github.io/demos-spiceup/stoned/" warn="assets used in video and demo are not included">}}

'**Stoned**' is a psychedelic effect focused on color-space manipulation, screen deformation, YIQ controls, and stylized line generation.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Stoned**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Stoned**.
4. Enable '**Intensity**' and the psychedelic parameters you want to control.

#### Parameter Configuration

{{< image src="stoned_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Stoned

This section follows the same sequence users see in the custom inspector, beginning with the main '**Stoned**' strength control and the standalone fields that come right after it.

{{< table >}}
| | |
|---|---|
| **Stoned** | Main normalized strength of the effect |
| **Range** | Clamp or stretch strong values |
| **Speed** | Speed of the evolving color clouds |
| **Definition** | Contour sharpness and cloud detail |
| **Displacement** | Background deformation strength |
| **Noise** | Extra breakup and granularity |
| **Color HUE** | Extra hue shift inside the internal color model |
| **Channels Strength** | Strength of each color channel |
| **YIQ** | YIQ luma / in-phase / quadrature control |
{{< /table >}}

{{< alert type="info" >}}
If you cycle **Color HUE** from 0 to 1 and back again, you can add extra psychedelia to the effect.
{{< /alert >}}

##### Lines

The custom inspector places these controls under '**Lines**', where they shape the stylized streaks layered over the psychedelic pattern.

{{< table >}}
| | |
|---|---|
| **Lines** | Converts soft structures into stronger neon streaks |
| **Strength** | Intensity of the line contribution |
{{< /table >}}

##### Tint

This standalone '**Tint**' field appears after `Lines` in the custom inspector and applies a final tint over the result.

{{< table >}}
| | |
|---|---|
| **Tint** | Final result tint |
{{< /table >}}

##### Color Blend

This final '**Color Blend**' control matches the last field in the custom inspector and defines how the effect is composited over the image.

{{< table >}}
| | |
|---|---|
| **Color Blend** | Blending mode used to composite the effect |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Stoned;

[SerializeField] private VolumeProfile volumeProfile;

private void SetHigh(float value)
{
  if (volumeProfile.TryGet(out StonedVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.stoned.overrideState = true;
    volume.stoned.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect uses a single render pass with procedural color-space operations.

* Pass Count: 1 blit pass.
* Texture Samples: Low.
* Complexity: O(1) per pixel with procedural color deformation.

##### Usage Patterns and Presets

###### Dreamy Potion

For magical intoxication with readable gameplay:
* Stoned: 0.2 - 0.4
* Displacement: 0.1 - 0.25
* Noise: 0.5 - 1.0
* Lines: 0.0 - 0.2

###### Psychedelic Overload

For strong surrealism:
* Stoned: 0.7 - 1.0
* Definition: 1.5 - 3.0
* YIQ: exaggerated
* Lines: 0.4 - 0.8

---
## 🧊 Frozen {#frozen}
{{< asset-header youtube="FPn7dk3fkG4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-frozen-249207" demo="https://fronkongames.github.io/demos-spiceup/frozen/" warn="assets used in video and demo are not included">}}

'**Frozen**' creates a layered frost overlay with distortion, cold tinting, and surface detail controls that can range from mild chill to near-complete visual obstruction.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Frozen**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Frozen**.
4. Enable '**Intensity**' and the frost parameters you want to tune.

#### Parameter Configuration

{{< image src="frozen_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Frozen

The layout below mirrors the custom inspector order, starting with the main '**Frozen**' strength control and the frost-layer settings that come next.

{{< table >}}
| | |
|---|---|
| **Frozen** | Main normalized intensity of the freezing state |
| **Tint** | Main frost tint |
| **Blend Layers** | Mix between the two frost layers |
| **Layer 0 / Layer 1** | Individual blend modes for both layers |
| **Bump** | Frost relief strength |
| **Sharpness** | Edge definition |
| **Volume** | Surface depth feel |
| **Distortion** | Screen refraction beneath the frost |
| **Vision Tint** | Strength of the visible-area tint |
| **Vision Tint Color** | Cold color cast over the visible area |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Frozen;

[SerializeField] private VolumeProfile volumeProfile;

private void SetCold(float value)
{
  if (volumeProfile.TryGet(out FrozenVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.frozen.overrideState = true;
    volume.frozen.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect executes in a single full-screen pass with layered procedural detail.

* Pass Count: 1 blit pass.
* Texture Samples: Moderate.
* Complexity: O(1) per pixel with additional frost and distortion math.

##### Usage Patterns and Presets

###### Light Frostbite

For early environmental exposure:
* Frozen: 0.2 - 0.4
* Distortion: 0.05 - 0.1
* Vision Tint Strength: 0.15 - 0.25

###### Full Freeze

For critical cold damage:
* Frozen: 0.8 - 1.0
* Blend Layers: 0.4 - 0.6
* Bump: 1.0 - 2.0
* Volume: 0.4 - 0.8

---
## ⚔️ Slash {#slash}
{{< asset-header youtube="GlGGW0EeYm0" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-slash-380758" demo="https://fronkongames.github.io/demos-spiceup/slash/" warn="assets used in video and demo are not included">}}

'**Slash**' is a cinematic screen-split effect that simulates a slashing blade cutting across the view. It combines image separation, edge glow, layered smoke, and color grading for dramatic combat or death transitions.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Slash**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Slash**.
4. Enable '**Intensity**' and the slash parameters you want to control.

#### Parameter Configuration

{{< image src="slash_0.png" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Slash

The main '**Slash**' block in the custom inspector defines the cut progression, angle, and screen split behavior.

{{< table >}}
| | |
|---|---|
| **Slash** | Progress of the slash from 0 to 1 |
| **Angle** | Angle of the slash in degrees |
| **Split** | Maximum distance the screen halves separate |
| **Distort** | Refraction strength at the split edge |
| **Fade** | Point at which the slash itself fades out |
| **Width** | Thickness of the core slash line |
{{< /table >}}

##### Glow

The '**Glow**' block in the custom inspector controls the light bloom along the slash edge.

{{< table >}}
| | |
|---|---|
| **Glow** | Color of the edge glow |
| **Blend** | Blend mode used for the glow |
| **Spread** | Glow spread and softness |
{{< /table >}}

##### Smoke #1

The first '**Smoke #1**' block in the custom inspector defines the bright smoke layer that trails the slash.

{{< table >}}
| | |
|---|---|
| **Smoke #1** | Size of the white smoke layer |
| **Blend** | Blend mode for the white smoke |
| **Color** | White smoke color |
| **Expand** | Smoke expansion outward from the slash |
| **Fade** | Point at which the white smoke fades out |
{{< /table >}}

##### Smoke #2

The '**Smoke #2**' block in the custom inspector defines the dark smoke layer beneath the bright one.

{{< table >}}
| | |
|---|---|
| **Smoke #2** | Size of the dark smoke layer |
| **Blend** | Blend mode for the dark smoke |
| **Color** | Dark smoke color |
| **Expand** | Smoke expansion outward from the slash |
| **Fade** | Point at which the dark smoke fades out |
{{< /table >}}

##### Background

This standalone '**Background**' control appears after the smoke blocks in the custom inspector and sets the color used to hide screen-edge clamping when the image splits.

{{< table >}}
| | |
|---|---|
| **Background** | Fill color revealed behind the split halves |
{{< /table >}}

##### Color

Open the '**Color**' foldout in the custom inspector to adjust the final grading applied to the effect.

{{< table >}}
| | |
|---|---|
| **Brightness** | Overall brightness |
| **Contrast** | Overall contrast |
| **Gamma** | Overall gamma |
| **Hue** | Global hue shift |
| **Saturation** | Global saturation |
{{< /table >}}

##### Runtime Control

```csharp
using System.Collections;
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Slash;

[SerializeField] private VolumeProfile volumeProfile;

private IEnumerator PlaySlash(float duration)
{
  if (volumeProfile.TryGet(out SlashVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.progress.overrideState = true;
    volume.progress.value = 0.0f;
    volume.intensity.value = 1.0f;

    float time = 0.0f;
    while (time < duration)
    {
      volume.progress.value = time / duration;
      time += volume.useScaledTime.value ? Time.deltaTime : Time.unscaledDeltaTime;
      yield return null;
    }

    volume.progress.value = 1.0f;
    volume.intensity.value = 0.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Slash Controller

`SlashController` is an optional helper component that animates the slash over time via a coroutine.

* **Duration**: total time of the slash animation in seconds.
* **VolumeProfile**: must contain the `SlashVolume` used by the controller.
* **Play()**: starts the slash from progress 0 and animates it to 1.
* **Stop()**: cancels the animation and resets progress to 0.
* **OnStart / OnProgress / OnStop**: Unity events fired during playback.

##### Performance Characteristics

The effect executes in a single full-screen render pass.

* Pass Count: 1 blit pass.
* Texture Samples: Low.
* Complexity: O(1) per pixel.

##### Usage Patterns and Presets

###### Sword Strike

For a sharp melee impact:
* Slash: animate 0.0 -> 1.0
* Angle: 149
* Split: 0.05 - 0.15
* Distort: 0.05 - 0.15
* Glow Spread: 30 - 50

###### Cinematic Kill

For a dramatic finishing blow:
* Slash: animate 0.0 -> 1.0
* Split: 0.2 - 0.4
* Smoke #1 Expand: 0.4 - 0.6
* Smoke #2 Expand: 0.5 - 0.8
* Background: black

---
## 💨 Speed Lines {#speedlines}
{{< asset-header youtube="KfDiwLYM6xw" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-speed-lines-250408" demo="https://fronkongames.github.io/demos-spiceup/speedlines/" warn="assets used in video and demo are not included">}}

'**Speed Lines**' generates anime-style radial streaks that amplify velocity, acceleration, and bursts of forward motion.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Speedlines**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Speedlines**.
4. Enable '**Intensity**' and the line parameters you want to use.

#### Parameter Configuration

{{< image src="speedlines_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Strength

The description here follows the custom inspector top to bottom, starting with the main radial-line controls before moving into the nested blend settings.

{{< table >}}
| | |
|---|---|
| **Strength** | Main line contribution |
| **Radius** | Overall effect radius |
| **Length** | Length of the streaks |
| **Speed** | Motion speed of the streak animation |
| **Frequency** | Density of the lines |
| **Softness** | Edge softness |
| **Noise** | Shape variation |
| **Aspect** | Preserve circular shape regardless of screen aspect |
{{< /table >}}

##### Blend

Within the custom inspector, the nested '**Blend**' block controls how the line colors are generated and composited.

{{< table >}}
| | |
|---|---|
| **Blend** | Blend mode used to mix the lines with the image |
| **Brightness** | Brightness of the line coloration |
| **Offset** | Gradient positioning |
| **Definition** | Gradient sharpness |
| **Border** | Border color of the lines |
| **Center** | Center color of the lines |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Speedlines;

[SerializeField] private VolumeProfile volumeProfile;

private void SetBoost(float value)
{
  if (volumeProfile.TryGet(out SpeedlinesVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.strength.overrideState = true;
    volume.strength.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect is implemented as a single pass and is generally lightweight.

* Pass Count: 1 blit pass.
* Texture Samples: Low.
* Complexity: O(1) per pixel with procedural radial pattern generation.

##### Usage Patterns and Presets

###### Dash Burst

For short ability bursts:
* Strength: 0.3 - 0.6
* Length: 1.5 - 2.5
* Speed: 3.0 - 6.0

###### Anime Sprint

For exaggerated movement:
* Strength: 0.7 - 1.0
* Frequency: 15 - 30
* Color Brightness: 1.5 - 3.0

---
## 👀 Double Vision {#doublevision}
{{< asset-header youtube="FPELiWUmtw4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-double-vision-252006" demo="https://fronkongames.github.io/demos-spiceup/doublevision/" warn="assets used in video and demo are not included">}}

'**Double Vision**' offsets and oscillates the image to create unstable binocular separation, making it ideal for intoxication, disorientation, and impact aftermath.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Double Vision**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Double Vision**.
4. Enable '**Intensity**' and the separation parameters you want to control.

#### Parameter Configuration

{{< image src="doublevision_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Strength

For '**Double Vision**', the parameter list below keeps the exact inspector order, from the main offsets through the blend settings.

{{< table >}}
| | |
|---|---|
| **Strength** | Direction and magnitude of the image offset |
| **Speed** | Oscillation speed on each axis |
| **Color Offset** | Independent offset for the color channels |
| **Blend Strength** | Strength of the doubled-image mix |
| **Color Blend** | Blend operation used to composite the result |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.DoubleVision;

[SerializeField] private VolumeProfile volumeProfile;

private void SetDisorientation(float value)
{
  if (volumeProfile.TryGet(out DoubleVisionVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.blendStrength.overrideState = true;
    volume.blendStrength.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect is lightweight and runs in a single pass.

* Pass Count: 1 blit pass.
* Texture Samples: Low.
* Complexity: O(1) per pixel.

##### Usage Patterns and Presets

###### Head Trauma

For impact-induced instability:
* Blend Strength: 0.3 - 0.5
* Strength: medium XY offsets
* Color Offset: subtle

###### Supernatural Distortion

For paranormal or teleport transitions:
* Blend Strength: 0.5 - 0.8
* Speed: uneven per-axis motion
* Color Offset: noticeable RGB phase split

---
## 🌧️ Rain {#rain}
{{< asset-header youtube="DKMAa_LY7yU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-rain-252460" demo="https://fronkongames.github.io/demos-spiceup/rain/" warn="assets used in video and demo are not included">}}

'**Rain**' simulates droplets on glass, visors, cameras, or lenses using layered static and dynamic water behavior.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Rain**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Rain**.
4. Enable '**Intensity**' and the wet-screen parameters you need.

#### Parameter Configuration

{{< image src="rain_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Droplets

In the custom inspector, the '**Droplets**' block controls the amount, size, movement, angle, and refraction of the rain pattern.

{{< table >}}
| | |
|---|---|
| **Droplets** | Main intensity of the raindrop system |
| **Size** | Droplet scale |
| **Speed** | Falling/trailing motion speed |
| **Rotation** | Overall slant of the drops |
| **Distortion** | Refraction strength applied to the background |
{{< /table >}}

##### Tint

The '**Tint**' block in the custom inspector determines how the droplets, ambient contribution, and moving trails are colored.

{{< table >}}
| | |
|---|---|
| **Tint** | Blend mode used to tint the effect |
| **Droplet** | Main droplet tint |
| **Ambient** | Ambient wet tint, alpha controls influence |
| **Tint trails** | Also tint moving trails |
{{< /table >}}

##### Layers

The custom inspector uses the '**Layers**' block to balance the stationary and moving droplet layers.

{{< table >}}
| | |
|---|---|
| **Static** | Stationary droplets |
| **Dynamic #0** | First moving droplet layer |
| **Dynamic #1** | Second moving droplet layer |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Rain;

[SerializeField] private VolumeProfile volumeProfile;

private void SetRain(float value)
{
  if (volumeProfile.TryGet(out RainVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.amount.overrideState = true;
    volume.amount.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect runs in a single pass and scales mostly with droplet complexity and distortion strength.

* Pass Count: 1 blit pass.
* Texture Samples: Moderate.
* Complexity: O(1) per pixel with layered droplet evaluation.

##### Usage Patterns and Presets

###### Light Drizzle

For subtle environmental weather:
* Amount: 0.15 - 0.3
* Size: 0.8 - 1.0
* Static Layer: high
* Dynamic Layers: low

###### Storm Lens

For wet helmet or camera glass:
* Amount: 0.6 - 1.0
* Distortion: 0.5 - 0.8
* Dynamic Layers: high
* Tint Trails: enabled

---
## 👻 Ghost Vision {#ghostvision}
{{< asset-header youtube="NyqkpzdqkNU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-ghost-vision-252730" demo="https://fronkongames.github.io/demos-spiceup/ghostvision/" warn="assets used in video and demo are not included">}}

'**Ghost Vision**' creates a tunnel-like field of view with animated organic noise, strong inner/outer color separation, and optional custom noise quality.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Ghost Vision**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Ghost Vision**.
4. Enable '**Intensity**' and the noise/focus parameters you need.

#### Parameter Configuration

{{< image src="ghostvision_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Quality

This breakdown preserves the exact custom inspector order, starting with the quality selection and the main viewing controls that appear before the color regions.

{{< table >}}
| | |
|---|---|
| **Quality** | Preset quality mode or custom FBM path |
| **High FBM / Low FBM** | Custom octave counts when using `Quality = Custom` |
| **Strength** | Main intensity of the effect |
| **Focus** | Center of the viewing cone |
| **Speed** | Turn/noise motion speed |
| **Aperture** | Width of the visible inner area |
| **Zoom** | Magnification feel of the center |
| **Aspect Ratio** | Preserve aspect ratio in the mask |
{{< /table >}}

##### Inner Color

The custom inspector exposes these controls under '**Inner Color**' to style the central viewing region.

{{< table >}}
| | |
|---|---|
| **Inner Color** | Base tint of the inner region |
| **Saturation** | Inner-region saturation |
| **Brightness** | Inner-region brightness |
| **Contrast** | Inner-region contrast |
| **Gamma** | Inner-region gamma |
{{< /table >}}

##### Outer Color

The '**Outer Color**' block in the custom inspector styles the outer falloff region.

{{< table >}}
| | |
|---|---|
| **Outer Color** | Base tint of the outer region |
| **Blend** | Blend mode used for the outer region |
| **Saturation** | Outer-region saturation |
| **Brightness** | Outer-region brightness |
| **Contrast** | Outer-region contrast |
| **Gamma** | Outer-region gamma |
{{< /table >}}

##### Debug View

This standalone '**Debug View**' control appears at the bottom of the custom inspector and visualizes the mask and affected region.

{{< table >}}
| | |
|---|---|
| **Debug View** | Visualize the mask and affected region |
{{< /table >}}

{{< alert type="info" >}}
Activate '**Debug view**' to see the area where the effect is most applied with a red tint.
{{< /alert >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.GhostVision;

[SerializeField] private VolumeProfile volumeProfile;

private void SetSpectralSense(float value)
{
  if (volumeProfile.TryGet(out GhostVisionVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.strength.overrideState = true;
    volume.strength.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect uses a single pass, but custom quality and octave-heavy noise increase shader cost.

* Pass Count: 1 blit pass.
* Texture Samples: Low.
* Complexity: O(1) per pixel with variable procedural-noise cost.

##### Usage Patterns and Presets

###### Monster POV

For predatory tunnel vision:
* Strength: 0.8 - 1.0
* Aperture: 2.0 - 4.0
* Outer Tint: dark or black

###### Paranormal Detector

For supernatural sensing:
* Strength: 0.3 - 0.6
* Inner Tint: pale or spectral
* Debug View: temporarily enabled while tuning

---
## 📺 Scanner {#scanner}
{{< asset-header youtube="cudFCcHb_HY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-scanner-253706" demo="https://fronkongames.github.io/demos-spiceup/scanner/" warn="assets used in video and demo are not included">}}

'**Scanner**' recreates the look of CCTV feeds, robotic optics, analog monitors, and unstable surveillance video.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Scanner**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Scanner**.
4. Enable '**Intensity**' and '**Strength**' plus the display artifacts you want to use.

#### Parameter Configuration

{{< image src="scanner_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Strength

The parameter order here mirrors the custom inspector exactly, starting with the core scanner controls before the foldout sections.

{{< table >}}
| | |
|---|---|
| **Strength** | Main activation strength of the effect |
| **Barrel** | CRT-like curvature strength |
| **Tint / Zoom** | Nested barrel tint and zoom controls |
| **Lines** | Number of main screen lines |
| **Tint / Blend** | Nested line tint and blend controls |
{{< /table >}}

{{< alert type="info" >}}
'**Intensity**' and '**Strength**' must be greater than 0 to activate the effect.
{{< /alert >}}

##### Scanline

{{< image src="scanner_1.jpg" wrapper="col-8 mx-auto">}}

Open the '**Scanline**' foldout in the custom inspector to control the moving scanline overlay described below.

{{< table >}}
| | |
|---|---|
| **Strength** | Strength of the scanline overlay |
| **Tint** | Scanline tint |
| **Blend** | Scanline blend mode |
| **Width** | Scanline width |
| **Speed** | Scanline movement speed |
{{< /table >}}

##### Vignette

{{< image src="scanner_2.jpg" wrapper="col-8 mx-auto">}}

The '**Vignette**' foldout in the custom inspector controls the edge darkening and flicker settings collected here.

{{< table >}}
| | |
|---|---|
| **Strength** | Edge darkening amount |
| **Blink** | Vignette flicker |
{{< /table >}}

##### Background

{{< image src="scanner_3.jpg" wrapper="col-8 mx-auto">}}

These controls live inside the '**Background**' foldout of the custom inspector and define the spaces between the lines.

{{< table >}}
| | |
|---|---|
| **Tint** | Background tint |
| **Blend** | Background blend mode |
{{< /table >}}

##### Glitches

{{< image src="scanner_4.jpg" wrapper="col-8 mx-auto">}}

The custom inspector gathers these analog and electronic imperfections inside the '**Glitches**' foldout.

{{< table >}}
| | |
|---|---|
| **Noise Band** | Horizontal band artifact strength |
| **Tint / Blend / Width / Speed** | Nested controls for the noise band |
| **Frame Noise** | Whole-frame jitter |
| **Signal Noise** | Static signal instability |
| **Interlace** | Interlace breakup |
| **Bad Signal** | Stronger transmission corruption |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Scanner;

[SerializeField] private VolumeProfile volumeProfile;

private void SetScannerStrength(float value)
{
  if (volumeProfile.TryGet(out ScannerVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.strength.overrideState = true;
    volume.strength.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect runs in a single pass with procedural display artifacts.

* Pass Count: 1 blit pass.
* Texture Samples: Low.
* Complexity: O(1) per pixel.

##### Usage Patterns and Presets

###### CCTV Feed

For surveillance cameras:
* Strength: 0.3 - 0.6
* Lines: high
* Barrel: 0.2 - 0.5
* Signal Noise: low to medium

###### Failing Robot Camera

For damaged mechanical vision:
* Strength: 0.7 - 1.0
* Noise Band: medium/high
* Frame Noise: medium
* Bad Signal: 0.3 - 0.8

---
## ☠️ Death Screen {#deathscreen}
{{< asset-header youtube="ewXstV38FWc" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-death-screen-254360" demo="https://fronkongames.github.io/demos-spiceup/deathscreen/" warn="assets used in video and demo are not included">}}

'**Death Screen**' is a blood wipe that can transition the screen from fully visible to almost completely overwhelmed by blood.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Death Screen**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Death Screen**.
4. Enable '**Intensity**' and the blood wipe parameters you want to animate.

#### Parameter Configuration

{{< image src="deathscreen_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Progress

This section keeps the same order shown in the custom inspector, beginning with the wipe progression and the nested `Blood` controls.

{{< table >}}
| | |
|---|---|
| **Progress** | Main wipe progression from 0 to 1 |
| **Blood** | Color of the blood area |
| **Blend** | Blend mode of the blood area |
| **Bevel** | Edge glow strength |
| **Color / Width** | Nested bevel color and width controls |
| **Wave seed** | Variation seed for the wipe contour |
{{< /table >}}

##### Not blood

The '**Not blood**' block in the custom inspector controls the treatment of the unaffected region.

{{< table >}}
| | |
|---|---|
| **Not blood** | Color of the unaffected region |
| **Saturation** | Saturation of the unaffected region |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.DeathScreen;

[SerializeField] private VolumeProfile volumeProfile;

private void SetDeathProgress(float value)
{
  if (volumeProfile.TryGet(out DeathScreenVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.progress.overrideState = true;
    volume.progress.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect is lightweight and based on a single full-screen pass.

* Pass Count: 1 blit pass.
* Texture Samples: Low.
* Complexity: O(1) per pixel.

##### Usage Patterns and Presets

###### Defeat Transition

For a clean death-state wipe:
* Progress: animate 0.0 -> 1.0
* Bevel: 0.2 - 0.4
* Blend: Solid

###### Possession / Corruption

For more stylized takeover effects:
* Progress: medium/high
* Not blood: tinted
* Waves: stronger variation

---
## 🌙 Purkinje {#purkinje}
{{< asset-header youtube="FGC6LDY1RGg" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-purkinje-255525" demo="https://fronkongames.github.io/demos-spiceup/purkinje/" warn="assets used in video and demo are not included">}}

'**Purkinje**' simulates the low-light shift in human color perception, where scenes become darker, reds diminish, and blue-green tones become more dominant.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Purkinje**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Purkinje**.
4. Enable '**Intensity**' and the low-light perception controls you want to use.

#### Parameter Configuration

{{< image src="purkinje_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Darkness

For '**Purkinje**', the explanation below follows the exact custom inspector order from darkness response through the final tint.

{{< table >}}
| | |
|---|---|
| **Darkness** | Global strength of the low-light adaptation |
| **Adaptation** | How strongly the effect reacts to scene luminance |
| **Peripheral Vision** | Makes the effect stronger away from screen center |
| **Tint** | Final hue shift of the adaptation |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Purkinje;

[SerializeField] private VolumeProfile volumeProfile;

private void SetNightAdaptation(float value)
{
  if (volumeProfile.TryGet(out PurkinjeVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.darkness.overrideState = true;
    volume.darkness.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect is lightweight and well suited to full-time use in night scenes.

* Pass Count: 1 blit pass.
* Texture Samples: Very low.
* Complexity: O(1) per pixel.

##### Usage Patterns and Presets

###### Natural Night Scene

For subtle night adaptation:
* Darkness: 0.2 - 0.4
* Adaptation: 0.5 - 0.7
* Peripheral Vision: 0.2 - 0.35

###### Horror Darkness

For more oppressive night response:
* Darkness: 0.5 - 0.8
* Tint: cool blue-green
* Peripheral Vision: 0.4 - 0.6

---
## 💥 Broken Screen {#brokenscreen}
{{< asset-header youtube="eqaPjR1KYPg" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-broken-screen-256124" demo="https://fronkongames.github.io/demos-spiceup/brokenscreen/" warn="assets used in video and demo are not included">}}

'**Broken Screen**' generates procedural fractures around an impact point and combines them with glass-like distortion and chromatic aberration.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Broken Screen**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Broken Screen**.
4. Enable '**Intensity**' and the fracture parameters you want to control.

#### Parameter Configuration

{{< image src="brokenscreen_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Impact

For '**Broken Screen**', the controls are documented in the same order they appear in the custom inspector, starting at the impact point and continuing through the fracture styling controls.

{{< table >}}
| | |
|---|---|
| **Impact** | Fracture center in normalized screen space |
| **Splits** | Number of fracture branches |
| **Width** | Thickness of the cracks |
| **Threshold** | Limit of where fracture coloration is applied |
| **Blend** | Blend mode used by the fracture color |
| **Color** | Tint of the broken glass lines |
| **Distortion** | Refraction strength in the background |
| **Aberration** | Color separation around the cracks |
| **Seed** | Random seed for reproducible patterns |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.BrokenScreen;

[SerializeField] private VolumeProfile volumeProfile;

private void CrackScreen()
{
  if (volumeProfile.TryGet(out BrokenScreenVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.impact.overrideState = true;
    volume.RandomValues();
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect is implemented in one pass and is usually inexpensive.

* Pass Count: 1 blit pass.
* Texture Samples: Low to moderate.
* Complexity: O(1) per pixel.

##### Usage Patterns and Presets

###### Bullet Impact

For sharp localized hits:
* Splits: 10 - 20
* Width: 0.5 - 1.2
* Distortion: 0.1 - 0.2

###### Shattered Visor

For catastrophic damage:
* Splits: 25 - 50
* Aberration: 0.2 - 0.5
* Distortion: 0.25 - 0.5

---
## 💓 Pulse {#pulse}
{{< asset-header youtube="63-RWxded2A" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-pulse-257920" demo="https://fronkongames.github.io/demos-spiceup/pulse/" warn="assets used in video and demo are not included">}}

'**Pulse**' creates an expanding frame or shockwave centered on a point of the screen. It is ideal for heartbeat cues, focus pulses, magical scans, or impact waves.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Pulse**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Pulse**.
4. Enable '**Intensity**' and the pulse parameters you want to animate.

#### Parameter Configuration

{{< image src="pulse_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Progress

The '**Pulse**' parameters are described in inspector order here, from the runtime timeline through the final color and blend controls.

{{< table >}}
| | |
|---|---|
| **Progress** | Animated pulse timeline from 0 to 1 |
| **Duration** | Natural duration of the event |
| **Center** | Pulse origin on the screen |
| **Alpha** | Maximum transparency of the pulse |
| **Scale** | Maximum pulse expansion |
| **Tint** | Pulse color |
| **Blend** | Blend operation of the pulse |
{{< /table >}}

##### Runtime Control

```csharp
using System.Collections;
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Pulse;

[SerializeField] private VolumeProfile volumeProfile;

private IEnumerator PlayPulse()
{
  if (volumeProfile.TryGet(out PulseVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.progress.overrideState = true;
    volume.progress.value = 0.0f;
    volume.intensity.value = 1.0f;

    float duration = volume.duration.value;
    float time = 0.0f;
    while (time < duration)
    {
      volume.progress.value = time / duration;
      time += volume.useScaledTime.value ? Time.deltaTime : Time.unscaledDeltaTime;
      yield return null;
    }

    volume.progress.value = 0.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect is lightweight and runs in a single pass.

* Pass Count: 1 blit pass.
* Texture Samples: Low.
* Complexity: O(1) per pixel.

##### Usage Patterns and Presets

###### Heartbeat

For medical or stress pulses:
* Duration: 0.5 - 0.8
* Scale: 2.0 - 3.0
* Tint: red

###### Shockwave

For impact bursts:
* Duration: 0.25 - 0.5
* Scale: 4.0 - 8.0
* Blend: Screen or Additive

---
## 🌪️ Shake {#shake}
{{< asset-header youtube="5Zc_0_BYOVw" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-shake-258721" demo="https://fronkongames.github.io/demos-spiceup/shake/" warn="assets used in video and demo are not included">}}

'**Shake**' is a screen-space shake effect that combines directional movement with zoom, distortion, and chromatic offsets.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Shake**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Shake**.
4. Enable '**Intensity**' and the shake parameters you want to animate.

#### Parameter Configuration

{{< image src="shake_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Direction

This section walks through '**Shake**' in the same order as the custom inspector, starting with direction, duration, and zoom.

{{< table >}}
| | |
|---|---|
| **Direction** | Base direction of the shake |
| **Duration** | Duration of one shake event |
| **Zoom** | Zoom component of the impact |
{{< /table >}}

##### Shake

The nested '**Shake**' block in the custom inspector defines the main violent motion layered over the directional impulse.

{{< table >}}
| | |
|---|---|
| **Shake** | Main shake amplitude |
| **Frequency** | Shake frequency |
| **Aberration** | RGB shift during the shake |
| **Distort** | Extra screen distortion |
{{< /table >}}

##### Noise

The custom inspector places these extra randomness controls inside the nested '**Noise**' block.

{{< table >}}
| | |
|---|---|
| **Noise** | Added randomness and irregularity |
| **Frequency** | Noise frequency |
{{< /table >}}

##### Runtime Control

```csharp
using System.Collections;
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Shake;

[SerializeField] private VolumeProfile volumeProfile;

private IEnumerator PlayShake()
{
  if (volumeProfile.TryGet(out ShakeVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.progress.overrideState = true;
    volume.progress.value = 0.0f;
    volume.intensity.value = 1.0f;

    float duration = volume.duration.value;
    float time = 0.0f;
    while (time < duration)
    {
      volume.progress.value = time / duration;
      time += volume.useScaledTime.value ? Time.deltaTime : Time.unscaledDeltaTime;
      yield return null;
    }

    volume.progress.value = 0.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect is implemented as a single pass and remains inexpensive.

* Pass Count: 1 blit pass.
* Texture Samples: Low.
* Complexity: O(1) per pixel.

##### Usage Patterns and Presets

###### Small Impact

For weapon kick or minor collisions:
* Duration: 0.1 - 0.25
* Zoom: 0.05 - 0.15
* Shake: 0.05 - 0.15

###### Earthquake

For prolonged instability:
* Duration: 0.5 - 1.5
* Shake: 0.2 - 0.5
* Noise: 0.2 - 0.6

---
## 🟢 Night Vision {#nightvision}
{{< asset-header youtube="7Dam3W04TzU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-night-vision-259563" demo="https://fronkongames.github.io/demos-spiceup/nightvision/" warn="assets used in video and demo are not included">}}

'**Night Vision**' is the most feature-rich effect in the bundle. It combines low-resolution rendering, blur, glow, luminance remapping, gradients, edge detection, distortion, noise, scanlines, UI overlays, and vignette shapes in one system.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Night Vision**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Night Vision**.
4. Enable '**Intensity**' and the vision-system parameters you want to control.

#### Parameter Configuration

{{< image src="nightvision_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Resolution

For '**Night Vision**', the parameter flow below matches the exact custom inspector order, starting with resolution, blur, and glow.

{{< table >}}
| | |
|---|---|
| **Resolution** | Internal render scale of the effect |
| **Blur** | Blur quality and softness |
| **Glow** | Additional phosphor glow |
{{< /table >}}

##### Color Grading

{{< image src="nightvision_1.jpg" wrapper="col-8 mx-auto">}}

Inside the custom inspector, the '**Color Grading**' foldout shapes the tonal response before the gradient remap is applied.

{{< table >}}
| | |
|---|---|
| **Exposure** | Exposure compensation |
| **Brightness** | Pre-gradient brightness |
| **Contrast** | Pre-gradient contrast |
| **Saturation** | Pre-gradient saturation |
{{< /table >}}

##### Gradient

{{< image src="nightvision_2.jpg" wrapper="col-8 mx-auto">}}

The '**Gradient**' foldout in the custom inspector controls the luminance remap and the gradient that colors the effect.

{{< table >}}
| | |
|---|---|
| **Strength** | How strongly the gradient replaces grayscale |
| **Tint** | Built-in gradient preset selection |
| **Custom Gradient** | Gradient used when `Tint` is set to `Custom` |
| **Luminance Range** | Brightness range remapping |
{{< /table >}}

##### Edge

{{< image src="nightvision_3.jpg" wrapper="col-8 mx-auto">}}

The custom inspector handles edge detection styling inside the '**Edge**' foldout.

{{< table >}}
| | |
|---|---|
| **Strength** | Edge detection strength |
| **Width** | Edge width |
| **Tint** | Edge tint |
| **Blend** | Edge blend mode |
{{< /table >}}

##### UI

{{< image src="nightvision_4.jpg" wrapper="col-8 mx-auto">}}

The reticle and overlay elements are configured in the custom inspector under the '**UI**' foldout.

{{< table >}}
| | |
|---|---|
| **Intensity** | Overall UI overlay intensity |
| **Center** | Overlay center |
| **Cross Width / Tint** | Cross size and color |
| **Grid Size / Tint** | Grid size and color |
| **Tint / Radius #0 / Radius #1 / Radius #2** | Circle tint plus the three circle radii |
{{< /table >}}

##### Vignette

{{< image src="nightvision_5.jpg" wrapper="col-8 mx-auto">}}

Use the '**Vignette**' foldout in the custom inspector to configure the framing controls summarized below.

{{< table >}}
| | |
|---|---|
| **Vignette** | Screen, binocular, or monocular framing mode |
| **Scale** | Vignette scale |
| **Softness** | Vignette softness |
{{< /table >}}

##### Glitches

{{< image src="nightvision_6.jpg" wrapper="col-8 mx-auto">}}

The custom inspector groups the distortion, digital noise, scanline, and RGB-offset artifacts inside the '**Glitches**' foldout.

{{< table >}}
| | |
|---|---|
| **Distortions Passes** | Number of distortion passes |
| **Barrel / Aberration** | Nested barrel distortion and chromatic aberration controls |
| **Digital Noise Threshold / Max Offset** | Digital-TV noise trigger and maximum offset |
| **Noise / Tint** | Analog noise amount and tint |
| **Scanline / Blend / Density / Tint** | Scanline artifact and its nested controls |
| **RGB Offset** | Black/white bias and phosphor feel |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.NightVision;

[SerializeField] private VolumeProfile volumeProfile;

private void SetNightVision(bool enabled)
{
  if (volumeProfile.TryGet(out NightVisionVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.intensity.value = enabled ? 1.0f : 0.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Night Vision Manager

{{< image src="nigthvision_manager.jpg" wrapper="col-8 mx-auto">}}

`NightVisionManager` is an optional helper component that turns the effect into a full gameplay system rather than just a volume override.

* **On**: the main runtime toggle.
* **VolumeProfile**: must contain the `NightVisionVolume` used by the manager.
* **SwitchOnTime / SwitchOffTime**: ramp-in and ramp-out duration.
* **AutomaticLightManagement**: automatically disables other realtime lights and manages a spotlight on the same object.
* **LightRange / LightInnerAngle / LightOuterAngle / LightIntensity / LightShadow / LightCullingMask**: spotlight configuration.
* **AudioSource / SwitchOnClip / SwitchOffClip**: optional switch sounds.
* **IgnoreLights**: realtime lights that should remain active when night vision turns on.

The manager also exposes an `OnSwitch` event and will create a hidden spotlight automatically if light management is enabled and no light is already present.

##### Performance Characteristics

This is one of the heavier effects in the bundle because it chains multiple operations.

* Pass Count: 3 blit-style passes.
* Texture Samples: Moderate to high depending on blur, UI, and noise settings.
* Memory: Additional temporary render textures are used for the pipeline stages.

##### Usage Patterns and Presets

###### Tactical NVG

For realistic night-ops presentation:
* Resolution: Half or Normal
* Blur: 1 - 2
* Glow: 1.0 - 2.5
* UI > Intensity: 0.05 - 0.15

###### Horror Camcorder Vision

For dirtier cinematic night vision:
* Blur: 2 - 4
* Edge > Strength: medium
* Noise: medium/high
* Vignette: binocular or monocular

---
## 🎥 BodyCam {#bodycam}
{{< asset-header youtube="pBp_WXNzlTY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-bodycam-260035" demo="https://fronkongames.github.io/demos-spiceup/bodycam/" warn="assets used in video and demo are not included">}}

'**BodyCam**' simulates the look of compact wearable cameras using lens warping, radial blur, flare artifacts, band-limited color, and sensor noise.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > BodyCam**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > BodyCam**.
4. Enable '**Intensity**' and the camera-style parameters you want to control.

#### Parameter Configuration

{{< image src="bodycam_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Fish eye

For '**BodyCam**', this section follows the exact custom inspector order, beginning with the '**Fish eye**' block and its nested lens-shaping controls.

{{< table >}}
| | |
|---|---|
| **Fish eye** | Lens zoom / warp |
| **Offset** | Shift of the lens center |
| **Vignette scale** | Edge shaping scale |
| **Vignette softness** | Edge shaping softness |
| **Aberration** | Chromatic aberration at the edges |
{{< /table >}}

##### Blur

The '**Blur**' block in the custom inspector contains the radial blur settings described here.

{{< table >}}
| | |
|---|---|
| **Blur** | Radial blur strength |
| **Samples** | Blur quality |
| **Falloff** | Blur falloff |
{{< /table >}}

##### Flare

Lens reflex behavior is configured in the custom inspector through the '**Flare**' block below.

{{< table >}}
| | |
|---|---|
| **Flare** | Lens reflex strength |
| **Radius** | Flare radius |
| **Angle** | Flare angle |
| **RGB** | RGB flare offsets |
{{< /table >}}

##### Chroma band

These standalone controls appear after `Flare` in the custom inspector and define the band-limited look of the sensor.

{{< table >}}
| | |
|---|---|
| **Chroma band / Luma band** | Band-limited color and luma resolution |
{{< /table >}}

##### Shadow tint

The custom inspector uses the '**Shadow tint**' block to control tonal bias in the darker parts of the image.

{{< table >}}
| | |
|---|---|
| **Shadow tint** | Color bias in darker tones |
| **White Level / Black Level** | Contrast/level shaping |
{{< /table >}}

##### Noise

This final standalone '**Noise**' control appears at the bottom of the custom inspector and adds signal noise to the result.

{{< table >}}
| | |
|---|---|
| **Noise** | Signal noise |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.BodyCam;

[SerializeField] private VolumeProfile volumeProfile;

private void SetBodyCam(bool enabled)
{
  if (volumeProfile.TryGet(out BodyCamVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.intensity.value = enabled ? 1.0f : 0.0f;
  }
}
```

You can simulate a reflection of a light with '**Angle**'. You can change it manually, or you can synchronize it with the Y axis of your character's rotation:

```csharp
volume.flareAngle.value = this.transform.eulerAngles.y;
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### BodyCam Roll

{{< image src="bodycam_1.jpg" wrapper="col-8 mx-auto">}}

`BodyCamRoll` is an optional helper component that writes camera-rotation inertia into `BodyCamVolume.offset` so the center of the effect lags behind the camera.

* **Strength**: amount of offset generated from rotation changes.
* **Speed**: how quickly the offset catches up.
* **UpdateRotation()**: resets the internal baseline rotation.

`UpdateRotation()` is useful after teleports, snap turns, cutscenes, or any hard transform reset, so the next frame does not produce a sudden offset jump.

Note that this component is designed for objects that move in the XZ plane, and therefore rotate on the Y axis (as in the vast majority of FPS). If in your game the displacement planes are different, you will have to modify the code.

##### Performance Characteristics

The effect is a little heavier than the simpler single-pass effects because it uses a two-stage render path.

* Pass Count: 2 blit-style passes.
* Texture Samples: Moderate and affected by blur sample count.
* Memory: Temporary render texture used between stages.

##### Usage Patterns and Presets

###### Police Body Camera

For a believable documentary look:
* Fish eye: 0.15 - 0.3
* Blur: 0.1 - 0.25
* Noise: 0.1 - 0.25
* Shadow tint: slightly blue

###### Horror Found Footage

For stronger stylization:
* Fish eye: 0.25 - 0.4
* Aberration: 2.0 - 4.0
* Noise: 0.25 - 0.5
* BodyCamRoll: enabled

---
## ✨ Lens Flare {#lensflare}
{{< asset-header youtube="9Z6wVV6XXPk" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-lens-flare-261769" demo="https://fronkongames.github.io/demos-spiceup/lensflare/" warn="assets used in video and demo are not included">}}

'**Lens Flare**' generates stylized flare streaks from bright regions of the image and is especially effective in high-contrast scenes.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Lens Flare**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Lens Flare**.
4. Enable '**Intensity**' and the flare parameters you want to tune.

#### Parameter Configuration

{{< image src="lensflare_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Iterations

For '**Lens Flare**', the explanation below keeps the exact inspector order, starting with the flare-generation controls before the nested blend and bands blocks.

{{< table >}}
| | |
|---|---|
| **Iterations** | Quality level and number of flare samples |
| **Scale** | Horizontal spread of the flares |
| **Threshold** | Brightness cutoff used to generate flares |
| **ACES** | Tonemapping influence |
| **Grain** | Grain added to the final image |
{{< /table >}}

##### Blend

The nested '**Blend**' block in the custom inspector controls how the flare is composited over the source image.

{{< table >}}
| | |
|---|---|
| **Blend** | Blend mode used to composite the flares |
| **Tint** | Flare color |
| **Gamma** | Gamma shaping of the flare response |
{{< /table >}}

##### Bands

The cinematic top-and-bottom band treatment is configured in the custom inspector inside the nested '**Bands**' block.

{{< table >}}
| | |
|---|---|
| **Bands** | Cinematic band strength |
| **Tint** | Band tint |
{{< /table >}}

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Lensflare;

[SerializeField] private VolumeProfile volumeProfile;

private void SetFlares(float value)
{
  if (volumeProfile.TryGet(out LensflareVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.threshold.overrideState = true;
    volume.threshold.value = value;
    volume.intensity.value = 1.0f;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

The effect runs in a single pass, but cost increases with iteration count.

* Pass Count: 1 blit pass.
* Texture Samples: Dependent on **Iterations**.
* Complexity: O(n) with respect to flare iteration count.

##### Usage Patterns and Presets

###### Clean Cinematic Flare

For bright sci-fi or police lights:
* Iterations: 24 - 32
* Threshold: 0.25 - 0.4
* Blend: Additive

###### Stylized Film Look

For heavier cinematic shaping:
* Iterations: 32 - 48
* ACES: 0.2 - 0.5
* Grain: 0.1 - 0.3
* Bands: 0.05 - 0.15

---
## 🌫️ Blurry {#blurry}
{{< asset-header youtube="izte-BmU-nw" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-blurry-251642" demo="https://fronkongames.github.io/demos-spiceup/blurry/" warn="assets used in video and demo are not included">}}

'**Blurry**' creates delayed blurred vision by blending the current frame with a configurable history of previous frames. It feels temporal rather than purely optical, which makes it well suited to dizziness, dream sequences, concussions, intoxication, and slow-motion shock states.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0.58f2 or higher.
* **Universal RP:** 17.0.3 or higher.

#### Installation Guide

##### Step 1: Add Renderer Feature

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select **Fronkon Games > Spice Up > Blurry**.

##### Step 2: Configure the Volume

1. Create a **Volume** component (Global or Local).
2. In the Volume component, create or assign a **Volume Profile**.
3. Click **Add Override** and select **Fronkon Games > Spice Up > Blurry**.
4. Enable '**Intensity**' and the frame-history parameters you want to control.

#### Parameter Configuration

{{< image src="blurry_0.jpg" wrapper="col-8 mx-auto">}}

With '**Intensity**' you can control the overall strength of the effect [0.0 - 1.0]. If it is 0, the effect will not be active.

##### Frames

For '**Blurry**', the notes below follow the exact custom inspector order, from the stored history size through the capture timing and history resolution.

{{< table >}}
| | |
|---|---|
| **Frames** | Number of history frames used, from 1 to 10 |
| **Wait** | Pause between captured frames |
| **Resolution** | Resolution scale of the stored history frames |
{{< /table >}}

Lower frame counts produce a milder smear. Higher values create stronger temporal blur, but increase memory use and the amount of visible lag in the effect.

##### Runtime Control

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.SpiceUp.Blurry;

[SerializeField] private VolumeProfile volumeProfile;

private void SetBlur(float value)
{
  if (volumeProfile.TryGet(out BlurryVolume volume))
  {
    volume.intensity.overrideState = true;
    volume.frames.overrideState = true;
    volume.intensity.value = value;
    volume.frames.value = 5;
  }
}
```

💡 Take a look at the code in the included demo to learn more about how the effect works.

##### Performance Characteristics

`Blurry` is one of the more memory-sensitive effects because it stores frame history.

* Pass Count: copy + effect pass, plus history management.
* Texture Samples: Multiple history-frame lookups depending on **Frames**.
* Memory: Up to 10 history render targets are maintained internally.

##### Usage Patterns and Presets

###### Concussion Blur

For gameplay-safe disorientation:
* Frames: 3 - 5
* Wait: 0.01 - 0.03
* Resolution: 0.75 - 1.0

###### Dream Sequence

For more pronounced temporal smear:
* Frames: 6 - 10
* Wait: 0.03 - 0.08
* Resolution: 0.25 - 0.75

---
## F.A.Q.

##### _Effect Not appearing_

If the effect doesn't appear in your scene:

1. **Verify Renderer Feature**: Check that the renderer feature is added to your Universal Renderer Data asset.
2. **Check Volume Profile**: Ensure a Volume component exists in your scene with the effect override enabled.
3. **Confirm Intensity**: Verify that the Intensity parameter is set to a value greater than 0.0 and enabled.
4. **Camera Settings**: Check that your camera has Post Processing enabled in the Camera component.

##### _How do I make the effect also affect the UI?_

If your UI is using '**Screen Space - Overlay**', it bypasses the camera and therefore bypasses the effect. Change the canvas to '**Screen Space - Camera**' and assign the camera used for rendering the effect.

{{< image src="ui.jpg" wrapper="col-6 mx-auto">}}

##### _Can I use it in a material?_

Yes! Any effect can easily be used on a material. Just follow these steps:

* In the '**Project**' window, open the '**Create**' menu with the right mouse button and select '**Create > Render Texture**'.
* Create a new camera and in '**Output Texture**' select the Render Texture previously created. Remember to activate '**Post Processing**' and select in '**Renderer**' where you have the effect added.
* In the material you want to use, select in '**Base Map**' the Render Texture.
<br>

##### _Why does changing a value from code sometimes do nothing?_

In URP volumes, the parameter override must be enabled. When setting values from code, remember to set `overrideState = true` for every parameter you want the volume system to apply.

---
## Support

Do you have any problem or any suggestions? Send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

If you want to report an error, it helps a lot if you include the [Unity log file](https://docs.unity3d.com/Manual/LogFiles.html).

{{< rawhtml >}}
<br><center><h4>
{{< /rawhtml >}}

{{< alert color="warning" >}}
If you are happy with this asset, consider writing a review in the store.

Thanks!
{{< /alert >}}

{{< rawhtml >}}
</center></h4>
{{< /rawhtml >}}
