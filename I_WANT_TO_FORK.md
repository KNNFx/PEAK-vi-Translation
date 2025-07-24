# I WANT TO FORK...
### Preface
> Welcome to fork and translate into other languages.
> 
> I'm glad to see if you are willing to use this project as a base for PEAK translation in your own language, and also publish in store as you want. 
> 
> I would be very grateful if you could indicate the source (´･ω･`)

## Replacing the Font
### Step 0: Preparation
- Unity (Unity 6000.1.9f1 in this guide)
- Install [`AssetBundle Browser`](https://github.com/Unity-Technologies/AssetBundles-Browser) in Unity
- The Font File (Use `.ttf` in this guide)
- The word sheet (Base on [教育部常用字4808字.txt](https://github.com/Watermelonnn/ChineseUsefulToolKit/blob/master/%E6%95%99%E8%82%B2%E9%83%A8%E5%B8%B8%E7%94%A8%E5%AD%974808%E5%AD%97.txt) in this guide)
> Better to confirm whether is this usage is allow in the font license

![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/fork/img_fork_font_guide0.png)

### Step 1: Make a TextMeshPro

- First, please navigate to `Window` ->`TextMeshPro` -> `Font Asset Creator`

![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/fork/img_fork_font_guide1_1.png)

- Then, select the font that u want in `Source Font`
  - If necessery, choose the font face that you want.
- Next, modify `Padding`, `Sampling Point Size`, `Atlas Resolution`, `Render Mode` yourself
  - Atlas Resolution is deppends on your situation, feel free to try and find the best choice on your own situation
  - In my case, `Padding` is 4px, `Sampling Point Size` is 75, `Atlas Resolution` is 8192x8192, `Render Mode` is RASTER
- Finally, press `Generate Font Atlas` and wait for some minutes
  - First build will be quiteeeeeeeee looooooooooooong
  - Feel free to take a coffee or take a break while waiting
- Once it finished, please:
  - Take a look missing characters to see need to increase the resolution
  - Take a look the preview of the font atlas
  - `Save as` your result if you are fulfill with this result

![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/fork/img_fork_font_guide1_2.png)

**IMPORTANT!!**<br>
- You will need to do the generation twice
- E.g. Save as `Normal.asset` first, then press the `Generate Font Atlas` and Save as `Transmit.asset` 
![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/fork/img_fork_font_guide1_3.png)

### Step 2: Inspector
![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/fork/img_fork_font_guide2.png)
**You will need to do it on both normal and transmit**
- Press the Expand button at the font's right side
- `normal Atlas`
  - Select `Bilinear` for the Filter Mode
- `normal Material`
  - Select `TextMeshPro/Distance Field` as the Shader

### Step 3: Packaging
- First, Navigate to `Window` -> `AssetBundle Browser`
- Then, Right click the left area and press `Add new bundle`
![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/fork/img_fork_font_guide3_2.png)

- Next, Pull `normal` and `transmit` into the bundle you just created
![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/fork/img_fork_font_guide3_1.png)

- Besides, Press the `Build` Tab, then select:
  - Build Target: `Standalone Windows`
  - Output Path: `Assets/AssetBundles`
  - Press `Build` button and wait
- ![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/fork/img_fork_font_guide3_3.png)

- Finally, once it done, you can find the font bundle *(sarasa_gothic in this example)* in `Assets/AssetBundles`
![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/fork/img_fork_font_guide3_4.png)

- Copy & Paste to `../BepInEx/config/FontPatcher/`, and change the name of it to ```00 <your_font_name_as_well>```
  - P.S. `00` means the priority of the font in this folder, `01` is the second priority, etc...

### FINISH~