---
author: Martin Bustos
title: Camera Transitions
showTitle: false
date: 3
description: Cinematic, realtime and easy-to-use transitions between cameras in a camera
tags: ["unity", "store", "camera", "transitions", "transition", "fade", "realtime", "cinematic", "cinema", "film"]
metadata: none
showImage: false
thumbnail:
  url: img/camera-transitions.jpg
---
{{< asset-header youtube="8eKo8r3TG44" store="" demo="https://fronkongames.github.io/demo-camera-transitions/" >}}

This asset provides a collection of **cinematic**, **realtime** and **easy-to-use** camera transition effects to enhance your games. Effortlessly switch between cameras with a variety of visual styles, from simple transitions to complex effects.

## Requirements

*   Unity 6000.0 LTS or newer.
*   Universal Render Pipeline (URP) 17.0.4 or newer.

## Installation

1.  Download and import the Camera Transitions asset from the Unity Asset Store into your Unity project.
2.  Ensure your project is configured to use URP. If not, please refer to the [official Unity documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-introduction.html) on how to set up URP.
3.  No additional setup is required. The asset is ready to use out of the box!

## Quick Start

To use a camera transition:

1.  Ensure you have at least two `Camera` objects in your scene.
2.  Add the `Transition Renderer Feature` as a `Renderer Feature`. This [official tutorial](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html) tells how to do it.
3.  Make sure there is an instance of `Transition Manager` in your scene. If not, create an empty GameObject and add the `Transition Manager` component to it.
4.  Call the static `Start` method of the desired transition class from your script.

**Example:**

```csharp
using UnityEngine;
using FronkonGames.CameraTransitions; // Import the namespace

public class TransitionTest : MonoBehaviour
{
    public Camera cameraA;
    public Camera cameraB;
    public float transitionDuration = 1.0f;

    void Start()
    {
        // Example: Start a CrossZoom transition from cameraA to cameraB
        TransitionCrossZoom.Start(cameraA, cameraB, transitionDuration);
    }
}
```

{{< alert color="info" >}}
This asset **does not handle scene loading** or switching between scenes. All transitions are performed between cameras that exist within a **scene**.
{{< /alert >}}

---

### Cross Zoom

<center><video controls loop="true" src="/store/camera-transitions/CrossZoom.webm"></video></center>

A zoom and cross-fade effect. The current camera zooms out while the new camera zooms in and fades, creating a smooth and dynamic transition.

**Parameters:**

*   `strength`: `float` (optional) - The intensity of the zoom effect. Determines how much the camera will scale during the transition. Default is `0.4f`. Range `[0.0f, 1.0f]`.
*   `quality`: `float` (optional) - Effect quality, affecting the smoothness or detail of the zoom. Default is `20.0f`. Range `[1.0f, 40.0f]`.

**Example Usage:**

```csharp
// Uses default strength and quality.
TransitionCrossZoom.Start(cameraA, cameraB, 1.0f);

// Uses custom strength and quality.
TransitionCrossZoom.Start(cameraA, cameraB, 1.0f, strength: 0.6f, quality: 30.0f);
```

---

### Bounce

<center><video controls loop="true" src="/store/camera-transitions/Bounce.webm"></video></center>

A bouncing effect for the transition. The outgoing camera appears to bounce off the screen, revealing the incoming camera.

**Parameters:**

*   `bounces`: `float` (optional) - The number of bounces during the transition. Default is `3.0f`. Recommended range `[1.0f, 10.0f]`.
*   `shadowColor`: `Color` (optional) - The color of the shadow effect beneath the bouncing element. Default is `Color(0.0f, 0.0f, 0.0f, 0.6f)`.
*   `shadowHeight`: `float` (optional) - The height or prominence of the shadow. Default is `0.075f`. Range `[0.0f, 0.2f]`.

**Example Usage:**

```csharp
// Uses default parameters.
TransitionBounce.Start(cameraA, cameraB, 1.5f);

// Uses custom parameters for more bounces and a different shadow.
TransitionBounce.Start(cameraA, cameraB, 1.5f, bounces: 5.0f, shadowColor: Color.blue, shadowHeight: 0.1f);
```

---

### Bars

<center><video controls loop="true" src="/store/camera-transitions/Bars.webm"></video></center>

A horizontal bars effect. The new camera is revealed through a series of horizontal bars that wipe across the screen.

**Parameters:**

*   This transition does not have any configurable parameters beyond the standard duration. The number and behavior of the bars are predefined in the shader.

**Example Usage:**

```csharp
TransitionBars.Start(cameraA, cameraB, 0.75f);
```

---

### Circle Crop

<center><video controls loop="true" src="/store/camera-transitions/CircleCrop.webm"></video></center>

Crops to a background color in a circle, then reveals the new camera.

**Parameters:**

*   `backgroundColor`: `Color` (optional) - The color of the circular crop area that appears during the transition. Defaults to `Color.black`.

**Example Usage:**

```csharp
// Uses the default black background.
TransitionCircleCrop.Start(cameraA, cameraB, 1.0f);

// Uses a custom background color (e.g., white).
TransitionCircleCrop.Start(cameraA, cameraB, 1.0f, Color.white);
```

---

### Chromatic Waves

<center><video controls loop="true" src="/store/camera-transitions/ChromaticWaves.webm"></video></center>

Creates a wave effect with chromatic aberration.

**Parameters:**

*   `amplitude`: `float` (optional) - The amplitude of the waves. Default is `1.0f`.
*   `waves`: `float` (optional) - The number of waves. Default is `30.0f`.
*   `colorSeparation`: `float` (optional) - The amount of color separation. Default is `0.3f`.

**Example Usage:**

```csharp
// Uses default parameters.
TransitionChromaticWaves.Start(cameraA, cameraB, 1.0f);

// Uses custom parameters.
TransitionChromaticWaves.Start(cameraA, cameraB, 1.0f, amplitude: 2.0f, waves: 15.0f, colorSeparation: 0.1f);
```

