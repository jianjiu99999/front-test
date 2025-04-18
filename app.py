from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # 轮播图图片（放在 static/img/carousel/ 下）
    carousel_images = [
        'img/carousel/img1.jpg',
        'img/carousel/img2.jpg',
        'img/carousel/img3.jpg'
    ]

    # 产品列表（放在 static/img/products/ 下）
    products = [
        {'name': '产品A', 'image': 'img/products/products1.jpg', 'desc': '产品A的简要描述'},
        {'name': '产品B', 'image': 'img/products/products2.jpg', 'desc': '产品B的简要描述'},
        {'name': '产品C', 'image': 'img/products/products3.jpg', 'desc': '产品C的简要描述'},
    ]

    company_intro = (
        "安徽海慧供应链科技有限公司是由海水泥(600585)、海型材(000619)、海爆信息技术公司等联合发起成立的，"
        "服务于海螺产业链供应链的科技型公司。海营供应链公司同时建设海中宝网络货运平台，"
        "以智营物流供应链平台为基础，在水泥行业开展网络货运业务和增值服务业务。"
    )

    footer_info = {
        'address': '安徽省芜湖市鸠江区安徽芜湖鸠江经济开发区电子产业园综合楼',
        'postcode': '241060',
        'tel': '0553-8396750',
        'mobile': '13799784529',
        'email': '348837935@qq.com',
        'copyright': (
            '© 2025 All Rights Reserved  安徽海慧供应链科技有限公司 版权所有 皖ICP备2020021255号'
        )
    }

    return render_template('index.html',
                           title='海慧供应链',
                           carousel_images=carousel_images,
                           products=products,
                           company_intro=company_intro,
                           footer=footer_info)

if __name__ == '__main__':
    app.run(debug=True)