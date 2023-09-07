---
title: "Artistic"
date: 2023-02-22T12:23:10+06:00
image: /store/artistic/mini.png
logo: /store/artistic/logo.png
description: "Enhance your creativity and get a unique style with this effects bundle."
type: "store"
---

'**Artistic**' contains the following assets:

* [One Bit](#onebit), a hipster, original and versatile look using a dithering with blue noise.
* [Oil Paint](#oilpaint), transform your games into pieces of art.

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Requirements

All '**Artistic**' effects are developed for '[Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html)' (or URP)', which means they will **not work** with Built-In, or HDRP.

You will need to have URP version 12.1 or higher installed. If you don't know how to do it, I recommend you to follow this [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/InstallURPIntoAProject.html).

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Using them in the Editor

Once installed, you have to add the effect you want to use from '**Artistic**' as a '[Render Feature](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature.html)'. This [official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/urp-renderer-feature-how-to-add.html) tells how to do it.

{{< imagecenter src="/store/artistic/editor_0.jpg" >}}

Remember that the camera you are using must have the '**Post Processing**' option enabled.

{{< imagecenter src="/store/artistic/editor_1.jpg" >}}

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Using them in code

You can also handle '**Artistic**' effects by code. The first thing you will have to do is to add the namespace of the effect you want to use.

They are all of the style 'FronkonGames.Artistic.XXXX', where XXXX is the name of the effect. For example, if the effect you want to use is '**One Bit**' the code would be:

{{< highlight csharp "linenos=false" >}}
using FronkonGames.Artistic.OneBit;
{{< /highlight >}}
</br>

And with this code you could check if the effect is added, and if it is not, add it.

{{< highlight csharp "linenos=false" >}}
if (OneBit.IsInRenderFeatures() == false)
    OneBit.AddRenderFeature();
{{< /highlight >}}
</br>

To modify any of the effect parameters, you must first request its __settings__. In the following example we change the intensity of the effect by half.

{{< highlight csharp "linenos=false" >}}
 OneBit.Settings settings = OneBit.GetSettings();

 settings.intensity = 0.5f;
 {{< /highlight >}}
</br>

If you are using an effect other than '**OneBit**' just change it to its name. Check the source code comments for more information.

---
# {#onebit}
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

{{< youtube Yz9j7iXuDhY >}}

{{< asset-buttons demo="https://fronkongames.github.io/store/demos/onebit/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/one-bit-216000">}}

Get a distinctive look with '**One Bit**', an original and versatile effect that uses a special type of dithering algorithm based on Blue Noise, similar to that used at the award-winning '_Return of the Obra Dinn_'.

Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/artistic/onebit_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

'**Edges**' (_2_) makes it remarked more the edges and '**Noise**' (_2_) affects the amount of noise that will appear on the screen. You can change the random seed used to generate the noise with '**Seed**'.

'**Blend**' (_4_), specifies the formula used to mix the original color of the screen with the effect. They are very similar to those you can find in '_Photoshop_'. With '**Color**' you can change the way a color (or several) effects the final result. The simplest is '**Solid**' and its '**Color**' parameter tints the image. Other modes are '**Horizontal**', '**Vertical**' and '**Circular**' and use two colors in a gradient in different directions.

{{< imagecenter src="/store/artistic/onebit_1.jpg" >}}

'**Ramp**' is another mode that uses the brightness of the original pixel to replace it in a color gradient. So the leftmost colors of the gradient would be used for the darker areas of the image and the rightmost colors would be used for the brighter areas. Click on the gradient to modify it to your liking. If the gradient you use does not have dark colors, the result may be too bright, and vice versa. You can modify the brightness range used with '**Luminance**'.

Click on '**search**' to open the color palette search tool.

{{< imagecenter src="/store/artistic/onebit_2.jpg" >}}

Just find a palette you like and click the '**Use**' button.

{{< notice note "" >}}
This tool requires an Internet connection.
{{< /notice >}}

In _6_, _7_ and _8_ you can modify the color range in each channel. Small values in these fields can create a '_retro_' effect.

When '**Invert**' (_9_) is activated, the color is inverted.

Finally, if you click on '**documentation**' (_10_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_11_). If you need to reset all the effect values, click on '**Reset**' (_12_).

---
# {#oilpaint}
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

{{< youtube Yz9j7iXuDhY >}}

{{< asset-buttons demo="https://fronkongames.github.io/store/demos/oilpaint/"}}

Transform your games into pieces of art in a very simple way. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/artistic/oilpaint_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

Finally, if you click on '**documentation**' (_10_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_11_). If you need to reset all the effect values, click on '**Reset**' (_12_).

{{< rawhtml >}}<br><br>{{< /rawhtml >}}
## Misc

All '**Artistic**' effects have a panel, '**Color**', in which you can modify the final color of the effect.

{{< imagecenter src="/store/artistic/color.jpg" >}}

They also have an '**Advanced**' panel with these options:

{{< imagecenter src="/store/artistic/advanced.jpg" >}}

Activate '**Affect the Scene View?**' (_1_) if you want the effect to be applied also in the '_Scene_' window of the Editor. With '**Filter mode**' (_2_) you can change the type of filter used.

Although it is not recommended to change it, with '**RenderPass event**' (_3_) you can modify at which point in the render pipeline the effect is applied. Finally, activate '**Enable profiling**' (_4_) to show in the '_Profiling_' window the metrics of the effect.

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Support

Do you have any problem or any suggestions? Click on "**support**" or send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

Remember that if you want to inform me of an error, it would help me if you sent to me the [log file](https://docs.unity3d.com/Manual/LogFiles.html).

If you are happy with this asset, **please consider leaving a positive review** in the store, it would really help me, **thanks**!
