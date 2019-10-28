# 前后端Restful API
## 1 登录与注册部分
### 1.1 Login
#### 基本请求格式
+ POST请求：
+ 必须包含key为body的入参，所有请求数据包装为JSON格式，并存放到入参body中==，示例如下：
```javascript
xxx/login?body={"username":"admin","password":"123456","captcha":"scfd","rememberMe":1}
```
#### 基本相应格式
```javascript
{
    code: 200,
    data: {
        message: "success"
    }
}
```
code : 请求处理状态

+ 200: 请求处理成功

+ 500: 请求处理失败

+ 401: 请求未认证，跳转登录页

+ 406: 请求未授权，跳转未授权提示页

data.message: 请求处理消息

+ code=200 且 data.message="success": 请求处理成功

+ code=200 且 data.message!="success": 请求处理成功, 普通消息提示：message内容

+ code=500: 请求处理失败，警告消息提示：message内容
