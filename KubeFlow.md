# 🧰 看看別人怎麼做 MLOps 系列文 - `Kubeflow`

## 😶 專案概述（Project Overview）

![image](https://hackmd.io/_uploads/B1N2Ldk8ke.png)

- **名稱：** Kubeflow
- **定位：** *這個專案的核心目標，端到端 MLOps 平台、模型追蹤、部署等功能*
- **開發者：** *???*
- **特點：** *一句話*
- **其它：** 
   - [minikube-docs](https://minikube.sigs.k8s.io/docs/)
   - [Kubectl 命令技巧大全](https://jimmysong.io/book/kubernetes-handbook/cli/kubectl-cheatsheet/)
   - https://s.itho.me/summit/2020/k8s/slides/2.%20%E4%BB%A5%20kubeflow%20%E9%80%B2%E8%A1%8C%20pytorch%20%E5%A4%A7%E8%A6%8F%E6%A8%A1%20AI%20%E8%A8%93%E7%B7%B4.pdf
   - https://erhwenkuo.github.io/kubeflow/env/
   - https://www.youtube.com/playlist?list=PLIivdWyY5sqLS4lN75RPDEyBgTro_YX7x
   - [从零搭建机器学习平台Kubeflow](https://blog.csdn.net/yanqianglifei/article/details/128432784)
   - [Kubernetes Intro](https://hackmd.io/@ltony1024/H1pGiet7L)
   - [How to Install Minikube on Ubuntu 18.04 / 20.04](https://phoenixnap.com/kb/install-minikube-on-ubuntu)
   - [Configure a Kubernetes Cluster with Control Plane, Worker Nodes, and Load Balancer with Ingress Controller 🚀](https://dev.to/katherine_lin_f690f55bbf7/configure-a-kubernetes-cluster-with-control-plane-worker-nodes-and-load-balancer-with-ingress-controller-2obl)

## 🚀 系統架構與主要元件

### `架構圖`

![](https://www.kubeflow.org/docs/started/images/kubeflow-architecture.drawio.svg)

### `主要元件（共 8 樣）`

1. **KServe** - Serverless Inferencing on Kubernetes
1. **Katib** - Hyperparameters optimization framework
1. **Model Registry** - Tracks and manages ML models for versioning and reproducibility
1. **Notebooks** - Support for JupyterLab, RStudio, and Visual Studio Code (code-server)
1. **Pipelines** - 將機器學習的各個步驟自動化跟可視化
1. **Spark Operator** - 運作 Spark Cluster
1. **Training Operator** - Fine-tuning and scalable distributed training of ML
1. **MPI Operator** - 使用 Message Passing Interface 來達成分散式運算

> - **Training Operator** 跟 **MPI Operator** 差在哪裡？
> - 哪種好？各自的使用場景？

### `開始前的準備工作`

- **硬體：** CPU、GPU、RAM 需求
- **作業系統：** Linux、Ubuntu、CentOS
- **相依工具：** Kubernetes、Kubectl、Docker、VirtualBox、Kubeadm（Minikube、GKE、EKS、AKS 免安裝）、Kubelet（Minikube、GKE、EKS、AKS 免安裝）、Kustomize

## 🚀 安裝紀錄

### `🔨 Kubernetes`

#### ⚙️ Minikube
> - 用於在本地機器上快速啟動和運行一個 Kubernetes 集群，便於開發和測試
> - 會使用到 VirtualBox

```shell
sudo apt-get update -y
sudo apt-get install curl
sudo apt-get install apt-transport-https
```

**安裝 VirtualBox 指令**
```shell
sudo apt install virtualbox virtualbox-ext-pack
```

**安裝 Minikube 指令**
```shell
wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo cp minikube-linux-amd64 /usr/local/bin/minikube
sudo chmod 755 /usr/local/bin/minikube
```

**確認 Minikube 的版本**
```shell
minikube version
```

![image](https://hackmd.io/_uploads/r1K4G1l8yl.png)


#### ⚙️ Kubectl
> 操作 Kubernetes 集群的主要工具

**安裝 Kubectl 的指令**

```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

**確認 Kubectl 的版本**
```shell
kubectl version -o json
```

![image](https://hackmd.io/_uploads/H1gBm1eIJx.png)

**安裝 Metrics Server**

```shell
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

```shell
# 調整設定
  template:
    metadata:
      creationTimestamp: null
      labels:
        k8s-app: metrics-server
    spec:
      containers:
      - args:
        - --cert-dir=/tmp
        - --secure-port=443
        - --kubelet-insecure-tls
        - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
        - --kubelet-use-node-status-port
        - --metric-resolution=15s
```

#### ⚙️ Kustomize
> 用於配置管理的輔助工具，增強了 YAML 文件的可重用性和靈活性

```shell
sudo snap install kustomize 
```

### `🔨 Kubeflow`

```shell
git clone https://github.com/kubeflow/manifests.git
cd manifests
while ! kustomize build example | kubectl apply -f -; do echo "Retrying to apply resources"; sleep 10; done
```

error

<details>
    
```shell
(base) hsiangjenli@acer:~/Desktop/manifests$ kubectl port-forward --address 0.0.0.0 svc/istio-ingressgateway -n istio-system 8080:80
error: unable to forward port because pod is not running. Current status=Pending
```

```shell
# 查看是什麼原因造成啟動失敗（CPU、RAM）
kubectl describe pod istio-ingressgateway-57c8b6474d-8cqfx -n istio-system
```
![image](https://hackmd.io/_uploads/BypbOEZIkl.png)

RAM 不足，改天嘗試把資源做調整。

```shell
docker pull docker.io/istio/proxyv2:1.23.2
minikube image load docker.io/istio/proxyv2:1.23.2
kubectl delete pod istio-ingressgateway-57c8b6474d-bxfml -n istio-system
kubectl get pods -n istio-system
```

</details>

```shell
Error from server (Invalid): error when creating "STDIN": CustomResourceDefinition.apiextensions.k8s.io "inferenceservices.serving.kserve.io" is invalid: metadata.annotations: Too long: must have at most 262144 bytes
```

**`kserve 沒安裝到`**

如果 Error log 出現 `InferenceService.serving.kserve.io`

<details>
    
- https://kserve.github.io/website/master/admin/serverless/serverless/#4-install-kserve
- https://github.com/kserve/kserve/issues/3487

```shell!
{"level":"error","ts":"2025-01-02T01:29:00Z","logger":"controller-runtime.source.EventHandler","msg":"if kind is a CRD, it should be installed before calling Start","kind":"InferenceService.serving.kserve.io","error":"no matches for kind \"InferenceService\" in version \"serving.kserve.io/v1beta1\"","stacktrace":"sigs.k8s.io/controller-runtime/pkg/internal/source.(*Kind[...]).Start.func1.1\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.18.5/pkg/internal/source/kind.go:71\nk8s.io/apimachinery/pkg/util/wait.loopConditionUntilContext.func1\n\t/go/pkg/mod/k8s.io/apimachinery@v0.30.4/pkg/util/wait/loop.go:53\nk8s.io/apimachinery/pkg/util/wait.loopConditionUntilContext\n\t/go/pkg/mod/k8s.io/apimachinery@v0.30.4/pkg/util/wait/loop.go:54\nk8s.io/apimachinery/pkg/util/wait.PollUntilContextCancel\n\t/go/pkg/mod/k8s.io/apimachinery@v0.30.4/pkg/util/wait/poll.go:33\nsigs.k8s.io/controller-runtime/pkg/internal/source.(*Kind[...]).Start.func1\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.18.5/pkg/internal/source/kind.go:64"}
```

```shell!
{"level":"error","ts":"2025-01-02T01:51:24Z","logger":"setup","msg":"unable to create controller","v1alpha1Controllers":"LocalModel","error":"no matches for kind \"InferenceService\" in version \"serving.kserve.io/v1beta1\"","stacktrace":"main.main\n\t/go/src/github.com/kserve/kserve/cmd/localmodel/main.go:147\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:271"}
```

```shell
# 檢查有沒有裝到，沒 output 就是沒裝到，要記得安裝
kubectl get crd | grep "inferenceservice"

# 安裝 cmd
kubectl apply --server-side -f https://github.com/kserve/kserve/releases/download/v0.14.1/kserve.yaml
```

</details>

**`RBAC 權限問題`**
> 看到 `forbidden` 高機率是 RBAC 權限不足
```shell!
failed to list *v1beta1.InferenceService: inferenceservices.serving.kserve.io is forbidden: User "system:serviceaccount:kubeflow:kserve-controller-manager" cannot list resource "inferenceservices" in API group "serving.kserve.io" at the cluster scope
```

<details>

```shell
# 確認權限，如果沒有出現任何權限設置代表要重新設定
kubectl get clusterrolebinding -n kubeflow | grep kserve-controller-manager
```
    
```yaml
# kserve-rbac.yaml

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kserve-controller-manager-role
rules:
- apiGroups: ["serving.kserve.io"]
  resources: ["inferenceservices", "trainedmodels", "inferencegraphs"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["networking.istio.io"]
  resources: ["virtualservices"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["serving.knative.dev"]
  resources: ["services"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: [""]
  resources: ["pods", "services", "endpoints", "events", "configmaps", "secrets"]
  verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kserve-controller-manager-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kserve-controller-manager-role
subjects:
- kind: ServiceAccount
  name: kserve-controller-manager
  namespace: kubeflow
```
    
```shell
# 執行權限設定
kubectl apply -f kserve-rbac.yaml

# 刪掉舊的 pod，會自動重啟
kubectl delete pod -n kubeflow -l app=kserve
```
    
</details>

**`MySQL database was not initialized`**

```shell!
WARNING: Logging before InitGoogleLogging() is written to STDERR
E0106 06:55:41.786863     1 mysql_metadata_source.cc:174] MySQL database was not initialized. Please ensure your MySQL server is running. Also, this error might be caused by starting from MySQL 8.0, mysql_native_password used by MLMD is not supported as a default for authentication plugin. Please follow <https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-default-authentication-plugin-considerations/>to fix this issue.
F0106 06:55:41.788921     1 metadata_store_server_main.cc:555] Check failed: absl::OkStatus() == status (OK vs. INTERNAL: mysql_real_connect failed: errno: , error:  [mysql-error-info='']) MetadataStore cannot be created with the given connection config.
*** Check failure stack trace: ***
```

<details>

```shell
# 找出跟 mysql 有關的 pod
kubectl get pods --all-namespaces | grep mysql
```
    
```shell
docker pull gcr.io/ml-pipeline/mysql:8.0.26
```
    
</details>

**`ml-pipeline`**

```shell
Error: failed to sync configmap cache: timed out waiting for the condition
```

<details>
    
- https://github.com/kubeflow/manifests/issues/2436

```shell
# 確認是否有少配置
kubectl describe configmap pipeline-api-server-config -n kubeflow
```
    
```shell
# 若有缺少則需要把必要配置加上，下面開啟配置
kubectl edit configmap pipeline-api-server-config-dc9hkg52h6 -n kubeflow
```

```yaml
data:
  DEFAULTPIPELINERUNNERSERVICEACCOUNT: default-editor
  MULTIUSER: "true"
  VISUALIZATIONSERVICE_NAME: ml-pipeline-visualizationserver
  VISUALIZATIONSERVICE_PORT: "8888"
  bucketName: mlpipeline
  dbHost: mysql.kubeflow.svc.cluster.local
  dbPort: "3306"
  pipelineDb: mlpipeline
```

```shell
kubectl rollout restart deployment ml-pipeline -n kubeflow
```

</details>


## 🚀 操作紀錄

### Minikube 指令

**`啟動/暫停/關閉/進入環境 MiniKube`**
```shell
# 啟動
minikube start
minikube start --memory=4096 --cpus=2

# 暫停
minikube pause

# 關閉
minikube stop

# 進入
minikube ssh

# 刪除
minikube delete
```
![image](https://hackmd.io/_uploads/HJJjB1eIyx.png)

**`查看 Minikube 的附加元件`**
```shell
minikube addons list
```

**`啟用/停用 Minikube 的附加元件`**
```shell
minikube addons enable {元件名稱}
minikube addons disable {元件名稱}
```

<details>

![image](https://hackmd.io/_uploads/SkDnK--Lyl.png)
    
</details>

**`開啟 Dashboard`**

> Dashboard 是一個輔助工具，用於圖形化地管理和監控 k8s 集群，但不是必須的

```shell
minikube dashboard --url
```

![image](https://hackmd.io/_uploads/ryTA3b-81e.png)
![image](https://hackmd.io/_uploads/rJB_A-WU1e.png)


### Kubectl 指令

**`設定 Kubectl 指令自動補全`**
```shell
source <(kubectl completion bash)
source <(kubectl completion zsh)
```

**`查看 kubectl 配置檔案`**

```python
kubectl config view
```
<details>

```yaml
# Output: 
apiVersion: v1
clusters: # 群集列表（可用的 k8s 集群）
- cluster:
    # API Server 端的憑證
    certificate-authority: /home/hsiangjenli/.minikube/ca.crt
    extensions:
    - extension:
        last-update: Tue, 31 Dec 2024 09:27:26 CST
        provider: minikube.sigs.k8s.io
        version: v1.34.0
      name: cluster_info
    server: https://192.168.49.2:8443
  name: minikube
contexts: # 上下文（連接 Kubernetes 集群的配置訊息）
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Tue, 31 Dec 2024 09:27:26 CST
        provider: minikube.sigs.k8s.io
        version: v1.34.0
      name: context_info
    namespace: default
    user: minikube
  name: minikube
current-context: minikube # 目前使用的上下文
kind: Config
preferences: {}
users: # 使用者憑證
- name: minikube
  user:
    # 用戶端的憑證
    client-certificate: /home/hsiangjenli/.minikube/profiles/minikube/client.crt
    client-key: /home/hsiangjenli/.minikube/profiles/minikube/client.key
```

</details>

**`查看 cluster 狀態，了解是否正常運行`**

```shell
kubectl cluster-info
```

<details>

<!--  -->
- 包含 Control Plane（控制平面）跟 Core 服務（例如：DNS）
<!--  -->
```shell
Kubernetes control plane is running at https://192.168.49.2:8443
CoreDNS is running at https://192.168.49.2:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

</details>

**`查看 k8s 節點資訊`**

節點分成 **Control Plane（過去叫做 Master Nodes）** 跟 **Worker Nodes**

```shell
# 列出所有節點
kubectl get nodes
```

```shell
# 節點詳細資訊
kubectl describe node minikube
```

<details>

```shell
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   18h   v1.31.0
```

![image](https://hackmd.io/_uploads/H1xKV--L1e.png)
    
</details>

**`查看節點 CPU、RAM 使用狀態`**
```shell
kubectl describe nodes
```

<details>

![image](https://hackmd.io/_uploads/Hk8OVzYU1x.png)
    
</details>

**`查看 k8s 中所有 pod`**
```shell
kubectl get pods -A
```

> Pod 是 k8s 中可以部屬的最小單位

<details>

![image](https://hackmd.io/_uploads/SyswGVZLJg.png)

</details>

**`查看特定 pod 的狀態或 log`**

```shell
# 狀態
kubectl describe pod {pod 的名稱} -n {namespace}

# log
kubectl logs {pod 的名稱} -c manager -n {namespace}
kubectl logs {pod 的名稱} -c container -n {namespace}
```

**`修改設定`**
```shell
kubectl edit deployment {pod 前綴名稱} -n {namespace}
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

### `替代專案`

<!-- ## 參考資料
- [以 kubeflow 進行 pytorch 大規模 AI 訓練](https://s.itho.me/summit/2020/k8s/slides/2.%20%E4%BB%A5%20kubeflow%20%E9%80%B2%E8%A1%8C%20pytorch%20%E5%A4%A7%E8%A6%8F%E6%A8%A1%20AI%20%E8%A8%93%E7%B7%B4.pdf)
 -->
