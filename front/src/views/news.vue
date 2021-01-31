<template>
  <div class="view-news">
    <bNav activeTab="news"></bNav>
    <div class="news-content">
      <div class="news-item-view" v-for="(item, index) in list" v-bind:key="index" @click="goDetail(item.pk)">
        <img class="news-image" :src="item.fields.image" >
        <div class="text">
          <div class="news-title"> {{ item.fields.name }}</div>
          <div class="news-date"> {{ datetimeFormat(item.fields.datetime)}}</div>
        </div>
        
      </div>
    </div>
    <el-pagination
      background
      layout="prev, pager, next"
      @current-change="page_change"
      :current-page="currentPage"
      :page-size="pageSize"
      :total="total_count"
    ></el-pagination>
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
  name: "news",
  data: function () {
    return {
      currentPage: 1,
      pageSize: 10,
      total_count: 0,
      load_news_url: "/api/load_news",
      list: [],
    };
  },
  created() {
    console.log("111");
    this.load_news();
  },
  computed: {
    datetimeFormat() {
      return function (datetime) {
        let prettyDatetime = datetime.slice(0, 19).replace("T", " ");
        return prettyDatetime;
      };
    },
  },
  methods: {
    page_change(currentPage) {
      console.log("currentPage", currentPage);
      this.currentPage = currentPage;
      this.load_news();
    },
    load_news() {
      var _this = this;
      let data = {
        offset: _this.pageSize * (_this.currentPage - 1),
        limit: _this.pageSize,
      };
      _this.$axios
        .get(_this.load_news_url, { params: data }) // 还可以直接把参数拼接在url后边
        .then(function (res) {
          console.log("res111", res);
          _this.list = res.data.objects;
          _this.total_count = res.data.total_count;
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
  justify-content: center;
}
.view-news {
  display: flex;
  flex-direction: column;
  width: 100%;
  align-items: center;
}
.news-content{
  width: 1050px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 80px;
  margin-bottom: 80px;
}

.news-item-view{
  width: 47%;
  padding: 10px;
  margin-bottom: 20px;
  height: 130px;
  display: flex;
  align-items: flex-start;
}

.news-image{
  width: 230px;
  height: 130px;
  margin-right: 10px;
}

.news-date{
  margin-top: 20px;
  color: rgb(71, 71, 71);
}
</style>
