---
author: Martin Bustos
title: Local AI
showTitle: false
date: 6
description: Generative AI entirely on your computer. No cloud, no subscription, no usage fees. Yours, private, forever
tags: ["unity", "store", "ai", "artificial intelligence", "music"]
metadata: none
showImage: true
thumbnail:
  url: img/localai.jpg
---

'**Local AI**' is a collection of **generative AI tools** that run entirely on your computer.

There is no cloud account, no subscription, no usage fees, and no per-prompt limits.

Your prompts and results stay on your machine.

It consists of the following assets:

* [🎵 Music](#music), generate songs offline from a style preset and optional lyrics.
* _and more to come..._

## Requirements

All '**Local AI**' assets are developed for **Unity 6** (version **6000.0** or higher) and the **Windows** x86_64 Editor. They run in the Editor, and they are not intended as a runtime player package unless a specific asset says otherwise.

Generation can run on the CPU, but a **GPU is recommend**: it is much faster.

If you don’t know how to install Unity 6, follow this [official tutorial](https://docs.unity3d.com/6000.0/Documentation/Manual/GettingStartedInstallingHub.html).

## Installation

1. Import the assets into your Unity project. If you've purchased the bundle, you'll be able to download all the assets from the store at no charge.
2. Open the tools from **Window → Fronkon Games → Local AI**.
3. Download the model files when the asset asks for them, or point it at a folder you already have.

{{< alert color="info" >}}
GGUF model weights are large. Keep them out of git. I recommend using a folder outside the project or adding `*.gguf` and `*.gguf.part` to your `.gitignore` file.
{{< /alert >}}

#
---
## 🎵 Music {#music}
{{< asset-header store="https://assetstore.unity.com/packages/tools/audio/local-ai-music-401726" youtube="mEzHKkLCFN8" >}}

'**Local AI: Music**' generates songs **offline** inside the Unity Editor. Describe style and arrangement, optionally write sectioned lyrics, then render a WAV on your machine.

* **Private and local.** Prompts, lyrics, and the WAV never leave your computer.
* **Editor-only.** Tools live under **Window → Fronkon Games → Local AI → Music**. Nothing is added to a player build unless you import the generated audio yourself.
* **Hundreds of styles.** Genre presets ship in the package, including instrumental variants. Duplicate and edit them, or create your own.
* **Optional lyrics.** Assign a lyric asset for a sung track. Leave lyrics empty (or use a style that describes no singer) and generation is treated as **instrumental** without rewriting the style asset.
* **WAV output.** Stereo, **44.1 kHz**, **16-bit PCM**. Length **5–300 s**.
* **Game-ready loops.** Enable **Seamless loop** to search for a natural wrap in the WAV and mark the imported AudioClip as loopable.
* **CUDA, then Vulkan, then CPU.** A GPU is not required. CUDA is used when a compatible NVIDIA GPU is present.

#### Requisites

To ensure optimal performance and compatibility, your project must meet the following requirements:

* **Unity:** 6000.0 or higher.
* **Editor:** Windows x86_64.
* **GPU:** not required. CUDA is used when a compatible NVIDIA GPU is present, then Vulkan, then CPU.
* **VRAM:** about **12 GB** for the included quantized models. A **16 GB** card is more comfortable.
* **Free space:** at least **10 GB** of free space.

#### Installation Guide

1. Import **Local AI: Music**.
2. Create a music style using the **Window → Fronkon Games → Local AI → Music → Style** tool (or use or modify one of the hundreds of included presets).
3. Create the lyrics using the **Window → Fronkon Games → Local AI → Music → Lyrics** tool.
4. Open **Window → Fronkon Games → Local AI → Music → Generator**. Select the style and lyrics.
5. Set the **Models** folder and click **Download**, or select a folder that already contains the five GGUF files.
6. Click `Generate`.

#### Tools

##### Style

{{< image src="music_style.png" wrapper="col-12 mx-auto">}}

A **Style** is a `MusicPreset` asset: a structured description of genre, mood, vocals, and arrangement. The generator turns this text into the caption sent to the model.

Create one with **New**, pick an existing asset in the object field, or start from a preset under `Editor/Presets/`. Changes are saved on the asset when you edit it.

##### Global

{{< table >}}
| | |
|---|---|
| **Style** | Genre and subgenre, for example `synthwave` or `acoustic folk`. |
| **Tempo** | Speed of the track, for example `96 BPM`. |
| **Key** | Key and scale, for example `C major`. |
| **Global Emotional Progression** | How the mood should evolve from the start of the song to the end. |
| **Scenarios & Imagery** | Listening context, pictures, and intended use (menu, trailer, in-game bed, and so on). |
| **Sonics & Production Profile** | Mix, soundstage, frequency balance, and dynamics. |
{{< /table >}}

##### Vocal Details

These fields describe a singer. If you generate **without** lyrics (or with empty section text), the generator builds an instrumental request and does **not** write these fields back onto the asset.

{{< table >}}
| | |
|---|---|
| **Vocal Gender & Timbre** | Who sings and how they sound (gender, range, timbre). |
| **Vocal Style** | Delivery, phrasing, and how the performance evolves. |
| **Harmony Vocals** | Backing vocals, choir, and stacks. |
| **Vocal FX** | Reverb, delay, widening, and other vocal processing. |
{{< /table >}}

##### Arrangement

{{< table >}}
| | |
|---|---|
| **Primary** | Main instruments present for most of the song. |
| **Secondary** | Supporting instruments and when they enter or drop out. |
| **Groove & Foundation Progression** | Rhythm, bass, drums, and how the groove changes over time. |
| **Textures & Spatial FX** | Atmosphere, spatial FX, and section transitions. |
{{< /table >}}

##### Lyrics

{{< image src="music_lyrics.png" wrapper="col-12 mx-auto">}}

A **Lyrics** asset is a `MusicLyric`: a title plus reorderable sections. Lyrics are **optional**. If you skip this asset, or every section has empty text, the generator treats the song as instrumental.

{{< alert color="info" >}}
The model has been trained on hundreds of hours of music featuring singers, so it tends to add vocals even when there aren't any.
{{< /alert >}}

{{< table >}}
| | |
|---|---|
| **Title** | Name of the lyric sheet (also used as the default file name when you click **New**). |
| **Sections** | Ordered list of parts. Drag to reorder. Use **+** to add a template, duplicate, or delete. |
| **Section** | Kind of part: Intro, Verse, Pre-Chorus, Chorus, Post-Chorus, Bridge, Instrumental, Solo, Outro, or **Custom** (your own heading). |
| **Text** | Sung lines for that section. Leave empty to emit `[instrumental]` for that part. |
| **Preview** | Opens a window with the tagged lyric sheet sent to the model (`[Verse]`, `[Chorus]`, and so on). |
{{< /table >}}

{{< alert color="info" >}}
Lyrics can be written in any language, but the model is trained and documented primarily on **English**. Non-English lyrics may work but are **not guaranteed**. Quality depends on the language and how clearly the **Style** describes the vocal character (for example, genre and timbre). There is no separate language control.
{{< /alert >}}

##### Multiple voices (experimental)

To assign different singers to different sections (for example, a duet) describe **both** voices in **Style → Vocal Details** (gender, timbre, and who sings which part).

Add **short** voice tags on their own lines inside the section text: `[male vocal]`, `[female vocal]`, or `[duet]`.

Caption-only instructions are usually not enough, tags in the lyrics matter too. Keep each tag to one or two words, longer tags may be sung aloud.

```
[Verse]
[male vocal]
I walked alone through midnight rain
Every street remembers your name

[Verse]
[female vocal]
You left a letter by the door
Said you weren't coming back no more

[Chorus]
[duet]
We were fire, we were flame
Nothing left but ash and shame
```

In the Style, name both singers and state who opens, for example, a deep male baritone on the first verse, a bright female soprano on the second, both joining the chorus, with no choir or doubled backing vocals. 

Section-level switching works best; line-by-line alternation usually fails. Casting is not deterministic, try different seeds and check the first few seconds; if the wrong voice opens, generate again.

{{< alert color="warning" >}}
Multi-voice experimental, not an official feature. Expect to re-roll several times for a usable take.
{{< /alert >}}

##### Generator

{{< image src="music_generator.png" wrapper="col-12 mx-auto">}}

Assign a style, optionally lyrics, then **Generate**. Native backends are tried in order: **CUDA → Vulkan → CPU**.

##### Diffusion

{{< table >}}
| | |
|---|---|
| **Seed** | DiT noise seed. **-1** picks a random seed. |
| **CFG** [1.0-3.5] | Diffusion guidance. Higher follows the style more strictly. Default: 1.7. |
| **Peak clip** [0-100] | Limits output peaks to reduce distortion. Default: 10. |
{{< /table >}}

##### Language Model

{{< table >}}
| | |
|---|---|
| **Seed** | Language-model sampling seed. **-1** picks a random seed. |
| **CFG** [1.0-3.0] | Language-model guidance. Default: 1.5. |
| **Top-k** [1-200] | Sampling is limited to the k most likely tokens. Default: 50. |
{{< /table >}}

##### Generation

{{< table >}}
| | |
|---|---|
| **Keep models loaded** | If enabled, GGUF weights stay in memory between runs (faster repeats, more RAM/VRAM). |
| **Preset** | The `MusicPreset` (style) to generate from. **New** creates an asset; **Edit** opens Style. |
| **Lyrics** | Optional `MusicLyric`. **New** creates an asset; **Edit** opens Lyrics. |
| **Duration** [5-300 s] | Length of the WAV. Default: 60. Output is always stereo **44.1 kHz** **16-bit PCM**. |
| **DiT steps** [8-50] | Diffusion transformer steps. Higher is slower and can be cleaner. Default: 30. |
| **Seamless loop** | After generate, search for a loopable wrap and mark the imported AudioClip as loopable. |
| **Models** | Folder that contains the five GGUF files. **Download** fetches them. |
| **Output** | Destination `.wav` path (stereo, 44.1 kHz, 16-bit PCM). **Pin** highlights the clip in the Project window if it is inside the project. |
| **Generate** | Starts generation. Disabled until a style is assigned and the model files are valid. |
{{< /table >}}

</br>

Powered by [MiniMax Music 3](https://huggingface.co/MiniMaxAI/MiniMax-Music3).

#
---
## F.A.Q.

##### _Will I run into any copyright issues?_

**Generated files are yours to ship** in games or media (commercial or not).

You **shouldn't** use this assets for other purposes besides generating assets for games or promotional material.

You **cannot** impersonate real people, plagiarize copyrighted works, or use it for illegal purposes.

**It's your responsibility**.

##### _Do I need to say that my game use AI?_

**It depends on the platform.**

For example, on [Steam](https://store.steampowered.com/news/group/4145017/view/3862463747997849618) you must disclose the use of generative AI if any AI-generated content or assets actually ship with your game or appear in your store and marketing materials.

---
## Support

Do you have any problem or any suggestions? Send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

If you want to report an error, it helps a lot if you include the [Unity log file](https://docs.unity3d.com/Manual/LogFiles.html).

{{< rawhtml >}}
<br><center><h4>
{{< /rawhtml >}}

{{< alert color="warning" >}}
If you are happy with this asset, consider writing a review in the store.

Thanks!
{{< /alert >}}

{{< rawhtml >}}
</center></h4>
{{< /rawhtml >}}
