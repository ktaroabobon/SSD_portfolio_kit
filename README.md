SSD_portfolio_kit
====

SSD判定のアプリです。犬と猫の種類が判定できます。

### 例）

![predict_dog01](https://user-images.githubusercontent.com/52523218/113596446-481afb80-9675-11eb-959c-885a1fcc617c.jpg)

また、判定可能な犬と猫の種類は以下の通りです。

```
犬種（計２５種）
・american_bulldog（アメリカン・ブルドッグ）
・american_pit_bull_terrier（アメリカン・ピット・ブル・テリア）
・basset_hound（バセット・ハウンド）
・beagle（ビーグル）
・boxer（ボクサー）
・chihuahua（チワワ）
・english_cocker_spaniel（イングリッシュ・コッカー・スパニエル）
・english_setter（イングリッシュ・セター） 
・german_shorthaired（ジャーマン・ショートヘアード・ポインター）
・great_pyrenees（グレート・ピレニーズ）
・havanese（ハバニーズ）
・japanese_chin（狆）
・keeshond（キースホンド）
・leonberger（レオンベルガー） 
・miniature_pinscher（ミニチュア・ピンシャー）
・newfoundland（ニューファンドランド）
・pomeranian（ポメラニアン）
・pug（パグ）
・saint_bernard（セント・バーナード）
・samoyed（サモエド）
・scottish_terrier（スコティッシュ・テリア）
・shiba_inu（柴犬）
・staffordshire_bull_terrier（スタッフォードシャー・ブル・テリア）
・wheaten_terrier（ソフトコーテッド・ウィートン・テリア）
・yorkshire_terrier（ヨークシャー・テリア）

猫種（計１２種）
・Abyssinian（アビシニアン）
・Bengal（ベンガル）
・Birman（バーマン） 
・Bombay（ボンベイ） 
・British_Shorthair（ブリティッシュ・ショートヘア）
・Egyptian_Mau（エジプシャン・マウ）
・Maine_Coon（メインクーン）
・Persian（ペルシャ）
・Ragdoll（ラグドール）
・Russian_Blue（ロシアンブルー）
・Siamese（シャム）
・Sphynx（スフィンクス） 
```

## Installation

```
git clone https://github.com/ktaroabobon/SSD_portfolio_kit.git
cd SSD_portfolio
pip install -r requirements.txt
```

## Usage

1. まずmedia/upload/に対象の画像データを配置します。（対応している拡張子はjpg, jpeg, pngのみです。）

```tree
media
 ├── predict
 └── upload
     └── dog01.jpg

```

2. setting.iniファイルを開き、image項目内のfile_nameを対象データ名に設定します。（拡張子まで指定してください。）

```settings.ini
[image]
file_name = dog01.jpg
```

3. プロジェクトディレクトリ下に移動してmain.pyを実行します。

```
cd SSD_portfolio_kit
python main.py
```

4. Window上に表示もしくは/media/predict下に予測画像が配置されていれば成功です。

```tree
media
 ├── predict
 │   └── dog01_predict.jpg
 └── upload
     └── dog01.jpg

```

## Author

・作成者：[ktaroabobon](https://github.com/ktaroabobon)
