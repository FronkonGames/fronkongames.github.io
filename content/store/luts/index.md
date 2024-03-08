---
title: "LUTs"
date: 2022-10-01
image: /store/luts/mini.png
logo: /store/luts/logo.png
description: "The largest collection of LUTs in the entire store"
type: "store"
---

'**LUTs**' is (or will be) the largest collection of LUTs of the entire store. Thanks to LUTs (or 'LookUp Table') you can completely transform the look of your games, making them more coherent with your artistic preferences.

{{< notice information "Wait a minute, what is a LUT?" >}}
If you don't know what a LUT is, [here is a good explanation](https://docs.unity3d.com/2018.3/Documentation/Manual/PostProcessing-UserLut.html) of how they are used in videogames.
{{< /notice >}}

'**LUTs**' contains the following assets:

* [Cyberpunk](#cyberpunk) (61 LUTs): apocalyptic future, looking cool.
* [Vintage](#vintage) (90 LUTs): nostalgia for the past.
* [Anime](#anime) (60 LUTs): vibrant tones, unique contrasts.
* [Synthwave](#synthwave) (50 LUTs): neon-drenched cyberpunk worlds.
* [Colors](#colors) (277 LUTs): a rainbow of colors for your games.

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Requirements

All '**LUTs**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP)', which means they will **not work** with Built-In, or HDRP.

You will need to have URP version 12.1 or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

{{< notice warning "" >}}
All LUTs are 3D textures, so the hardware must support it (>2014). 
{{< /notice >}}

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Using them in the Editor

Once installed, you have to add the effect you want to use from '**LUTs**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< imagecenter src="/store/luts/editor_0.jpg" >}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< imagecenter src="/store/luts/editor_1.jpg" >}}

All '**LUTs**' have an inspector similar to this one:

{{< imagecenter src="/store/luts/editor_2.jpg" >}}

With the intensity (_1_) set to _1.0_ the effect is fully applied, with 0 it is deactivated and with the intermediate values you get a mix between the original and the final image.

There are two modes (_2_), the quality mode and the performance mode. The first one uses high resolution 3D textures, while the second one uses smaller versions. For VR and mobile I recommend the second mode.

Each lut is contained in a _profile_ that you can find in the '_Profiles_' folder. By clicking on '**Profile**' (_3_) you will see all the available ones.

{{< imagecenter src="/store/luts/editor_3.jpg" >}}

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Using them in code

You can also handle '**LUTs**' effects by code. The first thing you will have to do is to add the namespace of the effect you want to use.

They are all of the style 'FronkonGames.LUTs.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**Cyberpunk**' the code would be:

{{< highlight csharp "linenos=false" >}}
using FronkonGames.LUTs.Cyberpunk;
{{< /highlight >}}
</br>

And with this code you could check if the effect is added, and if it is not, add it.

{{< highlight csharp "linenos=false" >}}
if (Cyberpunk.IsInRenderFeatures() == false)
    Cyberpunk.AddRenderFeature();
{{< /highlight >}}
</br>

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

{{< highlight csharp "linenos=false" >}}
 Cyberpunk.Settings settings = Cyberpunk.GetSettings();

 settings.intensity = 0.5f;
 {{< /highlight >}}
</br>

You can load a _profile_ in several ways. A _profile_ is nothing more than a ScriptableObject, so it must be referenced by some object to be included in the build.

A very simple way is to create a MonoBehaviour and add a list of _profiles_ to it. This way Unity will include in the build the _profiles_ that you have referenced.

{{< highlight csharp "linenos=false" >}}
public class ProfileBank : MonoBehaviour
{
  [SerializableField]
  private List<Profile> profiles = new();

  private void Awake()
  {
    // Set a random profile.
    if (profiles.Length > 0)
    {
      Cyberpunk.Settings settings = Cyberpunk.GetSettings();

      settings.profile = profiles[Random.Range(0, profiles.Length)];
    }
  }
}
{{< /highlight >}}
</br>

Another method you can use, more versatile, is to move the _profiles_ folder into the '_Resources_' folder. Everything included in this folder will be added to the build and you can load its content with the [Resources](https://docs.unity3d.com/ScriptReference/Resources.html) class:

{{< highlight csharp "linenos=false" >}}
// In this example the profiles are located
// inside Resources in the folder 'LUTs/Profiles/Cyberpunk'.
Cyberpunk.Settings settings = Cyberpunk.GetSettings();

Profile profile = Resources.Load<Profile>("LUTs/Profiles/Cyberpunk/Cyberpunk_01");

settings.profile = profile;
{{< /highlight >}}
</br>

With this method, you can unload the profile when you no longer want to use it.

{{< highlight csharp "linenos=false" >}}
Resources.UnloadAsset(profile);
{{< /highlight >}}
</br>

If you are using an effect other than '**Cyberpunk**' just change it to its name. Check the source code comments for more information.

---
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

# {#cyberpunk}
{{< youtube 9JZdwytXLbA >}}

{{< asset-buttons demo="https://fronkongames.github.io/demos-luts/cyberpunk/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-cyberpunk-275005">}}

In '**Cyberpunk**' you will find the look you are looking for in your futuristic games. Includes 62 high quality LUTs including:

* **Pink & Teal** (11): vibrant, dystopian look with intense pinks / purples / greens.
* **Neo Tokyo** (33): colors pop without oversaturation, shadows are desaturated.
* **Dystopia** (8): inspired by the movie Blade Runner 2049.
* **Cyberpunk** (10): retrofuturistism vibe.

{{<
  gallery match="cyberpunk/*"
  sortOrder="asc"
  rowHeight="100"
  margins="5"
  thumbnailResizeOptions="800x533 q100 Lanczos"
  showExif=false
  previewType="blur"
  embedPreview=true
  loadJQuery=true
  filterOptions= "[{label: 'Pink & Teal', description: 'Pink*'}, {label: 'Neo Tokyo', description: 'NeoTokyo*'}, {label: 'Dystopia', description: 'Dystopia*'}, {label: 'Cyberpunk', description: 'Cyberpunk*'}, {label: 'All', description: '.*'}]">}}

---
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

# {#vintage}
{{< youtube v052UeIjusk >}}

{{< asset-buttons demo="https://fronkongames.github.io/demos-luts/vintage/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-vintage-275594" >}}

The vintage and retro look you're looking for is in '**Vintage**', 90 high quality LUTs including:

* **Nostalgia** (10): nostalgic aesthetics of retro cinema.
* **Retro** (10): retro vibes to travel to other times.
* **70s** (8): a journey through the iconic eras of the 1970s and 1980s.
* **Noir** (30): rich, nostalgic tones of classic film noir.
* **Old Films** (8): nostalgic aesthetics of retro cinema.
* **Photo** (8): iconic look and feel of vintage Fujifilm.
* **Sepia** (8): warm nostalgic look, beautiful sepia tones.
* **Semi B&W** (8): different black and white balances.

{{<
  gallery match="vintage/*"
  sortOrder="asc"
  rowHeight="100"
  margins="5"
  thumbnailResizeOptions="800x533 q100 Lanczos"
  showExif=false
  previewType="blur"
  embedPreview=true
  loadJQuery=true
  filterOptions= "[{label: 'Nostalgia', description: 'Nostalgia*'}, {label: 'Retro', description: 'Retro*'}, {label: '70s', description: '70s*'}, {label: 'Noir', description: 'Noir*'}, {label: 'Old Films', description: 'OlFIlms*'}, {label: 'Photo', description: 'Photo*'}, {label: 'Sepia', description: 'Sepia*'}, {label: 'Semi B&W', description: 'SemiBW*'}, {label: 'All', description: '.*'}]">}}

---
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

# {#anime}
{{< youtube vCk9eIxhir4 >}}

{{< asset-buttons demo="https://fronkongames.github.io/demos-luts/anime/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-anime-276902" >}}

Vibrant tones, unique contrasts and a cinematic touch. 58 high quality LUTs including:

* **Anime** (18): vibrant blue tones that captures the dreamlike essence of anime.
* **Arcade** (10): palette of old Japanese arcade machines.
* **Game** (10): colorful and saturated video game environment.
* **Virtual** (10): tones of consoles of past generations.
* **Yolk** (10): creomous yellow tones and contrasts.

{{<
  gallery match="anime/*"
  sortOrder="asc"
  rowHeight="100"
  margins="5"
  thumbnailResizeOptions="800x533 q100 Lanczos"
  showExif=false
  previewType="blur"
  embedPreview=true
  loadJQuery=true
  filterOptions= "[{label: 'Anime', description: 'Anime*'}, {label: 'Arcade', description: 'Arcade*'}, {label: 'Game', description: 'Game*'}, {label: 'Virtual', description: 'Virtual*'}, {label: 'Yolk', description: 'Yolk*'}, {label: 'All', description: '.*'}]">}}

---
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

# {#synthwave}
{{< youtube 2pW7-FFgTUA >}}

{{< asset-buttons demo="https://fronkongames.github.io/demos-luts/synthwave/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-synthwave-278499" >}}

Neon-drenched cyberpunk worlds. 50 high quality LUTs including:

{{<
  gallery match="synthwave/*"
  sortOrder="asc"
  rowHeight="100"
  margins="5"
  thumbnailResizeOptions="800x533 q100 Lanczos"
  showExif=false
  previewType="blur"
  embedPreview=true
  loadJQuery=true
  filterOptions= "[{label: 'All', description: '.*'}]">}}

---
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

# {#colors}
{{< youtube L-cWwo7O3IY >}}

{{< asset-buttons demo="https://fronkongames.github.io/demos-luts/colors/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/luts-colors-278789" >}}

A rainbow of colors for your games. 277 high quality LUTs including:

* **Bleach** (10): higher contrast, reduced saturation and very distinctive look.
* **Bright** (52): white tones displaced to blue and more clarity.
* **Brownish** (8): warm brown tones.
* **Colorify** (25): based on Instagram filters.
* **Creative** (7): creative ways to handle color.
* **Crisp White** (8): infuses simplicity and luminosity.
* **Dark Green** (8): dark forests.
* **Dark Mood** (10): dark and moody elegance.
* **Golden** (2): luxurious and minimalist look.
* **Luxury Black** (10): .
* **Minimalist** (26): modern look, bringing a crisp, clean, and bright aesthetic.
* **Pastels** (16): soft pastel hues.
* **Pink** (10): warm and pink tones.
* **Teal and Orange** (70): perfect balance of teal and orange tones.
* **Vibrant** (12): vibrant and dynamic aesthetic.

{{<
  gallery match="colors/*"
  sortOrder="asc"
  rowHeight="100"
  margins="5"
  thumbnailResizeOptions="800x533 q100 Lanczos"
  showExif=false
  previewType="blur"
  embedPreview=true
  loadJQuery=true
  filterOptions= "[{label: 'Colorify', description: 'Colorify*'}, {label: 'Bleach', description: 'Bleach*'}, {label: 'Creative', description: 'Creative*'}, , {label: 'Crisp White', description: 'CrispWhite*'}, {label: 'Vibrant', description: 'Vibrant*'}, {label: 'Bright', description: 'Bright*'}, {label: 'Pastels', description: 'Pastels*'}, {label: 'Minimalist', description: 'Minimalist*'}, {label: 'Pink', description: 'Pink*'}, {label: 'Teal & Orange', description: 'TealAndOrange*'}, {label: 'Luxury Black', description: 'LuxuryBlack*'}, {label: 'Dark Mood', description: 'DarkMood*'}, {label: 'Golden', description: 'Golden*'}, {label: 'Brownish', description: 'Brownish*'}, {label: 'Dark Green', description: 'DarkGreen*'}, {label: 'All', description: '.*'}]">}}

---
{{< rawhtml >}}<br><br>{{< /rawhtml >}}
## Misc

All '**LUTs**' have an advanced color grading panel. Check '**Color grading**' (_1_) to activate it.

{{< imagecenter src="/store/luts/color.jpg" >}}

'**Exposure**' (_2_) changes the exposure, or brightness. Just below you have a contrast control (_3_) and an HDR color (_4_) without alpha channel to tint the image.

To move the color wheel, use '**Hue**' (_5_). To change the amount of color, use '**Saturation**' (_6_).

Select the tone operator, '**Tonemap**' (_7_), that best suits your needs. The most popular ones are available: Neutral, ACES and Reinhard. If you want more, you may be interested in '[Artistic: Tonemapper](http://localhost:1313/store/artistic.html#tonemapper)'.

With '**White balance**' (_8_) you can adjust the perceived _temperature_ of the image. First you can make it perceived cooler or warmer. The next parameter modifies the color used to vary the perceived temperature.

'**Split toning**' (_9_) is used to tint shadows and highlights of an image separately. A typical example is to push shadows toward cool blue and highlights toward warm orange.

'**Channel mixer**' (_10_) allows you to combine input RGB values to create a new RGB value. For example, you could swap R and G, subtract B from G, or add G to R to push green toward yellow.

The last setting is '**Shadow Midtones Highlights**' (_11_), it works like split-toning, except that it also allows adjustment of the midtones and decouples the shadow and highlight regions, making them configurable.

They also have an '**Advanced**' panel with these options:

{{< imagecenter src="/store/luts/advanced.jpg" >}}

Activate '**Affect the Scene View?**' (_1_) if you want the effect to be applied also in the '_Scene_' window of the Editor. With '**Filter mode**' (_2_) you can change the type of filter used.

Although it is not recommended to change it, with '**RenderPass event**' (_3_) you can modify at which point in the render pipeline the effect is applied. Finally, activate '**Enable profiling**' (_4_) to show in the '_Profiling_' window the metrics of the effect.

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Support

Do you have any problem or any suggestions? Click on "**support**" or send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

Remember that if you want to inform me of an error, it would help me if you sent to me the [log file](https://docs.unity3d.com/Manual/LogFiles.html).

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}

❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
{{< center >}}
If you are happy with this asset, <b>please consider leaving a positive review</b> in the store, it would really help me,
<b>thanks</b>!
{{< /center >}}
