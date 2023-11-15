# Kubus

Kubus is Kubernetes security scanner prototype which written in Python Standard Library based on CIS benchmark. This is just demo application for my personal projects.

> ## Disclaimer
> - This tool is non-commercial product
> - This tool doesn't has any relation to CIS products. It's just my personal project for learning [CIS Benchmark for Kubernetes](https://www.cisecurity.org/benchmark/kubernetes)
> - Every rules that reflected on the benchmarking are referencing [CIS Benchmark for Kubernetes](https://www.cisecurity.org/benchmark/kubernetes)
> - To seek the official tools for CIS you can visit this link: [https://www.cisecurity.org/cybersecurity-tools](https://www.cisecurity.org/cybersecurity-tools)


## How to run Kubus on Minikube ?

From upper level of the project directory, we have to compress the directory and copy it to Minikube `/home/docker` directory:

```
tar -cvzf kubus.tgz kubus
minikube cp kubus.tgz /home/docker/kubus.tgz
```

Once it's finished, you need to ssh to Minikube and extract the project:

```
$ minikube ssh
$ pwd
/home/docker
$ tar xzvf kubus.tgz
```

You can start to scan the k8s master node:

```
root@minikube:/home/docker# python3 kubus/kubus.py --dist minikube --target master

...

CIS-KUBE-131: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'terminated-pod-gc-threshold', 'param_value': '10'}' in kube-controller-manager process
CIS-KUBE-132: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'profiling', 'param_value': 'false'}' in kube-controller-manager process
CIS-KUBE-133: PASSED
CIS-KUBE-134: PASSED
CIS-KUBE-135: PASSED
CIS-KUBE-136: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'feature-gates', 'param_value': 'RotateKubeletServerCertificate=true'}' in kube-controller-manager process
CIS-KUBE-137: PASSED
CIS-KUBE-141: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'profiling', 'param_value': 'false'}' in kube-scheduler process
CIS-KUBE-142: PASSED
CIS-KUBE-21-A: PASSED
CIS-KUBE-21-B: PASSED
CIS-KUBE-22: PASSED
CIS-KUBE-23: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'auto-tls', 'param_value': 'false'}' in etcd process
CIS-KUBE-24-A: FAILED. Reason: check_running_process failed to find control value '--peer-client-file' in etcd process
CIS-KUBE-24-B: PASSED
CIS-KUBE-25: PASSED
CIS-KUBE-26: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'peer-auto-tls', 'param_value': 'false'}' in etcd process

==================== Summary ===================
Scan results:
    Passed: 42
    Failed: 28
    Skipped: 8
```

You can also try to scan for worker node:

```
root@minikube:/home/docker# python3 kubus/kubus.py --dist minikube --target worker
CIS-KUBE-411: FAILED. Reason: check_permission failed to find control value '600' in /etc/systemd process
CIS-KUBE-412: PASSED
CIS-KUBE-413: SKIPPED. Reason: Unsupported control
CIS-KUBE-414: SKIPPED. Reason: Unsupported control
CIS-KUBE-415: PASSED
CIS-KUBE-416: PASSED
CIS-KUBE-417: SKIPPED. Reason: Unsupported control
CIS-KUBE-418: SKIPPED. Reason: Unsupported control
CIS-KUBE-419: FAILED. Reason: check_permission failed to find control value '600' in /var/lib/kubelet/config.yaml process
CIS-KUBE-4110: PASSED
CIS-KUBE-421: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'anonymous-auth', 'param_value': 'false'}' in kubelet process
CIS-KUBE-422: PASSED
CIS-KUBE-423: PASSED
CIS-KUBE-424: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'read-only-port', 'param_value': '0'}' in kubelet process
CIS-KUBE-425: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'streaming-connection-idle-timeout', 'param_value': '0'}' in kubelet process
CIS-KUBE-426: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'make-iptables-util-chains', 'param_value': 'true'}' in kubelet process
CIS-KUBE-427: FAILED. Reason: check_running_process failed to find control value '--hostname-override' in kubelet process
CIS-KUBE-428: SKIPPED. Reason: Unsupported control
CIS-KUBE-429-A: PASSED
CIS-KUBE-429-B: PASSED
CIS-KUBE-4210: PASSED
CIS-KUBE-4211: FAILED. Reason: check_running_process failed to find control value '{'param_name': 'feature-gates', 'param_value': 'RotateKubeletServerCertificate=true'}' in kubelet process

==================== Summary ===================
Scan results:
    Passed: 9
    Failed: 10
    Skipped: 5

Scanning on worker node is finish....
```


## How to check new change with pre-commit ?

> Ensure that your project directory is git initialized

Install pre-commit on your environment or virtual environment:

```
$ pip install pre-commit
```

Install pre-commit dependencies within this project directory:

```
$ pre-commit install
```

Once it's finished, run pre-commit before commiting new changes:

```
% pre-commit run --all-files
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
black....................................................................Passed
ruff.....................................................................Passed
bandit...................................................................Passed
```

That means, your commit is safe according to pre-commit pipeline. If your pre-commit pipeline failed, you have to fix the failure one by one before commmiting new changes.
