---
author: Martin Bustos
title: LUTs
showTitle: false
date: 5
description: The largest collection of LUTs in the entire store
tags: ["unity", "store", "lut", "luts"]
metadata: none
modules: ["mgallery"]
showImage: true
thumbnail:
  url: img/luts.jpg
---

Thanks to LUTs you can completely transform the look of your games, making them more coherent with your artistic preferences.

'**[LUTs](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-bundle-282899?aid=1101l9zFC&utm_source=aff)**' contains the following assets:

* [Cyberpunk](#cyberpunk) (61 LUTs): apocalyptic future, looking cool.
* [Vintage](#vintage) (90 LUTs): nostalgia for the past.
* [Anime](#anime) (60 LUTs): vibrant tones, unique contrasts.
* [Synthwave](#synthwave) (50 LUTs): neon-drenched cyberpunk worlds.
* [Colors](#colors) (277 LUTs): a rainbow of colors for your games.
* [Places](#places) (225 LUTs): the right color for the right place.
* [Cinematic](#cinematic) (254 LUTs): the color of the movies, in your games.
* [Fantasy](#fantasy) (131 LUTs): worlds of fantasy and color.
* [Unreal](#unreal) (67 LUTs): colors from other worlds, stunning looks.
* [Action](#action) (163 LUTs): colors for action!
* [Horror](#horror) (598 LUTs): the colors of fear...
* [Sci-Fi](#scifi) (150 LUTs): futuristic and dystopian looks.

{{< badge title="You can obtain each effect separately, but if you want more effects, you might be interested in **'[LUTS BUNDLE](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-bundle-282899?aid=1101l9zFC&utm_source=aff)'** where you can find them all at a special price!" color="secondary">}}
{.h3}

## What is a LUT?

LUT, or '**L**ook**U**p **T**able', are a kind of color filter you use to alter the colors in your game. They apply predetermined sets of mathematical formulas to your game's existing colors to change those colors and achieve a desired look.

{{< image src="howto.png" caption="Source > LUTs > Screen" wrapper="text-center">}}

## Requirements

All '**LUTs**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP), which means they will **not work** with Built-In, or HDRP.

#### Unity 6 or Higher

The current bundle is centered on **Unity 6** and the **URP Render Graph** workflow. You will need **URP 17.0.3** or higher installed. If you need help with setup, follow the [official URP installation guide](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html).

Make sure that '_Compatibility Mode_' is **disabled** in '_Project Settings > Graphics > Render Graph_'.

{{< image src="compatibility_mode.jpg" wrapper="col-8 mx-auto">}}

## Installation

#### Step 1: Add Renderer Feature

The effects must be registered in your project's [URP configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html):

1. Locate your **Universal Renderer Data** asset.
2. Click **Add Renderer Feature** and select the desired distortion from **Fronkon Games > LUTs**.

{{< alert color="info" >}}
'_Quality_' levels (_Project Settings > Quality_) can have their own active '_Render Pipeline Asset_'.

If so, whatever you assign in '_Scriptable Render Pipeline Settings_' in '_Graphics_' will be ignored.

**Remember to add the effect to the quality levels you want to use.**
{{< /alert >}}

Once installed, you have to add the effect you want to use from '**LUTs**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

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
3. Click **Add Override** and select the desired LUT from **Fronkon Games > LUTs**.
4. Enable the '**Intensity**' parameter (and any others you wish to modify).
5. Assign one of the available profiles by clicking on '**LUT Profiles**'.

{{< alert color="info" >}}
Remember that for a parameter to take effect, you must activate it. Click on '**ALL**' to activate them all.
{{< /alert >}}

## Using them in the Editor

All '**LUTs**' have an inspector similar to this one:

{{< image src="editor_2.jpg" wrapper="col-8 mx-auto">}}

With the '**Intensity**' set to _1_ the effect is fully applied, with _0_ it is deactivated and with the intermediate values you get a mix between the original and the final image.

There are two modes, the _quality_ and the _performance_ mode. The first one uses high resolution 3D textures, while the second one uses smaller versions. For VR and mobile I recommend the second mode.

Each lut is contained in a _profile_ that you can find in the '_Profiles_' folder. By clicking on '**LUT Profile**' you will see all the available ones.

{{< image src="editor_3.jpg" wrapper="col-8 mx-auto">}}

Select the tone operator, '**Tonemap**', that best suits your needs. The most popular ones are available: Neutral, ACES and Reinhard. If you want more, you may be interested in '[Artistic: Tonemapper](/store/artistic/#tonemapper)'.

#### Color Grading

{{< image src="color.jpg" wrapper="col-8 mx-auto">}}

Color grading lets you fine-tune the final look of the image after selecting a LUT. It is useful to push a preset further, adapt it to a specific scene, or make small corrections without changing the selected profile.

'**Exposure**' changes the exposure, or brightness. Just below you have a contrast control and an HDR color, '**Tint**', to shift the whole image towards a specific color.

To rotate all colors around the color wheel, use '**HUE**'. To increase or decrease the overall amount of color, use '**Saturation**'.

'**Vibrance**' changes saturation in a more selective way. It boosts the less saturated colors first, so it is a good option when you want a stronger image without oversaturating colors that are already intense.

With '**White balance**' you can adjust the perceived _temperature_ of the image. First you can make it perceived cooler or warmer. The next parameter modifies the color used to vary the perceived temperature.

#### Split Toning

{{< image src="split_toning.jpg" wrapper="col-8 mx-auto">}}

'**Split toning**' is used to tint shadows and highlights of an image separately. A typical example is to push shadows toward cool blue and highlights toward warm orange.

Use '**Shadows**' to select the color applied to the darker parts of the image, and '**Highlights**' to choose the tint for the brighter areas. The '**Balance**' parameter shifts the transition between both ranges, giving more weight to shadows or highlights depending on the look you want.

#### Channel Mixer

{{< image src="channel_mixer.jpg" wrapper="col-8 mx-auto">}}

'**Channel mixer**' allows you to combine input RGB values to create a new RGB value. For example, you could swap R and G, subtract B from G, or add G to R to push green toward yellow.

Each output channel has its own control: '**Red**', '**Green**' and '**Blue**'. Inside each one, the three values define how much of the input red, green and blue channels will be used to build that final output channel. Default values keep the image unchanged, but changing them lets you remap colors, create stylized looks, or simulate color-filtered film responses.

#### Shadow Midtones Highlights

{{< image src="shadows.jpg" wrapper="col-8 mx-auto">}}

The last setting is '**Shadow Midtones Highlights**'. It works like split toning, but it also lets you adjust the midtones and configure the shadow and highlight ranges independently.

Use '**Shadows**', '**Midtones**' and '**Highlights**' to tint each tonal range separately. The '**Range**' sliders define where the shadows end and where the highlights begin, so you can decide how much of the image belongs to each region and create smoother or more aggressive transitions between them.

#### Advanced

They also have an '**Advanced**' panel with these options:

{{< image src="advanced.jpg" wrapper="col-8 mx-auto">}}

Activate '**Affect Scene View?**' if you want the effect to be applied also in the '_Scene_' window of the Editor.

## VR

To increase compatibility with VR devices, I recommend that you select '**Stereo Rendering Mode**' in '**Multi Pass**' mode:

{{< image src="vr.jpg" wrapper="col-6 mx-auto">}}

## Using them in code

Once you have added the effect in the Editor, you can also control '**LUTs**' effects by code.

First you must add the corresponding namespace. They are all of the style 'FronkonGames.LUTs.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**Cyberpunk**' the code would be:

```csharp
using FronkonGames.LUTs.Cyberpunk;
```

The effects use **Volumes**, so the usual workflow is to get the effect component from a `VolumeProfile` and then modify its parameters. In the following example we change the intensity of the effect by half.

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.LUTs.Cyberpunk;

public sealed class CyberpunkController : MonoBehaviour
{
  [SerializeField]
  private VolumeProfile volumeProfile;

  private CyberpunkVolume volume;

  private void Awake()
  {
    if (volumeProfile != null)
      volumeProfile.TryGet(out volume);
  }

  private void Start()
  {
    if (volume == null)
      return;

    volume.intensity.overrideState = true;
    volume.intensity.value = 0.5f;
  }
}
```

To activate or deactivate the effect, the simplest option is to change the intensity:

```csharp
if (volume != null)
{
  volume.intensity.overrideState = true;

  // Active.
  volume.intensity.value = 1.0f;

  // Inactive.
  volume.intensity.value = 0.0f;
}
```

You can load a _profile_ in several ways. A _profile_ is a `ScriptableObject`, so it must be referenced by some object, or loaded from a supported location such as `Resources`, to be included in the build.

A very simple way is to create a `MonoBehaviour` and add a list of _profiles_ to it. This way Unity will include in the build the _profiles_ that you have referenced.

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using FronkonGames.LUTs.Cyberpunk;

public sealed class ProfileBank : MonoBehaviour
{
  [SerializeField]
  private VolumeProfile volumeProfile;

  [SerializeField]
  private Profile[] profiles;

  private CyberpunkVolume volume;

  private void Awake()
  {
    if (volumeProfile != null)
      volumeProfile.TryGet(out volume);

    if (volume != null && profiles.Length > 0)
    {
      volume.profile.overrideState = true;
      volume.profile.value = profiles[Random.Range(0, profiles.Length)];
    }
  }
}
```

Another method you can use, more versatile, is to move the _profiles_ folder into the `Resources` folder. Everything included in this folder will be added to the build and you can load its content with the [Resources](https://docs.unity3d.com/ScriptReference/Resources.html) class:

```csharp
// In this example the profiles are located
// inside Resources in the folder '[...]Resources/LUTs/Profiles/Cyberpunk'.
Profile profile = Resources.Load<Profile>("LUTs/Profiles/Cyberpunk/Cyberpunk_01");

if (volume != null && profile != null)
{
  volume.profile.overrideState = true;
  volume.profile.value = profile;
}
```

With this method, you can unload the profile when you no longer want to use it.

```csharp
Resources.UnloadAsset(profile);
```

If you are using an effect other than '**Cyberpunk**', just change the namespace, the `VolumeComponent` type, and the profile path to match that effect. Remember that every parameter is a `VolumeParameter`, so in code you usually need to modify both `overrideState` and `value`.
#

---
## 🤖 Cyberpunk {#cyberpunk}
{{< asset-header youtube="9JZdwytXLbA" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-cyberpunk-275005" demo="https://fronkongames.github.io/demos-luts/cyberpunk/" warn="assets used in video and demo are not included">}}

Bring instant neon identity, cinematic contrast, and dystopian atmosphere to your futuristic worlds with '**Cyberpunk**'. Includes **62 high quality LUTs**.

#### Pink & Teal

Bold futuristic grading with intense pink, purple, and green accents for instantly recognizable neon worlds (11 LUTs).

{{< mgallery "list"="cyberpunk/Pink*" "cols"=4 "thumb"="16x9" >}}

#### Neo Tokyo

Punchy colors, controlled saturation, and desaturated shadows inspired by stylish futuristic cityscapes (33 LUTs).

{{< mgallery "list"="cyberpunk/NeoTokyo*" "cols"=4 "thumb"="16x9" >}}

#### Dystopia

Moody, cinematic palettes for bleak futures, towering skylines, and richly atmospheric sci-fi scenes (8 LUTs).

{{< mgallery "list"="cyberpunk/Dystopia*" "cols"=4 "thumb"="16x9" >}}

#### Cyberpunk

Retrofuturistic looks that blend synth nostalgia, neon glow, and modern cinematic energy (10 LUTs).

{{< mgallery "list"="cyberpunk/Cyberpunk*" "cols"=4 "thumb"="16x9" >}}

---
## 📼 Vintage {#vintage}
{{< asset-header youtube="v052UeIjusk" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-vintage-275594" demo="https://fronkongames.github.io/demos-luts/vintage/" warn="assets used in video and demo are not included">}}

'**Vintage**' gives your game timeless character with nostalgic tones, classic film looks, and beautifully aged color palettes. Includes **90 high quality LUTs**.

#### Nostalgia

Soft, emotional grading inspired by the warmth and charm of classic retro cinema (10 LUTs).

{{< mgallery "list"="vintage/Nostalgia*" "cols"=4 "thumb"="16x9" >}}

#### Retro

Distinctive retro looks that instantly transport your visuals to another era (10 LUTs).

{{< mgallery "list"="vintage/Retro*" "cols"=4 "thumb"="16x9" >}}

#### 70's

Authentic palettes inspired by the unforgettable style of the 70s and 80s (8 LUTs).

{{< mgallery "list"="vintage/70s*" "cols"=4 "thumb"="16x9" >}}

#### Noir

Deep shadows, elegant contrast, and smoky cinematic tones inspired by classic film noir (30 LUTs).

{{< mgallery "list"="vintage/Noir*" "cols"=5 "thumb"="16x9" >}}

#### Old Films

Aged film looks with the worn, imperfect charm of old reels and classic projection (8 LUTs).

{{< mgallery "list"="vintage/OlFilm*" "cols"=4 "thumb"="16x9" >}}

#### Photo

Photo-inspired looks with the soft contrast and color personality of vintage film photography (8 LUTs).

{{< mgallery "list"="vintage/Photo*" "cols"=4 "thumb"="16x9" >}}

#### Sepia

Warm sepia palettes that add heritage, memory, and timeless atmosphere to any scene (8 LUTs).

{{< mgallery "list"="vintage/Sepia*" "cols"=4 "thumb"="16x9" >}}

#### Semi B&W

Stylized near-monochrome looks with subtle tonal variation and elegant grayscale balance (8 LUTs).

{{< mgallery "list"="vintage/Semi*" "cols"=4 "thumb"="16x9" >}}

---
## 🎌 Anime {#anime}
{{< asset-header youtube="vCk9eIxhir4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-anime-276902" demo="https://fronkongames.github.io/demos-luts/anime/" warn="assets used in video and demo are not included">}}

'**Anime**' delivers bold color, expressive contrast, and stylized energy for worlds inspired by animation, arcades, and classic games. Includes **58 high quality LUTs**.

#### Anime

Dreamlike blue palettes and expressive contrast inspired by iconic anime moods and skies (18 LUTs).

{{< mgallery "list"="anime/anime*" "cols"=4 "thumb"="16x9" >}}

#### Arcade

Energetic palettes inspired by classic Japanese arcade cabinets and vibrant retro screens (10 LUTs).

{{< mgallery "list"="anime/arcade*" "cols"=4 "thumb"="16x9" >}}

#### Game

Colorful game-ready looks with lively saturation and playful visual punch (10 LUTs).

{{< mgallery "list"="anime/game*" "cols"=4 "thumb"="16x9" >}}

#### Virtual

Stylized palettes inspired by the look and feel of beloved past-generation consoles (10 LUTs).

{{< mgallery "list"="anime/virtual*" "cols"=4 "thumb"="16x9" >}}

#### Yolk

Creamy yellow highlights and rich contrast for warm, distinctive stylized scenes (10 LUTs).

{{< mgallery "list"="anime/yolk*" "cols"=4 "thumb"="16x9" >}}

---
## 🌆 Synthwave {#synthwave}
{{< asset-header youtube="2pW7-FFgTUA" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-synthwave-278499" demo="https://fronkongames.github.io/demos-luts/synthwave/" warn="assets used in video and demo are not included">}}

'**Synthwave**' fills your scenes with neon sunsets, electric nights, and irresistible retro-futuristic style. Includes **50 high quality LUTs**.

{{< mgallery "list"="synthwave/*" "cols"=5 "thumb"="16x9" >}}

---
## 🌈 Colors {#colors}
{{< asset-header youtube="L-cWwo7O3IY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-colors-278789" demo="https://fronkongames.github.io/demos-luts/colors/" warn="assets used in video and demo are not included">}}

'**Colors**' is a huge palette of ready-to-use looks for pushing mood, style, clarity, warmth, or bold creative grading in seconds. Includes **277 high quality LUTs**.

#### Bleach

Distinctive high-contrast looks with desaturated tones for a sharper, more dramatic image (10 LUTs).

{{< mgallery "list"="colors/bleach*" "cols"=4 "thumb"="16x9" >}}

#### Bright

Bright, airy grading with cool whites and extra clarity for clean, polished visuals (52 LUTs).

{{< mgallery "list"="colors/bright*" "cols"=5 "thumb"="16x9" >}}

#### Brownish

Warm earthy palettes that add natural richness and grounded atmosphere (8 LUTs).

{{< mgallery "list"="colors/brownish*" "cols"=4 "thumb"="16x9" >}}

#### Colorify

Social-inspired creative filters for quick, stylish color changes with strong personality (25 LUTs).

{{< mgallery "list"="colors/colorify*" "cols"=5 "thumb"="16x9" >}}

#### Creative

Inventive color treatments for developers looking for unusual and memorable looks (7 LUTs).

{{< mgallery "list"="colors/creative*" "cols"=3 "thumb"="16x9" >}}

#### Crisp White

Crisp, luminous looks that feel fresh, minimalist, and premium (8 LUTs).

{{< mgallery "list"="colors/crisp*" "cols"=3 "thumb"="16x9" >}}

#### Dark Green

Deep green palettes perfect for forests, moody landscapes, and darker natural environments (8 LUTs).

{{< mgallery "list"="colors/darkgreen*" "cols"=3 "thumb"="16x9" >}}

#### Dark Mood

Sophisticated dark looks with moody contrast and elegant cinematic atmosphere (10 LUTs).

{{< mgallery "list"="colors/darkmood*" "cols"=4 "thumb"="16x9" >}}

#### Golden

Minimal but luxurious gold-tinted looks for premium, elegant presentation (2 LUTs).

{{< mgallery "list"="colors/golden*" "cols"=2 "thumb"="16x9" >}}

#### Luxury Black

Refined blends of gold and black for luxurious scenes with soft, high-end contrast (10 LUTs).

{{< mgallery "list"="colors/luxury*" "cols"=4 "thumb"="16x9" >}}

#### Minimalist

Modern clean looks with bright whites, neat contrast, and a sleek contemporary feel (26 LUTs).

{{< mgallery "list"="colors/minimalist*" "cols"=4 "thumb"="16x9" >}}

#### Pastels

Soft pastel palettes for gentle, charming, and inviting visuals (16 LUTs).

{{< mgallery "list"="colors/pastel*" "cols"=4 "thumb"="16x9" >}}

#### Pink

Warm pink-infused looks that add softness, style, and color identity (10 LUTs).

{{< mgallery "list"="colors/pink*" "cols"=4 "thumb"="16x9" >}}

#### Teal and Orange

The classic teal-and-orange blockbuster balance, tuned for striking cinematic contrast (70 LUTs).

{{< mgallery "list"="colors/teal*" "cols"=5 "thumb"="16x9" >}}

#### Vibrant

High-energy color grading with vivid tones and immediate visual impact (12 LUTs).

{{< mgallery "list"="colors/vibrant*" "cols"=4 "thumb"="16x9" >}}

---
## 🗺️ Places {#places}
{{< asset-header youtube="XpqdRRJdz4U" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-places-279132" demo="https://fronkongames.github.io/demos-luts/places/" warn="assets used in video and demo are not included">}}

'**Places**' helps every environment feel more believable, memorable, and atmospheric with looks tailored to specific locations and seasons. Includes **225 high quality LUTs**.

#### Adventure

Adventure-ready looks that enhance natural landscapes with richer atmosphere and stronger color separation (15 LUTs).

{{< mgallery "list"="places/adventure*" "cols"=4 "thumb"="16x9" >}}

#### Autumn

Autumn palettes full of warm leaves, golden light, and seasonal richness (15 LUTs).

{{< mgallery "list"="places/autum*" "cols"=4 "thumb"="16x9" >}}

#### Nature

Natural grading that makes landscapes feel cleaner, richer, and more majestic (9 LUTs).

{{< mgallery "list"="places/nature*" "cols"=3 "thumb"="16x9" >}}

#### Outdoor

Versatile outdoor looks with sunlit color, natural balance, and broad environment appeal (26 LUTs).

{{< mgallery "list"="places/outdoor*" "cols"=5 "thumb"="16x9" >}}

#### Snow

Crisp winter palettes that enhance snow, cold light, and ethereal outdoor beauty (31 LUTs).

{{< mgallery "list"="places/snow*" "cols"=5 "thumb"="16x9" >}}

#### Summer

Warm, saturated summer looks full of sunlight, energy, and holiday atmosphere (18 LUTs).

{{< mgallery "list"="places/summer*" "cols"=5 "thumb"="16x9" >}}

#### Sunset

Luminous sunset grading with warm skies and glowing horizon tones (20 LUTs).

{{< mgallery "list"="places/sunset*" "cols"=5 "thumb"="16x9" >}}

#### Travel

Travel-inspired looks with varied color moods for memorable destinations and postcard-like scenes (7 LUTs).

{{< mgallery "list"="places/travel*" "cols"=3 "thumb"="16x9" >}}

#### Urban

Urban looks that strengthen contrast, mood, and city atmosphere without losing realism (18 LUTs).

{{< mgallery "list"="places/urban*" "cols"=5 "thumb"="16x9" >}}

#### Western

Dusty, sunbaked palettes made for prairies, trails, and classic western moods (8 LUTs).

{{< mgallery "list"="places/western*" "cols"=3 "thumb"="16x9" >}}

#### XMas

Festive holiday palettes rich in warmth, sparkle, and seasonal charm (59 LUTs).

{{< mgallery "list"="places/xmas*" "cols"=5 "thumb"="16x9" >}}

---
## 🎬 Cinematic {#cinematic}
{{< asset-header youtube="zhGBdWJ_8rI" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-cinematic-279333" demo="https://fronkongames.github.io/demos-luts/cinematic/" warn="assets used in video and demo are not included">}}

'**Cinematic**' brings movie-grade color to your game with a wide range of dramatic, elegant, and emotionally charged looks. Includes **254 high quality cinematic LUTs**.

#### Analog

Looks inspired by analog media and film-style conversion for instantly cinematic images (10 LUTs).

{{< mgallery "list"="cinematic/analog*" "cols"=4 "thumb"="16x9" >}}

#### Drama

Moody palettes with rich brown tones and strong emotional cinematic character (25 LUTs).

{{< mgallery "list"="cinematic/drama*" "cols"=5 "thumb"="16x9" >}}

#### Epic

Large-scale cinematic looks built for epic scenes, sweeping worlds, and dramatic moments (20 LUTs).

{{< mgallery "list"="cinematic/epic*" "cols"=5 "thumb"="16x9" >}}

#### High Contrast

Punchy cinematic grading with saturated color and bold high-contrast impact (15 LUTs).

{{< mgallery "list"="cinematic/high*" "cols"=5 "thumb"="16x9" >}}

#### Hollywood

Elegant movie-inspired looks that capture the polish and prestige of classic Hollywood (48 LUTs).

{{< mgallery "list"="cinematic/hollywood*" "cols"=5 "thumb"="16x9" >}}

#### Horror

Dark cinematic palettes with vivid reds and intense shadows for unsettling drama (15 LUTs).

{{< mgallery "list"="cinematic/horror*" "cols"=5 "thumb"="16x9" >}}

#### Indie

Subtle, tasteful filmic looks inspired by the color language of indie cinema (30 LUTs).

{{< mgallery "list"="cinematic/indie*" "cols"=5 "thumb"="16x9" >}}

#### Retro

Retro movie-inspired looks that channel the style of unforgettable films from past decades (51 LUTs).

{{< mgallery "list"="cinematic/retro*" "cols"=5 "thumb"="16x9" >}}

#### Romance

Soft, intimate palettes that add romance, warmth, and emotional glow to your scenes (40 LUTs).

{{< mgallery "list"="cinematic/romance*" "cols"=5 "thumb"="16x9" >}}

---
## 🐉 Fantasy {#fantasy}
{{< asset-header youtube="kNT1Au3LY6s" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-fantasy-279569" demo="https://fronkongames.github.io/demos-luts/fantasy/" warn="assets used in video and demo are not included">}}

'**Fantasy**' gives your worlds magical color, mystical atmosphere, and heroic wonder, from bright adventure to dark legend. Includes **131 high quality fantasy LUTs**.

#### Fantasy

Magical looks with vivid color and mystical atmosphere for enchanted worlds (50 LUTs).

{{< mgallery "list"="fantasy/fantasy*" "cols"=5 "thumb"="16x9" >}}

#### Dark Fantasy

Brooding fantasy palettes full of danger, mystery, and shadowy magic (36 LUTs).

{{< mgallery "list"="fantasy/dark*" "cols"=5 "thumb"="16x9" >}}

#### Movies & TV Shows

Fantasy looks inspired by beloved movies and TV worlds, from epic kingdoms to magical academies (45 LUTs).

{{< mgallery "list"="fantasy/movies*" "cols"=5 "thumb"="16x9" >}}

---
## 🛸 Unreal {#unreal}
{{< asset-header youtube="PqITkuWFoKk" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-unreal-279579" demo="https://fronkongames.github.io/demos-luts/unreal/" warn="assets used in video and demo are not included">}}

'**Unreal**' offers bold original looks for strange worlds, unusual moods, and highly stylized visual experiments. Includes **67 high quality original LUTs**.

#### Weird

Unconventional palettes inspired by infrared vision and other surreal visual distortions (27 LUTs).

{{< mgallery "list"="unreal/weird*" "cols"=5 "thumb"="16x9" >}}

#### Monotone

Single-color and monochrome looks for minimalist, graphic, and striking presentation (8 LUTs).

{{< mgallery "list"="unreal/monotone*" "cols"=3 "thumb"="16x9" >}}

#### Duotone

Stylized duo-tone palettes built from complementary colors with strong graphic appeal (14 LUTs).

{{< mgallery "list"="unreal/duotone*" "cols"=5 "thumb"="16x9" >}}

#### Thermal

Heat-vision inspired looks ideal for scanners, special goggles, and tactical display effects (10 LUTs).

{{< mgallery "list"="unreal/thermal*" "cols"=5 "thumb"="16x9" >}}

#### Day to night

Looks tuned for convincing day-to-night transitions and stylized time-of-day shifts (8 LUTs).

{{< mgallery "list"="unreal/day*" "cols"=3 "thumb"="16x9" >}}

---
## 💥 Action {#action}
{{< asset-header youtube="PrSI6uIoUd0" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-action-280076" demo="https://fronkongames.github.io/demos-luts/action/" warn="assets used in video and demo are not included">}}

'**Action**' is built for impact, intensity, and cinematic momentum, helping your action scenes feel bigger, sharper, and more exciting. Includes **163 high quality action LUTs**.

#### Action

High-energy looks that add cinematic depth, punch, and momentum to gameplay (26 LUTs).

{{< mgallery "list"="action/action*" "cols"=5 "thumb"="16x9" >}}

#### Apocalypse

Harsh, ruined-world palettes for apocalyptic scenes filled with tension and danger (50 LUTs).

{{< mgallery "list"="action/apocalypse*" "cols"=5 "thumb"="16x9" >}}

#### Automotive

Sleek automotive-inspired looks with glossy contrast and high-performance visual attitude (23 LUTs).

{{< mgallery "list"="action/automotive*" "cols"=5 "thumb"="16x9" >}}

#### Military

Military-inspired palettes with gritty contrast and the tone of modern war cinema (15 LUTs).

{{< mgallery "list"="action/military*" "cols"=5 "thumb"="16x9" >}}

#### Movies

Movie-inspired action looks made to evoke iconic blockbusters and high-stakes set pieces (30 LUTs).

{{< mgallery "list"="action/movie*" "cols"=5 "thumb"="16x9" >}}

#### Sports

Fast, dynamic looks with strong color and broadcast-style intensity (19 LUTs).

{{< mgallery "list"="action/sport*" "cols"=5 "thumb"="16x9" >}}

---
## 👻 Horror {#horror}
{{< asset-header youtube="SoM5cH3c_YY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-horror-280345" demo="https://fronkongames.github.io/demos-luts/horror/" warn="assets used in video and demo are not included">}}

'**Horror**' is packed with sinister palettes for suspense, dread, supernatural menace, and unforgettable scares. Includes **598 high quality scary LUTs**.

#### Darkness

Dark oppressive looks filled with shadow, unease, and haunted atmosphere (100 LUTs).

{{< mgallery "list"="horror/darkness*" "cols"=5 "thumb"="16x9" >}}

#### Halloween

A huge collection of festive spooky looks inspired by pumpkins, autumn nights, and Halloween iconography (305 LUTs).

{{< mgallery "list"="horror/halloween*" "cols"=5 "thumb"="16x9" >}}

#### Movies

Looks inspired by classic horror cinema, from eerie tension to full nightmare energy (11 LUTs).

{{< mgallery "list"="horror/movie*" "cols"=5 "thumb"="16x9" >}}

#### Terror

Suspense-driven palettes crafted to build anxiety, dread, and pure terror (132 LUTs).

{{< mgallery "list"="horror/terror*" "cols"=5 "thumb"="16x9" >}}

#### Vampire

Gothic looks inspired by vampire fiction, crimson highlights, and aristocratic darkness (50 LUTs).

{{< mgallery "list"="horror/vampire*" "cols"=5 "thumb"="16x9" >}}

---
# 🚀 Sci-Fi {#scifi}
{{< asset-header youtube="ItmAGy08gAY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-sci-fi-280709" demo="https://fronkongames.github.io/demos-luts/scifi/" warn="assets used in video and demo are not included">}}

'**Sci-Fi**' gives your worlds futuristic color, alien atmosphere, and bold cinematic identity across dystopian, high-tech, and spacefaring settings. Includes **150 high quality sci-fi LUTs**.

#### Dystopia

Dark futuristic palettes for neon dystopias, collapsing cities, and high-tech decay (50 LUTs).

{{< mgallery "list"="scifi/dystopia*" "cols"=5 "thumb"="16x9" >}}

#### Future

Futuristic movie-inspired grading for sleek technology, rain-soaked skylines, and advanced worlds (50 LUTs).

{{< mgallery "list"="scifi/future*" "cols"=5 "thumb"="16x9" >}}

#### Sci-Fi

Versatile science-fiction looks inspired by genre classics, space adventures, and alien horizons (50 LUTs).

{{< mgallery "list"="scifi/scifi*" "cols"=5 "thumb"="16x9" >}}

#
---
## F.A.Q.

##### _Effect Not appearing_

If the effect doesn't appear in your scene:

1. **Verify Renderer Feature**: Check that the renderer feature is added to your Universal Renderer Data asset.
2. **Check Volume Profile**: Ensure a Volume component exists in your scene with the effect override enabled.
3. **Confirm Intensity**: Verify that the Intensity parameter is set to a value greater than 0.0 and enabled.
4. **Camera Settings**: Check that your camera has Post Processing enabled in the Camera component.

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
<br>

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