---

### Color Distance

<center><video controls loop="true" src="/store/camera-transitions/ColorDistance.webm"></video></center>

Transitions pixels based on the color difference between the two cameras.

**Parameters:**

*   `power`: `float` (optional) - Power curve for the overall transition. Affects the speed and intensity of the transition based on color differences. Recommended range `[1.0, 10.0]`. Default is `5.0f`.

**Example Usage:**

```csharp
// Uses the default power value.
TransitionColorDistance.Start(cameraA, cameraB, 1.0f);

// Uses a custom power value.
TransitionColorDistance.Start(cameraA, cameraB, 1.0f, power: 2.5f);
```

---

### Cube

<center><video controls loop="true" src="/store/camera-transitions/Cube.webm"></video></center>

A 3D cube rotation effect. The current view rotates out on one face of a cube while the new view rotates in on another.

**Parameters:**

*   `perspective`: `float` (optional) - The amount of perspective distortion applied to the cube. Range `[0.0, 1.0]`. Default is `0.7f`.
*   `zoom`: `float` (optional) - The zoom level of the camera during the transition. Range `[0.0, 100.0]`. Default is `0.3f`.
*   `reflection`: `float` (optional) - The intensity of the reflection on the cube faces. Range `[0.0, 1.0]`. Default is `0.4f`.
*   `elevation`: `float` (optional) - The perceived elevation or height of the cube. Range `[0.0, 100.0]`. Default is `3.0f`.

**Example Usage:**

```csharp
// Uses default parameters.
TransitionCube.Start(cameraA, cameraB, 1.5f);

// Uses custom parameters for a stronger perspective and less reflection.
TransitionCube.Start(cameraA, cameraB, 1.5f, perspective: 0.9f, zoom: 0.2f, reflection: 0.1f, elevation: 2.0f);
```

---

### Doom

<center><video controls loop="true" src="/store/camera-transitions/Doom.webm"></video></center>

