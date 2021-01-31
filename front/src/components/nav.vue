<template>
  <div id="b-nav">
    <div class="b-left">
      <img
        class="b-logo"
        src="https://s2.d2scdn.com/f6703e8c-5ef3-4da7-96d1-77d5b5fec96e.png"
        alt="网络错误"
      />
      <div class="b-h1">上海天广消防器材有限公司</div>
    </div>
    <div class="b-right">
      <div
        v-bind:class="[activeTab == item.id ? 'active' : '']"
        v-for="(item, index) in navList"
        v-bind:key="index"
      >
        <router-link :to="item.url">{{ item.name }}</router-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    activeTab: String,
  },
  name: "bNav",
  data: function () {
    return {
      navList: [
        { id: "index", name: "首页", url: "index" },
        { id: "intro", name: "公司简介", url: "intro" },
        { id: "news", name: "新闻资讯", url: "news" },
        { id: "product", name: "产品展示", url: "product" },
        { id: "project", name: "工程案例", url: "project" },
        { id: "contact", name: "联系我们", url: "contact" },
      ],
    };
  },
  created() {
    console.log(this.activeTab);
  },
  methods: {},
};
</script>
<style>
a{ 
    text-decoration:none !important;
    color:#303030; 
}
template {
  display: flex;
  width: 100%;
  justify-content: flex-start;
}
.b-logo {
  width: 100px;
  height: 75px;
}
.b-h1 {
  font-size: 25px;
  font-family: "microsoft yahei";
}

.b-right {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 550px;
}

.b-left {
  display: flex;
  align-items: center;
  justify-content: center;
}

#b-nav {
  display: flex;
  width: 1050px;
  height: 85px;
  align-items: center;
  justify-content: space-between;
}
.active a{
  color: red !important;
}
</style>
