# Kubus

Kubus is Kubernetes security scanner prototype which written in Python Standard Library based on CIS benchmark. This is just demo application for my personal projects.

> ## Disclaimer
> - This tool is non-commercial product
> - This tool doesn't has any relation to CIS products. It's just my personal project for learning [CIS Benchmark for Kubernetes](https://www.cisecurity.org/benchmark/kubernetes)
> - Every rules that reflected on the benchmarking are referencing [CIS Benchmark for Kubernetes](https://www.cisecurity.org/benchmark/kubernetes)
> - To seek the official tools for CIS you can visit this link: [https://www.cisecurity.org/cybersecurity-tools](https://www.cisecurity.org/cybersecurity-tools)


## How to test Kubus on Minikube ?


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
