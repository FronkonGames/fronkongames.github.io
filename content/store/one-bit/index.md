---
title: "One Bit"
date: 2022-03-23T12:23:10+06:00
image: /store/one-bit/mini.png
logo: /store/one-bit/logo.png
demo: https://fronkongames.github.io/store/demos/one-bit/
store: https://assetstore.unity.com/packages/slug/216000
youtube: https://www.youtube.com/watch?v=WY10wS39GDw
description: "A hipster, original and versatile look using a dithering with blue noise"
type: "store"
---

Get a distinctive look with '**One Bit**', an original and versatile effect that uses a special type of dithering algorithm based on Blue Noise, similar to that used at the award-winning '**Return of the Obra Dinn**'.

{{< rawhtml >}}</br>{{< /rawhtml >}}
## Configuration for Builtin

To use '**One Bit**' for Builtin render (Unity default render) you just have to add the '**One Bit (Builtin)**' component to the camera of your scene.

{{< imagecenter src="/store/one-bit/editor_0.jpg" >}}

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Configuration for URP

To use '**One Bit**' with URP render (Universal Render Pipeline), the first thing you should do is install the '**Universal RP**' package version **10.8.1 or higher**. For more information on how to do this, you can follow [this official tutorial](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@10.8/manual/InstallURPIntoAProject.html).

Once the '**Universal RP**' package is installed correctly, you can now install '**One Bit**'. Once installed, locate the file '**Universal Render Pipeline Asset**'. You can find it in the window '**Project Settings**' > '**Graphics**':

{{< imagecenter src="/store/one-bit/editor_1.jpg" >}}

Select it and locate the file that appears in '**Render List**':

{{< imagecenter src="/store/one-bit/editor_2.jpg" >}}

Now you can add '**One Bit URP**' by clicking on '**Add Renderer Feature**':

{{< imagecenter src="/store/one-bit/editor_3.jpg" >}}

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Editor

Once installed you will see something like this:

{{< imagecenter src="/store/one-bit/editor_4.jpg" >}}

'**Amount**' controls the intensity of the effect. If you set it to 0, is like is deactivated.

In the '**Pattern**' section you can change the type of noise used for the dithering. '**Edges**' makes it remarked more the edges and '**Noise Strength**' affects the amount of noise that will appear on the screen.

The '**Color**' section is responsible for the final color of the image. The first parameter, '**Blend mode**', specifies the formula used to mix the original color of the screen with the effect. They are very similar to those you can find in 'Photoshop'.

With '**Color mode**' you can change the way a color (or several) effects the final result. The simplest is '**Solid**' and its '**Color**' parameter tints the image.

With '**Horizontal**', '**Vertical**' and '**Circular**' you can use a two-color gradient.

{{< imagecenter src="/store/one-bit/editor_5.jpg" >}}

'**Ramp**' is a mode in which a five-color gradient is applied to the final image according to the luminosity of each pixel, applying the first color of the gradient to the darker pixels and the fifth to the brightest. You can control the rank of the brightness used with '**Luminance**'.

To facilitate the task of choosing gradients you can click on '**search**', with which you open a tool to search gradients (_requires Internet connection_):

{{< imagecenter src="/store/one-bit/editor_6.jpg" >}}

You just have to find the gradient and press on '**Use**' where you like the most.

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Code (Built-In)

You can also use '**One Bit**' from your code. The first thing you have to do is to add the namespace:

{{< highlight csharp "linenos=false" >}}
using FronkonGames.OneBit;
{{< /highlight >}}
</br>

If you are still using Unity's default rendering system, **Built-In**, you will have to look for the '**OneBit_BuiltIn**' component in your scene:

{{< highlight csharp "linenos=false" >}}
OneBit_BuiltIn oneBit = FindObjectOfType<OneBit_BuiltIn>();
{{< /highlight >}}
</br>

You can also set the component from the Editor and not have to search for it:

{{< highlight csharp "linenos=false" >}}
[SerializeField]
private OneBit_BuiltIn oneBit;
{{< /highlight >}}
</br>

Once you have the component, you only have to use its properties to modify it. For example, to change the intensity by half:

{{< highlight csharp "linenos=false" >}}
[SerializeField]
oneBit.Amount = 0.5f;
{{< /highlight >}}
</br>

See the file '_FronkonGames/OneBit/Runtime/BuiltIn/OneBit_BuiltIn.cs_' for all properties.

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Code (URP)

If you use the '_Universal Render Pipeline_' (or **URP**), you will also have to add the namespace first:

{{< highlight csharp "linenos=false" >}}
using FronkonGames.OneBit;
{{< /highlight >}}
</br>

Now you must request the Render Feature that you added in the Editor (see '_Configuration for URP_'). You will need to use '_Reflection_' so you will have to add it:

{{< highlight csharp "linenos=false" >}}
using System.Reflection;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
{{< /highlight >}}
</br>

Create a function like this:

{{< highlight csharp "linenos=false" >}}
public OneBit_URP GetOneBitRendererFeature()
{
    OneBit_URP oneBitURP = null;

    UniversalRenderPipelineAsset pipelineAsset = (UniversalRenderPipelineAsset)GraphicsSettings.renderPipelineAsset;
    if (pipelineAsset != null)
    {
        FieldInfo propertyInfo = pipelineAsset.GetType().GetField("m_RendererDataList", BindingFlags.Instance | BindingFlags.NonPublic);
        ScriptableRendererData scriptableRendererData = ((ScriptableRendererData[])propertyInfo?.GetValue(pipelineAsset))?[0];
        for (int i = 0; i < scriptableRendererData.rendererFeatures.Count && oneBitURP == null; ++i)
        {
            if (scriptableRendererData.rendererFeatures[i] is OneBit_URP)
                oneBitURP = scriptableRendererData.rendererFeatures[i] as OneBit_URP;
        }
    }

    return oneBitURP;
}
{{< /highlight >}}
</br>

I hope that in the future, Unity will make this task easier, but for now it is the only option. Remember that when using '_Reflection_', this function can affect performance so **I don't recommend** to do it inside '_Update()_' or similar.

Once we have the _Renderer Feature_ of '**One Bit**', we can request its '_settings_' and modify its parameters. For example, to change the intensity by half:

{{< highlight csharp "linenos=false" >}}
oneBitURP = GetOneBitRendererFeature();
if (oneBitURP != null)
    oneBitURP.settings.amount = 0.5f;
{{< /highlight >}}
</br>

Check the file '_FronkonGames/OneBit/Runtime/URP/OneBit_FeatureSettings.cs_' for all properties.

{{< rawhtml >}}</br>{{< /rawhtml >}}{{< rawhtml >}}</br>{{< /rawhtml >}}
## Support

Do you have any problem or any suggestions? Click on "**support**" or send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

Remember that if you want to inform me of an error, it would help me if you sent to me the [log file](https://docs.unity3d.com/Manual/LogFiles.html).

If you are happy with this asset, **please consider leaving a positive review** in the store, it would really help me, **thanks**!