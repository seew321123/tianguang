<template>
  <div class="b-intro">
    <div class="b-title">
      <div class="b-h1">公司简介</div>
      <div class="b-h2">ABOUT US</div>
    </div>
    <div v-html='config.aboutUs'></div>
    <el-button style="margin-top:20px;width:100px"><router-link to="/intro">查看更多</router-link></el-button>
  </div>
</template>
<script>
export default {
  name: "intro",
  data: function () {
    return {
      config: {},
      load_config_url: "/api/load_config",
    };
  },
  created() {
      this.load_config()
  },
  methods: {
        load_config() {
      var _this = this;
      _this.$axios
        .get(_this.load_config_url) // 还可以直接把参数拼接在url后边
        .then(function (res) {
          console.log("res", res);
          _this.config = res.data.object;
          _this.fileList.push({
            name: _this.config.headerImage,
            url: _this.config.headerImage,
            uid: new Date().getTime(),
            status: "success",
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
<style>
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

.b-h2{
  font-size: 15px;
  font-weight: bold;
  color: rgb(156, 156, 156);
}

#b-nav {
  display: flex;
  width: 1050px;
  height: 85px;
  align-items: center;
  justify-content: space-between;
}
.active div{
    color:red;
}

.b-intro{
  margin-top: 80px;
  width:1200px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
</style>
