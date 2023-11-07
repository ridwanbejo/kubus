from typing import List, Dict, Any

from ..utils.commands import (
    get_dir_owner_group,
    get_dir_permission,
    get_file_owner_group,
    get_file_permission,
    get_running_process,
)
from .benchmarker import KubusCISBenchmark


class KubusScanner:
    def __init__(
        self,
        cni_file_path: str = None,
        distribution: str = "standard",
        node_target: str = "worker",
    ) -> None:
        self.cis_benchmark = KubusCISBenchmark(cni_file_path, distribution)
        self.node_target = node_target

    def run(self) -> None:
        if self.node_target == "master":
            master_node_controls = self.cis_benchmark.get_master_node_controls()

            self.evaluate(master_node_controls)

            print("Scanning on master node is finish....")
        elif self.node_target == "worker":
            worker_node_controls = self.cis_benchmark.get_worker_node_controls()

            self.evaluate(worker_node_controls)

            print("Scanning on worker node is finish....")

        else:
            print("Can't run scanner on unknown node target ...")

    def evaluate(self, controls: Dict[str, Any]) -> None:
        for control in controls:
            if control["control_item"] is None:
                print(
                    "{0}: SKIPPED. Reason: user don't specify the filepath".format(
                        control["control_id"]
                    )
                )
            else:
                control_value = control["control_value"]
                action_operator = control["action_operator"]
                action_result = self.action(control)

                if isinstance(type(action_result), str):
                    if control_value is not None:
                        if action_operator == "in":
                            if control_value in action_result:
                                print("{0}: PASSED".format(control["control_id"]))
                            else:
                                print(
                                    "{0}: FAILED. Reason: {1} failed to find control value '{2}' in {3} process".format(
                                        control["control_id"],
                                        control["action_type"],
                                        control["control_value"],
                                        control["control_item"],
                                    )
                                )
                                # print(action_result)
                        elif action_operator == "not_in":
                            if control_value not in action_result:
                                print("{0}: PASSED".format(control["control_id"]))
                            else:
                                print(
                                    "{0}: FAILED. Reason: {1} found control value '{2}' in {3} process".format(
                                        control["control_id"],
                                        control["action_type"],
                                        control["control_value"],
                                        control["control_item"],
                                    )
                                )
                                # print(action_result)
                        elif action_operator == "in_param":
                            if control_value["param_name"] in action_result:
                                control_param_value = self.get_param(
                                    action_result, control_value["param_name"]
                                )

                                if control_value["param_value"] in control_param_value:
                                    print("{0}: PASSED".format(control["control_id"]))
                                else:
                                    print(
                                        "{0}: FAILED. Reason: {1} failed to find control value '{2}' in {3} process".format(
                                            control["control_id"],
                                            control["action_type"],
                                            control["control_value"],
                                            control["control_item"],
                                        )
                                    )
                                    # print(control_param_value)
                            else:
                                print(
                                    "{0}: FAILED. Reason: Couldn't find param name '{1}' in '{2}' process".format(
                                        control["control_id"],
                                        control_value["param_name"],
                                        control["control_item"],
                                    )
                                )
                                # print(action_result)
                        elif action_operator == "not_in_param":
                            if control_value["param_name"] in action_result:
                                control_param_value = self.get_param(
                                    action_result, control_value["param_name"]
                                )

                                if (
                                    control_value["param_value"]
                                    not in control_param_value
                                ):
                                    print("{0}: PASSED".format(control["control_id"]))
                                else:
                                    print(
                                        "{0}: FAILED. Reason: {1} found control value '{2}' for {3} process".format(
                                            control["control_id"],
                                            control["action_type"],
                                            control["control_value"],
                                            control["control_item"],
                                        )
                                    )
                                    # print(control_param_value)
                            else:
                                print(
                                    "{0}: FAILED. Reason: Couldn't find param name '{1}' in {2} process".format(
                                        control["control_id"],
                                        control_value["param_name"],
                                        control["control_item"],
                                    )
                                )
                                # print(action_result)
                    else:
                        print(
                            "{0}: SKIPPED. Reason: Unsupported control".format(
                                control["control_id"]
                            )
                        )
                elif isinstance(type(action_result), list):
                    eval_result = self.evaluate_multi_line(action_result, control_value)
                    if eval_result is True:
                        print("{0}: PASSED".format(control["control_id"]))
                    else:
                        print(
                            "{0}: FAILED. Reason: Couldn't evaluate multiple control values '{1}' in {2} ".format(
                                control["control_id"],
                                control["control_value"],
                                control["control_item"],
                            )
                        )
                        # print(action_result)

    def evaluate_multi_line(self, action_result: Any, control_value: str) -> bool:
        action_result_count = len(action_result)

        counter = 0
        for result in action_result:
            if result != "":
                if control_value in result:
                    counter = counter + 1

        if counter == action_result_count:
            return True
        else:
            return False

    def action(self, control: Dict[str, Any]) -> Any:
        action_type = control["action_type"]
        control_item = control["control_item"]

        if action_type == "check_permission":
            result = get_file_permission(control_item)
        elif action_type == "check_ownership":
            result = get_file_owner_group(control_item)
        elif action_type == "check_dir_permission":
            result = get_dir_permission(control_item)
        elif action_type == "check_dir_ownership":
            result = get_dir_owner_group(control_item)
        elif action_type == "check_running_process":
            result = get_running_process(control_item)
        else:
            result = None

        return result

    def get_param(self, action_result: Any, param_name: str) -> List[str]:
        params = action_result.split(" --")
        param = [x for x in params if param_name in x][0]

        return param
