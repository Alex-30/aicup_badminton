# aicup_badminton
(aicup badminton contest)

TEAM_3006

TrackNetV2 與 NFL- MultiPose Estimation using YOLOv8 & Mediapipe 在文件處有放置連結

catch_ori.py：將原始影像加上 TrackNet 出來後的羽球點座標

check_file_is_open.py：在影片轉影像後，檢查影像是否可正常開啟

draw_track.py：在做完 TrackNet 之後，將 X 軸與 Y 軸的羽球軌跡路線畫出來，並標註擊球瞬間點像

event.py：求出羽球及打瞬間的幀數(影格速率)

get_court.py：移動球場影像檔位置

homogeneous.py：用齊次座標求出羽球實際垂直座標

line_detection.py：從原始影像中偵測出球場框架

move_test.py：移動 testing 資料，方便統一做處理

split.py：將原始影片分割數份放入 google cloud platform 中進行羽球追蹤

test_line.py：從 testing 影像中偵測出球場框架

test_video_to_img：處理 testing data，在經過骨架偵測之後，將所需的幀數從影片中取出，過程中包含了結合球場框架與點繪羽球座標

train_video_to_img：處理 training data，在經過骨架偵測之後，將所需的幀數從影片中取出，過程中包含了結合球場框架與點繪羽球座標

using_event.py：執行量產動作，每次都會呼叫 event.py 程式

video_to_img：最一開始將 training data 的所有影片轉成影像

badminton-train.ipynb：模型訓練
