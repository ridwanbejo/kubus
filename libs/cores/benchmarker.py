from .controls import KubusCISControls


class KubusCISBenchmark:
    def __init__(self, cni_file_path, distribution):
        self.cni_file_path = cni_file_path
        self.set_config(distribution)
        self.kubus_ci_controls = KubusCISControls()

    def set_config(self, distribution):
        if distribution == "standard":
            self.library_path = "/var/lib"
            self.certs_path = "/etc/kubernetes/pki"
            self.kubelet_service_path = (
                "/etc/systemd/system/kubelet.service.d/kubeadm.conf"
            )
            self.kubelet_config_path = "/etc/kubernetes/kubelet.conf"
            self.kubelet_lib_config_path = "/var/lib/kubelet/config.yaml"
        elif distribution == "minikube":
            self.library_path = "/var/lib/minikube"
            self.certs_path = self.library_path + "/certs"
            self.kubelet_service_path = "/etc/systemd"
            self.kubelet_config_path = "/etc/kubernetes/kubelet.conf"
            self.kubelet_lib_config_path = "/var/lib/kubelet/config.yaml"

    def get_master_node_controls(self):
        etcd_path = self.library_path + "/etcd"

        master_node_audit_controls = self.kubus_ci_controls.get_control_1_1(
            self.cni_file_path, etcd_path, self.certs_path
        )

        master_node_audit_controls += self.kubus_ci_controls.get_control_1_2()
        master_node_audit_controls += self.kubus_ci_controls.get_control_1_3()
        master_node_audit_controls += self.kubus_ci_controls.get_control_1_4()
        master_node_audit_controls += self.kubus_ci_controls.get_control_2()
        master_node_audit_controls += self.kubus_ci_controls.get_control_3_1()
        master_node_audit_controls += self.kubus_ci_controls.get_control_3_2()

        return master_node_audit_controls

    def get_worker_node_controls(self):
        worker_node_audit_controls = self.kubus_ci_controls.get_control_4_1(
            self.kubelet_service_path,
            self.kubelet_config_path,
            self.kubelet_lib_config_path,
        )
        worker_node_audit_controls += self.kubus_ci_controls.get_control_4_2()

        return worker_node_audit_controls
