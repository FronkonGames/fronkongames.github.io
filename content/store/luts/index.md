---
title: "LUTs"
date: 2022-10-01
image: /store/luts/mini.png
logo: /store/luts/logo.png
description: "The largest collection of LUTs in the entire store"
type: "store"
---

**LUTs**' is (or will be) the largest collection of LUTs of the entire store. Thanks to LUTs (or 'LookUp Table') you can completely transform the look of your games, making them more coherent with your artistic preferences.

'**LUTs**' contains the following assets:

* [Cyberpunk](#cyberpunk) (61 LUTs): apocalyptic future, looking cool.

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Requirements

All '**LUTs**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP)', which means they will **not work** with Built-In, or HDRP.

You will need to have URP version 12.1 or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

{{< notice warning "" >}}
All LUTs are 3D textures, so the hardware must support it (+2014). 
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
Profile profile = Resources.Load<Profile>("LUTs/Profiles/Cyberpunk/Cyberpunk_01");

Cyberpunk.Settings settings = Cyberpunk.GetSettings();

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

{{< asset-buttons demo="https://fronkongames.github.io/demos-luts/cyberpunk/">}}

Finally, if you click on '**documentation**' (_4_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_5_). If you need to reset all the effect values, click on '**Reset**' (_6_).

---
{{< rawhtml >}}<br><br>{{< /rawhtml >}}
## Misc

All '**LUTs**' have an advanced color grading panel. Check '**Color grading**' (_1_) to activate it.

{{< imagecenter src="/store/luts/color.jpg" >}}

They also have an '**Advanced**' panel with these options:

{{< imagecenter src="/store/luts/advanced.jpg" >}}

Activate '**Affect the Scene View?**' (_1_) if you want the effect to be applied also in the '_Scene_' window of the Editor. With '**Filter mode**' (_2_) you can change the type of filter used.

Although it is not recommended to change it, with '**RenderPass event**' (_3_) you can modify at which point in the render pipeline the effect is applied. Finally, activate '**Enable profiling**' (_4_) to show in the '_Profiling_' window the metrics of the effect.

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Support

Do you have any problem or any suggestions? Click on "**support**" or send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

Remember that if you want to inform me of an error, it would help me if you sent to me the [log file](https://docs.unity3d.com/Manual/LogFiles.html).

If you are happy with this asset, **please consider leaving a positive review** in the store, it would really help me, **thanks**!
