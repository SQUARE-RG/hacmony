import os
import shutil
from dotenv import load_dotenv
from hmbot.device import Device
from hmbot.explorer.llm import LLM
from hmbot.proto import OperatingSystem, ExploreGoal, ResourceType

load_dotenv()

if __name__ == '__main__':
    # 处理output文件夹
    output_dir = 'output'
    if os.path.exists(output_dir):
        # 如果文件夹存在，清空它
        for item in os.listdir(output_dir):
            item_path = os.path.join(output_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(f"已清空 {output_dir} 文件夹")
    else:
        # 如果文件夹不存在，创建它
        os.makedirs(output_dir)
        print(f"已创建 {output_dir} 文件夹")
    
    device = Device('211df697', OperatingSystem.ANDROID)
    llm = LLM(device=device, url=os.getenv("BASE_URL"), model=os.getenv("MODEL"), api_key=os.getenv("API_KEY"))
    llm.explore(key=ExploreGoal.HARDWARE, value=ResourceType.AUDIO, max_steps=20, output_dir='output/')
