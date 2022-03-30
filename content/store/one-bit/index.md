---
title: "One Bit"
date: 2022-03-23T12:23:10+06:00
image: /store/one-bit/mini.png
logo: /store/one-bit/logo.png
demo: https://fronkongames.github.io/store/demos/one-bit/
store: https://assetstore.unity.com/packages/slug/216000
youtube: https://www.youtube.com/watch?v=WY10wS39GDw
description: "A hipster, original and versatile look using a dithering with blue noise."
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
## Use

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
## Support

Do you have any problem or any suggestions? Click on "**support**" or send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

Remember that if you want to inform me of an error, it would help me if you sent to me the [log file](https://docs.unity3d.com/Manual/LogFiles.html).

{{< rawhtml >}}</br><center><b><h1>Thanks for your interest in my asset!</h1></b></center>{{< /rawhtml >}}