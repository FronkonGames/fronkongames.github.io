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
* [Photo](#photo), recreates the authentic look & feel of professional cameras.
* [Shockwave](#shockwave), stunning shockwave effects with customizable distortion.
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

All effects are compatible with **Unity 6**, and use [Render Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html). You will need to have URP version *17.0.2* or higher installed. In the [official documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html) you can find the steps to install it correctly.

Make sure that the '_Compatibility Mode_' is **disabled** (_Project Settings > Graphics > Render Graph_).

{{< image src="compatibility_mode.jpg" wrapper="col-6 mx-auto">}}

#### Unity 2022.3 or higher

You will need to have URP version *12.1.15* or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).


## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Artistic**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

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

Once you have added the effect in the Editor, you can also handle '**Artistic**' effects by code. 

First you must add the corresponding namespace. They are all of the style 'FronkonGames.Artistic.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**One Bit**' the code would be:

```csharp
using FronkonGames.Artistic.OneBit;
```

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

```csharp
OneBit.Settings settings = OneBit.Instance.settings;

settings.intensity = 0.5f;
```

And how can I activate and deactivate the effect? It's as easy as that:

```csharp
OneBit oneBit = OneBit.Instance;

// Switch between active and inactive.
if (oneBit.isActive == true)
  oneBit.SetActive(false);
else
  oneBit.SetActive(true);
```

{{< alert color="warning" icon="fas triangle-exclamation" >}}
The Instance function uses [Reflection](https://learn.microsoft.com/en-us/dotnet/fundamentals/reflection/reflection), and is therefore expensive. I recommend that you save the Instance value to use it without affecting performance.
{{< /alert >}}

If you are using an effect other than '**OneBit**' just change it to its name. Check the source code comments for more information.

#
---
## One Bit {#onebit}
{{< asset-header youtube="Yz9j7iXuDhY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/one-bit-216000" demo="https://fronkongames.github.io/demos-artistic/onebit/" warn="assets used in video and demo are not included">}}

Get a distinctive look with '**One Bit**', an original and versatile effect that uses a special type of dithering algorithm based on Blue Noise, similar to that used at the award-winning '_Return of the Obra Dinn_'.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="onebit_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

'**Edges**' (_2_) makes it remarked more the edges and '**Noise**' (_2_) affects the amount of noise that will appear on the screen. You can change the random seed used to generate the noise with '**Seed**'.

'**Blend**' (_4_), specifies the formula used to mix the original color of the screen with the effect. They are very similar to those you can find in '_Photoshop_'. With '**Color**' you can change the way a color (or several) effects the final result. The simplest is '**Solid**' and its '**Color**' parameter tints the image. Other modes are '**Horizontal**', '**Vertical**' and '**Circular**' and use two colors in a gradient in different directions.

{{< image src="onebit_1.jpg" wrapper="col-6 mx-auto">}}

'**Gradient**' is another mode that uses the brightness of the original pixel to replace it in a color gradient. So the leftmost colors of the gradient would be used for the darker areas of the image and the rightmost colors would be used for the brighter areas. Click on the gradient to modify it to your liking. If the gradient you use does not have dark colors, the result may be too bright, and vice versa. You can modify the brightness range used with '**Luminance**'.

Click on '**🔍**' icon to open the **Palette Tool**.

{{< image src="onebit_2.jpg" wrapper="col-6 mx-auto">}}

Simply enter the color you want to search for and **Palette Tool** will search over **6000** color palettes from [color-hex](https://www.color-hex.com/). Once you find the one that best fits your needs, click on the button with the name to apply it to the gradient.

In _6_, _7_ and _8_ you can modify the color range in each channel. Small values in these fields can create a '_retro_' effect.

When '**Invert**' (_9_) is activated, the color is inverted.

---
## Oil Paint {#oilpaint}
{{< asset-header youtube="A9jtFpXo02Q" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-oil-paint-264134" demo="https://fronkongames.github.io/demos-artistic/oilpaint/" warn="assets used in video and demo are not included">}}

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
{{< asset-header youtube="ixqjMNnUSus" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-tilt-shift-265465" demo="https://fronkongames.github.io/demos-artistic/tiltshift/" warn="assets used in video and demo are not included">}}

Used to simulate a miniature scene, something very used in cinema as in the [race scene](https://www.youtube.com/watch?v=QetnuKbo1XI) of '_The Social Network_'. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="tiltshift_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

You can modify the angle (_2_), aperture (_3_) and offset (_4_) of the effect. Also the blur intensity (_5_) and distortion (_6_).

You can also modify certain color parameters in the 'focused' (_7_) area (where the effect is not applied) and in the 'unfocus' (_8_) area.

{{< image src="tiltshift_1.jpg" wrapper="col-6 mx-auto" >}}

In order to better adjust these parameters, you can activate '**Debug**' (_9_) to better see how the effect is applied. With this parameter activated, the areas with more intensity of the effect will be tinted red, and those with less intensity will be tinted blue.

---
## Photo {#photo}
{{< asset-header youtube="LPs97XIfQTE" store="https://assetstore.unity.com/packages/slug/315961" demo="https://fronkongames.github.io/demos-artistic/photo/" warn="assets used in video and demo are not included">}}

A versatile film camera simulator, offering a comprehensive suite of effects that mimic the charm and character of analog photography. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="photo_0.png" wrapper="col-6 mx-auto">}}

#### Focus

The focus system simulates the depth of field effects found in real cameras. With a range from -1.0 to 1.0 (with 0.0 being perfect focus), you can create everything from tack-sharp images to dreamy, soft-focus scenes. The focus offset parameter controls how much the image shifts when out of focus, while the blur strength determines the intensity of the blurring effect.

This creates a realistic simulation of a camera's focusing mechanism, perfect for creating cinematic moments or highlighting specific elements in your scene.

#### Grid

The grid overlay simulates the viewfinder elements found in traditional cameras. When enabled, it creates a subtle points grid that helps with composition and framing. You can customize the color and blending mode to match your aesthetic preferences.

This feature is particularly useful for creating a diegetic camera interface or simulating the experience of looking through a vintage camera viewfinder.

#### Rings

The rings feature adds concentric circles to your view, simulating the optical elements inside a camera lens. With controls for thickness, sharpness, and individual ring scaling, you can create everything from subtle lens effects to pronounced artistic overlays. The ring split parameter allows you to adjust the spacing between rings, creating various optical patterns.
These rings can be colored and blended with the image in different ways, offering extensive creative possibilities.

#### Frost

The frost effect creates a soft, diffused glow around the edges of your frame, similar to what might be seen in vintage lenses or when shooting in cold conditions. You can adjust the intensity, color, and blending mode to achieve various atmospheric effects.

This subtle effect adds depth and character to your scenes, especially when combined with other lens effects.

#### Chromatic aberration

Chromatic aberration simulates the color fringing that occurs in real lenses when light wavelengths fail to converge at the same point. The effect can be controlled globally and fine-tuned per color channel, allowing for precise control over the look. From subtle, realistic lens imperfections to bold, stylized color separation, this effect adds authentic character to your camera.

#### Vignetting

The vignette effect darkens the corners of the image, drawing attention to the center of the frame. Choose between circular and rectangular vignettes, and adjust the size, smoothness, and aspect ratio to achieve your desired look. Vignetting is essential for creating authentic film looks and directing the viewer's attention to important elements in your scene.

#### Film grain

Film grain adds texture and character to your images, simulating the granular appearance of photographic film. Adjust the intensity to create anything from a subtle texture to a pronounced grainy look. This effect is crucial for achieving authentic film aesthetics and can add warmth and organic quality to digital imagery.

#### Aperture simulation

The aperture controls simulate the opening in a camera lens through which light passes. Adjust the size and number of blades.

#### Film manufactures

Accurate simulations of popular film stocks, each with its unique characteristics:

**Agfa Vista 400** provides a cool color balance with strong blue and green response, perfect for creating a budget film look.

**Cinestill 800T** delivers that cinematic quality with its distinctive red halation effect, ideal for night scenes and moody interiors.

**Fuji Velvia 50** offers high saturation and punchy contrast with enhanced red and blue response, making it perfect for landscape photography.

**Fuji C200** emphasizes cool tones with a blue bias, while **Fuji Pro 400H** delivers soft, natural skin tones with a neutral gray balance, making it excellent for portraits.

**Lomography Color 800** creates a distinctive look with heavy grain, cyan shift, and crushed shadows, perfect for creating a hipster aesthetic.

**ORWO UT18** simulates cinema film stock with green/magenta bias and soft highlight shoulder, while **Kodak Ektar 100** delivers ultra-vivid colors and high contrast.

**Kodak Portra 400**, a favorite among portrait photographers, offers soft highlight rolloff and enhanced greens for flattering skin tones.

**Kodak Gold 200** brings golden hues and a green boost, perfect for warm, nostalgic scenes.

For instant camera enthusiasts, **Polaroid 600** simulation provides warm tones and a strong vignette.

Finally, **Ilford HP5** offers a classic black and white look for timeless monochrome imagery.

#### Glitches and Imperfections

The charm of analog photography often comes from its imperfections. '**Photo**' offers several parameters to simulate these characteristics:

Chromatic fringing adds color separation in high-contrast areas, while dust particles can be added to simulate dirty lenses or aged film. Light leaks create those beautiful streaks of light that occur when light penetrates the camera body, with controls for both intensity and animation speed.

Color bleeding simulates the way colors can bleed into adjacent areas on film, and the expired years parameter recreates the look of film that has been stored beyond its expiration date, with shifts in color balance and contrast.

For **Cinestill 800T** film users, the halation effect creates that distinctive red glow around bright light sources, adding authenticity to night scenes and images with strong light sources.

---
## Shockwave {#shockwave}
{{< asset-header youtube="Lyg2Og-kzWM" store="https://assetstore.unity.com/packages/slug/330713" demo="https://fronkongames.github.io/demos-artistic/shockwave/" warn="assets used in video and demo are not included">}}

Create stunning shockwave effects with customizable distortion, chromatic aberration, flares, and edge detection. Perfect for explosions, time jumps, portals, and other dramatic visual effects. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="shockwave_0.png" wrapper="col-8 mx-auto">}}

#### Common Settings

``Intensity`` controls the overall intensity of the shockwave effect [0.0, 1.0]. When set to 0, the effect is completely disabled and will not execute. Values between 0 and 1 provide proportional effect strength, allowing for smooth transitions and blending with other post-processing effects.

#### Core Shockwave Parameters

``Radius`` defines the radius of the shockwave effect [0.0, 1.0]. A value of 0 indicates no shockwave is present, while a value of 1 creates a shockwave that extends beyond the screen boundaries. This parameter is fundamental to the effect's visual impact and should be animated to create the characteristic expanding wave motion.

``Center`` specifies the origin point of the shockwave in normalized screen coordinates [0.0, 1.0] for both X and Y components. The center point determines where the shockwave emanates from, with (0.5, 0.5) representing the center of the screen. This parameter is crucial for positioning the effect relative to specific game events or visual elements.

``Strength`` controls the intensity of the shockwave distortion [0.0, 5.0]. Higher values create more pronounced visual effects, while lower values provide subtle distortions. This parameter affects the magnitude of displacement and color shifts within the shockwave area.

``Width`` determines the thickness of the shockwave ring [0.01, 0.75]. This parameter controls how wide the visible shockwave band appears, affecting the overall visual density and impact of the effect.

#### Ring Configuration

``Ring Width (Inner/Outer)`` these parameters control the inner and outer boundaries of the shockwave ring [0.01, 1.0], allowing for asymmetric ring shapes and complex visual patterns. The inner width defines the distance from the center where the effect begins, while the outer width determines where it ends.

``Ring Sharpness`` controls the falloff rate of the shockwave effect from the ring center [1.0, 32.0]. Higher values create sharper, more defined edges, while lower values produce softer, more gradual transitions. This parameter significantly affects the visual quality and realism of the shockwave.

``Ring Skew`` applies asymmetric distortion to the ring thickness [-1.0, 1.0], pushing the effect either inward (negative values) or outward (positive values) from the center. This parameter enables creative variations in shockwave appearance and can simulate directional forces.

#### Color and Visual Effects

``Color Strength`` provides per-channel control over the color intensity of the shockwave effect. Each component (R, G, B) can be adjusted independently to create color-specific distortions and chromatic effects.

``Shockwave Color Blend`` determines how the shockwave color interacts with the underlying image. Different blend modes provide various visual effects, from solid overlays to hue shifts and additive blending.

``Chromatic Aberration`` creates color separation effects by applying different displacement amounts to each color channel. This parameter simulates lens distortion and adds cinematic realism to the shockwave effect.

#### Noise Effects

``Noise Amount`` controls the intensity of procedural noise applied to the shockwave [0.0, 1.0]. Noise adds organic variation and breaks up uniform patterns, creating more natural-looking effects.

``Noise Scale`` determines the frequency of the noise pattern [0.1, 64.0]. Higher values create fine-grained noise, while lower values produce larger, more visible noise patterns.

``Noise Speed`` controls the animation speed of the noise pattern [0.0, 5.0]. This parameter enables dynamic noise movement that can enhance the sense of energy and motion in the shockwave.

#### Flare Effects

``Flares Amount`` controls the intensity of lens flare effects within the shockwave area [0.0, 1.0]. Flares add bright highlights and lens artifacts that enhance the cinematic quality of the effect.

``Flares Color Blend`` determines the blending mode for flare colors, allowing for various visual treatments from solid overlays to additive effects.

``Flares Color`` specifies the base color of the flare effects. This parameter enables customization of the flare appearance to match specific visual themes or artistic requirements.

``Flares Frequency`` controls the density of flare elements within the shockwave [0.0, 64.0]. Higher values create more numerous, smaller flares, while lower values produce fewer, larger flare elements.

``Flares Speed`` determines the animation speed of flare effects [0.0, 5.0]. This parameter enables dynamic flare movement that can enhance the sense of energy and motion.

``Flares Threshold`` controls the brightness threshold at which flares become visible [0.0, 1.0]. This parameter enables fine-tuning of flare visibility and can be used to create more subtle or dramatic effects.

``Flares Softness`` controls the blur amount applied to flare effects [0.0, 10.0]. Higher values create softer, more diffused flares, while lower values produce sharper, more defined flare elements.

#### Inside Zone Effects

``Inside Tint`` applies a color tint to the area inside the shockwave ring. This parameter enables atmospheric effects and can simulate environmental changes within the shockwave area.

``Color Blend`` determines how the inside zone tint interacts with the underlying image. Different blend modes provide various visual treatments for the interior area.

#### Color Correction

``Brightness`` adjusts the overall brightness of the affected area [-1.0, 1.0]. Negative values darken the image, while positive values brighten it, enabling atmospheric and mood adjustments.

``Contrast`` controls the contrast ratio of the affected area [0.0, 2.0]. Values below 1.0 reduce contrast, while values above 1.0 increase it, affecting the visual impact and clarity of the effect.

``Gamma`` adjusts the gamma correction of the affected area [0.1, 10.0]. This parameter enables fine-tuning of the tonal response and can be used to match specific visual styles or compensate for display characteristics.

``Hue`` controls the hue shift applied to the affected area [0.0, 1.0]. This parameter enables color grading effects and can be used to create specific atmospheric conditions or artistic treatments.

``Saturation`` controls the color saturation of the affected area [0.0, 2.0]. Values below 1.0 reduce saturation (toward grayscale), while values above 1.0 increase it, enabling dramatic color effects.

#### Edge Effects

``Edge Amount`` controls the intensity of edge highlighting effects [0.0, 1.0]. Edge effects create bright outlines and highlights that enhance the visual definition of objects within the shockwave area.

``Edge Color Blend`` determines the blending mode for edge colors. The default Hue mode creates color-shifted edges that can enhance the visual impact of the effect.

``Edge Color`` specifies the base color for edge highlighting effects. This parameter enables customization of edge appearance to match specific visual themes.

``Edge Width`` controls the thickness of edge highlighting in texels [0.1, 5.0]. This parameter affects the visual prominence and definition of edge effects.

#### Edge Noise

``Edge Noise Amount`` controls the intensity of noise applied to edge effects [0.0, 1.0]. Edge noise adds organic variation to edge highlighting, creating more natural and dynamic visual results.

``Edge Noise Scale`` determines the frequency of edge noise patterns [0.1, 64.0]. This parameter controls the granularity and detail level of edge noise effects.

``Edge Noise Speed`` controls the animation speed of edge noise effects [0.0, 10.0]. Dynamic edge noise can enhance the sense of energy and motion in the shockwave.

#### Edge Plasma

``Edge Plasma Amount`` controls the intensity of plasma effects applied to edges [0.0, 1.0]. Plasma effects create animated, energy-like patterns that enhance the visual impact of edge highlighting.

``Edge Plasma Scale`` determines the frequency of plasma patterns [0.01, 64.0]. This parameter controls the size and detail level of plasma effects.

``Edge Plasma Speed`` controls the animation speed of plasma effects [0.0, 10.0]. Dynamic plasma can create compelling energy animations that enhance the shockwave's visual appeal.

#### Hue Variation Effects

``Hue Variation Amount`` controls the intensity of hue variation effects [0.0, 1.0]. When enabled, this parameter creates color shifts that vary across the shockwave area, adding dynamic color movement.

``Hue Variation Angular Scale`` controls the angular frequency of hue variation patterns [0.0, 2.0]. This parameter determines how many color bands appear around the shockwave center.

``Hue Variation Speed`` controls the animation speed of hue variation effects [-10.0, 10.0]. Positive values create clockwise rotation, while negative values create counterclockwise rotation.

``Hue Variation Radial Amount`` controls the intensity of radial hue variation effects [0.0, 1.0]. This parameter creates color shifts that vary with distance from the shockwave center.

``Hue Variation Radial Scale`` determines the radial frequency of hue variation patterns [0.0, 64.0]. This parameter controls how many color rings appear from the center outward.

---
## Color Isolation {#colorisolation}
{{< asset-header youtube="XfHdKU1qTF4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-color-isolation-266086" demo="https://fronkongames.github.io/demos-artistic/colorisolation/" warn="assets used in video and demo are not included">}}

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
{{< asset-header youtube="Xjax-orCmVY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-sharpen-266728" demo="https://fronkongames.github.io/demos-artistic/sharpen/" warn="assets used in video and demo are not included">}}

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
{{< asset-header youtube="XcLXlvqG5yU" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-tonemapper-267617" demo="https://fronkongames.github.io/demos-artistic/tonemapper/" warn="assets used in video and demo are not included">}}

Provides industry-standard tone mapping operators combined with professional color grading tools. It supports both HDR and LDR rendering pipelines and offers precise control over every aspect of your image's tone and color reproduction.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="tonemapper_0.jpg" wrapper="col-8 mx-auto">}}

#### Common Settings

* `Intensity`, controls the overall strength of the tonemapping effect. **Note**: An intensity of 0 will disable the effect entirely.

#### Tonemapping Operators

Choose from **28 different tonemapping algorithms**, each with unique characteristics:

{{< image src="tonemapper_1.jpg" wrapper="col-4 mx-auto">}}

##### Basic Operators
- **Linear**: Simple linear mapping (good reference point)
- **Logarithmic**: Natural logarithm-based mapping
- **Exponential**: Exponential curve mapping
- **Clamping**: Simple luminance threshold clamping

##### Reinhard Family
- **SimpleReinhard**: Basic Reinhard operator
- **LumaReinhard**: "Photographic Tone Reproduction for Digital Images" (Reinhard 2002)
- **LumaInvertedReinhard**: Reinhard with inverted luminance (Brian Karis)
- **WhiteLumaReinhard**: Luminance-based Reinhard with white preservation

##### Filmic Operators
- **Filmic**: Basic filmic tonemapping
- **FilmicAldridge**: Hejl and Burgess-Dawson variation (Graham Aldridge)
- **Hejl2015**: ACES-like curve (Jim Hejl)
- **Uncharted2**: Hable curve from Uncharted 2
- **WatchDogs**: Ubisoft's Watch Dogs tonemapper
- **PieceWise**: Power curve by John Hable (Epic Games)

##### ACES Family
- **ACES**: "ACES Filmic Tone Mapping Curve" (Narkowicz 2015)
- **ACESOscars**: Official ACES with pastel hue preservation
- **ACESHill**: Stephen Hill's ACES curve fit (@self_shadow)
- **ACESNarkowicz**: Krzysztof Narkowicz's ACES implementation

##### Advanced Operators
- **Lottes**: "HDR theory and optimization" (Lottes 2016)
- **Uchimura**: Gran Turismo tonemapper (Uchimura 2017)
- **Unreal**: UE3/UE4 tonemapper (Romain Guy adaptation)
- **RomBinDaHouse**: Tech art curve (Roman Galashov)
- **Oklab**: Oklab color space-based mapping

##### Technical Operators
- **Max3/Max3Inverted**: Optimized reversible tonemapper (Timothy Lottes)
- **PBRNeutral**: Khronos PBR neutral tonemapper
- **Schlick**: Simple rational function
- **Drago**: Adaptive logarithmic mapping
- **AGX**: Latest industry standard (Blender/Filament implementation)

#### Operator-Specific Parameters

* `White Level` (Linear, Logarithmic, WhiteLumaReinhard, Hejl2015, Clamping): Controls white point exposure level
* `Cutoff` (FilmicAldridge): Black point cutoff threshold
* `Linear Controls` (WatchDogs): Linear White and Color
* `Punchy Look` (AGX): Enables the characteristic AGX "punchy" appearance

#### Color Filter

{{< image src="tonemapper_2.jpg" wrapper="col-8 mx-auto">}}

Basic color grading controls for overall image adjustment.

* `Exposure`: Overall brightness adjustment
* `Color Filter`: Overall color tint applied to the image
* `White Balance`
  - `Temperature`: Negative = cooler (blue), Positive = warmer (yellow)
  - `Tint`: Negative = green, Positive = magenta
* `Vibrance`: Color vibrance
  - `Balance`: RGB channel multipliers (Default: 1, 1, 1)

#### Lift, Midtones & Gain (LMG)

{{< image src="tonemapper_3.jpg" wrapper="col-8 mx-auto">}}

Professional color grading controls inspired by ASC-CDL standard.

* `Lift` (Shadows)
  - `Color`: RGB shadow adjustment (Default: White)
  - `Brightness`: 0.0 to 2.0 (Default: 1.0)
* `Midtones`
  - `Color`: RGB midtone adjustment (Default: White)
  - `Brightness`: 0.0 to 2.0 (Default: 1.0)
* `Gain` (Highlights)
  - `Color`: RGB highlight adjustment (Default: White)
  - `Brightness`: 0.0 to 2.0 (Default: 1.0)

#### Tone Curve Controls

{{< image src="tonemapper_4.jpg" wrapper="col-8 mx-auto">}}

Film-emulation curve adjustments for precise tonal control.

* `Black Point`: Lifts blacks for faded film look
* `White Point`: Lowers whites for vintage appearance
* `Toe Strength`: Controls shadow rolloff smoothness
* `Shoulder Strength`: Controls highlight rolloff smoothness

#### Channel Mixer

{{< image src="tonemapper_5.jpg" wrapper="col-8 mx-auto">}}

Remap color channels for creative color effects.

* `Red Output`: Controls RGB influence on red output
* `Green Output`: Controls RGB influence on green output
* `Blue Output`: Controls RGB influence on blue output

#### Split Toning

{{< image src="tonemapper_6.jpg" wrapper="col-8 mx-auto">}}

Apply different colors to shadows and highlights.

* `Highlight Tint`: Color applied to bright image areas
* `Shadow Tint`: Color applied to dark image areas
* `Balance`: Negative favors shadows, positive favors highlights

#### Selective Color

{{< image src="tonemapper_7.jpg" wrapper="col-8 mx-auto">}}

CMYK adjustments for specific color ranges.

Each color range (Reds, Yellows, Greens, Cyans, Blues, Magentas, Whites, Neutrals, Blacks) supports:
- **Cyan**: -1.0 to 1.0
- **Magenta**: -1.0 to 1.0
- **Yellow**: -1.0 to 1.0
- **Black**: -1.0 to 1.0

#### Advanced Vibrance

{{< image src="tonemapper_8.jpg" wrapper="col-8 mx-auto">}}

Enhanced vibrance controls with selective adjustments.

---
## Comic {#comic}
{{< asset-header youtube="W4t0Cnk1Q0U" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-comic-269586" demo="https://fronkongames.github.io/demos-artistic/comic/" warn="assets used in video and demo are not included">}}

Simulates the printing technique used in comics and newspapers: [halftone](https://en.wikipedia.org/wiki/Halftone). Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< image src="comic_0.jpg" wrapper="col-6 mx-auto">}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The scale of the points can be modified with '**Scale**' (_2_). The operation used to blend the color of these points with the original image can be adjusted with '**Color blend**' (_3_).

To increase the feeling of seeing a comic book, you can add a stroke effect with '**Edge**' (_4_).

If you want to finely adjust the angle of each color point, you can modify it with '**CMYK pattern**' (_5_).

---
## Neon {#neon}
{{< asset-header youtube="nNVYDesYfF8" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-neon-270269" demo="https://fronkongames.github.io/demos-artistic/neon/" warn="assets used in video and demo are not included">}}

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
{{< asset-header youtube="kgwMRlHzGxs" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-spark-270898" demo="https://fronkongames.github.io/demos-artistic/spark/" warn="assets used in video and demo are not included">}}

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
{{< asset-header youtube="rSE8fjbire4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-radial-blur-271547" demo="https://fronkongames.github.io/demos-artistic/radialblur/" warn="assets used in video and demo are not included">}}

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
