class KubusCISControls:
    def __init__(self):
        pass

    # DONE
    def get_control_1_1(self, cni_file_path, etcd_path, certs_path):
        control = [
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-111",
                "control_item": "/etc/kubernetes/manifests/kube-apiserver.yaml",
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-112",
                "control_item": "/etc/kubernetes/manifests/kube-apiserver.yaml",
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-113",
                "control_item": "/etc/kubernetes/manifests/kube-controller-manager.yaml",
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-114",
                "control_item": "/etc/kubernetes/manifests/kube-controller-manager.yaml",
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-115",
                "control_item": "/etc/kubernetes/manifests/kube-scheduler.yaml",
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-116",
                "control_item": "/etc/kubernetes/manifests/kube-scheduler.yaml",
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-117",
                "control_item": "/etc/kubernetes/manifests/etcd.yaml",
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-118",
                "control_item": "/etc/kubernetes/manifests/kube-scheduler.yaml",
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-119",
                "control_item": cni_file_path,
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1110",
                "control_item": cni_file_path,
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1111",
                "control_item": etcd_path,
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1112",
                "control_item": etcd_path,
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1113",
                "control_item": "/etc/kubernetes/admin.conf",
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1114",
                "control_item": "/etc/kubernetes/admin.conf",
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1115",
                "control_item": "/etc/kubernetes/scheduler.conf",
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1116",
                "control_item": "/etc/kubernetes/scheduler.conf",
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1117",
                "control_item": "/etc/kubernetes/controller-manager.conf",
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1118",
                "control_item": "/etc/kubernetes/controller-manager.conf",
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1119",
                "control_item": certs_path,
                "control_value": "root root",
                "action_type": "check_dir_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1120",
                "control_item": certs_path + "/*.crt",
                "control_value": "rw-------",
                "action_type": "check_dir_permission",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "control_plane_node_configuration_files",
                "control_id": "CIS-KUBE-1121",
                "control_item": certs_path + "/*.key",
                "control_value": "rw-------",
                "action_type": "check_dir_permission",
                "action_operator": "in",
            },
        ]

        return control

    # DONE
    def get_control_1_2(self):
        control = [
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-121",
                "control_item": "kube-apiserver",
                "control_value": "--anonymous-auth",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-122",
                "control_item": "kube-apiserver",
                "control_value": "--token-auth-file",
                "action_type": "check_running_process",
                "action_operator": "not_in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-123",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "disable-admission-plugins",
                    "param_value": "DenyServiceExternalIPs",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-124-A",
                "control_item": "kube-apiserver",
                "control_value": "--kubelet-client-certificate",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-124-B",
                "control_item": "kube-apiserver",
                "control_value": "--kubelet-client-key",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-125",
                "control_item": "kube-apiserver",
                "control_value": "--kubelet-certificate-authority",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-126",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "authorization-mode",
                    "param_value": "AlwaysAllow",
                },
                "action_type": "check_running_process",
                "action_operator": "not_in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-127",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "authorization-mode",
                    "param_value": "Node",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-128",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "authorization-mode",
                    "param_value": "RBAC",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-129",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "enable-admission-plugins",
                    "param_value": "EventRateLimit",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1210",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "enable-admission-plugins",
                    "param_value": "AlwaysAdmit",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1211",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "enable-admission-plugins",
                    "param_value": "AlwaysPullImages",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1212",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "enable-admission-plugins",
                    "param_value": "SecurityContextDeny",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1213",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "disable-admission-plugins",
                    "param_value": "ServiceAccount",
                },
                "action_type": "check_running_process",
                "action_operator": "not_in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1214",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "disable-admission-plugins",
                    "param_value": "NamespaceLifecycle",
                },
                "action_type": "check_running_process",
                "action_operator": "not_in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1215",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "enable-admission-plugins",
                    "param_value": "NodeRestriction",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1216",
                "control_item": "kube-apiserver",
                "control_value": "--secure-account",
                "action_type": "check_running_process",
                "action_operator": "not_in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1217",
                "control_item": "kube-apiserver",
                "control_value": {"param_name": "profiling", "param_value": "false"},
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1218",
                "control_item": "kube-apiserver",
                "control_value": "--audit-log-path",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1219",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "audit-log-maxage",
                    "param_value": "30",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1220",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "audit-log-maxage",
                    "param_value": "10",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1221",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "audit-log-maxsize",
                    "param_value": "100",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1222",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "request-timeout",
                    "param_value": "200s",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1223",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "service-account-lookup",
                    "param_value": "true",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1224",
                "control_item": "kube-apiserver",
                "control_value": "--service-account-key-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1225-A",
                "control_item": "kube-apiserver",
                "control_value": "--etcd-certfile",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1225-B",
                "control_item": "kube-apiserver",
                "control_value": "--etcd-keyfile",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1226-A",
                "control_item": "kube-apiserver",
                "control_value": "--tls-cert-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1226-B",
                "control_item": "kube-apiserver",
                "control_value": "--tls-private-key-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1227",
                "control_item": "kube-apiserver",
                "control_value": "--client-ca-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1228",
                "control_item": "kube-apiserver",
                "control_value": "--etcd-cafile",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1229",
                "control_item": "kube-apiserver",
                "control_value": "--encryption-provider-config",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1230",  # CIS control is not supported in this version.
                "control_item": "kube-apiserver",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "api_server",
                "control_id": "CIS-KUBE-1231",
                "control_item": "kube-apiserver",
                "control_value": {
                    "param_name": "tls-cipher-suites",
                    "param_value": "TLS_AES_128_GCM_SHA256,TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SH A256,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SH A256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SH A384,TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305,TLS_ECDHE_ECDSA_WITH_CHACHA20_POL Y1305_SHA256,TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_128_C BC_SHA,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_CBC_S HA,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305 ,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256,TLS_RSA_WITH_3DES_EDE_CBC_SHA,TL S_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_128_GCM_SHA256,TLS_RSA_WITH_AES_2 56_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
        ]

        return control

    # DONE
    def get_control_1_3(self):
        control = [
            {
                "control_category": "control_plane_components",
                "control_type": "controller_manager",
                "control_id": "CIS-KUBE-131",
                "control_item": "kube-controller-manager",
                "control_value": {
                    "param_name": "terminated-pod-gc-threshold",
                    "param_value": "10",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "controller_manager",
                "control_id": "CIS-KUBE-132",
                "control_item": "kube-controller-manager",
                "control_value": {"param_name": "profiling", "param_value": "false"},
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "controller_manager",
                "control_id": "CIS-KUBE-133",
                "control_item": "kube-controller-manager",
                "control_value": {
                    "param_name": "use-service-account-credentials",
                    "param_value": "true",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "controller_manager",
                "control_id": "CIS-KUBE-134",
                "control_item": "kube-controller-manager",
                "control_value": "--service-account-private-key-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "controller_manager",
                "control_id": "CIS-KUBE-135",
                "control_item": "kube-controller-manager",
                "control_value": "--root-ca-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "controller_manager",
                "control_id": "CIS-KUBE-136",
                "control_item": "kube-controller-manager",
                "control_value": {
                    "param_name": "feature-gates",
                    "param_value": "RotateKubeletServerCertificate=true",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "controller_manager",
                "control_id": "CIS-KUBE-137",
                "control_item": "kube-controller-manager",
                "control_value": {
                    "param_name": "bind-address",
                    "param_value": "127.0.0.1",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
        ]

        return control

    # DONE
    def get_control_1_4(self):
        control = [
            {
                "control_category": "control_plane_components",
                "control_type": "scheduler",
                "control_id": "CIS-KUBE-141",
                "control_item": "kube-scheduler",
                "control_value": {"param_name": "profiling", "param_value": "false"},
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "control_plane_components",
                "control_type": "scheduler",
                "control_id": "CIS-KUBE-142",
                "control_item": "kube-controller-manager",
                "control_value": {
                    "param_name": "bind-address",
                    "param_value": "127.0.0.1",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
        ]

        return control

    # DONE
    def get_control_2(self):
        control = [
            {
                "control_category": "etcd",
                "control_type": "etcd",
                "control_id": "CIS-KUBE-21-A",
                "control_item": "etcd",
                "control_value": "--cert-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "etcd",
                "control_type": "etcd",
                "control_id": "CIS-KUBE-21-B",
                "control_item": "etcd",
                "control_value": "--key-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "etcd",
                "control_type": "etcd",
                "control_id": "CIS-KUBE-22",
                "control_item": "etcd",
                "control_value": {
                    "param_name": "client-cert-auth",
                    "param_value": "true",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "etcd",
                "control_type": "etcd",
                "control_id": "CIS-KUBE-23",
                "control_item": "etcd",
                "control_value": {"param_name": "auto-tls", "param_value": "false"},
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "etcd",
                "control_type": "etcd",
                "control_id": "CIS-KUBE-24-A",
                "control_item": "etcd",
                "control_value": "--peer-client-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "etcd",
                "control_type": "etcd",
                "control_id": "CIS-KUBE-24-B",
                "control_item": "etcd",
                "control_value": "--peer-key-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "etcd",
                "control_type": "etcd",
                "control_id": "CIS-KUBE-25",
                "control_item": "etcd",
                "control_value": {
                    "param_name": "peer-client-cert-auth",
                    "param_value": "true",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "etcd",
                "control_type": "etcd",
                "control_id": "CIS-KUBE-26",
                "control_item": "etcd",
                "control_value": {
                    "param_name": "peer-auto-tls",
                    "param_value": "false",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "etcd",
                "control_type": "etcd",
                "control_id": "CIS-KUBE-27",  # CIS control is not supported in this version.
                "control_item": "etcd",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
        ]

        return control

    # DONE
    def get_control_3_1(self):
        control = [
            {
                "control_category": "control_plane_configuration",
                "control_type": "authentication_and_authorization",
                "control_id": "CIS-KUBE-311",  # CIS control is not supported in this version.
                "control_item": "kube-apiserver",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_configuration",
                "control_type": "authentication_and_authorization",
                "control_id": "CIS-KUBE-312",  # CIS control is not supported in this version.
                "control_item": "kube-apiserver",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_configuration",
                "control_type": "authentication_and_authorization",
                "control_id": "CIS-KUBE-313",  # CIS control is not supported in this version.
                "control_item": "kube-apiserver",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
        ]

        return control

    # DONE
    def get_control_3_2(self):
        control = [
            {
                "control_category": "control_plane_configuration",
                "control_type": "logging",
                "control_id": "CIS-KUBE-321",
                "control_item": "kube-apiserver",
                "control_value": "--audit-policy-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "control_plane_configuration",
                "control_type": "logging",
                "control_id": "CIS-KUBE-322",  # CIS control is not supported in this version.
                "control_item": "kube-apiserver",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
        ]

        return control

    # DONE
    def get_control_4_1(
        self, kubelet_service_path, kubelet_config_path, kubelet_lib_config_path
    ):
        control = [
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-411",
                "control_item": kubelet_service_path,
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-412",
                "control_item": kubelet_service_path,
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-413",  # CIS control is not supported in this version.
                "control_item": "kube-proxy",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-414",  # CIS control is not supported in this version.
                "control_item": "kube-proxy",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-415",
                "control_item": kubelet_config_path,
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-416",
                "control_item": kubelet_config_path,
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-417",  # CIS control is not supported in this version.
                "control_item": "kubelet",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-418",  # CIS control is not supported in this version.
                "control_item": "kubelet",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-419",
                "control_item": kubelet_lib_config_path,
                "control_value": "600",
                "action_type": "check_permission",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "worker_node_configuration_file",
                "control_id": "CIS-KUBE-4110",
                "control_item": kubelet_lib_config_path,
                "control_value": "root:root",
                "action_type": "check_ownership",
                "action_operator": "in",
            },
        ]

        return control

    # DONE
    def get_control_4_2(self):
        control = [
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-421",
                "control_item": "kubelet",
                "control_value": {
                    "param_name": "anonymous-auth",
                    "param_value": "false",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-422",
                "control_item": "kubelet",
                "control_value": {
                    "param_name": "authorization-mode",
                    "param_value": "AlwaysAllow",
                },
                "action_type": "check_running_process",
                "action_operator": "not_in_param",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-423",
                "control_item": "kubelet",
                "control_value": "--client-ca-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-424",
                "control_item": "kubelet",
                "control_value": {"param_name": "read-only-port", "param_value": "0"},
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-425",
                "control_item": "kubelet",
                "control_value": {
                    "param_name": "streaming-connection-idle-timeout",
                    "param_value": "0",
                },
                "action_type": "check_running_process",
                "action_operator": "not_in_param",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-426",
                "control_item": "kubelet",
                "control_value": {
                    "param_name": "make-iptables-util-chains",
                    "param_value": "true",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-427",
                "control_item": "kubelet",
                "control_value": "--hostname-override",
                "action_type": "check_running_process",
                "action_operator": "not_in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-428",  # CIS control is not supported in this version.
                "control_item": "kubelet",
                "control_value": None,
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-429-A",
                "control_item": "kubelet",
                "control_value": "--tls-cert-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-429-B",
                "control_item": "kubelet",
                "control_value": "--tls-private-key-file",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-4210",
                "control_item": "kubelet",
                "control_value": "--rotate-certificates",
                "action_type": "check_running_process",
                "action_operator": "not_in",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-4211",
                "control_item": "kubelet",
                "control_value": {
                    "param_name": "feature-gates",
                    "param_value": "RotateKubeletServerCertificate=true",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-4212",
                "control_item": "kubelet",
                "control_value": {
                    "param_name": "tls-cipher-suites",
                    "param_value": "TLS_AES_128_GCM_SHA256,TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SH A256,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SH A256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SH A384,TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305,TLS_ECDHE_ECDSA_WITH_CHACHA20_POL Y1305_SHA256,TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_128_C BC_SHA,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_CBC_S HA,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305 ,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256,TLS_RSA_WITH_3DES_EDE_CBC_SHA,TL S_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_128_GCM_SHA256,TLS_RSA_WITH_AES_2 56_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384",
                },
                "action_type": "check_running_process",
                "action_operator": "in_param",
            },
            {
                "control_category": "worker_nodes",
                "control_type": "kubelet",
                "control_id": "CIS-KUBE-4213",
                "control_item": "kubelet",
                "control_value": "--pod-max-pids",
                "action_type": "check_running_process",
                "action_operator": "in",
            },
        ]

        return control

    # UNIMPLEMENTED
    def get_control_5_1(self):
        pass

    # UNIMPLEMENTED
    def get_control_5_2(self):
        pass

    # UNIMPLEMENTED
    def get_control_5_3(self):
        pass

    # UNIMPLEMENTED
    def get_control_5_4(self):
        pass

    # UNIMPLEMENTED
    def get_control_5_5(self):
        pass

    # UNIMPLEMENTED
    def get_control_5_7(self):
        pass
