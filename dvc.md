# 🧰 看看別人怎麼做 MLOps 系列文 - `DVC`

## 😶 專案概述（Project Overview）

![image](https://hackmd.io/_uploads/rkYOvSXPye.png)

- **名稱**：DVC（Data Version Control）
- **定位**：資料族譜 + 實驗追蹤 [^ithelp_dvc_1]
- **開發者**：*???*
- **特點**：像是使用 git 一樣做 data 的版本控制 [^ithelp_dvc_1]
- **其它**： 
- **文件**：
   - https://dvc.org/doc
   - https://github.com/iterative/dvc
   - [DVC 使用指南：常用术语](https://juejin.cn/post/7064363665138384910)

## 🚀 系統架構與主要元件

### `架構圖`

### `主要元件`

### `開始前的準備工作`

- **硬體**：無
- **作業系統**：無
- **相依工具**：git、VS-Code、DataChain（Optional）

## 🚀 安裝紀錄

### `DVC 安裝`
```shell
pip install dvc
```

> ![image](https://hackmd.io/_uploads/ry65FxIP1e.png)
> 額外支援像是 AWS、Azure、GCP 甚至是 Hadoop
> - **OSS (Object Storage Service)**：阿里巴巴
> - **WebDAV (Web Distributed Authoring and Versioning)**：透過 HTTP/HTTPS 訪問和管理遠端伺服器上的文件，例如：Google Drive

### `VScode Extension`
![image](https://hackmd.io/_uploads/r1SaM8Qwye.png)


### `初始化專案`
執行以下指令後會產生以下三個檔案 `.dvc/.gitignore`、`.dvc/config`、`.dvcignore`

```shell
git init
dvc init 
```

### `下載示範資料`

```shell
dvc get https://github.com/iterative/dataset-registry \
          get-started/data.xml -o data/data.xml
```

## 🚀 操作紀錄

### `追蹤 data 指令`
1. 原本在 `data` 這個資料夾底下只有 `data.xml`
1. 在執行完 `dvc add` 之後會額外產生 `.gitignore` 跟 `data.xml.dvc` 兩個檔案

```shell
dvc add data/data.xml # 產生追蹤檔
git add data/data.xml.dvc data/.gitignore # 使用 git 追蹤
```

```yaml
# data.xml.dvc

outs:
- md5: 22a1a2931c8370d3aeedd7183606fd7f
  size: 14445097
  hash: md5
  path: data.xml
```

### `設定保存不同版本 data 的位置`
```shell
dvc remote add -d mylocal /tmp/dvcstore
```

```shell
dvc push # 把檔案 push 上去
dvc pull # 把檔案 pull 下來
```

```shell
ls /tmp/dvcstore # 就可以看到檔案出現在這裡
```

### `Pipeline stages`
- https://dvc.org/doc/command-reference/stage

```shell
dvc stage add -n <stage_name> -d <dependency> -o <output> <command>
```

```shell
dvc stage add -n "Transform English Letter to upper Case" \
    -d "test_2.txt" \
    -d "test_dvc.py" \
    -o "processed_test_2.txt" \
    python test_dvc.py --file test_1.txt
```

會產生一個 dvc.yaml 的檔案

```yaml
# dvc.yaml
stages:
  Transform English Letter to upper Case:
    cmd: python test_dvc.py --file test_1.txt
    deps:
    - test_2.txt
    - test_dvc.py
    outs:
    - processed_test_2.txt
```

執行 `dvc.yaml` 檔案

```shell
dvc repro
```

```javascript
(base) hsiangjenli@acer:~/Downloads/github/test-dvc$ dvc repro
Running stage 'Transform English Letter to upper Case':                                                                                                                            
> python test_dvc.py --file test_2.txt
Generating lock file 'dvc.lock'                                                                                                                                                    
Updating lock file 'dvc.lock'

To track the changes with git, run:

        git add dvc.lock

To enable auto staging, run:

        dvc config core.autostage true
Use `dvc push` to send your updates to remote storage.
```

按照上面指示，`git add dvc.lock` 跟 `dvc config core.autostage true`

```shell
dvc dag # 呈現所有 pipeline
```

## 🤖 總結（優勢與劣勢分析）

### `優點`
- 好用嗎？
- 界面直覺嗎？
- 社群活躍度？
- 容易擴展？

### `缺點`
- 部署複雜？
- 須額外搭配其他程式使用？
   - git、vscode

### `替代專案`

[^ithelp_dvc_1]: Data Version Control(DVC)使用概述
https://ithelp.ithome.com.tw/articles/10229847

[^aif_mlops]: MLOps 工具介紹（二）：常見的資料管理工具
https://edge.aif.tw/mlops-data-management-tools/