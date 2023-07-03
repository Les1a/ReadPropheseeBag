from metavision_core.event_io import EventsIterator
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='MetavisionRAW转换为CSV和TXT文件.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input_dir', default="./data", required=False, help='MetavisionRAW文件路径')
    parser.add_argument('-c', '--csv_output_dir', default="./csv", required=False, help='CSV输出文件夹路径')
    parser.add_argument('-t', '--txt_output_dir', default="./txt", required=False, help='TXT输出文件夹路径')
    parser.add_argument('-s', '--start_ts', type=int, default=0, help='起始时间戳（微秒）')
    parser.add_argument('-d', '--max_duration', type=int, default=1e6 * 60, help='最大持续时间（微秒）')
    parser.add_argument('--delta_t', type=int, default=1000000, help='事件片段的时间间隔（微秒）')
    return parser.parse_args()


def raw_to_csv(input_dir, output_folder, start_ts, max_duration, delta_t):
    """将MetavisionRAW格式转换为CSV格式"""
    for filename in os.listdir(output_folder):
        if filename.endswith(".raw"):
            input_path = os.path.join(input_dir, filename)
            if os.path.isfile(input_path):
                output_file = os.path.join(output_folder, os.path.basename(input_path)[:-4] + ".csv")
            else:
                raise TypeError(f'Fail to access file: {input_path}')

            mv_iterator = EventsIterator(input_path=input_path, delta_t=delta_t, start_ts=start_ts, max_duration=max_duration)

            with open(output_file, 'w') as csv_file:
                for evs in mv_iterator:
                    for (x, y, p, t) in evs:
                        csv_file.write("%d,%d,%d,%d\n" % (x, y, p, t))

            if os.path.exists(output_file):
                print(f"save CSV：{output_file}")
            else:
                print(f"fail CSV：{output_file}")


def csv_to_txt(input_folder, output_folder):
    """将CSV格式转换为TXT格式"""
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            # 构建输入文件路径和输出文件路径
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename[:-4] + ".txt")

            # 读取CSV文件并将其转换为TXT文件
            with open(input_path, "r") as csv_file, open(output_path, "w") as txt_file:
                for line in csv_file:
                    txt_file.write(line.replace(",", " "))

            # 确认输出文件是否存在
            if os.path.exists(output_path):
                print(f"save TXT：{output_path}")
            else:
                print(f"fail TXT：{output_path}")


def main():
    args = parse_args()
    raw_to_csv(args.input_dir, args.csv_output_dir, args.start_ts, args.max_duration, args.delta_t)
    csv_to_txt(args.csv_output_dir, args.txt_output_dir)


if __name__ == "__main__":
    main()