A circular iris wipe with a noisy, Doom-like ([the game](https://www.youtube.com/watch?v=S7IEg0_qNXs)) screen melt effect.

**Parameters:**

*   `barWidth`: `int` (optional) - The width of the "bars" or columns in the melt effect. Default is `50`. Range `[0, N]` (non-negative).
*   `amplitude`: `float` (optional) - The height difference or displacement amplitude of the bars during the melt. Range `[0.0, 25.0]`. Default is `2.0f`.
*   `noise`: `float` (optional) - The amount of noise applied to the bar heights, creating a more chaotic melt. Range `[0.0, 1.0]`. Default is `0.1f`.
*   `frequency`: `float` (optional) - The frequency of the noise pattern. Range `[0.0, 100.0]`. Default is `1.0f`.

**Example Usage:**

```csharp
// Uses default parameters.
TransitionDoom.Start(cameraA, cameraB, 1.2f);

// Uses custom parameters for a more pronounced effect.
TransitionDoom.Start(cameraA, cameraB, 1.2f, barWidth: 30, amplitude: 5.0f, noise: 0.3f, frequency: 2.0f);
```

---

### Fade To Color

<center><video controls loop="true" src="/store/camera-transitions/FadeToColor.webm"></video></center>

Fades the current camera to a solid color, then fades from that color to the new camera.

**Parameters:**

*   `strength`: `float` (optional) - Determines how much the solid color dominates at the peak of the transition. A value of `1.0` means the screen will be fully the `fadeColor`. Range `[0.0, 1.0]`. Default is `0.3`.
*   `fadeColor`: `Color` (optional) - The solid color used for the fade. Default is `Color.black`.

**Example Usage:**

```csharp
// Fades to black with default strength.
TransitionFadeToColor.Start(cameraA, cameraB, 1.0f);

// Fades to white with a stronger effect.
TransitionFadeToColor.Start(cameraA, cameraB, 1.0f, strength: 0.8f, fadeColor: Color.white);
```

---

### Fade To Grayscale

<center><video controls loop="true" src="/store/camera-transitions/FadeToGrayscale.webm"></video></center>

Fades the current camera to grayscale, then fades from grayscale to reveal the new camera.

**Parameters:**

*   `strength`: `float` (optional) - Controls the intensity of the grayscale effect at the peak of the transition. A value of `1.0` means the camera will be fully desaturated. Range `[0.0, 1.0]`. Default is `0.3`.

**Example Usage:**

```csharp
// Fades to grayscale with default strength.
TransitionFadeToGrayscale.Start(cameraA, cameraB, 1.0f);

// Fades to grayscale with a stronger effect.
TransitionFadeToGrayscale.Start(cameraA, cameraB, 1.0f, strength: 0.9f);
```

---

### Flash

<center><video controls loop="true" src="/store/camera-transitions/Flash.webm"></video></center>

A bright flash effect that briefly illuminates the screen, transitioning to the new camera.

**Parameters:**

*   `strength`: `float` (optional) - The strength or phase of the flash effect. Affects how much the flash color dominates. Range `[0.0, 1.0]`. Default is `0.3`.
*   `intensity`: `float` (optional) - The brightness intensity of the flash color. Range `[0.0, 5.0]`. Default is `3.0`.
*   `zoom`: `float` (optional) - The amount of zoom effect applied during the flash. Range `[0.0, 1.0]`. Default is `0.5`.
*   `velocity`: `float` (optional) - The speed of the flash effect. Range `[0.1, 10.0]`. Default is `3.0`.
*   `flashColor`: `Color` (optional) - The color of the flash. Default is `Color.white`.

**Example Usage:**

```csharp
// Uses default white flash.
TransitionFlash.Start(cameraA, cameraB, 0.5f);

// Uses a custom red flash with higher intensity and faster speed.
TransitionFlash.Start(cameraA, cameraB, 0.5f, strength: 0.5f, intensity: 4.0f, zoom: 0.2f, velocity: 5.0f, flashColor: Color.red);
```

---

### Flip

<center><video controls loop="true" src="/store/camera-transitions/Flip.webm"></video></center>

Flips the view horizontally or vertically to reveal the new camera.

**Parameters:**

*   `mode`: `TransitionAxis` (optional) - Determines the axis of the flip. Can be `TransitionAxis.Horizontal` or `TransitionAxis.Vertical`. Default is `TransitionAxis.Vertical`.
*   `compress`: `bool` (optional) - If `true`, the image will appear to compress along the flip axis during the transition. If `false`, it will flip without compression. Default is `true`.

**Example Usage:**

```csharp
// Uses default vertical flip with compression.
TransitionFlip.Start(cameraA, cameraB, 0.8f);

// Uses a horizontal flip without compression.
TransitionFlip.Start(cameraA, cameraB, 0.8f, mode: TransitionAxis.Horizontal, compress: false);
```

---

### Fold

<center><video controls loop="true" src="/store/camera-transitions/Fold.webm"></video></center>

Folds the camera like a piece of paper, revealing the new camera underneath.

**Parameters:**

*   `mode`: `TransitionAxis` (optional) - Determines the direction of the fold. Can be `TransitionAxis.Horizontal` or `TransitionAxis.Vertical`. Default is `TransitionAxis.Vertical`.
*   `compress`: `bool` (optional) - If `true`, the image will appear to compress as it folds. If `false`, it folds without compression, maintaining its aspect ratio more strictly during the fold. Default is `true`.

**Example Usage:**

```csharp
// Uses default vertical fold with compression.
TransitionFold.Start(cameraA, cameraB, 1.0f);

// Uses a horizontal fold without compression.
TransitionFold.Start(cameraA, cameraB, 1.0f, mode: TransitionAxis.Horizontal, compress: false);
```

---

### Focus

<center><video controls loop="true" src="/store/camera-transitions/Focus.webm"></video></center>

Creates a depth-of-field-like focus effect. The camera blurs and zooms in a way that simulates a camera lens changing focus, with different parts of the screen (rings) zooming at different rates.

**Parameters:**

*   `focalDepthPoint`: `float` (optional) - The point in the transition (normalized time `[0.01, 0.99]`) at which the incoming camera starts to become clear and mix with the outgoing camera. Default is `0.8`.
*   `focalLength`: `float` (optional) - Controls the softness or duration of the mix between the two cameras after the `focalDepthPoint` is reached. A smaller value means a sharper, quicker focus change. Range `[0.01, 0.5]`. Default is `0.07`.
*   `zoomIntensity`: `float` (optional) - The overall intensity of the zoom effect applied during the transition. Range `[0.0, 1.0]`. Default is `0.2`.
*   `ringZoomFactors`: `Vector4` (optional) - A `Vector4` defining the relative zoom factors for four concentric rings, from the center outwards (x=center, y=mid, z=mid-outer, w=outer). These values are scaled by `zoomIntensity`. Default is `(0.1f, 0.15f, 0.2f, 0.25f)`.

**Example Usage:**

```csharp
// Uses default parameters for a subtle focus shift.
TransitionFocus.Start(cameraA, cameraB, 1.5f);

// Custom parameters for a more pronounced and faster focus effect.
TransitionFocus.Start(cameraA, cameraB, 1.5f, 
                      focalDepthPoint: 0.6f, 
                      focalLength: 0.05f, 
                      zoomIntensity: 0.35f, 
                      ringZoomFactors: new Vector4(0.05f, 0.1f, 0.15f, 0.3f));
```

---

### Galaxy

<center><video controls loop="true" src="/store/camera-transitions/Galaxy.webm"></video></center>

Creates a galaxy-like swirl or pattern effect for the transition.

**Parameters:**

*   `kx`: `float` (optional) - Controls the horizontal influence or frequency of the galaxy pattern. Range `[0.1, 10.0]`. Default is `1.5`.
*   `ky`: `float` (optional) - Controls the vertical influence or frequency of the galaxy pattern. Range `[0.1, 10.0]`. Default is `0.5`.
*   `q`: `float` (optional) - Quality or detail factor for the generated patterns. Higher values can lead to more complex or defined shapes. Range `[0.5, 10.0]`. Default is `3.0`.
*   `invert`: `bool` (optional) - If `true`, inverts the transition effect, potentially changing which parts of the pattern appear first or how they evolve. Default is `false`.

**Example Usage:**

```csharp
// Uses default parameters for a standard galaxy swirl.
TransitionGalaxy.Start(cameraA, cameraB, 2.0f);

// Custom parameters for a different pattern and inverted effect.
TransitionGalaxy.Start(cameraA, cameraB, 2.0f, 
                       kx: 2.5f, 
                       ky: 1.0f, 
                       q: 5.0f, 
                       invert: true);
```

---

### Gate

<center><video controls loop="true" src="/store/camera-transitions/Gate.webm"></video></center>

A gate-like opening effect. The current camera splits and opens like a set of gates, revealing the new camera behind it.

**Parameters:**

*   `perspective`: `float` (optional) - The amount of perspective applied to the "gates" as they open. Range `[0.0, 1.0]`. Default is `0.4`.
*   `depth`: `float` (optional) - Affects the perceived depth or thickness of the gates. Range `[0.0, 100.0]`. Default is `3.0`.
*   `reflection`: `float` (optional) - The intensity of reflections on the inner surfaces of the opening gates. Range `[0.0, 1.0]`. Default is `0.4`.

**Example Usage:**

```csharp
// Uses default parameters for a standard gate opening.
TransitionGate.Start(cameraA, cameraB, 1.2f);

// Custom parameters for a more dramatic gate effect with less reflection.
TransitionGate.Start(cameraA, cameraB, 1.2f, perspective: 0.6f, depth: 5.0f, reflection: 0.1f);
```

---

### Glitch

<center><video controls loop="true" src="/store/camera-transitions/Glitch.webm"></video></center>

A digital glitch distortion effect. The camera fragments and distorts as it transitions to the new view.

**Parameters:**

*   `strength`: `float` (optional) - Controls the intensity of the glitch and displacement effect. Higher values result in more pronounced distortion. Range `[0.0, 10.0]`. Default is `0.4`.

**Example Usage:**

```csharp
// Uses default glitch strength.
TransitionGlitch.Start(cameraA, cameraB, 0.7f);

// Uses a stronger glitch effect.
TransitionGlitch.Start(cameraA, cameraB, 0.7f, strength: 1.5f);
```

---

### Glass

<center><video controls loop="true" src="/store/camera-transitions/Glass.webm"></video></center>

Creates a glass-like distortion effect, as if viewing the camera through a textured or irregular piece of glass.

**Parameters:**

*   `size`: `float` (optional) - Controls the size or scale of the distortion pattern. Default is `0.04`.
*   `zoom`: `float` (optional) - Affects the zoom factor of the distortion, influencing how much the "glass" appears to magnify or refract. Default is `50.0`.
*   `colorSeparation`: `float` (optional) - The amount of chromatic aberration or color splitting introduced by the glass effect. Default is `0.3`.

**Example Usage:**

```csharp
// Uses default glass distortion parameters.
TransitionGlass.Start(cameraA, cameraB, 1.0f);

// Custom parameters for a coarser distortion with more color separation.
TransitionGlass.Start(cameraA, cameraB, 1.0f, size: 0.1f, zoom: 30.0f, colorSeparation: 0.6f);
```

---

### Gradient

<center><video controls loop="true" src="/store/camera-transitions/Gradient.webm"></video></center>

Uses a grayscale texture to control the wipe pattern between camera. The transition progresses based on the luminance values of the gradient texture.

**Parameters:**

*   `gradientTexture`: `Texture` (**required**) - The grayscale texture that defines the wipe pattern. Brighter areas of the texture will transition earlier than darker areas.
*   `borderSize`: `float` (optional) - Controls the thickness of the border effect during the wipe. Range `[0.0, 0.5]`. Default is `0.1`.
*   `softness`: `float` (optional) - Determines the softness or feathering of the transition edge. Higher values create a smoother, more blended edge. Range `[0.001, 0.25]`. Default is `0.05`.

**Example Usage:**

```csharp
public Texture2D myGradientPattern; // Assign this in the Inspector

// ...

// Uses a custom gradient texture with default border and softness.
TransitionGradient.Start(cameraA, cameraB, 1.5f, myGradientPattern);

// Uses a custom gradient with specific border and softness.
TransitionGradient.Start(cameraA, cameraB, 1.5f, myGradientPattern, borderSize: 0.05f, softness: 0.1f);
```

In the `FronkonGames/CameraTransitions/Gradients/Textures` folder you can find more than **250 gradients** that you can use.

A `GradientBank` ScriptableObject (_Create > Fronkon Games > Camera Transitions > Gradient Bank_) is also provided with the asset. You can create instances of `GradientBank` to store collections of gradient textures and easily use them in your transitions.

**Example Usage:**

```csharp
public GradientBank gradientBank; // Assign this in the Inspector

// ...

// Uses the first texture of the gradient bank.
TransitionGradient.Start(cameraA, cameraB, 1.5f, gradientBank.textures[0]);

// Uses a random texture of the gradient bank.
TransitionGradient.Start(cameraA, cameraB, 1.5f,
                         gradientBank.textures[Random.Range(0, gradientBank.textures.Count)]);
```

---

### Grid Flip

<center><video controls loop="true" src="/store/camera-transitions/GridFlip.webm"></video></center>

Reveals the next camera through a grid of cells that flip over, either sequentially or with some randomness.

**Parameters:**

*   `size`: `Vector2Int` (optional) - The number of columns (x) and rows (y) in the grid. Range `[(1,1), (100,100)]`. Default is `(4,4)`.
*   `pause`: `float` (optional) - Duration of a pause at the beginning (showing the original camera) and end (showing the new camera) of the transition, during which cells are static. This value is a fraction of the total transition time. Range `[0.0, 0.49]`. Default is `0.1`.
*   `dividerWidth`: `float` (optional) - The width of the dividers or gaps between grid cells, expressed as a fraction of a cell's size. Range `[0.0, 0.5]`. Default is `0.05`.
*   `backgroundColor`: `Color` (optional) - The color shown in the dividers between cells and during the pause phases if the cells don't cover the entire screen. Default is `Color.black`.
*   `randomness`: `float` (optional) - A factor that introduces randomness to the flip timing of individual cells. A value of `0.0` means cells flip in a more ordered sequence, while `1.0` introduces maximum randomness. Range `[0.0, 1.0]`. Default is `0.1`.

**Example Usage:**

```csharp
// Uses default parameters for a 4x4 grid flip.
TransitionGridFlip.Start(cameraA, cameraB, 1.5f);

// Custom parameters for a larger grid with more randomness and a different background.
TransitionGridFlip.Start(cameraA, cameraB, 2.0f, 
                         size: new Vector2Int(10, 6), 
                         pause: 0.05f, 
                         dividerWidth: 0.02f, 
                         backgroundColor: Color.blue, 
                         randomness: 0.5f);
```

---

### Hexagon

<center><video controls loop="true" src="/store/camera-transitions/Hexagon.webm"></video></center>

Creates a transition effect using a grid of resizing or appearing hexagons.

**Parameters:**

*   `steps`: `int` (optional) - Controls the number of discrete steps or stages in the hexagonal animation. Affects the granularity of the effect. Default is `50`.
*   `horizontalHexagons`: `float` (optional) - Determines the number of hexagons that would fit horizontally across the screen, influencing their individual size. Default is `20.0`.

**Example Usage:**

```csharp
// Uses default hexagon parameters.
TransitionHexagon.Start(cameraA, cameraB, 1.3f);

// Custom parameters for larger hexagons (fewer horizontally) and more steps.
TransitionHexagon.Start(cameraA, cameraB, 1.3f, steps: 70, horizontalHexagons: 10.0f);
```

---

### Ink Spread

<center><video controls loop="true" src="/store/camera-transitions/InkSpread.webm"></video></center>

An organic ink spread effect using noise. The new camera is revealed as if ink is spreading across the screen.

**Parameters:**

*   `noiseScale`: `float` (optional) - Controls the scale of the noise pattern that drives the ink spread. Smaller values create larger, more spread-out patterns; larger values create finer, more detailed patterns. Range `[1.0, 50.0]`. Default is `10.0`.
*   `noiseSpeed`: `float` (optional) - Determines how fast the noise pattern evolves or animates over time. A value of `0` results in a static noise pattern. Range `[0.0, 2.0]`. Default is `0.1`.

**Example Usage:**

```csharp
// Uses default ink spread parameters.
TransitionInkSpread.Start(cameraA, cameraB, 1.8f);

// Custom parameters for a larger scale, faster evolving ink spread.
TransitionInkSpread.Start(cameraA, cameraB, 1.8f, noiseScale: 5.0f, noiseSpeed: 0.5f);
```

---

### Linear Blur

<center><video controls loop="true" src="/store/camera-transitions/LinearBlur.webm"></video></center>

Applies a linear blur effect during the transition. The camera smoothly blurs and then unblurs to reveal the new camera.

**Parameters:**

*   `intensity`: `float` (optional) - Controls the maximum intensity of the blur effect. Range `[0.0, 1.0]`. Default is `0.1`.
*   `passes`: `int` (optional) - Determines the number of blur passes, which affects the quality and smoothness of the blur. More passes result in a smoother blur but can be more performance-intensive. Range `[1, 8]`. Default is `8`.

**Example Usage:**

```csharp
// Uses default blur intensity and passes.
TransitionLinearBlur.Start(cameraA, cameraB, 1.0f);

// Uses a stronger blur with fewer passes for a potentially faster but less smooth effect.
TransitionLinearBlur.Start(cameraA, cameraB, 1.0f, intensity: 0.3f, passes: 4);
```

---

### Luminance Melt

<center><video controls loop="true" src="/store/camera-transitions/LuminanceMelt.webm"></video></center>

Melts the camera based on its luminance (brightness) values, revealing the new camera. Pixels will "melt" or "drip" away depending on their brightness and the chosen parameters.

**Parameters:**

*   `meltDownwards`: `bool` (optional) - If `true`, the melt effect moves downwards (pixels drip down). If `false`, it moves upwards. Default is `true`.
*   `luminanceThreshold`: `float` (optional) - The luminance value that serves as a threshold for the melt effect. Range `[0.0, 1.0]`. Default is `0.8`.
*   `checkAboveThreshold`: `bool` (optional) - If `true`, pixels brighter than `luminanceThreshold` are affected by the melt. If `false`, pixels darker than `luminanceThreshold` are affected. Default is `false` (affects darker pixels).

**Example Usage:**

```csharp
// Default: darker pixels melt downwards.
TransitionLuminanceMelt.Start(cameraA, cameraB, 1.5f);

// Brighter pixels melt upwards, with a lower luminance threshold.
TransitionLuminanceMelt.Start(cameraA, cameraB, 1.5f, 
                              meltDownwards: false, 
                              luminanceThreshold: 0.5f, 
                              checkAboveThreshold: true);
```

---

### Mosaic

<center><video controls loop="true" src="/store/camera-transitions/Mosaic.webm"></video></center>

A mosaic pixelation effect. The camera transitions by breaking into mosaic tiles that change to reveal the new camera.

**Parameters:**

*   `steps`: `Vector2` (optional) - Controls the size and apparent movement of the mosaic cells. These are integer step values for how the mosaic pattern is constructed. Avoid `(0,0)`. Range for each component is typically `[-10, 10]`. Default is `(1,1)`.
*   `rotate`: `bool` (optional) - If `true`, the individual mosaic cells will be randomly rotated during the transition, adding to the effect. Default is `false`.

**Example Usage:**

```csharp
// Uses default mosaic parameters.
TransitionMosaic.Start(cameraA, cameraB, 1.0f);

// Custom steps for a different mosaic pattern, with cell rotation enabled.
TransitionMosaic.Start(cameraA, cameraB, 1.0f, steps: new Vector2(2, -1), rotate: true);
```

---

### Page Curl

<center><video controls loop="true" src="/store/camera-transitions/PageCurl.webm"></video></center>

Simulates a page curling effect, where the current camera curls up or away like a sheet of paper to reveal the new camera.

**Parameters:**

*   `angle`: `float` (optional) - The angle of the page curl in degrees. This determines the direction from which the page curls. Range `[0.0, 180.0]`. Default is `45.0`.
*   `radius`: `float` (optional) - The radius of the curl itself. Smaller values create a tighter curl. Range `[0.0, 1.0]`. Default is `0.1`.
*   `frontShadow`: `bool` (optional) - If `true`, a shadow effect is applied to the front (visible side) of the curling page. Default is `true`.
*   `backTransparency`: `float` (optional) - Controls the transparency of the back side of the curling page. `0.0` is fully transparent, `1.0` is fully opaque. Range `[0.0, 1.0]`. Default is `0.25`.
*   `backShadow`: `bool` (optional) - If `true`, a shadow effect is applied to the back side of the curling page. Default is `true`.
*   `innerShadow`: `bool` (optional) - If `true`, a shadow effect is applied to the area of the camera being revealed, where the page is curling away from. Default is `true`.

**Example Usage:**

```csharp
// Uses default page curl parameters.
TransitionPageCurl.Start(cameraA, cameraB, 1.5f);

// Custom parameters for a tighter curl from a different angle, with more back page transparency.
TransitionPageCurl.Start(cameraA, cameraB, 1.5f, 
                         angle: 120.0f, 
                         radius: 0.05f, 
                         frontShadow: false, 
                         backTransparency: 0.5f, 
                         backShadow: true, 
                         innerShadow: true);
```

---

### Pixelate

<center><video controls loop="true" src="/store/camera-transitions/Pixelate.webm"></video></center>

A pixelation reveal effect. The outgoing camera becomes increasingly pixelated, then resolves into the new camera which starts pixelated and becomes clear.

**Parameters:**

*   `pixelSize`: `float` (optional) - Controls the size of the pixels during the transition. Larger values result in a more coarse pixelation. Default is `50.0f`. Range `[0.0f, N]` (non-negative).

**Example Usage:**

```csharp
// Uses default pixel size.
TransitionPixelate.Start(cameraA, cameraB, 1.0f);

// Uses a larger pixel size for a more blocky effect.
TransitionPixelate.Start(cameraA, cameraB, 1.0f, pixelSize: 100.0f);
```

---

### Polka Dots

<center><video controls loop="true" src="/store/camera-transitions/PolkaDots.webm"></video></center>

A polka dot reveal effect. The new camera is revealed through a pattern of growing (or shrinking) polka dots.

**Parameters:**

*   `dots`: `float` (optional) - Controls the number of dots that would fit across the screen, effectively determining their size. Range `[1.0, 100.0]`. Default is `20.0`.
*   `center`: `Vector2` (optional) - The center point (in normalized screen coordinates, `(0,0)` is center) from which the polka dots appear to scale or originate. Range typically `[(-1,-1), (1,1)]` but can be outside for off-screen origins. Default is `(0,0)` (center of the screen).

**Example Usage:**

```csharp
// Uses default polka dot parameters.
TransitionPolkaDots.Start(cameraA, cameraB, 1.0f);

// Custom parameters for fewer, larger dots, originating from the top-left.
TransitionPolkaDots.Start(cameraA, cameraB, 1.0f, dots: 8.0f, center: new Vector2(-1.0f, 1.0f));
```

---

### Radial

<center><video controls loop="true" src="/store/camera-transitions/Radial.webm"></video></center>

A radial wipe effect. The new camera is revealed by a wipe that rotates around the center of the screen, similar to a clock hand.

**Parameters:**

*   `clockwise`: `bool` (optional) - If `true`, the radial wipe proceeds in a clockwise direction. If `false`, it proceeds counter-clockwise. Default is `true`.

**Example Usage:**

```csharp
// Uses default clockwise radial wipe.
TransitionRadial.Start(cameraA, cameraB, 1.0f);

// Uses a counter-clockwise radial wipe.
TransitionRadial.Start(cameraA, cameraB, 1.0f, clockwise: false);
```

---

### Ripple

<center><video controls loop="true" src="/store/camera-transitions/Ripple.webm"></video></center>

Creates a ripple distortion effect, as if a disturbance is spreading across the screen, transitioning from one camera to the other.

**Parameters:**

*   `amplitude`: `float` (optional) - Controls the height or intensity of the ripple waves. Default is `100.0`.
*   `speed`: `float` (optional) - Determines the speed at which the ripples propagate across the screen. Default is `50.0`.

**Example Usage:**

```csharp
// Uses default ripple amplitude and speed.
TransitionRipple.Start(cameraA, cameraB, 1.0f);

// Custom parameters for a more pronounced and faster ripple.
TransitionRipple.Start(cameraA, cameraB, 1.0f, amplitude: 150.0f, speed: 75.0f);
```

---

### Roto Zoom

<center><video controls loop="true" src="/store/camera-transitions/RotoZoom.webm"></video></center>

Creates a rotating and zooming effect. The camera scales down while rotating around a central point, then the new camera scales up and rotates into place.

**Parameters:**

*   `center`: `Vector2` (optional) - The center point (in normalized screen coordinates, `(0.5, 0.5)` is the screen center) for the rotation and zoom effect. Default is `(0.5, 0.5)`.
*   `rotations`: `float` (optional) - The number of full 360-degree rotations the camera will perform during the transition. Can be fractional. Default is `1.0`.
*   `scale`: `float` (optional) - The initial (and final) scale factor. The camera zooms from/to this scale. A higher value means more zoom. Default is `8.0`.
*   `backColor`: `Color` (optional) - The background color visible in areas outside the scaled and rotated image, especially when the image is zoomed out. Default is a dark gray `(0.15, 0.15, 0.15, 1.0)`.

**Example Usage:**

```csharp
// Uses default RotoZoom parameters.
TransitionRotoZoom.Start(cameraA, cameraB, 1.5f);

// Custom parameters for more rotations, less zoom, and a different background color.
TransitionRotoZoom.Start(cameraA, cameraB, 1.5f, 
                         center: new Vector2(0.25f, 0.75f), 
                         rotations: 2.5f, 
                         scale: 4.0f, 
                         backColor: Color.blue);
```

---

### Schwifty

<center><video controls loop="true" src="/store/camera-transitions/Schwifty.webm"></video></center>

A psychedelic warping effect. The camera distorts with a "[schwifty](https://www.youtube.com/watch?v=4ctK1aoWuqY)" visual style, transitioning to the new camera.

**Parameters:**

*   `intensity`: `float` (optional) - Controls the overall intensity of the schwifty distortion. Internally, this value is scaled (multiplied by `0.1` in the shader). Range `[0.0, 1.0]`. Default is `0.3`.
*   `amplitude`: `float` (optional) - Affects the amplitude or magnitude of the warping and distortion. Range `[0.0, 20.0]`. Default is `10.0`.

**Example Usage:**

```csharp
// Uses default schwifty parameters.
TransitionSchwifty.Start(cameraA, cameraB, 1.0f);

// Custom parameters for a more intense and amplified schwifty effect.
TransitionSchwifty.Start(cameraA, cameraB, 1.0f, intensity: 0.8f, amplitude: 15.0f);
```

---

### Simple

<center><video controls loop="true" src="/store/camera-transitions/Simple.webm"></video></center>

A simple linear fade between camera. The outgoing camera fades out while the incoming camera fades in.

**Parameters:**

*   This transition does not have any configurable parameters beyond the standard duration.

**Example Usage:**

```csharp
TransitionSimple.Start(cameraA, cameraB, 1.0f);
```

---

### Slice

<center><video controls loop="true" src="/store/camera-transitions/Slice.webm"></video></center>

Creates a slicing effect for the transition. The camera is divided into a number of slices that transition sequentially or with a smooth overlap.

**Parameters:**

*   `count`: `float` (optional) - The number of slices the screen is divided into. Range `[1.0, 100.0]`. Default is `10.0f`.
*   `smoothness`: `float` (optional) - Controls the smoothness of the transition between slices. A lower value means sharper, more distinct slice transitions, while a higher value creates a softer overlap between slices. Range `[0.0, 1.0]`. Default is `0.5f`.

**Example Usage:**

```csharp
// Uses default slice count and smoothness.
TransitionSlice.Start(cameraA, cameraB, 1.0f);

// Custom parameters for more slices and a sharper transition.
TransitionSlice.Start(cameraA, cameraB, 1.0f, count: 20.0f, smoothness: 0.1f);
```

---

### Smash

<center><video controls loop="true" src="/store/camera-transitions/Smash.webm"></video></center>

Creates a vertical squash and stretch effect, accompanied by color separation, as if the camera is being "smashed" down and then bouncing back with the new camera.

**Parameters:**

*   `colorSeparation`: `float` (optional) - Controls the amount of chromatic aberration or color splitting that occurs during the squash and stretch. Higher values increase the separation. Default is `0.04`.

**Example Usage:**

```csharp
// Uses default color separation.
TransitionSmash.Start(cameraA, cameraB, 0.8f);

// Uses a higher color separation for a more pronounced effect.
TransitionSmash.Start(cameraA, cameraB, 0.8f, colorSeparation: 0.1f);
```

---

### Smooth Circle

<center><video controls loop="true" src="/store/camera-transitions/SmoothCircle.webm"></video></center>

A smooth circular wipe. The new camera is revealed by a circle that expands from (or contracts to) a central point, with a soft, anti-aliased edge.

**Parameters:**

*   `smoothness`: `float` (optional) - Controls the softness or feathering of the circle's edge. Higher values create a more gradual transition at the edge. Range `[0.0, 1.0]`. Default is `0.3`.
*   `center`: `Vector2` (optional) - The center point (in normalized screen coordinates, `(0.0, 0.0)` is bottom-left, `(1.0, 1.0)` is top-right) from which the circle expands or to which it contracts. Default is `(0.5, 0.5)` (screen center).
*   `invert`: `bool` (optional) - If `false` (default), the circle expands to reveal the new camera. If `true`, the circle contracts, with the old camera disappearing into the center point, revealing the new camera around it. Default is `false`.

**Example Usage:**

```csharp
// Uses default parameters for a circle expanding from the center.
TransitionSmoothCircle.Start(cameraA, cameraB, 1.0f);

// Custom parameters for a circle contracting to the top-right with more smoothness.
TransitionSmoothCircle.Start(cameraA, cameraB, 1.0f, 
                             smoothness: 0.6f, 
                             center: new Vector2(1.0f, 1.0f), 
                             invert: true);
```

---

### Smooth Line

<center><video controls loop="true" src="/store/camera-transitions/SmoothLine.webm"></video></center>

A transition that wipes across the screen along a configurable angle with a soft edge.

**Parameters:**

*   `smoothness`: `float` (optional) - Defines the softness of the transition's edge. Default is `0.5f`. Range `[0.0f, 1.0f]`.
*   `angle`: `float` (optional) - The angle of the wipe line in degrees. `0` degrees is typically a vertical wipe from left to right (or right to left if inverted), `90` degrees is a horizontal wipe. Default is `45.0f`. Range `[0.0f, 360.0f]`.

**Example Usage:**

```csharp
// Uses default smoothness and angle.
TransitionSmoothLine.Start(cameraA, cameraB, 1.0f);

// Custom angle and smoothness.
TransitionSmoothLine.Start(cameraA, cameraB, 1.0f, angle: 90.0f, smoothness: 0.1f);
```

---

### Swap

<center><video controls loop="true" src="/store/camera-transitions/Swap.webm"></video></center>

two cameras swap places with a 3D perspective effect. One camera slides out while the other slides in, often with a sense of depth and optional reflection.

**Parameters:**

*   `perspective`: `float` (optional) - Controls the amount of perspective distortion during the swap. Higher values create a more pronounced 3D effect. Default is `0.2f`. Range `[0.0f, 1.0f]`.
*   `depth`: `float` (optional) - Affects the perceived depth or distance of the swapping planes. Default is `3.0f`. Range `[0.0f, 100.0f]`.
*   `reflection`: `float` (optional) - Intensity of the reflection effect on the planes. Default is `0.05f`. Range `[0.0f, 1.0f]`.

**Example Usage:**

```csharp
// Uses default parameters.
TransitionSwap.Start(cameraA, cameraB, 1.0f);

// Custom perspective and depth, no reflection (implicitly 0.05).
TransitionSwap.Start(cameraA, cameraB, 1.0f, perspective: 0.5f, depth: 5.0f);

// With a noticeable reflection.
TransitionSwap.Start(cameraA, cameraB, 1.0f, reflection: 0.6f);
```

---

### Valentine

<center><video controls loop="true" src="/store/camera-transitions/Valentine.webm"></video></center>

A heart-themed transition. Often involves a heart shape expanding or contracting to reveal the new camera, possibly with a colored border.

**Parameters:**

*   `border`: `float` (optional) - The width of the heart shape's border. Default is `25.0f`. Range `[0.0f, 100.0f]`.
*   `borderColor`: `Color` (optional) - The color of the heart's border. Default is `Color.red` (1,0,0,1).

**Example Usage:**

```csharp
// Uses default border width and color.
TransitionValentine.Start(cameraA, cameraB, 1.0f);

// Custom border width and a pink border color.
TransitionValentine.Start(cameraA, cameraB, 1.0f, border: 10.0f, borderColor: new Color(1.0f, 0.75f, 0.8f));
```

---

### Vortex

<center><video controls loop="true" src="/store/camera-transitions/Vortex.webm"></video></center>

A spiraling vortex or whirlpool effect. The image appears to be sucked into or expelled from a central point with a twisting motion.

**Parameters:**

*   `distortion`: `float` (optional) - Controls the intensity or tightness of the vortex effect. Higher values create a more pronounced spiral. Default is `0.3f`. Range `[0.0f, 1.0f]`.

**Example Usage:**

```csharp
// Uses default distortion.
TransitionVortex.Start(cameraA, cameraB, 1.0f);

// A more intense vortex.
TransitionVortex.Start(cameraA, cameraB, 1.0f, distortion: 0.7f);
```

---

### Warp Wave

<center><video controls loop="true" src="/store/camera-transitions/WarpWave.webm"></video></center>

A wave-like distortion warps the camera as it transitions. The wave can be horizontal or vertical, and its curvature can be adjusted.

**Parameters:**

*   `mode`: `TransitionAxis` (enum) (optional) - Determines the direction of the wave. Can be `TransitionAxis.Horizontal` or `TransitionAxis.Vertical`. Default is `TransitionAxis.Horizontal`.
*   `curvature`: `float` (optional) - Controls the amount of bend or curve in the wave. Default is `0.5f`. Range `[0.0f, 5.0f]`.

**Example Usage:**

```csharp
// Uses default horizontal wave with default curvature.
TransitionWarpWave.Start(cameraA, cameraB, 1.0f);

// A vertical wave with more pronounced curvature.
TransitionWarpWave.Start(cameraA, cameraB, 1.0f, mode: TransitionAxis.Vertical, curvature: 2.0f);
```

---

### Wind

<center><video controls loop="true" src="/store/camera-transitions/Wind.webm"></video></center>

A wind-swept effect. The camera appears to be blown away by streaks of wind, revealing the new camera beneath.

**Parameters:**

*   `size`: `float` (optional) - Controls the size or thickness of the wind streaks. Default is `0.2f`. Range `[0.0f, 1.0f]`.

**Example Usage:**

```csharp
// Uses default wind streak size.
TransitionWind.Start(cameraA, cameraB, 1.0f);

// Larger, more prominent wind streaks.
TransitionWind.Start(cameraA, cameraB, 1.0f, size: 0.5f);
```

---

### Water Drop

<center><video controls loop="true" src="/store/camera-transitions/WaterDrop.webm"></video></center>

A water drop ripple effect. The transition emanates from the center of the screen like ripples from a water drop, revealing the new camera.

**Parameters:**

*   `amplitude`: `float` (optional) - Controls the amplitude or height of the ripple waves. Recommended range `[1.0f, 100.0f]`. Default is `30.0f`.
*   `speed`: `float` (optional) - Determines the speed at which the ripple waves propagate outwards. Recommended range `[1.0f, 100.0f]`. Default is `30.0f`.

**Example Usage:**

```csharp
// Uses default water drop parameters.
TransitionWaterDrop.Start(cameraA, cameraB, 1.0f);

// Custom parameters for a stronger and faster ripple.
TransitionWaterDrop.Start(cameraA, cameraB, 1.0f, amplitude: 50.0f, speed: 60.0f);
```

---

### Wipe

<center><video controls loop="true" src="/store/camera-transitions/Wipe.webm"></video></center>

A directional wipe effect. The new camera is revealed by a line that wipes across the screen, either horizontally or vertically.

**Parameters:**

*   `mode`: `TransitionAxis` (optional) - Determines the direction of the wipe. Can be `TransitionAxis.Horizontal` or `TransitionAxis.Vertical`. Default is `TransitionAxis.Vertical`.

**Example Usage:**

```csharp
// Uses default vertical wipe.
TransitionWipe.Start(cameraA, cameraB, 1.0f);

// Uses a horizontal wipe.
TransitionWipe.Start(cameraA, cameraB, 1.0f, mode: TransitionAxis.Horizontal);
```

---

### Zoom

<center><video controls loop="true" src="/store/camera-transitions/Zoom.webm"></video></center>

A zoom and crossfade effect. The current camera zooms out, and as it zooms, it begins to fade into the new camera.

**Parameters:**

*   `zoomQuickness`: `float` (optional) - Controls how quickly the zoom portion of the effect completes within the total transition duration. A value of `0.2` means the zoom finishes very early in the transition, while `1.0` means it finishes at the very end. The fade to the next camera typically starts slightly before the zoom completes. Range `[0.2f, 1.0f]`. Default is `0.8f`.

**Example Usage:**

```csharp
// Uses default zoom quickness.
TransitionZoom.Start(cameraA, cameraB, 1.0f);

// Custom parameter for a faster initial zoom.
TransitionZoom.Start(cameraA, cameraB, 1.0f, zoomQuickness: 0.4f);
```

---
#
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
