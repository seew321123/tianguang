<template>
  <div class="newsContainer">
    <bNav activeTab="news"></bNav>
    <div class="big-image" style="width: 100%;">
      <img style="width: 100%;height: 500px" src="http://qn22vegbe.hn-bkt.clouddn.com/20171010175143_V107580_aace4f19.jpg" alt="图片加载失败">
    </div>
    <div class="b-intro">
      <div class="b-title">
        <div class="b-h1">资讯详情</div>
        <div class="b-h2">news-DETAIL</div>
      </div>
      <div class="news-container-detail">
        <div class="news-detail-right" style="color: rgb(126, 122, 122);">
          <h1> 资讯标题:{{ item.fields.name }}</h1>
          <div class="news-detail-desc" v-html="item.fields.description">
          </div>
        </div>
      </div>
    </div>
    <myfooter></myfooter>
  </div>
</template>
<script>
  import bNav from "@/components/nav.vue";
  import myfooter from "@/components/footer.vue";
  export default {
    components: {
      bNav,
      myfooter,
    },
    name: "newsdetail",
    data: function () {
      return {
        item: null,
        news_detail_url: "/api/news_detail",
        currentPage: 1,
        pageSize: 10,
        total_count: 0,
      };
    },
    created() {
      console.log('params', this.$route.query)
      this.load_news();
    },
    methods: {
      load_news() {
        var _this = this;
        let pk = _this.$route.query.pk
        let data = {
          pk: pk
        }
        _this.$axios
          .get(_this.news_detail_url, {
            params: data
          }) // 还可以直接把参数拼接在url后边
          .then(function (res) {
            console.log("res", res);
            _this.item = res.data.object;
            console.log(_this.item);
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

  .news-container-detail {
    padding: 10px;
    display: flex;
    flex-direction: row;
    justify-content: start;
    border: solid 1px rgb(207, 207, 207);
  }
  .news-detail-desc *{
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .news-detail-item {
    width: 355px;
    height: 436px;
    /* border: solid 1px rgb(207, 207, 207); */
    margin-bottom: 20px;
    margin-right: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    overflow: hidden;
  }

  .news-item:hover {
    border: solid 1px rgb(207, 4, 4);
    cursor: pointer;
  }

  .news-item img {
    width: 355px;
    height: 355px;
  }

  .news-name {
    text-align: center;
  }

  .newsContainer {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  .buttonGroup{
    display: flex;
  }
  .button-item{
    position: relative;
    font-size: 24px;
    width: 150px;
    height: 60px;
    line-height: 60px;
    text-align: center;
    color: rgb(207, 4, 4);
    border: solid 1px rgb(207, 4, 4);
    border-radius: 10px;
    margin: 0 20px;
    transition: ease-in-out 0.3s;
    cursor: pointer;
  }
  .phone{
    position: absolute;
    display: none;
    transition: ease-in-out 1s;
  }
  .wechat{
    position: absolute;
    display: none;
    transition: ease-in-out 1s;
  }
  .button-item:hover{
    background-color: rgb(207, 4, 4);
    color: white;
  }
  .button-item[data-key="phone"]:hover .phone{
    opacity: 1;
    color: rgb(207, 4, 4);
    display: block;
  }
  .button-item[data-key="wechat"]:hover .wechat{
    opacity: 1;
    color: rgb(207, 4, 4);
    display: block;
  }
  .wechat img{
    width: 200px;
    height: 200px;
  }
</style>