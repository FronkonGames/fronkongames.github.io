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

{{< alert color="light" >}}
You can obtain each effect separately, but if you want multiple effects, you might be interested in **'[LUTS BUNDLE](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-bundle-282899?aid=1101l9zFC&utm_source=aff)'** where you can find them all at a special price!
{{< /alert >}}

## What is a LUT?

LUT, or '**L**ook**U**p **T**able', are a kind of color filter you use to alter the colors in your game. They apply predetermined sets of mathematical formulas to your game's existing colors to change those colors and achieve a desired look.

{{< image src="howto.png" caption="Source > LUTs > Screen" wrapper="text-center">}}

## Requirements

All '**LUTs**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP), which means they will **not work** with Built-In, or HDRP.

#### Unity 6 or higher

All effects are compatible with **Unity 6**, and use the new [Render Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html). You will need to have URP version *17.0.2* or higher installed. In the [official documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html) you can find the steps to install it correctly.

#### Unity 2022.3 or higher

You will need to have URP version *12.1.15* or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

## Using them in the Editor

Once installed, you have to add the effect you want to use from '**LUTs**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< image src="editor_0.jpg" wrapper="col-6 mx-auto">}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< image src="editor_1.jpg" wrapper="col-6 mx-auto">}}

All '**LUTs**' have an inspector similar to this one:

{{< image src="editor_2.jpg" wrapper="col-6 mx-auto">}}

With the intensity (_1_) set to _1.0_ the effect is fully applied, with 0 it is deactivated and with the intermediate values you get a mix between the original and the final image.

There are two modes (_2_), the quality mode and the performance mode. The first one uses high resolution 3D textures, while the second one uses smaller versions. For VR and mobile I recommend the second mode.

Each lut is contained in a _profile_ that you can find in the '_Profiles_' folder. By clicking on '**Profile**' (_3_) you will see all the available ones.

{{< image src="editor_3.jpg" wrapper="col-6 mx-auto">}}

All '**LUTs**' have an advanced color grading panel. Check '**Color grading**' (_1_) to activate it.

{{< image src="color.jpg" wrapper="col-6 mx-auto">}}

'**Exposure**' (_2_) changes the exposure, or brightness. Just below you have a contrast control (_3_) and an HDR color (_4_) without alpha channel to tint the image.

To move the color wheel, use '**Hue**' (_5_). To change the amount of color, use '**Saturation**' (_6_).

Select the tone operator, '**Tonemap**' (_7_), that best suits your needs. The most popular ones are available: Neutral, ACES and Reinhard. If you want more, you may be interested in '[Artistic: Tonemapper](/store/artistic/#tonemapper)'.

With '**White balance**' (_8_) you can adjust the perceived _temperature_ of the image. First you can make it perceived cooler or warmer. The next parameter modifies the color used to vary the perceived temperature.

'**Split toning**' (_9_) is used to tint shadows and highlights of an image separately. A typical example is to push shadows toward cool blue and highlights toward warm orange.

'**Channel mixer**' (_10_) allows you to combine input RGB values to create a new RGB value. For example, you could swap R and G, subtract B from G, or add G to R to push green toward yellow.

The last setting is '**Shadow Midtones Highlights**' (_11_), it works like split-toning, except that it also allows adjustment of the midtones and decouples the shadow and highlight regions, making them configurable.

They also have an '**Advanced**' panel with these options:

{{< image src="advanced.jpg" wrapper="col-6 mx-auto">}}

Activate '**Affect the Scene View?**' (_1_) if you want the effect to be applied also in the '_Scene_' window of the Editor. With '**Filter mode**' (_2_) you can change the type of filter used.

Although it is not recommended to change it, with '**RenderPass event**' (_3_) you can modify at which point in the render pipeline the effect is applied. Finally, activate '**Enable profiling**' (_4_) to show in the '_Profiling_' window the metrics of the effect.

## VR

To increase compatibility with VR devices, I recommend that you select '**Stereo Rendering Mode**' in '**Multi Pass**' mode:

{{< image src="vr.jpg" wrapper="col-6 mx-auto">}}

## Using them in code

Once you have added the effect in the Editor, you can also handle '**LUTs**' effects by code. 

First you must add the corresponding namespace. They are all of the style 'FronkonGames.LUTs.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**Cyberpunk**' the code would be:

```csharp
using FronkonGames.LUTs.Cyberpunk;
```

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

```csharp
Cyberpunk.Settings settings = Cyberpunk.Instance.settings;

settings.intensity = 0.5f;
```

And how can I activate and deactivate the effect? It's as easy as that:

