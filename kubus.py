from libs.cores.scanner import KubusScanner

scanner = KubusScanner(distribution="minikube")
scanner.run()

print("Scanning is finish....")
