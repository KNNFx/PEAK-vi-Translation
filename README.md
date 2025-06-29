![PEAK_ZH_TW_LOGO](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/Logo.png)
# PEAK 繁體中文翻譯模組 by Voc-夜芷冰
![version](https://img.shields.io/badge/version-1.0.5-pink)
![make-with-love](https://camo.githubusercontent.com/da124fe0d303f3da8682918930b2f99caf16cda69474c01b4c48598d38f71613/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d616b655f776974685f2545322539442541342545462542382538462d7768697465)
[![wakatime](https://wakatime.com/badge/user/ca727ba5-9112-4612-b454-d5e407277a51/project/97d38b2f-ce2b-418e-9492-9f3687c2bf1a.svg)](https://wakatime.com/badge/user/ca727ba5-9112-4612-b454-d5e407277a51/project/97d38b2f-ce2b-418e-9492-9f3687c2bf1a)

## 感謝使用本翻譯模組
- 如對你有幫助，請給個讚和收藏吧 :D
- 發現翻譯有問題嗎？可以到 [Coding Band](https://discord.gg/uXatcbWKv2) 的 [`👾｜問題發表｜questions`](https://discord.com/channels/880921456903618610/1067563572865024223) 提出 / 在 [GitHub](https://github.com/Vocaloid2048/PEAK-zh-tw-Translation/) 提交 Issues (先不要PR)
- **如真的很有需要，或者長時間沒收到答覆**，請先加入Discord伺服器，然後在私訊我：`vocaloid2048`
  - 直接説問題就好！不要只加好友，很大程度會被當作釣魚

## 🚧請留意！
- 本模組並非官方製作，部分内容由AI輔助翻譯，或有文法錯漏！<br>
- 目前繼續施工優化翻譯中 （超怕不小心用了粵語語法）
- 本模組由 `Coding Band` 的 Voc-夜芷冰 基於 [PEAK Russian Translation](https://thunderstore.io/c/peak/p/RTLC/PEAK_Russian_Translation/) 製作<br>
- 目前僅在 [Thunderstore](https://thunderstore.io/c/peak/p/Vocaloid2048/PEAK_Traditional_Chinese_Translation/) 和 [GitHub](https://github.com/Vocaloid2048/PEAK-zh-tw-Translation) 發佈
- 歡迎到 [`⛰️丨攀爬好手丨peak-chat`](https://discord.com/channels/880921456903618610/1387706673875124344) 一起分享心得哦~<br>
- 部分文字（如護照、地圖名字）因爲字體緣故，只能使用英文（原文）展示，惟可以透過[【非必須】設定替代用字體](#非必須設定替代用字體) 完成設定展示繁體中文

## ✒️翻譯内容放在...
路徑：`%appdata%\com.kesomannen.gale\peak\profiles\<你的設定檔, 預設是Default>\BepInEx\config\zh-tw-voc\Text\`
|檔案名字|分類|
|---|---|
|Achievement.txt|成就、徽章、階級相關|
|Book.txt|求生指南|
|Challenge.txt|攀登挑戰相關|
|Item.txt|物品|
|LoadingAndRepeat.txt|加載頁面、進度式重覆内容|
|Settings.txt|設定頁|
|UI.txt|介面、動作等雜項|
|NeedTPMText.txt.disable|*【非必須】需要使用替代字體的内容<br>按照 [【非必須】設定替代用字體](#非必須設定替代用字體) 完成設定*|

## 💭夜芷冰的呢喃
```
各位安安~ 這裏是夜芷冰 (寫星鐵app的那個)
最近在朋友的推薦下得悉這款酷酷的遊戲
不過目前只有英文版 實在有點卻步...

本來打算直接找找有沒有繁體中文翻譯的模組
結果沒找到QAQ 只找到俄文、日文等等
又不想用簡體中文...

後來想説試試自己做 參考一下REPO中文化模組和俄文模組
左改右改幾次後就發布這個版本了
弄的時候也沒甚麼説甚麼很宏大的理由
單純因爲不方便而做一個方便出來w
之後就可以和朋友一起玩了ww
```

## 💻如何安裝翻譯模組？
### 📦使用 Gale Mod Manager (推薦)
- 請先下載、安裝 [Gale Mod Manager](https://thunderstore.io/c/lethal-company/p/Kesomannen/GaleModManager/)
- 遊戲選擇「PEAK」，按需要自行新增設定檔
- 在 Mod Manager 搜尋 `PEAK Traditional Chinese Translation`
- 按下下載按鈕，等待相依模組＆本翻譯模組下載完成
- 透過 Mod Manager 中的「Launch Game」按鈕啟動遊戲，搞掂！

### 🧰若有需要手動修改設定檔的話...
- 請先在 [GitHub](https://github.com/Vocaloid2048/PEAK-zh-tw-Translation) 下載原始碼
- 下載完成後解壓縮zip檔案
- 開新一個檔案總管，在上面的路徑輸入並前往:
  - Gale Mod Manager: `%appdata%\com.kesomannen.gale\peak\profiles\<你的設定檔, 預設是Default>\`
  - 直接安裝在遊戲：`安裝的SteamLibrary位置\steamapps\common\PEAK\`
- 然後把解壓縮完成的資料夾貼上在這裡
- P.S. 直接安裝在遊戲的話需要留意，你需要自行安裝[BepInEx](https://github.com/BepInEx/BepInEx/releases) 和 [AutoTranslator](https://github.com/bbepis/XUnity.AutoTranslator)

`Folder Tree` of *Gale Mod Manager* (Ref. only)
<details>

```
- peak\profiles
  - <你的設定檔, 預設用Default>
    - BepInEx
      - ...
      - config
        - AutoTranslatorConfig.ini
        - zh-tw-voc
          - Text
            - xxx.txt ...
          - Texture
            - xxx.png ... (目前暫時未打算更新這邊)
        - ...
      - plugins
        - Vocaloid2048-PEAK_Traditional_Chinese_Translation
          - ...
        - ...
```

</details>

## ⛰️截圖
||||
|---|---|---|
|![img1.png](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/img1.png)|![img2.png](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/img2.png)|![img3.png](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/img3.png)|
|![img4.png](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/img4.png)|![img5.png](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/img5.png)|![img6.png](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/IMG/img6.png)|

## ✒️翻譯有問題！
各位大大可以到 [Coding Band](https://discord.gg/uXatcbWKv2) 的  [👾｜問題發表｜questions](https://discord.com/channels/880921456903618610/1067563572865024223) 提出<br>
也歡迎在 [GitHub Repo](https://github.com/Vocaloid2048/PEAK-zh-tw-Translation/) 提交 Issues (先不要PR)<br>
如真的很有需要，上面兩個方法都沒收到回覆，請先加入Discord伺服器，然後在私訊我：`vocaloid2048`
  - 不用問可否問問題！請記得要發信息！不要只加好友哦~
  - 不然的話會當是釣魚

### 遊戲内有些地方是☐☐☐誒
- 請幫忙先確認是否[【非必須】設定替代用字體](#非必須設定替代用字體)所述問題
- 否則，這個可能是因爲這邊字體沒有包含該文字
- 請透過 GitHub Issue / Discord 回報給我，（附上圖片）指出該文字，以便修正，謝謝！

### 用詞、語法問題
- 請透過 GitHub Issue / Discord 回報給我，直接提供修正的部分會更加好~

## 🙏🏻銘謝 Special Thanks
### [✯RTLC Team](https://discord.gg/QahpjZzGkm)
- This mod base on [PEAK Russian Translation](https://thunderstore.io/c/peak/p/RTLC/PEAK_Russian_Translation/)
- Thanks for @DimaLooper and RTLC permitted for this mod

## 📑【非必須】設定替代用字體

- 使用MiSans TC VF 字體作替代用
  - 基於 [教育部常用字4808字.txt](https://github.com/Watermelonnn/ChineseUsefulToolKit/blob/master/%E6%95%99%E8%82%B2%E9%83%A8%E5%B8%B8%E7%94%A8%E5%AD%974808%E5%AD%97.txt) 來製作
  - Unity font asset creator -> AssetsBundle Browser

- 請把 `NeedTPMText.txt.disable` 的 `.disable` （副檔名）刪除
  - 路徑：`%appdata%\com.kesomannen.gale\peak\profiles\<你的設定檔, 預設是Default>\BepInEx\config\zh-tw-voc\Text\NeedTPMText.txt.disable`

### Gale Mod Manager
- 先在 Gale Mod Manager 右鍵剛剛安裝好的繁中翻譯模組
- 選擇 `Open folder` 開啟檔案總管後，應見到一個 `misans_tc_vf_sdf_xxxx` 檔案
  - 這個是字體（TextMeshPro） 檔案，打不開是正常的，不要改動它的名字
- 複製該檔案，並在 `PEAK 遊戲根目錄` 貼上
  - 位置: `安裝的SteamLibrary位置\steamapps\common\PEAK\`
- 透過 Glae Mod Manager 啟動遊戲，看到主頁面Logo上方版本括號內不是☐☐☐即可

### 手動安裝
- 先在本repo按下 `misans_tc_vf_sdf_xxxx` 並下載
- 複製該檔案，並在 `PEAK 遊戲根目錄` 貼上
  - 位置: `安裝的SteamLibrary位置\steamapps\common\PEAK\`
- 啟動遊戲，看到主頁面Logo上方版本括號內不是☐☐☐即可