```csharp
Cyberpunk cyberpunk = Cyberpunk.Instance;

// Switch between active and inactive.
if (cyberpunk.isActive == true)
  cyberpunk.SetActive(false);
else
  cyberpunk.SetActive(true);
```

{{< alert color="warning" icon="fas triangle-exclamation" >}}
The Instance function uses [Reflection](https://learn.microsoft.com/en-us/dotnet/fundamentals/reflection/reflection), and is therefore expensive. I recommend that you save the Instance value to use it without affecting performance.
{{< /alert >}}

You can load a _profile_ in several ways. A _profile_ is nothing more than a ScriptableObject, so it must be referenced by some object to be included in the build.

A very simple way is to create a MonoBehaviour and add a list of _profiles_ to it. This way Unity will include in the build the _profiles_ that you have referenced.

```csharp
public class ProfileBank : MonoBehaviour
{
  [SerializableField]
  private List<Profile> profiles = new();

  private void Awake()
  {
    // Set a random profile.
    if (profiles.Length > 0)
    {
      Cyberpunk.Settings settings = Cyberpunk.Instance.settings;

      settings.profile = profiles[Random.Range(0, profiles.Length)];
    }
  }
}
```

Another method you can use, more versatile, is to move the _profiles_ folder into the '_Resources_' folder. Everything included in this folder will be added to the build and you can load its content with the [Resources](https://docs.unity3d.com/ScriptReference/Resources.html) class:

```csharp
// In this example the profiles are located
// inside Resources in the folder 'LUTs/Profiles/Cyberpunk'.
Cyberpunk.Settings settings = Cyberpunk.Instance.settings;

Profile profile = Resources.Load<Profile>("LUTs/Profiles/Cyberpunk/Cyberpunk_01");

settings.profile = profile;
```

With this method, you can unload the profile when you no longer want to use it.

```csharp
Resources.UnloadAsset(profile);
```

If you are using an effect other than '**Cyberpunk**' just change it to its name. Check the source code comments for more information.
#

---
## Cyberpunk {#cyberpunk}
{{< asset-header youtube="9JZdwytXLbA" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-cyberpunk-275005" demo="https://fronkongames.github.io/demos-luts/cyberpunk/">}}

In '**Cyberpunk**' you will find the look you are looking for in your futuristic games. Includes **62 high quality LUTs**.

### Pink & Teal

Vibrant, dystopian look with intense pinks / purples / greens (11 LUTs).

{{< mgallery "list"="cyberpunk/Pink*" "cols"=4 "thumb"="16x9" >}}

### Neo Tokyo

Colors pop without oversaturation, shadows are desaturated (33 LUTs).

{{< mgallery "list"="cyberpunk/NeoTokyo*" "cols"=4 "thumb"="16x9" >}}

### Dystopia

Inspired by the movie Blade Runner 2049 (8 LUTs).

{{< mgallery "list"="cyberpunk/Dystopia*" "cols"=4 "thumb"="16x9" >}}

### Cyberpunk

A retrofuturistism vibe (10 LUTs).

{{< mgallery "list"="cyberpunk/Cyberpunk*" "cols"=4 "thumb"="16x9" >}}

---
## Vintage {#vintage}
{{< asset-header youtube="v052UeIjusk" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-vintage-275594" demo="https://fronkongames.github.io/demos-luts/vintage/">}}

The vintage and retro look you're looking for is in '**Vintage**'. Includes **90 high quality LUTs**.

### Nostalgia

Nostalgic aesthetics of retro cinema (10 LUTs).

{{< mgallery "list"="vintage/Nostalgia*" "cols"=4 "thumb"="16x9" >}}

### Retro

Retro vibes to travel to other times (10 LUTs).

{{< mgallery "list"="vintage/Retro*" "cols"=4 "thumb"="16x9" >}}

### 70's

A journey through the iconic eras of the 1970s and 1980s (8 LUTs).

{{< mgallery "list"="vintage/70s*" "cols"=4 "thumb"="16x9" >}}

### Noir

Rich, nostalgic tones of classic film noir (30 LUTs).

{{< mgallery "list"="vintage/Noir*" "cols"=5 "thumb"="16x9" >}}

### Old Films

Nostalgic aesthetics of retro cinema (8 LUTs).

{{< mgallery "list"="vintage/OlFilm*" "cols"=4 "thumb"="16x9" >}}

### Photo

Iconic look and feel of vintage Fujifilm (8 LUTs).

{{< mgallery "list"="vintage/Photo*" "cols"=4 "thumb"="16x9" >}}

### Sepia

Warm nostalgic look, beautiful sepia tones (8 LUTs).

{{< mgallery "list"="vintage/Sepia*" "cols"=4 "thumb"="16x9" >}}

### Semi B&W

Different black and white balances (8 LUTs).

{{< mgallery "list"="vintage/Semi*" "cols"=4 "thumb"="16x9" >}}

---
## Anime {#anime}
{{< asset-header youtube="vCk9eIxhir4" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-anime-276902" demo="https://fronkongames.github.io/demos-luts/anime/">}}

Vibrant tones, unique contrasts and a cinematic touch. Includes **58 high quality LUTs**.

### Anime

Vibrant blue tones that captures the dreamlike essence of anime (18 LUTs).

{{< mgallery "list"="anime/anime*" "cols"=4 "thumb"="16x9" >}}

### Arcade

Palette of old Japanese arcade machines (10 LUTs).

{{< mgallery "list"="anime/arcade*" "cols"=4 "thumb"="16x9" >}}

### Game

Colorful and saturated video game environment (10 LUTs).

{{< mgallery "list"="anime/game*" "cols"=4 "thumb"="16x9" >}}

### Virtual

Tones of consoles of past generations (10 LUTs).

{{< mgallery "list"="anime/virtual*" "cols"=4 "thumb"="16x9" >}}

### Yolk

Creomous yellow tones and contrasts (10 LUTs).

{{< mgallery "list"="anime/yolk*" "cols"=4 "thumb"="16x9" >}}

---
## Synthwave {#synthwave}
{{< asset-header youtube="2pW7-FFgTUA" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-synthwave-278499" demo="https://fronkongames.github.io/demos-luts/synthwave/">}}

Neon-drenched cyberpunk worlds. Includes **50 high quality LUTs**.

{{< mgallery "list"="synthwave/*" "cols"=5 "thumb"="16x9" >}}

---
## Colors {#colors}
{{< asset-header youtube="L-cWwo7O3IY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-colors-278789" demo="https://fronkongames.github.io/demos-luts/colors/">}}

A rainbow of colors for your games. Includes **277 high quality LUTs**.

### Bleach

Higher contrast, reduced saturation and very distinctive look (10 LUTs).

{{< mgallery "list"="colors/bleach*" "cols"=4 "thumb"="16x9" >}}

### Bright

White tones displaced to blue and more clarity (52 LUTs).

{{< mgallery "list"="colors/bright*" "cols"=5 "thumb"="16x9" >}}

### Brownish

Warm brown tones (8 LUTs).

{{< mgallery "list"="colors/brownish*" "cols"=4 "thumb"="16x9" >}}

### Colorify

Based on Instagram filters (25 LUTs).

{{< mgallery "list"="colors/colorify*" "cols"=5 "thumb"="16x9" >}}

### Creative

Creative ways to handle color (7 LUTs).

{{< mgallery "list"="colors/creative*" "cols"=3 "thumb"="16x9" >}}

### Crisp White

Infuses simplicity and luminosity (8).

{{< mgallery "list"="colors/crisp*" "cols"=3 "thumb"="16x9" >}}

### Dark Green

Dark forests (8 LUTs).

{{< mgallery "list"="colors/darkgreen*" "cols"=3 "thumb"="16x9" >}}

### Dark Mood

Dark and moody elegance (10 LUTs).

{{< mgallery "list"="colors/darkmood*" "cols"=4 "thumb"="16x9" >}}

### Golden

Luxurious and minimalist look (2 LUTs).

{{< mgallery "list"="colors/golden*" "cols"=2 "thumb"="16x9" >}}

### Luxury Black

Blend of gold and black tones, soft contrasts (10 LUTs).

{{< mgallery "list"="colors/luxury*" "cols"=4 "thumb"="16x9" >}}

### Minimalist

Modern look, bringing a crisp, clean, and bright aesthetic (26 LUTs).

{{< mgallery "list"="colors/minimalist*" "cols"=4 "thumb"="16x9" >}}

### Pastels

Soft pastel hues (16 LUTs).

{{< mgallery "list"="colors/pastel*" "cols"=4 "thumb"="16x9" >}}

### Pink

Warm and pink tones (10 LUTs).

{{< mgallery "list"="colors/pink*" "cols"=4 "thumb"="16x9" >}}

### Teal and Orange

Perfect balance of teal and orange tones (70 LUTs).

{{< mgallery "list"="colors/teal*" "cols"=5 "thumb"="16x9" >}}

### Vibrant

Vibrant and dynamic aesthetic (12 LUTs).

{{< mgallery "list"="colors/vibrant*" "cols"=4 "thumb"="16x9" >}}

---
## Places {#places}
{{< asset-header youtube="XpqdRRJdz4U" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-places-279132" demo="https://fronkongames.github.io/demos-luts/places/">}}

The right color for the right place. Includes **225 high quality LUTs**.

### Adventure

Colors of natural environments enhanced (15 LUTs).

{{< mgallery "list"="places/adventure*" "cols"=4 "thumb"="16x9" >}}

### Autumn

Warm and vibrant hues of fall (15 LUTs).

{{< mgallery "list"="places/autum*" "cols"=4 "thumb"="16x9" >}}

### Nature

Enhance the majesty of nature (9 LUTs).

{{< mgallery "list"="places/nature*" "cols"=3 "thumb"="16x9" >}}

### Outdoor

Feature summery colors and natural tones (26 LUTs).

{{< mgallery "list"="places/outdoor*" "cols"=5 "thumb"="16x9" >}}

### Snow

Infuse crisp and ethereal beauty of winter (31 LUTs).

{{< mgallery "list"="places/snow*" "cols"=5 "thumb"="16x9" >}}

### Summer

Higher contrast, warm and saturated tones (18 LUTs).

{{< mgallery "list"="places/summer*" "cols"=5 "thumb"="16x9" >}}

### Sunset

Natural warm and luminous colors (20 LUTs).

{{< mgallery "list"="places/sunset*" "cols"=5 "thumb"="16x9" >}}

### Travel

Creative and varied color grading (7 LUTs).

{{< mgallery "list"="places/travel*" "cols"=3 "thumb"="16x9" >}}

### Urban

Enhance color grading, contrast, and atmosphere (18 LUTs).

{{< mgallery "list"="places/urban*" "cols"=5 "thumb"="16x9" >}}

### Western

Dusty trails and sunsets over prairies (8 LUTs).

{{< mgallery "list"="places/western*" "cols"=3 "thumb"="16x9" >}}

### XMas

The richness of holiday colors (59 LUTs).

{{< mgallery "list"="places/xmas*" "cols"=5 "thumb"="16x9" >}}

---
## Cinematic {#cinematic}
{{< asset-header youtube="zhGBdWJ_8rI" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-cinematic-279333" demo="https://fronkongames.github.io/demos-luts/cinematic/">}}

The color of the movies, in your games. Includes **254 high quality cinematic LUTs**.

### Analog

Mimics analog tapes and 'Log to Rec 709' effect (10 LUTs).

{{< mgallery "list"="cinematic/analog*" "cols"=4 "thumb"="16x9" >}}

### Drama

Moody brown tones and a touch of cinematic allure (25 LUTs).

{{< mgallery "list"="cinematic/drama*" "cols"=5 "thumb"="16x9" >}}

### Epic

From vintage tones to modern cinematic effects (20 LUTs).

{{< mgallery "list"="cinematic/epic*" "cols"=5 "thumb"="16x9" >}}

### High Contrast

Saturated colors and high contrast (15 LUTs).

{{< mgallery "list"="cinematic/high*" "cols"=5 "thumb"="16x9" >}}

### Hollywood

Elegance of classic Hollywood films (48 LUTs).

{{< mgallery "list"="cinematic/hollywood*" "cols"=5 "thumb"="16x9" >}}

### Horror

Vibrant reds and powerful darks (15 LUTs).

{{< mgallery "list"="cinematic/horror*" "cols"=5 "thumb"="16x9" >}}

### Indie

Filmic colors and tones in independent films (30 LUTs).

{{< mgallery "list"="cinematic/indie*" "cols"=5 "thumb"="16x9" >}}

### Retro

Color grading and cinematic styles of iconic films from the past (51 LUTs).

{{< mgallery "list"="cinematic/retro*" "cols"=5 "thumb"="16x9" >}}

### Romance

An instant dose of love (40 LUTs).

{{< mgallery "list"="cinematic/romance*" "cols"=5 "thumb"="16x9" >}}

---
## Fantasy {#fantasy}
{{< asset-header youtube="kNT1Au3LY6s" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-fantasy-279569" demo="https://fronkongames.github.io/demos-luts/fantasy/">}}

Worlds of fantasy and color. Includes **131 high quality fantasy LUTs**.

### Fantasy

Beautiful colors and a mystical vibe (50 LUTs).

{{< mgallery "list"="fantasy/fantasy*" "cols"=5 "thumb"="16x9" >}}

### Dark Fantasy

Dark and mysterious magic (36 LUTs).

{{< mgallery "list"="fantasy/dark*" "cols"=5 "thumb"="16x9" >}}

### Movies & TV Shows

Movies / tv-shows inspired: Game Of Thrones, Harry Potter, ... (45 LUTs).

{{< mgallery "list"="fantasy/movies*" "cols"=5 "thumb"="16x9" >}}

---
## Unreal {#unreal}
{{< asset-header youtube="PqITkuWFoKk" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-unreal-279579" demo="https://fronkongames.github.io/demos-luts/unreal/">}}

Colors from other worlds, stunning looks. Includes **67 high quality originals LUTs**.

### Weird

Inspired by infrared vision (27 LUTs).

{{< mgallery "list"="unreal/weird*" "cols"=5 "thumb"="16x9" >}}

### Monotone

Mono-color tone and black & white (8 LUTs).

{{< mgallery "list"="unreal/monotone*" "cols"=3 "thumb"="16x9" >}}

### Duotone

Duo-tone complementary colors (14 LUTs).

{{< mgallery "list"="unreal/duotone*" "cols"=5 "thumb"="16x9" >}}

### Thermal

Thermal vision goggles colors (10 LUTs).

{{< mgallery "list"="unreal/thermal*" "cols"=5 "thumb"="16x9" >}}

### Day to night

Transitions from day to night (8 LUTs).

{{< mgallery "list"="unreal/day*" "cols"=3 "thumb"="16x9" >}}

---
## Action {#action}
{{< asset-header youtube="PrSI6uIoUd0" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-action-280076" demo="https://fronkongames.github.io/demos-luts/action/">}}

Perfect looks for action games. Includes **163 high quality action LUTs**.

### Action

Cinematic depth and vibrant energy to your games (26 LUTs).

{{< mgallery "list"="action/action*" "cols"=5 "thumb"="16x9" >}}

### Apocalypse

Horror atmosphere (50 LUTs).

{{< mgallery "list"="action/apocalypse*" "cols"=5 "thumb"="16x9" >}}

### Automotive

Car photography filters for sport look (23 LUTs).

{{< mgallery "list"="action/automotive*" "cols"=5 "thumb"="16x9" >}}

### Military

Colors inspired by cinematic war movies (15 LUTs).

{{< mgallery "list"="action/military*" "cols"=5 "thumb"="16x9" >}}

### Movies

Inspired by the best action movies of all time (30 LUTs).

{{< mgallery "list"="action/movie*" "cols"=5 "thumb"="16x9" >}}

### Sports

Dynamic colors and intensity (19 LUTs).

{{< mgallery "list"="action/sport*" "cols"=5 "thumb"="16x9" >}}

---
## Horror {#horror}
{{< asset-header youtube="SoM5cH3c_YY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-horror-280345" demo="https://fronkongames.github.io/demos-luts/horror/">}}

The color of fear. Includes **598 high quality scary LUTs**.

### Darkness

Dark tones and spooky shades (100 LUTs).

{{< mgallery "list"="horror/darkness*" "cols"=5 "thumb"="16x9" >}}

### Halloween

Colors inspired by the Halloween holiday (305 LUTs).

{{< mgallery "list"="horror/halloween*" "cols"=5 "thumb"="16x9" >}}

### Movies

Inspired by classic horror movies (11 LUTs).

{{< mgallery "list"="horror/movie*" "cols"=5 "thumb"="16x9" >}}

### Terror

Looks that inspire suspense and terror (132 LUTs).

{{< mgallery "list"="horror/terror*" "cols"=5 "thumb"="16x9" >}}

### Vampire

Colors inspired by vampire movies (50 LUTs).

{{< mgallery "list"="horror/vampire*" "cols"=5 "thumb"="16x9" >}}

---
# Sci-Fi {#scifi}
{{< asset-header youtube="ItmAGy08gAY" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-sci-fi-280709" demo="https://fronkongames.github.io/demos-luts/scifi/">}}

Colors of other worlds. Includes **150 high quality sci-fi LUTs**.

### Dystopia

Dystopian neon realities (50 LUTs).

{{< mgallery "list"="scifi/dystopia*" "cols"=5 "thumb"="16x9" >}}

### Future

Looks from movies like Blade Runner (50 LUTs).

{{< mgallery "list"="scifi/future*" "cols"=5 "thumb"="16x9" >}}

### Sci-Fi

Colors inspired by science fiction classics (50 LUTs).

{{< mgallery "list"="scifi/scifi*" "cols"=5 "thumb"="16x9" >}}

#
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
