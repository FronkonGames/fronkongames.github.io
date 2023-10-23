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
* [Tilt Shift](#tiltshift), used to simulate a miniature scene.
* [Color Isolation](#colorisolation), isolates areas by color and applies effects.

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

{{< asset-buttons demo="https://fronkongames.github.io/demos-artistic/onebit/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/one-bit-216000">}}

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

{{< youtube A9jtFpXo02Q >}}

{{< asset-buttons demo="https://fronkongames.github.io/demos-artistic/oilpaint/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-oil-paint-264134" >}}

Transform your games into pieces of art in a very easy way. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/artistic/oilpaint_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

Oil Paint provides you with a wide variety of algorithms (__2__) to choose from to best suit your needs. They are as follows:

* **Kuwahara Basic**: the simplest and fastest based on the algorithm created by [Michiyoshi Kuwahara](https://en.wikipedia.org/wiki/Kuwahara_filter).
* **Kuwahara Generalized**: a version that fixes some problems of the previous one, based on the work of [Acerola](https://www.youtube.com/@Acerola_t).
* **Kuwahara Directional**: a Sobel filter is added to improve the denoising process.
* **Kuwahara Anisotropic**: improves the quality in the smallest details, based on the paper '[Image and Video Abstraction by Anisotropic Kuwahara Filtering](https://www.researchgate.net/publication/220507613_Image_and_Video_Abstraction_by_Anisotropic_Kuwahara_Filtering)'.
* **Tomita-Tsuji**: a steroid version of Kuwahara's algorithm, with the best visual results but with a performance decrease.
* **Symmetric Nearest Neighbour**: another smoothing algorithm designed to preserve image edges. Much more efficient than the previous ones.

Depending on the selected algorithm, you will see different parameters although all of them have '**Passes**'. This parameter specifies the number of passes of the algorithm to be performed. If it is 1, the algorithm will only run once per pixel.

If you increase the value, the effect will be greatly enhanced but you will multiply the cost of the effect. I only recommend that the value be greater than 1 if you are going to use it on powerful hardware (consoles and PC).

You can add an extra algorithm to better define details with '**Improve details**' (__3__): Emboss and Sharpen. Note that adding this algorithm creates an additional pass and therefore lower performance.

Still not enough? Raise the value of '**Water Color**' (__4__) to add an water color paint effect to the image.

If you need more control, activate '**Process depth**' (__5__).

{{< imagecenter src="/store/artistic/oilpaint_1.jpg" >}}

With '**Depth curve**' (__1__) you can adjust the intensity of the effect depending on the depth. In the values of the example you can see that the effect would have the maximum intensity except in the farthest areas it would tend to 0. With this you can avoid that small details in the background of the scene disappear because of the effect. You can also adjust the intensity of the curve with '**Depth power**' (__2__).

Adjusting these two parameters can be complicated by not being able to see clearly how the curve varies. Activate '**View depth curve**' (__4__) and you will see that the areas with the most intense effect are warmer and the areas with the least are cooler.

{{< video src="/store/artistic/oilpaint_2.mp4" >}}

Don't want the effect to be applied to the sky? Disable '**Sample sky**' (__3__).

Finally, if you click on '**documentation**' (_7_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_8_). If you need to reset all the effect values, click on '**Reset**' (_9_).

---
# {#tiltshift}
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

{{< youtube ixqjMNnUSus >}}

{{< asset-buttons demo="https://fronkongames.github.io/demos-artistic/tiltshift/" store="https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/artistic-tilt-shift-265465" >}}

Used to simulate a miniature scene, something very used in cinema as in the [race scene](https://www.youtube.com/watch?v=QetnuKbo1XI) of '_The Social Network_'. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/artistic/tiltshift_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

You can modify the angle (_2_), aperture (_3_) and offset (_4_) of the effect. Also the blur intensity (_5_) and distortion (_6_).

You can also modify certain color parameters in the 'focused' (_7_) area (where the effect is not applied) and in the 'unfocus' (_8_) area.

{{< imagecenter src="/store/artistic/tiltshift_1.jpg" >}}

In order to better adjust these parameters, you can activate '**Debug**' (_9_) to better see how the effect is applied. With this parameter activated, the areas with more intensity of the effect will be tinted red, and those with less intensity will be tinted blue.

Finally, if you click on '**documentation**' (_11_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_12_). If you need to reset all the effect values, click on '**Reset**' (_13_).

---
# {#colorisolation}
{{< rawhtml >}}<br><br>{{< /rawhtml >}}

{{< youtube XfHdKU1qTF4 >}}

{{< asset-buttons demo="https://fronkongames.github.io/demos-artistic/colorisolation/" >}}

Isolates areas by color and applies effects. Once installed, when you select your '_Universal Renderer Data_', you will see something like this:

{{< imagecenter src="/store/artistic/colorisolation_0.jpg" >}}

With '**Intensity**' (_1_) you can control the intensity of the effect. If it is 0, the effect will not be active.

Finally, if you click on '**documentation**' (_11_) you will go to the online documentation. If you need support, you can send me an email to '_frokongames@gmail.com_' or you can click on '**support**' (_12_). If you need to reset all the effect values, click on '**Reset**' (_13_).

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
