mdso_log_paths = {
    'mdso_h0_log_path': '/opt/ciena/bp2/scriptplan_2.1.46-2_0/log/plan-log/',
    'mdso_h1_log_path': '/opt/ciena/bp2/scriptplan_2.1.46-2_1/log/plan-log/',
    'mdso_h2_log_path': '/opt/ciena/bp2/scriptplan_2.1.46-2_2/log/plan-log/',
}
bppath = mdso_log_paths.keys()
for path in bppath:
    print(mdso_log_paths[path])