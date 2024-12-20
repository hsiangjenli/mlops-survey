# 🧰 看看別人怎麼做 MLOps 系列文 - `ZenML`

## 😶 專案概述（Project Overview）

![image](https://hackmd.io/_uploads/HkUHyUfSJl.png)


- **名稱：** ZenML
- **定位：** 結合主流雲端（AWS、GCP、Azure）和常見工具（Docker、MLFlow、k8s 等），任君挑選，可簡化流程管理與部署
- **開發者：** [ZenML](https://www.zenml.io/company)
- **特點：** ZenML 是一個專門為 ML 設計的 Pipeline 框架。可與主流雲端服務（AWS、Azure、GCP）一起使用，並將市面上常見的 MLOps 工具（如 MLFlow、Google Cloud Vertex AI、Kubeflow、Airflow 和容器技術）集結在一起，提供一個模組化、高度整合的程式界面，簡化機器學習工作流程的管理和部署

## 🚀 系統架構與主要元件

### `架構圖`

<details>

![image](https://hackmd.io/_uploads/H1xulOCVkx.png)

![](https://cdn.prod.website-files.com/65264f6bf54e751c3a776db1/6530058c5159f040612deed1_continuous-training.gif)

![](https://cdn.prod.website-files.com/65264f6bf54e751c3a776db1/6530058a7a5cc2736c17a76d_batch-inference.gif)

</details>

### `主要角色`
- **Data Scientist（模型開發）：** 讓 DS 可以在地端訓練模型、可以使用裝飾器的方式快速設定 Pipeline、紀錄訓練時的 log
- **ML Engineer（模型部屬）：** ML 的生命週期、確保可結果重現性（不同版本的模型跟資料）、自動部屬模型
- **Platform Engineer（基礎設施與工具整合）：** 提供 DS、ML Engineer 一個很簡單的訓練及部屬環境，讓他們可以專注於自己的專業，免去煩惱訓練環境炸掉、設定模型紀錄工具或雲端資源的使用細節

### `主要元件`
- **Stack：** 包含 Orchestrator、Artifact store、Other
  1. ***Orchestrator***：執行 Pipeline 的工具，例如：Airflow、Kubeflow、Google Cloud VertexAI 等...
  2. ***Artifact store***：保存每個執行步驟下的產物（清洗完的資料、切分完後的訓練測試集、訓練完成的模型）
  3. ***Other***：其他像是存放 Docker Image 的 Container Registries
- **Pipeline：** 就是 Flow Chart（一系列步驟的組合）的程式碼版，主要是目的是希望：(1) 自動化重複性任務，減少手動干預 (2) 提高程式碼的可讀性和維護性

### `開始前的準備工作`
- **硬體：** 無。ZenML 主的賣點是它們的 WebUI，所有訓練都是在 DS 自己的電腦上運作，然後把結果回傳到 ZenML 的 Server 做統一管理跟呈現
- **作業系統：** 無（Linux 為佳）
- **相依工具：** 
   - [ZenML Studio（Visual Studio Code Extension）](https://marketplace.visualstudio.com/items?itemName=ZenML.zenml-vscode)- 提供 Stack、Pipeline 和 Server 設定互動的視覺化工具，支援 DAG 檢視、動態配置同步及狀態監控
   - AWS、GCP、Azure
   - kubeflow
   - Docker
- **其它：**
   - [Core concepts](https://docs.zenml.io/getting-started/core-concepts)
   - [Docs](https://docs.zenml.io/)
   - [ZenML API](https://sdkdocs.zenml.io/0.71.0/)
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

打開 http://localhost:8080 就有了

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

### `Monitor`

使用 MLFlow 來紀錄 training 的 metrics

```python
# setup mlflow 為 tracking 的指令
zenml integration install mlflow -y
zenml model-deployer register mlflow_deployer --flavor=mlflow
zenml experiment-tracker register mlflow_experiment_tracker --flavor=mlflow
```

<details>

> **MLFlow 會紀錄每次的 training 的結果，像是 loss、accuracy、訓練時間等...**

![image](https://hackmd.io/_uploads/ryCsflZHke.png)

> **點進去看會有每次訓練的詳細 log**

![image](https://hackmd.io/_uploads/HklQQee-Hke.png)

</details>

### `Deployment`
- ZenML 並沒有提供部屬的功能，是使用其他開源程式做部屬
- [Model Deployers](https://docs.zenml.io/stack-components/model-deployers/mlflow)
- [MLOps with ZenML and MLFlow: how can we build a model training pipeline? — a practical example](https://medium.com/@kattsonbastos/mlops-with-zenml-and-mlflow-how-can-we-build-a-model-training-pipeline-a-practical-example-6a5f24f5eefc)

### `CLI`
- `zenml stack get` - Find out the name of the currently active stack in ZenML
<!-- - `zenml experiment-tracker flavor list` -  -->


<!-- ### `Error`
```bash
StackValidationError: Step `train_model` requires experiment tracker 'default' which is not configured in the stack 'default'. Available experiment trackers: set().
``` -->

## 🤖 總結（優勢與劣勢分析）

<!-- - 主要的 pipeline 是由 zenML 進行開發 -->
- 但是其它的像是 model tracking、model deployment 都是結合現成的開源專案一起使用

### `優點`
- 可以集結市面上常見的雲端跟開源 MLOps 工具

![image](https://hackmd.io/_uploads/ByVMUoRVJe.png)

### `缺點`
- **部署複雜？** 不會複雜，但是功能都鎖 pro 版本
- **須額外搭配其他程式使用？** 需要，提供很多其他工具，但也是要設定，也是麻煩
- Pipeline 有視覺化的功能，也可以看每個 step 的程式碼，但是點進去不能直接修改程式，小可惜，也沒有比較同個 pipeline 不同程式版本的功能

### `替代專案`
- Kubeflow