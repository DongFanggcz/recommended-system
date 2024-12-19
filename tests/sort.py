import os
import json
from datetime import datetime

# 设置全局变量用于控制调试模式
DEBUG_MODE = False  # 控制是否输出调试信息
INCLUDE_TIMESTAMP_IN_OUTPUT = True  # 控制是否在输出的JSON中包含时间戳
INCLUDE_FILE_PATH = False  # 控制是否在输出的JSON中包含文档的完整路径
OUTPUT_DIRECTORY = "tests/outputs"  # 输出目录的路径

def debug_print(message):
    """根据DEBUG_MODE的值决定是否打印调试信息"""
    if DEBUG_MODE:
        print(message)

# 目标根目录
#root_directory = "tests/documents"
root_directory = "tests/testData/7cacb5ec-1bd8-4b43-93aa-c60f0f16bc43"
# 用于存储所有文件夹uuid及其upload_date的列表
files_info = []

# 遍历根目录中的所有文件夹
for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)

    # 确保是文件夹
    if os.path.isdir(folder_path):
        # 遍历文件夹内的所有 JSON 文件
        for json_file_name in os.listdir(folder_path):
            if json_file_name.endswith(".json"):
                uuid_json_path = os.path.join(folder_path, json_file_name)

                # 确保文件是有效的 JSON 文件
                if os.path.exists(uuid_json_path):
                    with open(uuid_json_path, 'r', encoding='utf-8') as f:
                        try:
                            data = json.load(f)
                            # 提取 upload_date 和 user_uuid 字段
                            upload_date = data.get('upload_date')
                            user_uuid = data.get('user_uuid')

                            if upload_date and user_uuid:
                                # 将 upload_date 转换为 datetime 对象以便排序
                                upload_date_obj = datetime.strptime(upload_date, "%Y-%m-%d %H:%M:%S")
                                # 保存文件夹的 uuid 和对应的上传时间
                                files_info.append((folder_name, upload_date_obj, uuid_json_path))
                                debug_print(f"Read file: {uuid_json_path} with upload_date: {upload_date} and uuid: {folder_name}")
                            else:
                                debug_print(f"Missing 'upload_date' or 'user_uuid' in {uuid_json_path}")
                        except json.JSONDecodeError:
                            debug_print(f"Error decoding JSON in file: {uuid_json_path}")
                else:
                    debug_print(f"File not found: {uuid_json_path}")

# 根据 upload_date 排序，从新到旧
files_info.sort(key=lambda x: x[1], reverse=True)

# 提取排序后的 uuid，并决定是否包括时间戳
if INCLUDE_TIMESTAMP_IN_OUTPUT:
    # 包括时间戳
    if INCLUDE_FILE_PATH:
        # 包括文件路径
        sorted_data = [{"uuid": file[0], "upload_date": file[1].strftime("%Y-%m-%d %H:%M:%S"), "file_path": file[2]} for file in files_info]
    else:
        # 不包括文件路径
        sorted_data = [{"uuid": file[0], "upload_date": file[1].strftime("%Y-%m-%d %H:%M:%S")} for file in files_info]
else:
    # 不包括时间戳，只输出 uuid
    if INCLUDE_FILE_PATH:
        sorted_data = [{"uuid": file[0], "file_path": file[2]} for file in files_info]
    else:
        sorted_data = [file[0] for file in files_info]

# 确保输出目录存在
if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

# 将排序后的数据写入新的 JSON 文件
output_json_path = os.path.join(OUTPUT_DIRECTORY, "sorted_uuids.json")
with open(output_json_path, 'w', encoding='utf-8') as output_file:
    json.dump(sorted_data, output_file, ensure_ascii=False, indent=4)

debug_print(f"Sorted UUIDs have been written to {output_json_path}")
