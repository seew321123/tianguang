<template>
  <div class="b-intro">
    <div class="b-title">
      <div class="b-h1">企业咨询</div>
      <div class="b-h2">NEWS</div>
    </div>
    <div class="index-content">
    <div class="index-left">
    <div v-if="list.length>0">
      <img :src="list[0].fields.image" />
    </div>
    </div>
    <div class="news-container">
      <div v-for="(item, index) in list" v-bind:key="index">
      <div class="news-item" @click=goDetail(item.pk)>
        <div class="news-name">{{ item.fields.name }}</div>
      </div>
    </div>
    </div>
    </div>

    <el-button style="margin-top: 20px; width: 100px"><router-link to="/news">查看更多</router-link></el-button>
  </div>
</template>
<script>
export default {
  name: "news",
  data: function () {
    return {
      list: [],
      load_news_url: "/api/load_news",
    };
  },
  created() {
    this.load_news();
  },
  methods: {
    load_news() {
      var _this = this;
      let data = {
        offset: 0,
        limit: 4,
      };
      _this.$axios
        .get(_this.load_news_url, { params: data }) // 还可以直接把参数拼接在url后边
        .then(function (res) {
          console.log("res", res);
          _this.list = res.data.objects;
          console.log(_this.list);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    goDetail(pk){
      console.log('goDetail=>pk', pk)
      this.$router.push({
      path: '/newsdetail',
      // name: 'mallList',
      query: {
        pk: pk
      }
      })
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

.b-h2 {
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
.active div {
  color: red;
}

.b-intro {
  margin-top: 80px;
  width: 1200px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.index-content{
  display: flex;
  width: 100%;
}

.index-left{
  width:50%;
}

.index-left img{
  width: 570px;
  height: 380px;
}

.news-container{
  width:50%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.news-item{
  width:590px;
  height:90px;
  border: solid 1px rgb(207, 207, 207);
  display: flex;
  align-items: center;
  justify-content: space-around;
}

.news-name{
  text-align: center;
}
</style>
