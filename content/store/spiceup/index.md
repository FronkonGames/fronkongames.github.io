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
* [Drunk](#drunk), simulates the effects of alcohol on the player.
* [Stoned](#stoned), imitates the impact or symptoms of feeling high or intoxicated.

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
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

{{< youtube rChUFliVX_E >}}

{{< asset-buttons demo="https://fronkongames.github.io/store/demos/damage/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-damage-247019">}}

'**Damage**' is a visual indicator of the damage suffered by the player. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/spiceup/damage_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

The damage must be **normalized**, or in other words between 0 and 1 (inclusive). Being 0 a perfectly healthy player and 1 a perfectly dead one. You can adjust its value with '**Damage**' (_1_), although most commonly you will modify it via code.

Let's say that '_DamageMax_' is a constant that indicates the maximum amount of damage the player can receive and '_damage_' is the variable with the damage received:

{{< highlight csharp "linenos=false" >}}
Damage.GetSettings().damage = damage / DamageMax;
{{< /highlight >}}
</br>

It can also be calculated from health:

{{< highlight csharp "linenos=false" >}}
Damage.GetSettings().damage = 1.0f - (health / HealthMax);
{{< /highlight >}}
</br>

Visually the damage is represented by three effects: _Liquid_, _Veins_ and _Drops_. You can configure how much they affect the final result using their sliders.

{{< gallery-slider dir="/images/store/spiceup/damage/" auto-slide="3000" width="600px" height="400px" color="#ffff" >}}

* Liquid: is the liquid that expands from the edges of the screen.
* Veins: simulates the capillary vessels of the human eye and add an extra 'gore'.
* Drops: adds dynamic liquid drops. '_Range_' is the number of droplet layers, with each layer having droplets of similar sizes. With '_Scale_' you control their size and with '_Speed_' the speed at which they disappear.

To indicate impacts, and the direction they come from, you can use '**Impact strength**' (_3_). These impacts will be displayed on the edges of the screen and will indicate the direction from which the impact is coming, the top part being a frontal impact, and the bottom part a rear impact.

{{< imagecenter src="/store/spiceup/damage_2.jpg" >}}

The time it stays on screen can be configured with: '_Rise time_', '_Wait time_' and '_Fall time_'. You can also adjust its thickness and the smoothness of the edges.

To get an idea of the effect, you can do it with '**Simulate impact**' (_13_).

{{< imagecenter src="/store/spiceup/damage_1.jpg" >}}

And how do I do it in the game? Very simple, 'Damage' takes care of everything. First it sets the target of the hits. The most typical case would be on the player. If 'player' is a GameObject that represents the player, it would be like this:

{{< highlight csharp "linenos=false" >}}
Damage.Target = player.transform;
{{< /highlight >}}
</br>

Now you will only have to call the 'Impact' function every time the unfortunate player receives an impact. If you do not specify the origin of the hit, a flash effect (general damage) will be created. If you specify who caused the damage, an impact with direction will be created.

{{< highlight csharp "linenos=false" >}}
// Flash effect.
Damage.Impact(0.25f);

// Impact with direction.
Damage.Impact(0.5f, zombie.transform);
{{< /highlight >}}
</br>

{{< notice tip >}}
* Damage must be **normalized**, i.e. from 0 to 1.
* The maximum number of hits with direction on the screen is **4**.
* The plane in which the direction is calculated is the XZ.
{{< /notice >}}

You can change the color in '**Color gradient**'. From the gradient used (_4_), through the color and ending with how the effect blends with the screen.

{{< notice tip >}}
If the final result is too dark, or too bright, try one of the many Blend operations included.
{{< /notice >}}

To modify the definition of the edges, change '**Definition**' (_5_). The final brightness of the effect can be set with '**Brightness**' (_6_).

To simulate a _more organic_ substance, a Vonoroi type noise can be applied to distort the effect. You can adjust its parameters in '**Noise**' (_7_).

With '**Distortion**' (_9_) you can modify how much the effect distorts the screen.

In some games you may have seen how they apply a _black and white_ effect as the player loses life. You can recreate it with '**Desaturation**' (_9_). This parameter is not modified according to '**Damage**' (_2_), so you will have to modify it manually.

To simulate some _volume_ to the liquid, a slight shimmer effect is applied to the top edges. Modify this effect in '**Edge**' (_10_).

Another effect you may have seen in other games, is how the player blinks, or loses peripheral vision. This effect can be adjusted with '**Blink**' (_11_). Like '**Desaturation**' (_9_), this effect must be adjusted manually.

{{< notice warning >}}
Very high values of '_Speed_' can create a **stroboscopic** effect that **may affect some users**.
{{< /notice >}}

Do values close to 1 of '**Damage**' (_2_) make the effect too intense? Adjust the range with '**Remap damage**' (_12_). By lowering the upper range somewhat, you will make very high values lower.

Finally, if you click on '**documentation**' (_14_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_15_). If you need to reset all the effect values, click on '**Reset**' (_16_).

# {#drunk}
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

{{< youtube L7agg4NP7XU >}}

{{< asset-buttons demo="https://fronkongames.github.io/store/demos/drunk/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/spice-up-drunk-247929">}}

With '**Drunk**' you can let players know that they are drinking too much.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/spiceup/drunk_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Drunkenness**' (_2_) you control the overall intensity of the effect. The higher the value, the more intense the result. You can also adjust the speed of the oscillations and their amplitude.

{{< notice warning >}}
High values of this effect may cause dizziness. Use with caution.
{{< /notice >}}

'**Swinging**' (_3_) causes the camera to swing. In addition to the intensity, you can control its speed.

With '**Distortion**' you can modify how the image is distorted, you can also control the speed and frequency of the distortion. You can also add to the image distortion, a displacement of the color channels (RGB) with '**Aberration**' (_5_).

'**Blink**' (_6_) adds to the effect a blinking of the eyes. You can also control with '**Eye**' (_7_) the point of the vision, being (0.5, 0.5) the center of the screen.

Do values close to 1 of '**Drunkenness**' (_2_) make the effect too intense? Adjust the range with '**Remap damage**' (_8_). By lowering the upper range somewhat, you will make very high values lower.

Finally, if you click on '**documentation**' (_9_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_10_). If you need to reset all the effect values, click on '**Reset**' (_11_).

# {#stoned}
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

{{< youtube 5f_TMTkHXM0 >}}

{{< asset-buttons demo="https://fronkongames.github.io/store/demos/stoned/" >}}

Too many potions? With '**Stoned**' you can simulate the effect of drinking too many.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/spiceup/stoned_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

With '**Stoned**' (_2_) you control the overall intensity of the effect. The higher the value, the more intense the result.

The first thing you can adjust is the speed of the effect with '**Speed**' (_3_). You can add some volume with '**Definition**' (_4_).

With '**Displacement**' (_5_) you can adjust the screen deformation. You can increase the granularity with '**Noise**' (_6_).

With '**Hue**' (_7_) you can shift the final color of the effect (is not the same control as the one in 'Color').

{{< notice tip >}}
If you cycle from 0 to 1 and back again, you can add extra psychedelia to the effect.
{{< /notice >}}

Adjust the strength of each color channel with '**Channel**' (_8_).

Internally, the effect uses the YIQ color space (used by the analog NTSC TV). In '**Luma info**' you can adjust its parameters. See more information about the [YIQ color space here](https://en.wikipedia.org/wiki/YIQ).

**Lines** (_10_) transforms the clouds of the effect into lines of intense color.

{{< video src="/store/spiceup/stoned_1.mp4">}}

{{< notice tip >}}
If you use lines and add ['Bloom' postprocessing](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/post-processing-bloom.html), you can get a very interesting effect. Adjust the intensity of 'Bloom' well to avoid annoying flares.
{{< /notice >}}

Finally, if you click on '**documentation**' (_14_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_15_). If you need to reset all the effect values, click on '**Reset**' (_16_).

With '**Tint**' (_11_) you can color the final result with the color of your choice. In '**Blend**' (_12_) you can select from a large list of color mixing functions. The selected function will be the one that blends the effect with the screen.

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
