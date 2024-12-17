# 🧰 看看別人怎麼做 MLOps 系列文 - `ZenML`

## 😶 專案概述（Project Overview）

```
{截圖}
```

- **名稱：** ZenML
- **定位：** *？？？*
- **開發者：** [ZenML](https://www.zenml.io/company)
- **特點：** *？？？*

## 🚀 系統架構與主要元件

### `架構圖`
![image](https://hackmd.io/_uploads/H1xulOCVkx.png)


### `主要角色`
- **Data Scientist：**
- **ML Engineer：**
- **Platform Engineer：**

### `主要元件`
- **Stack：**
- **Pipeline：**

### `開始前的準備工作`
- **硬體：** CPU、GPU、RAM 需求
- **作業系統：** Linux、Ubuntu
- **相依工具：** 
   - [ZenML Studio（Visual Studio Code Extension）](https://marketplace.visualstudio.com/items?itemName=ZenML.zenml-vscode)- 提供 Stack、Pipeline 和 Server 設定互動的視覺化工具，支援 DAG 檢視、動態配置同步及狀態監控
   - AWS、GCP、Azure
   - kubeflow
- **其它：**
   - [Core concepts](https://docs.zenml.io/getting-started/core-concepts)
   - [Docs](https://docs.zenml.io/)
   - [Starter Guide](https://docs.zenml.io/user-guide/starter-guide)
   - [Blog](https://www.zenml.io/blog)
   - [Road Map](https://community.zenml.io/roadmap)
   - [Quickly spin up MLOps infrastructure using Terraform](https://github.com/zenml-io/mlstacks)

## `價格`
![image](https://hackmd.io/_uploads/SyHtWd0EJg.png)

## 🚀 安裝紀錄（免費版）

### 安裝 Server 在 Local 

```python
docker run -it -d -p 8080:8080 zenmldocker/zenml-server
```

### 安裝 Client 在 Local 
```bash
pip install "zenml==0.71.0"

# 下載範例程式碼
git clone --depth 1 https://github.com/zenml-io/zenml.git && cd zenml/examples/quickstart

# 初始化專案
zenml init
```
### Client 遠端連線
```bash
# 登入 Local Server
zenml login --local 

# 登入 Remote Server
zenml login {zenml_server_url}
```
![image](https://hackmd.io/_uploads/ByUiUcR4kg.png)


## 🚀 操作紀錄

### `Pipeline`

以視覺化方式呈現整個訓練流程，每個區塊包含一小段程式碼，明確定義輸入與輸出，以提升程式的可維護性

<details>
    
![image](https://hackmd.io/_uploads/HJuJs9AEkl.png)
![image](https://hackmd.io/_uploads/SyiLsc041g.png)
    
</details>

### `Register Model`

列出已經訓練、註冊好的 model，方便未來使用

```python
zenml model list # 要用 GUI 的話要 pro 版本
```

![image](https://hackmd.io/_uploads/BJMzMiANJg.png)
    

### `Artifact`

```python
zenml artifact list # 要用 GUI 的話要 pro 版本
```

<details>

> **試用 pro 版本**

![Untitled presentation](https://hackmd.io/_uploads/By72khRVyg.png)

> **Staging & Production**

![Untitled presentation (1)](https://hackmd.io/_uploads/SkZeQ30NJg.png)

</details>

## 🤖 總結（優勢與劣勢分析）

### `優點`
- 好用嗎？
- 界面直覺嗎？
- 社群活躍度？
- 容易擴展？

![image](https://hackmd.io/_uploads/ByVMUoRVJe.png)

### `缺點`
- 部署複雜？
- 須額外搭配其他程式使用？

### `替代專案`