import uuid
import os
import json

# 创建一个文件夹路径
folder_path = "tests\generatedDate"

# 使用 uuid4() 生成一个随机的 UUID
random_user_uuid =   uuid.uuid4()
random_document_uuid =   uuid.uuid4()
# 获取当前工作目录
current_directory = os.getcwd()
current_directory = os.path.join(current_directory, folder_path)

# 构造新文件夹的路径（使用 UUID 作为文件夹名称）
folder_path = os.path.join(current_directory, str(random_user_uuid))

# 如果文件夹不存在，则创建文件夹
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"文件夹 '{folder_path}' 已创建！")
else:
    print(f"文件夹 '{folder_path}' 已经存在。")

# 创建要写入JSON文件的数据
data = {
    "username": "df123",
    "user_uuid": str(random_user_uuid),
    "upload_date": "2021-01-01 12:00:00",
    "document_name": "markdown.md",
    "public": True,
    "document_uuid": str(random_document_uuid)
}

# 构造JSON文件的路径
json_file_path = os.path.join(folder_path, "data.json")

# 将数据写入到JSON文件
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"JSON文件已生成！文件路径：{json_file_path}")
