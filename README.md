# coolapk-python


### 开始
```bash
$ git clone https://github.com/Winter-is-comingXK/coolapk-python.git && cd coolapk-python
$ pip install -r requirements.txt
```

### 功能列表
- 每分钟自动更新一次头像，可以配合linux的systemd挂在服务器上使用


### 启动方式
```bash
$ python time_avatar.py
```

### 额外信息
- 本代码从 [ikws4](https://github.com/ikws4/coolapk-python) 处fork而来
- 修复了一个导致无法上传图像的bug
- 将 utils/image.py 中的相对路径换成绝对路径

*对api/api.py 第 75 行修改即可*

**修改前**
```python3
'imgFile': (str(random.random()), image, 'image/jpeg')
```
**修改后**
```python3
'imgFile': ('png.png', image, 'image/jpeg')
```
