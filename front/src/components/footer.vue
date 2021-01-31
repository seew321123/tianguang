<template>
  <div class="b-footer">
  <div class="b-footer-content">
    <div class="footer-item">
      <h1>contact</h1>
      <div>地址：上海市松江区泗砖路600号A座</div>
      <div>电话：400-8827-567</div>
      <div>邮箱：tgxf@hotmail.com</div>
      <div>微信号：shtgxf</div>
    </div>
    <div class="footer-item"><router-link style="color: white;" to="/intro">公司简介</router-link></div>
    <div class="footer-item"><router-link style="color: white;" to="/news">资讯中心</router-link></div>
    <div class="footer-item"><router-link style="color: white;" to="/product">产品中心</router-link></div>
    <div class="footer-item"><router-link style="color: white;" to="/project">工程案例</router-link></div>
    <div class="footer-item"><router-link style="color: white;" to="/contact">联系我们</router-link></div>
  </div>
  </div>
</template>
<script>
export default {
  name: "myfooter",
  data: function () {
    return {
      navList: [
        { id: "index", name: "首页" },
        { id: "intro", name: "公司简介" },
        { id: "news", name: "新闻资讯" },
        { id: "product", name: "产品展示" },
        { id: "project", name: "工程案例" },
        { id: "contact", name: "联系我们" },
      ],
    };
  },
  created() {
  },
  methods: {},
};
</script>
<style>
template {
  display: flex;
  width: 100%;
  justify-content: flex-start;
}
.b-footer{
  margin-top: 80px;
  width: 100%;
  background-color: rgb(58, 58, 58);
  display: flex;
  justify-content: center;
}
.b-footer-content{
  color: rgb(214, 214, 214);
  align-items: center;
  justify-content: space-between;
  width: 1050px;
  height:220px;
  display: flex;
}
</style>
