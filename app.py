from flask import Flask, render_template, request, session, redirect, url_for
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

 
# 初始化Moonshot AI客户端
client = OpenAI(
    api_key = os.getenv("MOONSOT_API_KEY"),  
    base_url = "https://api.moonshot.cn/v1",
)

app = Flask(__name__)
app.secret_key = 'blockchain_demo_secret_key'  # 为session添加密钥
 
@app.route("/",methods=["GET","POST"])
def index():
    # 清除session中的用户名，确保重新登录
    session.pop('username', None)
    return render_template("index.html")
 
@app.route("/main",methods=["GET","POST"])
def main():
    if request.method == "POST":
        # 如果是POST请求，从表单获取用户名
        username = request.form.get("q")
        if username:
            session['username'] = username
    
    # 获取存储在session中的用户名
    username = session.get('username')
    
    # 如果没有用户名且不是通过表单提交，重定向到首页
    if not username and request.method != "POST":
        return redirect(url_for('index'))
        
    return render_template("main.html", r=username)
 
@app.route("/genAI",methods=["GET","POST"])
def genAI():
    # 确保用户已登录
    if 'username' not in session:
        return redirect(url_for('index'))
        
    q = request.form.get("q")
    
    # 使用Moonshot API替代Google PaLM
    completion = client.chat.completions.create(
        model = "moonshot-v1-8k",
        messages = [
            {"role": "system", "content": "你是一个区块链和智能合约专家，擅长解释相关技术概念。你会为用户提供安全，有帮助，准确的回答。"},
            {"role": "user", "content": q}
        ],
        temperature = 0.3,
    )
    
    # 获取AI回复
    response = completion.choices[0].message.content
    
    return render_template("genAI.html", r=response)

@app.route("/DApp",methods=["GET","POST"])
def DApp():
    # 确保用户已登录
    if 'username' not in session:
        return redirect(url_for('index'))
        
    return render_template("DApp.html")

# 添加一个新的新的路由，用于展示个人信息
@app.route("/info",methods=["GET","POST"])
def info():
    # 确保用户已登录
    if 'username' not in session:
        return redirect(url_for('index'))
        
    return render_template("info.html")

 
if __name__ == "__main__":
    app.run(debug=True)
