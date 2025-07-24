# 疑難排解 Troubleshoot by Voc-夜芷冰
![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/troubleshoot/zzz_bug.png)
## 前言
為了方便各位能儘快解決當前遇到的問題<br>
以及無須等待這邊回覆，故此特撰本文，不定期更新<br>
請善用 `Ctrl+F` 搜尋關鍵詞

若有不符合您的問題/多次嘗試後依然不行<br>
**請先加入Discord伺服器**，然後在私信我：`vocaloid2048`<br>
**直接説問題就好！不要只加好友，很大程度會被當作釣魚**

## Mod Manager 啟動相關問題

### `BepInEx preloader not found`
**請確認您的設定檔是否已經安裝了這三個模組**
- 一般情況下，當您安裝繁中翻譯時，它會自動安裝其餘兩個依賴
- 若有遺漏，請自行查找安裝
![](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/troubleshoot/img_default_list.png)


### `Failed to read BepInEx core directory` / 但啟動後沒有發現 `LogOutput.log`
這個有點麻煩，可能是根本連模組都沒啟動到，解決辦法如下：
|步驟|圖片|
|---|---|
|請開啟一個新的檔案總管，輸入這個路徑<br>`%appdata%\com.kesomannen.gale\peak\profiles\<設定檔的名字，一般是Default>\BepInEx`|![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/troubleshoot/img_explorer_navigate.png)|
|接着，請把圖中這三個檔案複製（不要複製資料夾！）|![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/troubleshoot/img_default_profile_explorer.png)|
|然後，請到Steam的收藏庫，右鍵左邊遊戲列表的 `PEAK`，按照圖中選擇|![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/troubleshoot/img_steam_list.png)|
|正確按下後，您應該會開了一個新的檔案總管<br>請把上面説的三個檔案在這邊貼上，**確保不要有 `BepInEx` 資料夾**!|![alt text](https://raw.githubusercontent.com/Vocaloid2048/PEAK-zh-tw-Translation/refs/heads/main/_IMG/troubleshoot/img_peak_steam_explorer.png)|
|回到Mod Launcher，按下Launch game即可||

### 承上，都已經正確安裝，但啟動後依然沒有模組
- 若果確認的話，請把 `BepInEx` 資料夾也複製到上面説的位置
- 然後直接在Steam啟動PEAK

## 舊版本設定替代用字體 (v1.0.6或以前)
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