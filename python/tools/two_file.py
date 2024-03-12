import argparse

parser = argparse.ArgumentParser(
    description="badcase show", formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("--data_path", type=str, default="", help="")
parser.add_argument(
    "--fn_path",
    type=str,
    default=r"D:\invest_cai_80694\Downloads\fn_0.5.txt",
    help="",
)
parser.add_argument(
    "--fp_path",
    type=str,
    default=r"D:\invest_cai_80694\Downloads\fp_0.5.txt",
    help="",
)
parser.add_argument(
    "--out_path",
    type=str,
    default=r"D:\invest_cai_80694\Downloads\result.txt",
    help="",
)
args = parser.parse_args()


def get_list_by_txt(path):
    with open(path, mode="r") as f:
        list = f.readlines()
    return [i.strip("\n") for i in list]


fn_list = get_list_by_txt(args.fn_path)
fp_list = get_list_by_txt(args.fn_path)


def get_three_time_frame(frame_list):
    frame_dic = {}
    for i in frame_list:
        key, value = i.split(",")[0], i.split(",")[-1]
        if int(value) >= 3:
            frame_dic[key] = value
    return frame_dic


fn_dic = get_three_time_frame(fn_list)
fp_dic = get_three_time_frame(fp_list)


def distinct_key_by_dic(dict1, dict2):
    result = {key: str(dict1.get(key, "0")) + "," + str(dict2.get(key, "0")) for key in set(dict1) | set(dict2)}
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))


merged_dict = distinct_key_by_dic(fn_dic, fp_dic)

with open(args.out_path, mode="w") as f:
    f.write("frame_name,fn,fp\n")
    for k, v in merged_dict.items():
        f.write(k + "," + v + "\n")
