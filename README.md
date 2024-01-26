# Image_Convert
根据 https://www.freeconvert.com/ 的 API 库制作的一个图片格式修改程序。

A converter that can automatically send requests to https://www.freeconvert.com/ and change image type.

# 需要下载的文件/File to download
**ZH**: 
1. 请下载这里的 **Converter.py** 和 **requirements.txt**
2. 首先使用 pip 下载 requirements.txt 中的内容，然后按照下面的要求进行初始配置。

**EN**: 
1. **Converter.py** and **requirements.txt** are what you may need to download.
2. Use pip to get packages the program requires, and set up the program as follows.

# 快速上手/Get Started
**ZH**:
1. 先去 https://www.freeconvert.com/pricing#api 申请一个免费的 API 密钥，复制保存到文本文档中（文件命名为 **converter_token.txt**），再将该文档拖到程序图标上，程序会自动生成一个 **Converter_Config.json** 文件（切勿移动或修改）。
2. 要改变图片格式时，将原图片拖动到该程序图标上，在弹出的命令框中输入期望转换的目标格式。大概 10 秒左右，就会有一个同名的新图片生成在原始图片的文件夹中。

**EN**:
1. To use it, get an access token at https://www.freeconvert.com/pricing#api (You may select a free API token). Create a file named **converter_token.txt**, paste your API token, and drag the file into the program. A file named **Converter_Config.json** will be generated under the same folder as the program **(Do not move it)**.
2. Whenever you need to transform an image to another type, simply drag it into this program, and type in whatever type you want. Soon you'll find it in the same folder as the image.
