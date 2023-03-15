---
title: "Spice Up"
date: 2023-02-22T12:23:10+06:00
image: /store/spiceup/mini.png
logo: /store/spiceup/logo.png
description: "A large selection of assets to give juice to your FPS / VR games."
type: "store"
---

'**Spice Up**' is a large selection of effects to give juice to your FPS / VR games. It consists of the following assets:

* [Damage](#damage), a visual indicator of health and damage received.

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Requirements

All '**Spice Up**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP)', which means they will **not work** with Built-In, or HDRP.

You will need to have URP version 12.1 or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Spice Up**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< imagecenter src="/store/spiceup/editor_0.jpg" >}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< imagecenter src="/store/spiceup/editor_1.jpg" >}}

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Using them in code

You can also handle '**Spice Up**' effects by code. The first thing you will have to do is to add the namespace of the effect you want to use.

They are all of the style 'FronkonGames.SpiceUp.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**Damage**' the code would be:

{{< highlight csharp "linenos=false" >}}
using FronkonGames.SpiceUp.Damage;
{{< /highlight >}}
</br>

And with this code you could check if the effect is added, and if it is not, add it.

{{< highlight csharp "linenos=false" >}}
if (Damage.IsInRenderFeatures() == false)
    Damage.AddRenderFeature();
{{< /highlight >}}
</br>

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

{{< highlight csharp "linenos=false" >}}
 Damage.Settings settings = Damage.GetSettings();

 settings.intensity = 0.5f;
 {{< /highlight >}}
</br>

If you are using an effect other than '**Damage**' just change it to its name. Check the source code comments for more information.

# {#damage}
{{< rawhtml >}}</br></br></br>{{< /rawhtml >}}

{{< youtube rChUFliVX_E >}}

{{< rawhtml >}}
<br>
<div class="text-center">
    <a href="https://fronkongames.github.io/store/demos/damage/" class="btn btn-default">🕹️ Demo</a>
    <a href="" class="btn btn-default">🛒 Store (soon)</a>
</div>
</br>
{{< /rawhtml >}}

'**Damage**' is a visual indicator of the damage suffered by the player. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/spiceup/damage_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

{{< imagecenter src="/store/spiceup/damage_1.jpg" >}}

The damage must be normalized, or in other words between 0 and 1 (inclusive). Being 0 a perfectly healthy player and 1 a perfectly dead one. You can adjust its value with '**Damage**' (_1_), although most commonly you will modify it via code.

Let's say that '_DamageMax_' is a constant that indicates the maximum amount of damage the player can receive and '_damage_' is the variable with the damage received:

{{< highlight csharp "linenos=false" >}}
if (Damage.IsInRenderFeatures() == false)
    Damage.GetSettings().damage = damage / DamageMax;
{{< /highlight >}}
</br>

It can also be calculated from health:

{{< highlight csharp "linenos=false" >}}
if (Damage.IsInRenderFeatures() == false)
    Damage.GetSettings().damage = (1.0f - (health / HealthMax));
{{< /highlight >}}
</br>

Finally, if you click on '**documentation**' (_14_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_15_). If you need to reset all the effect values, click on '**Reset**' (_16_).

{{< rawhtml >}}<br><br>{{< /rawhtml >}}
## Misc

All '**Spice Up**' effects have a panel, '**Color**', in which you can modify the final color of the effect.

{{< imagecenter src="/store/spiceup/color.jpg" >}}

They also have an '**Advanced**' panel with these options:

{{< imagecenter src="/store/spiceup/advanced.jpg" >}}

Activate '**Affect the Scene View?**' (_1_) if you want the effect to be applied also in the '_Scene_' window of the Editor. With '**Filter mode**' (_2_) you can change the type of filter used.

Although it is not recommended to change it, with '**RenderPass event**' (_3_) you can modify at which point in the render pipeline the effect is applied. Finally, activate '**Enable profiling**' (_4_) to show in the '_Profiling_' window the metrics of the effect.

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Support

Do you have any problem or any suggestions? Click on "**support**" or send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

Remember that if you want to inform me of an error, it would help me if you sent to me the [log file](https://docs.unity3d.com/Manual/LogFiles.html).

If you are happy with this asset, **please consider leaving a positive review** in the store, it would really help me, **thanks**!
