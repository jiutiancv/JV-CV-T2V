import cv2
import os

def extract_first_frame(input_folder):
    # 遍历指定文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith((".mp4", ".avi")):  # 根据需要处理的视频格式调整
            video_path = os.path.join(input_folder, filename)
            cap = cv2.VideoCapture(video_path)

            ret, frame = cap.read()
            if ret:
                # 保存第一帧为PNG格式
                cv2.imwrite(os.path.join('image', f"{filename[:-4]}.png"), cv2.resize(frame[:,512:,:],(64,64)))

            cap.release()
    print("First frames extracted and saved.")

# 调用函数
input_folder = 'video'  # 替换为你视频文件的文件夹路径
extract_first_frame(input_folder)
